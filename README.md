    # Multi-Object Smart UV Unwrap - Blender Addon

**Developer**: [Sudip Soni](https://github.com/Sudip13)  
**Repository**: [https://github.com/Sudip13/Blender-Plugins](https://github.com/Sudip13/Blender-Plugins)

A Blender addon that provides smart UV unwrapping functionality for multiple objects simultaneously, keeping each object's UV islands separate instead of sharing the same UV map.

## Problem Solved

By default, when you select multiple objects in Blender and use "Smart UV Project", all objects share the same UV space, which can cause overlapping and unwanted UV island mixing. This addon solves that by unwrapping each selected object individually, ensuring each object maintains its own separate UV islands with optional pack islands optimization.

## Features

- 🎯 **Multi-Object Processing**: Process multiple selected objects simultaneously
- 🏝️ **Separate UV Islands**: Each object gets its own UV coordinate space (no shared UV maps)
- 📦 **Pack Islands**: Optional UV island packing with customizable margins
- 🔄 **Rotation Optimization**: Allow island rotation for better space utilization
- ⚙️ **Customizable Settings**: Adjust angle limits, island margins, and area weights
- 🚀 **Quick Presets**: High Quality, Fast, Tight Pack, and No Pack presets
- 🎨 **User-Friendly UI**: Clean panel in the 3D Viewport sidebar
- 📝 **Built-in Instructions**: Step-by-step guidance in the UI

## Installation

### Method 1: Download and Install
1. Download this repository as a ZIP file
2. Open Blender
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` and select the downloaded ZIP file
3. Enable the addon by checking the box next to "Multi-Object Smart UV Unwrap"

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
3. Click **"Multi-Object Smart UV Unwrap"**
<img width="800" height="400" alt="2b" src="https://github.com/user-attachments/assets/fcde89f1-bcb4-4cbb-85d6-7bb19ce0078c" />
<img width="800" height="400" alt="3b" src="https://github.com/user-attachments/assets/bd687c8e-92e8-4a24-902d-e56adc41dbc5" />

### Advanced Usage
- Use the **operator panel** (bottom left after running) to adjust settings:
  - **Angle Limit**: Controls edge splitting sensitivity
  - **Island Margin**: Space between UV islands
  - **Area Weight**: Preservation of surface area ratios
  - **Correct Aspect**: Account for image aspect ratios

### Quick Presets
- **High Quality**: Better results with tight packing and rotation
  - Angle Limit: 60°
  - Island Margin: 0.01
  - Area Weight: 0.2
  - Correct Aspect: On
  - Pack Islands: On with tight margins

- **Fast**: Faster processing for quick iterations
  - Angle Limit: 80°
  - Island Margin: 0.05
  - Area Weight: 0.0
  - Correct Aspect: Off
  - Pack Islands: On with loose margins

- **Tight Pack**: Maximum UV space efficiency
  - Optimized for texture atlases
  - Minimal margins between islands
  - Rotation enabled for best fit

- **No Pack**: Traditional unwrapping without packing
  - Individual islands remain as generated
  - No additional optimization

## Technical Details

### Compatibility
- **Blender Version**: 2.80+ (Compatible with Blender 2.8, 3.x, 4.x series)
- **Mode Requirements**: Works in any mode (Object, Edit, etc.)
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
multi_object_smart_uv_unwrap/
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
- Blender 2.80+
- Python knowledge for modifications
- Understanding of Blender's Python API (bpy)

### Extending the Addon
The addon is structured for easy extension:
- Add new operators in `operators/`
- Add new UI elements in `ui/`
- Register new classes in the respective `__init__.py` files

## License

This addon is provided as-is for educational and practical use. Feel free to modify and distribute according to your needs.

## Developer

**Sudip Soni**
- 🔗 GitHub: [Sudip13](https://github.com/Sudip13)
- 📧 Repository: [Blender-Plugins](https://github.com/Sudip13/Blender-Plugins)
- 🐛 Issues: [Report Bugs](https://github.com/Sudip13/Blender-Plugins/issues)

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests at the GitHub repository.

### How to Contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Made with ❤️ by [Sudip Soni](https://github.com/Sudip13) for the Blender community**
