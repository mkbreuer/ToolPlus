# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.


# LOAD MODUL #    
import bpy
from bpy.props import *

"""
bl_info = {
    "name": "To All",
    "author": "Manuel Geissinger",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "Properties",
    "description": "Copies settings, modifiers to all selected objects",
    "warning": "",
    "wiki_url": "https://www.artunchained.de/tiny-new-addon-to-all/",
    "category": "Objects",
    }
""" 
   
bpy.types.Scene.excludeMod = BoolProperty(name='Exclude viewport invisible', description='This will exclude modifiers that are set to invisible (eye-icon)', default=True)

    
class toAll(bpy.types.Operator):
    """Copies or append modifiers from active to all selected"""
    bl_idname = "tp_ops.to_all"
    bl_label = "Copy to all"
    bl_options = {'REGISTER', 'UNDO'}
    
    mode = bpy.props.StringProperty(default="")

    def execute(self, context):
        if bpy.context.active_object is not None:
            scene = bpy.context.scene
            active = bpy.context.active_object
            
            if "selected" in self.mode:
                objects = bpy.context.selected_objects
            if "children" in self.mode:
                objects = active.children
                
            for ob in objects:
                if ob != active:
                                
                    if "modifier" in self.mode:
                        if ob.type == 'MESH' or ob.type == 'CURVE':
                            if not "append" in self.mode:
                                for mod in ob.modifiers:
                                    ob.modifiers.remove(mod)
                                    
                            for mod in active.modifiers:
                                if not (bpy.context.scene.excludeMod and mod.show_viewport == False):
                                    currentMod = ob.modifiers.new(mod.name, mod.type)
                                    
                                    # collect names of writable properties
                                    properties = [p.identifier for p in mod.bl_rna.properties if not p.is_readonly]

                                    # copy those properties
                                    for prop in properties:
                                        setattr(currentMod, prop, getattr(mod, prop))


        return {'FINISHED'}
