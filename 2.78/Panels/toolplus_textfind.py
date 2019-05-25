# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and / or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####



bl_info = {
    "name": "T+ TextFind",
    "author": "Marvin.K.Breuer(MKB)",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "Text Editor > Property Shelf [CTRL+T] >> Panel: Find+",
    "description": "alternate text find panel for the text editor",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MODULE #
import bpy
from bpy.types import Panel
from bpy.app.translations import pgettext_iface as iface_

class TEXT_TP_Custom(Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Find+"

    def draw(self, context):
        layout = self.layout

        st = context.space_data

        # find
        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(st, "find_text", text="")
        row.operator("text.find_set_selected", text="", icon='TEXT')
        col.operator("text.find")

        col.separator()

        # duplicate
        col = layout.column(align=True)
        row = col.row(align=True)

        row.operator("text.jump", text="Jump", icon='FRAME_NEXT')
        row.operator("text.convert_whitespace", text="Space", icon='SHORTDISPLAY').type='SPACES'
        row.operator("text.uncomment", text="clear", icon='RESTRICT_VIEW_OFF')
        row.operator("text.comment", text="#", icon='RESTRICT_VIEW_ON')
        col.operator("text.duplicate_line", text="Duplicate")


        col.separator()
   
        # replace
        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(st, "replace_text", text="")
        row.operator("text.replace_set_selected", text="", icon='TEXT')
        col.operator("text.replace")

        # settings
        layout.prop(st, "use_match_case")

        row = layout.row(align=True)
        row.prop(st, "use_find_wrap", text="Wrap")
        row.prop(st, "use_find_all", text="All")

        layout.operator("wm.console_toggle")
        




# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
        
        
