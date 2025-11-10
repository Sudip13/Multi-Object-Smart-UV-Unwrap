bl_info = {
    "name": "Multi-Object Smart UV Unwrap",
    "author": "Sudip Soni",
    "version": (1, 4, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Smart UV",
    "description": "Fast smart UV unwrap multiple objects individually with separate UV islands and pack islands optimization",
    "warning": "",
    "doc_url": "https://github.com/Sudip13/Blender-Plugins",
    "tracker_url": "https://github.com/Sudip13/Blender-Plugins/issues",
    "support": "COMMUNITY",
    "category": "UV",
}

import bpy
from . import operators
from . import ui


def register():
    """Register all addon classes and properties"""
    operators.register()
    ui.register()


def unregister():
    """Unregister all addon classes and properties"""
    ui.unregister()
    operators.unregister()


if __name__ == "__main__":
    register()