# Script_Editing
A script editing workspace for the Blender Text Editor

# Tutorial:
https://www.youtube.com/watch?v=dc2KgXyM0ko

# Install:
- Download: Code - Download Zip
- Unzip
- Rename the folder inside the zip to Script_Editing - remove '-main'
- Copy the folder into: C:\Program Files\Blender Foundation\Blender 2.90\2.90\scripts\startup\bl_app_templates_system
- Start Blender.
- In the Welcome pop-up select 'Script Editing'.
- In the File menu - Defaults - Load Factory Settings(this is the only way to execute the init file in the workspace template).

The UI should now look different and the add-ons should be installed and enabled.

# Included add-ons:
- Addon Installer Script Runner https://github.com/1C0D/Addon_Installer-Script_Runner-BlenderAddon
- Addon Reloader: https://github.com/karmaral/addon-reloader
- Code Editor https://github.com/K-410/blender-scripts/blob/master/2.8/code_editor.py
- Console Easy Text Edit https://github.com/1C0D/console_easy_text_edit-Blender
- Intellisense https://github.com/tin2tin/Intellisense_for_Blender_Text_Editor
- Search Online Reference https://github.com/tin2tin/Search-API-Reference
- Snippets Library https://github.com/Pullusb/snippetsLibrary
- Text Marker https://github.com/samytichadou/TextMarker_blender_addon
- Text Formatting https://github.com/tin2tin/Trim-Whitespace-Change-Case-and-Split-Join-Lines/blob/master/Trim-Whitespace-Change-Case-and-Split-Join-Lines.py
- Textension https://github.com/K-410/textension

# Enabled Blender native add-ons:
- Edit Operator https://docs.blender.org/manual/en/dev/addons/development/edit_operator.html
- Icon Get https://docs.blender.org/manual/en/dev/addons/development/icon_viewer.html
- Is Key Free https://docs.blender.org/manual/en/dev/addons/development/is_key_free.html

# How to expand:
- Have an __init__.py file in the folder of the add-on.
- Copy the name in the init file.
- Zip the folder.
- In Script_Editing/__init__.py paste the name of the add-on if it should be enabled.

# VScode color theme:
https://gist.github.com/tin2tin/18f86237a54dd307296cfa7692b81a26
