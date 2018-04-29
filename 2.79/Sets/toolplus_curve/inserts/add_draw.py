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
#


bl_info = {
    "name": "T+ Curve Draw",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 1, 0),
    "blender": (2, 7, 9),
    "location": "3D View",
    "description": "",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


# MAIN OPERATOR #
class VIEW3D_TP_Draw_Curve(bpy.types.Operator):
    bl_description = "create empty bezier curve object for curve draw"
    bl_idname = "tp_ops.draw_curve"
    bl_label = "C-Draw"
    bl_options = {'REGISTER', 'UNDO'}

   
    my_draw = bpy.props.EnumProperty(
      items = [("tp_cur",  "Cursor",   "cursor",   "BLANK1", 1),
               ("tp_sur",  "Surface",  "surface",  "BLANK1", 2)], 
               name = "curve stroke options",
               default = "tp_cur",
               description="curve stroke options")
                                   
   
    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        col = layout.column(align = True)

        box = col.box().column(1)   

        row = box.row(1)      
        row.prop(self, "my_draw", text=" ", expand=True)          

        box.separator()


    def execute(self, context):

        bpy.ops.curve.primitive_bezier_curve_add(view_align=False, enter_editmode=False, location=(4.8951, -8.25161, 19.013), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.object.location_clear()
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.delete(type='VERT')

        WM = context.window_manager

        if self.my_draw == "tp_cur":
            bpy.context.scene.tool_settings.curve_paint_settings.depth_mode = 'CURSOR'
            bpy.ops.curve.draw('INVOKE_DEFAULT')       
        else:
            bpy.context.scene.tool_settings.curve_paint_settings.depth_mode = 'SURFACE'
            bpy.ops.curve.draw('INVOKE_DEFAULT')

        
        return {'FINISHED'}



def menu_curve(self, context):
    layout = self.layout

    if context.mode =="OBJECT":
        
        self.layout.operator("tp_ops.draw_curve", text="Curve Draw", icon="LINE_DATA") 




# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)
   
    # Add menus to Add menu
    bpy.types.INFO_MT_curve_add.append(menu_curve)


def unregister():   
    bpy.utils.unregister_module(__name__)

    # Remove menus from the Add menu
    bpy.types.INFO_MT_curve_add.remove(menu_curve)

if __name__ == "__main__":
    register()