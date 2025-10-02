# Ferbos File Editor

A Home Assistant custom integration that provides file editing capabilities for configuration files through WebSocket API.

## Features

- Append lines to `configuration.yaml` with validation and reload
- Create/edit any files in the Home Assistant config directory
- Automatic backup creation before file modifications
- WebSocket API endpoints: `ferbos/config/add` and `ferbos/ui/add`
- Safe file operations with directory traversal protection

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to "Integrations"
3. Click the three dots in the top right corner and select "Custom repositories"
4. Add this repository URL: `https://github.com/ikhsanfauzan2812/ferbos-file-editor`
5. Select "Integration" as the category
6. Click "Add"
7. Find "Ferbos File Editor" in the integration list and install it
8. Restart Home Assistant

### Manual Installation

1. Download the latest release
2. Copy the `custom_components/ferbos_file_editor` folder to your Home Assistant's `custom_components` directory
3. Restart Home Assistant

## Configuration

1. Go to Settings → Devices & Services
2. Click "Add Integration"
3. Search for "Ferbos File Editor"
4. Click to add the integration

## Usage

### Configuration File Editing (`ferbos/config/add`)

Append lines to `configuration.yaml`:

```json
{
  "id": 1,
  "type": "ferbos/config/add",
  "args": {
    "lines": [
      "# New sensor configuration",
      "sensor:",
      "  - platform: template",
      "    sensors:",
      "      my_sensor:",
      "        value_template: '{{ states(\"sensor.temperature\") }}'"
    ],
    "validate": true,
    "reload_core": true,
    "backup": true
  }
}
```

### General File Operations (`ferbos/ui/add`)

Create or edit any file in the config directory:

```json
{
  "id": 1,
  "type": "ferbos/ui/add",
  "args": {
    "path": "www/sidebar-config.yaml",
    "template": "title: 'My Dashboard'\ndefault_path: /main\norder:\n  - item: 'Overview'\n    order: 1",
    "backup": true,
    "overwrite": true
  }
}
```

### Parameters

**ferbos/config/add:**
- `lines`: Array of strings to append to configuration.yaml
- `validate`: Boolean, validate config after changes (default: true)
- `reload_core`: Boolean, reload core config after changes (default: true)  
- `backup`: Boolean, create backup before changes (default: true)

**ferbos/ui/add:**
- `path`: Relative path from config directory (e.g., "www/file.yaml")
- `template`: String content to write to file
- `lines`: Alternative to template, array of lines to write
- `backup`: Boolean, create backup if file exists (default: true)
- `overwrite`: Boolean, allow overwriting existing files (default: false)

## Security

- All file operations are restricted to the Home Assistant config directory
- Directory traversal protection (prevents `../` paths)
- Automatic backup creation before modifications
- Local file system access only (no remote operations)

## License

MIT License
