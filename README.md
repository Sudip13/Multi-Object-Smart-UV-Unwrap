    # Smart UV Unwrap Individual - Blender Addon

A Blender addon that provides smart UV unwrapping functionality for individual objects, keeping each object's UV islands separate instead of sharing the same UV map.

## Problem Solved

By default, when you select multiple objects in Blender and use "Smart UV Project", all objects share the same UV space, which can cause overlapping and unwanted UV island mixing. This addon solves that by unwrapping each selected object individually, ensuring each object maintains its own separate UV islands.

## Features

- 🎯 **Individual Object Processing**: Each selected object is unwrapped separately
- 🏝️ **Separate UV Islands**: No shared UV space between objects
- ⚙️ **Customizable Settings**: Adjust angle limits, island margins, and area weights
- 🚀 **Quick Presets**: High Quality and Fast presets for common use cases
- 🎨 **User-Friendly UI**: Clean panel in the 3D Viewport sidebar
- 📝 **Built-in Instructions**: Step-by-step guidance in the UI

## Installation

### Method 1: Download and Install
1. Download this repository as a ZIP file
2. Open Blender
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` and select the downloaded ZIP file
5. Enable the addon by checking the box next to "Smart UV Unwrap Individual"

### Method 2: Manual Installation
1. Download/clone this repository
2. Copy the entire folder to your Blender addons directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\[version]\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender/[version]/scripts/addons/`
   - **Linux**: `~/.config/blender/[version]/scripts/addons/`
3. Restart Blender
4. Enable the addon in Preferences > Add-ons

## Usage

### Basic Usage
1. Select multiple mesh objects in your scene
2. Switch to **Edit Mode** (`Tab` key)
3. Open the **Smart UV** panel in the 3D Viewport sidebar (`N` key)
4. Click **"Smart UV Unwrap Individual"**

### Advanced Usage
- Use the **operator panel** (bottom left after running) to adjust settings:
  - **Angle Limit**: Controls edge splitting sensitivity
  - **Island Margin**: Space between UV islands
  - **Area Weight**: Preservation of surface area ratios
  - **Correct Aspect**: Account for image aspect ratios

### Quick Presets
- **High Quality**: Better results, slower processing
  - Angle Limit: 60°
  - Island Margin: 0.01
  - Area Weight: 0.2
  - Correct Aspect: On

- **Fast**: Faster processing, good for quick iterations
  - Angle Limit: 80°
  - Island Margin: 0.05
  - Area Weight: 0.0
  - Correct Aspect: Off

## Technical Details

### Compatibility
- **Blender Version**: 3.0+
- **Mode Requirements**: Edit Mode with mesh objects
- **Object Types**: Mesh objects only

### How It Works
1. The addon iterates through each selected mesh object
2. For each object, it:
   - Sets the object as active
   - Ensures proper UV layer exists
   - Selects all faces of that object
   - Performs smart UV unwrapping with specified parameters
   - Updates the mesh data
3. Each object maintains its own UV coordinate space

### File Structure
```
smart_uv_unwrap_individual/
├── __init__.py              # Main addon entry point
├── operators/
│   ├── __init__.py         # Operators module init
│   └── smart_uv_unwrap.py  # Main UV unwrapping operator
├── ui/
│   ├── __init__.py         # UI module init
│   └── smart_uv_panel.py   # 3D Viewport panel
└── README.md               # This documentation
```

## Troubleshooting

### Common Issues

**Q: The panel doesn't appear in the sidebar**
- A: Make sure you're in Edit Mode with a mesh object selected

**Q: "No mesh objects selected" warning**
- A: Select at least one mesh object before running the operation

**Q: UV unwrapping seems to fail on some objects**
- A: Ensure objects have faces and valid geometry

**Q: Objects still share UV space**
- A: This addon works in Edit Mode - make sure you're not in Object Mode

### Getting Help
If you encounter issues:
1. Check that you're in Edit Mode
2. Verify mesh objects are selected
3. Ensure objects have faces
4. Check the Blender console for error messages

## Development

### Requirements
- Blender 3.0+
- Python knowledge for modifications
- Understanding of Blender's Python API (bpy)

### Extending the Addon
The addon is structured for easy extension:
- Add new operators in `operators/`
- Add new UI elements in `ui/`
- Register new classes in the respective `__init__.py` files

## License

This addon is provided as-is for educational and practical use. Feel free to modify and distribute according to your needs.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

---

**Made with ❤️ for the Blender community**