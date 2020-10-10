# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.app.handlers import persistent
import os

@persistent
def load_handler(dummy):
    from bpy import context
    screen = context.screen
    for area in screen.areas:
        if area.type == 'FILE_BROWSER':
            space = area.spaces.active
            params = space.params
            params.use_filter_folder = True
            params.use_filter = True

    path_to_script_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = sorted(os.listdir(path_to_script_dir))

    script_list =[]
    for item in file_list:
        if item.endswith('.zip'):
            script_list.append(item)

    for file in file_list:
        path_to_file = os.path.join(path_to_script_dir, item)
        print(path_to_file)
        bpy.ops.preferences.addon_install(overwrite=True, target='DEFAULT', filepath=path_to_file, filter_folder=True, filter_python=False, filter_glob="*.py;*.zip")

    enableTheseAddons = ['textension', 'TextMarker', 'code_editor', 'text_formatting']

    for string in enableTheseAddons:
        name = enableTheseAddons
        bpy.ops.preferences.addon_enable(module = string)


def register():
    bpy.app.handlers.load_factory_startup_post.append(load_handler)


def unregister():
    bpy.app.handlers.load_factory_startup_post.remove(load_handler)


if __name__ == "__main__":
    register()