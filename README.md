# Script_Editing
A script editing workspace for the Blender Text Editor

# Tutorial:
[![](http://img.youtube.com/vi/dc2KgXyM0ko/0.jpg)](http://www.youtube.com/watch?v=dc2KgXyM0ko "")

# Install:
[![](http://img.youtube.com/vi/ufSyony6eRE/0.jpg)](http://www.youtube.com/watch?v=ufSyony6eRE "")
- Download: Code - Download Zip
- Unzip
- Rename the folder inside the zip to Script_Editing - remove '-main'
- Copy the folder into: C:\Program Files\Blender Foundation\Blender 2.90\2.90\scripts\startup\bl_app_templates_system
- Start Blender.
- In the Welcome pop-up select 'Script Editing'.
- In the File menu - Defaults - Load Factory Settings(this is the only way to execute the init file in the workspace template).

The UI should now look different and the add-ons should be installed and enabled.

# Included add-ons:
Addon Installer Script Runner https://github.com/1C0D/Addon_Installer-Script_Runner-BlenderAddon

![alt text](Screenshots/Addon%20Managemet.jpg?raw=true)

Addon Reloader: https://github.com/karmaral/addon-reloader

![alt text](Screenshots/Addon%20Reloader.jpg?raw=true)

Code Editor https://github.com/K-410/blender-scripts/blob/master/2.8/code_editor.py

![alt text](Screenshots/codeeditor.jpg?raw=true)

Console Easy Text Edit https://github.com/1C0D/console_easy_text_edit-Blender

Intellisense https://github.com/tin2tin/Intellisense_for_Blender_Text_Editor

![alt text](Screenshots/Intellisense.jpg?raw=true)

Python Module Manager https://github.com/amb/blender_pip

![alt text](Screenshots/Python%20Module%20Manager.jpg?raw=true)

Search Online Reference https://github.com/tin2tin/Search-API-Reference

![alt text](Screenshots/Search%20Online.jpg?raw=true)

Snippets Library https://github.com/Pullusb/snippetsLibrary

![alt text](Screenshots/Snippets.jpg?raw=true)

Text Marker https://github.com/samytichadou/TextMarker_blender_addon

![alt text](Screenshots/TextMarkers.jpg?raw=true)

Text Formatting https://github.com/tin2tin/Trim-Whitespace-Change-Case-and-Split-Join-Lines/blob/master/Trim-Whitespace-Change-Case-and-Split-Join-Lines.py

![alt text](Screenshots/Formatting.jpg?raw=true)

Textension https://github.com/K-410/textension

![alt text](Screenshots/textension.jpg?raw=true)

View System Console Output 

![alt text](Screenshots/View%20System%20Console%20Output.jpg?raw=true)

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
