import bpy
import bmesh
from bpy.types import Operator
from bpy.props import FloatProperty, BoolProperty


class MESH_OT_smart_uv_unwrap_individual(Operator):
    """Multi-Object Smart UV unwrap - unwrap multiple objects individually with separate UV islands"""
    bl_idname = "mesh.smart_uv_unwrap_individual"
    bl_label = "Multi-Object Smart UV Unwrap"
    bl_description = "Smart UV unwrap multiple objects individually with separate UV islands and pack optimization"
    bl_options = {'REGISTER', 'UNDO'}

    # Properties for the operator
    angle_limit: FloatProperty(
        name="Angle Limit",
        description="Angle limit for edge splitting",
        default=1.15192,  # ~66 degrees in radians
        min=0.0,
        max=3.14159,  # 180 degrees
        subtype='ANGLE'
    )
    
    island_margin: FloatProperty(
        name="Island Margin",
        description="Margin between UV islands",
        default=0.02,
        min=0.0,
        max=1.0
    )
    
    area_weight: FloatProperty(
        name="Area Weight",
        description="Weight for area preservation",
        default=0.0,
        min=0.0,
        max=1.0
    )
    
    correct_aspect: BoolProperty(
        name="Correct Aspect",
        description="Map UVs taking image aspect ratio into account",
        default=True
    )
    
    pack_islands: BoolProperty(
        name="Pack Islands",
        description="Pack UV islands after unwrapping to optimize space usage",
        default=True
    )
    
    pack_margin: FloatProperty(
        name="Pack Margin",
        description="Margin between islands when packing",
        default=0.001,
        min=0.0,
        max=0.1
    )
    
    pack_rotate: BoolProperty(
        name="Rotate Islands",
        description="Allow rotation of islands during packing for better space utilization",
        default=True
    )

    @classmethod
    def poll(cls, context):
        """Check if the operator can be executed"""
        return (context.selected_objects and
                any(obj.type == 'MESH' for obj in context.selected_objects))

    def execute(self, context):
        """Execute the UV unwrapping operation - OPTIMIZED VERSION"""
        # Store the current active object and mode
        original_active = context.active_object
        original_mode = context.mode
        original_selection = list(context.selected_objects)
        
        # Get all selected mesh objects
        mesh_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        
        if not mesh_objects:
            self.report({'WARNING'}, "No mesh objects selected")
            return {'CANCELLED'}
        
        # Count processed objects
        processed_count = 0
        failed_objects = []
        total_objects = len(mesh_objects)
        
        # Single progress report for start
        self.report({'INFO'}, f"Processing {total_objects} objects...")
        
        try:
            # Ensure we're in Object mode ONCE
            if context.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
            
            # Process each mesh object with optimized workflow
            for i, obj in enumerate(mesh_objects):
                try:
                    # Verify object has geometry (fast check)
                    if len(obj.data.polygons) == 0:
                        continue
                    
                    # OPTIMIZED SELECTION: Direct selection without clearing all
                    for other_obj in context.selected_objects:
                        if other_obj != obj:
                            other_obj.select_set(False)
                    
                    obj.select_set(True)
                    context.view_layer.objects.active = obj
                    
                    # Ensure UV layer exists (create if needed)
                    if not obj.data.uv_layers:
                        obj.data.uv_layers.new()
                    else:
                        obj.data.uv_layers.active_index = 0
                    
                    # SINGLE MODE SWITCH: Enter Edit mode
                    bpy.ops.object.mode_set(mode='EDIT')
                    
                    # Select all faces ONCE
                    bpy.ops.mesh.select_all(action='SELECT')
                    
                    # Perform smart UV unwrap
                    bpy.ops.uv.smart_project(
                        angle_limit=self.angle_limit,
                        island_margin=self.island_margin,
                        area_weight=self.area_weight,
                        correct_aspect=self.correct_aspect
                    )
                    
                    # Pack islands if requested (in same edit session)
                    if self.pack_islands:
                        bpy.ops.uv.pack_islands(
                            margin=self.pack_margin,
                            rotate=self.pack_rotate
                        )
                    
                    # SINGLE MODE SWITCH: Return to Object mode
                    bpy.ops.object.mode_set(mode='OBJECT')
                    
                    processed_count += 1
                    
                except Exception as obj_error:
                    failed_objects.append(f"{obj.name}: {str(obj_error)}")
                    
                    # Ensure we're back in Object mode even if error occurred
                    try:
                        if context.mode != 'OBJECT':
                            bpy.ops.object.mode_set(mode='OBJECT')
                    except:
                        pass
                    continue
                
        except Exception as e:
            self.report({'ERROR'}, f"Critical error during UV unwrapping: {str(e)}")
            return {'CANCELLED'}
        
        finally:
            # OPTIMIZED RESTORATION: Batch operations
            try:
                # Ensure we're in Object mode
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                    
                # Restore original selection efficiently
                for obj in context.selected_objects:
                    obj.select_set(False)
                
                for obj in original_selection:
                    if obj:  # Check if object still exists
                        obj.select_set(True)
                
                # Restore original active object
                if original_active and original_active in original_selection:
                    context.view_layer.objects.active = original_active
                
                # Restore original mode if needed
                if original_mode != 'OBJECT':
                    try:
                        if original_mode == 'EDIT_MESH':
                            bpy.ops.object.mode_set(mode='EDIT')
                        else:
                            mode = original_mode.split('_')[0].lower()
                            if mode in ['edit', 'sculpt', 'paint']:
                                bpy.ops.object.mode_set(mode=mode.upper())
                    except:
                        pass
                        
                # Single update at the end
                bpy.context.view_layer.update()
                
            except Exception as restore_error:
                self.report({'WARNING'}, f"Could not fully restore original state: {str(restore_error)}")
        
        # Single final report
        if failed_objects:
            self.report({'WARNING'}, f"Completed: {processed_count}/{total_objects} objects unwrapped successfully")
        else:
            self.report({'INFO'}, f"SUCCESS: All {processed_count} objects unwrapped with individual UV maps!")
        
        return {'FINISHED'}

    def draw(self, context):
        """Draw the operator properties in the UI"""
        layout = self.layout
        
        # UV Unwrapping Settings
        box = layout.box()
        box.label(text="UV Unwrapping Settings", icon='UV_DATA')
        box.prop(self, "angle_limit")
        box.prop(self, "island_margin")
        box.prop(self, "area_weight")
        box.prop(self, "correct_aspect")
        
        # Pack Islands Settings
        box = layout.box()
        box.label(text="Pack Islands Settings", icon='PACKAGE')
        box.prop(self, "pack_islands")
        
        if self.pack_islands:
            col = box.column()
            col.prop(self, "pack_margin")
            col.prop(self, "pack_rotate")


def register():
    """Register the operator"""
    bpy.utils.register_class(MESH_OT_smart_uv_unwrap_individual)


def unregister():
    """Unregister the operator"""
    bpy.utils.unregister_class(MESH_OT_smart_uv_unwrap_individual)