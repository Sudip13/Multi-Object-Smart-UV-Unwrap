bl_info = {
    "name": "Smart UV Unwrap Individual",
    "author": "Your Name",
    "version": (1, 3, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Smart UV",
    "description": "Smart UV unwrap individual objects with separate UV islands and pack islands optimization",
    "warning": "",
    "doc_url": "",
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