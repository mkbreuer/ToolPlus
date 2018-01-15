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


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


class View3D_TP_Copy_Menu(bpy.types.Menu):
    """Copy"""
    bl_label = "Copy"
    bl_idname = "View3D_TP_Copy_Menu"

    def draw(self, context):
        layout = self.layout
            
        layout.operator_context = 'INVOKE_REGION_WIN'

        display_copy = context.user_preferences.addons[__package__].preferences.tab_menu_copy
        if display_copy == 'on':
               
                mode_string = context.mode                
                if mode_string == 'OBJECT':
                    layout.operator("object.duplicate_move", text="Dupli Move")
                    layout.operator("object.duplicate_move_linked", text="Dupli Link")    
                elif mode_string == 'EDIT_MESH':
                    layout.operator("mesh.duplicate_move", text="Dupli Move", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_CURVE':
                    layout.operator("curve.duplicate_move", text="Dupli Move", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_SURFACE':
                    layout.operator("curve.duplicate_move", text="Dupli Move", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_METABALL':
                    layout.operator("mball.duplicate_move", text="Dupli Move", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_ARMATURE':
                    layout.operator("armature.duplicate_move", text="Dupli Move", icon="MOD_BOOLEAN")

                layout.separator()


        mode_string = context.mode                
        if mode_string == 'OBJECT':
                
            layout.operator("tp_ops.mft_radialclone_popup", text="Radial Clone")
            layout.operator("tp_ops.copy_to_meshtarget", text="Copy to Target")        
            
        
            display_arewo = context.user_preferences.addons[__package__].preferences.tab_menu_arewo
            if display_arewo == 'on':

                layout.separator()
                
                layout.operator("tp_ops.copy_to_cursor", text="Copy 2 Cursor")                                    
                layout.operator("object.simplearewo", text="ARewO") 


            display_array = context.user_preferences.addons[__package__].preferences.tab_menu_array
            if display_array == 'on':

                layout.separator()
                
                layout.menu("tp_menu.copyshop_array_menu")


            display_array = context.user_preferences.addons[__package__].preferences.tab_menu_optimize
            if display_array == 'on':
                
                layout.separator()
                
                layout.menu("tp_menu.copyshop_optimize_menu")


            display_origin = context.user_preferences.addons[__package__].preferences.tab_menu_origin
            if display_origin == 'on':

                layout.separator()
                
                layout.menu("tp_menu.copyshop_origin_menu")
                    



class View3D_TP_Copy_Origin_Menu(bpy.types.Menu):
    """Set Origin"""
    bl_label = "Set Origin"
    bl_idname = "tp_menu.copyshop_origin_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("tp_ops.origin_plus_z", text="Top", icon="LAYER_USED")  
        props = layout.operator("object.origin_set", text="Middle", icon="LAYER_USED")
        props.type = 'ORIGIN_GEOMETRY'
        props.center = 'BOUNDS'
        layout.operator("tp_ops.origin_minus_z", text="Bottom", icon="LAYER_USED")


class View3D_TP_Copy_Optimize_Menu(bpy.types.Menu):
    """Optimize"""
    bl_label = "Optimize"
    bl_idname = "tp_menu.copyshop_optimize_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.make_links_data","Links Data").type='OBDATA'
        layout.operator("tp_ops.make_single","Unlinks Data")                        
        layout.operator("object.select_linked", text="Sel. Linked")   
        layout.operator("object.join", text="Join all")   



class View3D_TP_Copy_Array_Menu(bpy.types.Menu):
    """ArrayTools"""
    bl_label = "ArrayTools"
    bl_idname = "tp_menu.copyshop_array_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("tp_ops.x_array", text="X Array")    
        layout.operator("tp_ops.y_array", text="Y Array")    
        layout.operator("tp_ops.z_array", text="Z Array")   
        
        

# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()