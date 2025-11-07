from . import smart_uv_unwrap

def register():
    """Register all operators"""
    smart_uv_unwrap.register()

def unregister():
    """Unregister all operators"""
    smart_uv_unwrap.unregister()