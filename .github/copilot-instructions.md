# Blender Smart UV Unwrap Addon Development

This workspace contains a Blender addon that provides smart UV unwrapping functionality for individual objects, keeping each object's UV islands separate instead of sharing the same UV map.

## Project Structure
- **`__init__.py`** - Main addon entry point with registration
- **`operators/`** - Contains the UV unwrapping operators
- **`ui/`** - UI panels and interface elements
- **`README.md`** - Installation and usage documentation

## Development Guidelines
- Follow Blender addon development conventions
- Use proper operator registration and bl_info structure
- Implement proper error handling for UV operations
- Maintain compatibility with Blender 3.0+

## Addon Functionality
The addon provides:
1. Smart UV unwrapping for individual objects
2. Separate UV islands per object (no shared UV maps)
3. UI panel in 3D Viewport for easy access
4. Support for multiple object selection

## Technical Requirements
- Blender Python API (bpy)
- bmesh for mesh operations
- UV unwrapping utilities from Blender