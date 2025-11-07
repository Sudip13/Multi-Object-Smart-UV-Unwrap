from . import smart_uv_panel

def register():
    """Register all UI panels"""
    smart_uv_panel.register()

def unregister():
    """Unregister all UI panels"""
    smart_uv_panel.unregister()