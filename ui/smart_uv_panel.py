import bpy
from bpy.types import Panel


class VIEW3D_PT_smart_uv_unwrap(Panel):
    """Smart UV Unwrap Panel in 3D Viewport sidebar"""
    bl_label = "Smart UV Individual"
    bl_idname = "VIEW3D_PT_smart_uv_unwrap"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Smart UV"
    bl_context = "objectmode"

    @classmethod
    def poll(cls, context):
        """Show panel when mesh objects are available"""
        return (context.selected_objects and
                any(obj.type == 'MESH' for obj in context.selected_objects))

    def draw(self, context):
        """Draw the panel UI"""
        layout = self.layout
        
        # Main title
        col = layout.column(align=True)
        col.label(text="Individual Object UV Unwrap", icon='UV')
        
        # Separator
        col.separator()
        
        # Instructions
        box = layout.box()
        box.label(text="Instructions:", icon='INFO')
        box.label(text="1. Select multiple objects")
        box.label(text="2. Click 'Smart UV Unwrap Individual'")
        box.label(text="3. Each object gets separate UV maps")
        box.label(text="4. Works in any mode!")
        
        # Mode indicator
        mode_box = layout.box()
        mode_box.label(text=f"Current Mode: {context.mode}", icon='EDITMODE_HLT')
        if context.mode == 'EDIT_MESH':
            mode_box.label(text="⚠️ Will switch to Object mode", icon='INFO')
        
        # Separator
        layout.separator()
        
        # Main operator button
        col = layout.column(align=True)
        col.scale_y = 1.5
        
        # Check if there are selected objects
        selected_count = len([obj for obj in context.selected_objects if obj.type == 'MESH'])
        
        if selected_count == 0:
            col.label(text="No mesh objects selected", icon='ERROR')
            col.enabled = False
        elif selected_count == 1:
            col.label(text=f"1 object selected", icon='OBJECT_DATA')
        else:
            col.label(text=f"{selected_count} objects selected", icon='OBJECT_DATA')
        
        # Main operator button
        op = col.operator(
            "mesh.smart_uv_unwrap_individual",
            text="Smart UV Unwrap Individual",
            icon='UV_DATA'
        )
        
        # Additional options section
        layout.separator()
        
        # Quick presets
        box = layout.box()
        box.label(text="Quick Presets:", icon='PRESET')
        
        # First row of presets
        row = box.row(align=True)
        
        # High Quality preset
        op_hq = row.operator(
            "mesh.smart_uv_unwrap_individual",
            text="High Quality"
        )
        op_hq.angle_limit = 1.0472  # 60 degrees
        op_hq.island_margin = 0.01
        op_hq.area_weight = 0.2
        op_hq.correct_aspect = True
        op_hq.pack_islands = True
        op_hq.pack_margin = 0.001
        op_hq.pack_rotate = True
        
        # Fast preset
        op_fast = row.operator(
            "mesh.smart_uv_unwrap_individual",
            text="Fast"
        )
        op_fast.angle_limit = 1.39626  # 80 degrees
        op_fast.island_margin = 0.05
        op_fast.area_weight = 0.0
        op_fast.correct_aspect = False
        op_fast.pack_islands = True
        op_fast.pack_margin = 0.002
        op_fast.pack_rotate = False
        
        # Second row of presets
        row = box.row(align=True)
        
        # Tightly Packed preset
        op_tight = row.operator(
            "mesh.smart_uv_unwrap_individual",
            text="Tight Pack"
        )
        op_tight.angle_limit = 1.15192  # 66 degrees
        op_tight.island_margin = 0.02
        op_tight.area_weight = 0.1
        op_tight.correct_aspect = True
        op_tight.pack_islands = True
        op_tight.pack_margin = 0.0005  # Very tight packing
        op_tight.pack_rotate = True
        
        # No Packing preset
        op_no_pack = row.operator(
            "mesh.smart_uv_unwrap_individual",
            text="No Pack"
        )
        op_no_pack.angle_limit = 1.15192
        op_no_pack.island_margin = 0.02
        op_no_pack.area_weight = 0.0
        op_no_pack.correct_aspect = True
        op_no_pack.pack_islands = False
        
        # Tips section
        layout.separator()
        box = layout.box()
        box.label(text="Tips:", icon='LIGHTBULB')
        box.label(text="• Each object gets its OWN UV map")
        box.label(text="• No shared UV coordinates")
        box.label(text="• Pack Islands optimizes UV space")
        box.label(text="• Perfect for individual texturing")
        box.label(text="• Use Tight Pack for texture atlases")


def register():
    """Register the panel"""
    bpy.utils.register_class(VIEW3D_PT_smart_uv_unwrap)


def unregister():
    """Unregister the panel"""
    bpy.utils.unregister_class(VIEW3D_PT_smart_uv_unwrap)