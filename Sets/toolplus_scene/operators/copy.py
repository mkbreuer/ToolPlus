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

# <pep8 compliant>
"""
Modifier Snippet from :

bl_info = {
    "name": "Copy Attributes Menu",
    "author": "Bassam Kurdali, Fabian Fricke, Adam Wiseman",
    "version": (0, 4, 7),
    "blender": (2, 63, 0),
    "location": "View3D > Ctrl-C",
    "description": "Copy Attributes Menu from Blender 2.4",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Copy_Attributes_Menu",
    "tracker_url": "https://projects.blender.org/tracker/index.php?func=detail&aid=22588",
    "category": "..."}

"""

import bpy
from mathutils import Matrix


@classmethod
def object_poll_func(cls, context):
    return(len(context.selected_objects) > 1)

def generic_copy(source, target, string=""):
    """ copy attributes from source to target that have string in them """
    for attr in dir(source):
        if attr.find(string) > -1:
            try:
                setattr(target, attr, getattr(source, attr))
            except:
                pass
    return

def object_invoke_func(self, context, event):
    wm = context.window_manager
    wm.invoke_props_dialog(self)
    return {'RUNNING_MODAL'}


class VIEW3D_TP_CopySelectedObjectModifiers(bpy.types.Operator):
    """copy choosen modifiers from active to selected"""
    bl_idname = "tp_ops.copy_choosen_mods"
    bl_label = "Copy Modifiers"

    selection = bpy.props.BoolVectorProperty(size=32)

    poll = object_poll_func
    invoke = object_invoke_func
    
    def draw(self, context):
        layout = self.layout
        for idx, const in enumerate(context.active_object.modifiers):
            layout.prop(self, 'selection', index=idx, text=const.name,
               toggle=True)

    def execute(self, context):
        scene = bpy.context.scene
        active = context.active_object
        selected = context.selected_objects[:]
        selected.remove(active)

        for obj in selected:
            for index, flag in enumerate(self.selection):
                if flag:
                    old_modifier = active.modifiers[index]
                    new_modifier = obj.modifiers.new(\
                       type=active.modifiers[index].type,
                       name=active.modifiers[index].name)
                    generic_copy(old_modifier, new_modifier)
       
        return{'FINISHED'}



    
def register():
    
    bpy.utils.register_module(__name__)

def unregister():
   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()





