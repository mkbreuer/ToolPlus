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

import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons


# Object is a Canvas
def isCanvas(_obj):
    try:
        if _obj["BoolToolRoot"]:
            return True
    except:
        return False


# Object is a Brush Tool Bool
def isBrush(_obj):
    try:
        if _obj["BoolToolBrush"]:
            return True
    except:
        return False




# BRUSH MENU #
class VIEW3D_TP_Brush_Menu(bpy.types.Menu):
    bl_label = "Brush Tools"
    bl_idname = "VIEW3D_TP_Brush_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()
        
        button_boolean_union_brush = icons.get("icon_boolean_union_brush")
        layout.operator("tp_ops.tboolean_union", text="BT-Union", icon_value=button_boolean_union_brush.icon_id)            
        
        button_boolean_intersect_brush = icons.get("icon_boolean_intersect_brush")
        layout.operator("tp_ops.tboolean_inters", text="BT-Intersect", icon_value=button_boolean_intersect_brush.icon_id)
        
        button_boolean_difference_brush = icons.get("icon_boolean_difference_brush")
        layout.operator("tp_ops.tboolean_diff", text="BT-Difference", icon_value=button_boolean_difference_brush.icon_id)
        
        layout.separator()

        button_boolean_rebool_brush = icons.get("icon_boolean_rebool_brush")
        layout.operator("tp_ops.tboolean_slice", text="BT-SliceRebool", icon_value=button_boolean_rebool_brush.icon_id)

        layout.operator_context = 'INVOKE_REGION_WIN'
        button_boolean_draw = icons.get("icon_boolean_draw")
        layout.operator("tp_ops.draw_polybrush", text="BT-DrawPoly", icon_value=button_boolean_draw.icon_id)
       


# BEVEL MENU #
class VIEW3D_TP_Bevel_Menu(bpy.types.Menu):
    bl_label = "Bool Bevel"
    bl_idname = "VIEW3D_TP_Bevel_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()
        
        button_boolean_bevel = icons.get("icon_boolean_bevel")
        layout.operator("object.boolean_bevel", text="BoolBevel", icon_value=button_boolean_bevel.icon_id)

        button_boolean_sym = icons.get("icon_boolean_sym")
        layout.operator("object.boolean_bevel_symmetrize", text="SymBevel", icon_value=button_boolean_sym.icon_id)

        button_boolean_pipe = icons.get("icon_boolean_pipe")                       
        layout.operator("object.boolean_bevel_make_pipe", text="BoolPipe", icon_value=button_boolean_pipe.icon_id)

        if bpy.data.objects.find('BOOLEAN_BEVEL_CURVE') != -1 and bpy.data.objects.find('BOOLEAN_BEVEL_GUIDE') != -1:
    
            button_boolean_custom = icons.get("icon_boolean_custom")
            layout.operator("object.boolean_custom_bevel", text="CustomBevel", icon_value=button_boolean_custom.icon_id)
    


# BEVEL FIX MENU #
class VIEW3D_TP_Bevel_Fix_Menu(bpy.types.Menu):
    bl_label = "Delete / Apply"
    bl_idname = "VIEW3D_TP_Bevel_Fix_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()

        layout.operator("object.boolean_bevel_remove_objects", text="Rem.Guides", icon='GHOST_DISABLED')
        layout.operator("object.boolean_bevel_remove_pipes", text="Rem.Pipe", icon='IPO_CIRC')                        
     
        if len(bpy.context.selected_objects) > 0 and bpy.context.object.mode == "OBJECT":
            
            layout.operator("object.boolean_bevel_remove_modifiers", text="Rem.Mod", icon='X')
            layout.operator("object.boolean_bevel_apply_modifiers", text="Apply.Mod", icon='FILE_TICK')

        layout.separator()        
       
        layout.operator("tp_ops.cleanup_boolbevel", text="Finished", icon='PANEL_CLOSE')



# MAIN MENU #
class VIEW3D_TP_Boolean_Menu(bpy.types.Menu):
    bl_label = "Boolean"
    bl_idname = "VIEW3D_TP_Boolean_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()
        
        if context.mode == 'OBJECT':

            display_bool_direct = context.user_preferences.addons[__package__].preferences.tab_bool_direct 
            if display_bool_direct == 'on':
                               
                button_boolean_union = icons.get("icon_boolean_union")
                layout.operator("tp_ops.bool_union_obm_menu", text="Union", icon_value=button_boolean_union.icon_id)

                button_boolean_intersect = icons.get("icon_boolean_intersect")
                layout.operator("tp_ops.bool_intersect_obm_menu", text="Intersect", icon_value=button_boolean_intersect.icon_id)

                button_boolean_difference = icons.get("icon_boolean_difference")
                layout.operator("tp_ops.bool_difference_obm_menu", text="Difference", icon_value=button_boolean_difference.icon_id)
                            
                layout.separator() 

                button_boolean_substract = icons.get("icon_boolean_substract")
                layout.operator("btool.direct_subtract", icon_value=button_boolean_substract.icon_id)              

                button_boolean_rebool = icons.get("icon_boolean_rebool")
                layout.operator("tp_ops.bool_rebool_obm_menu", "SliceRebool", icon_value=button_boolean_rebool.icon_id)
 

 
            display_btbool_brush = context.user_preferences.addons[__package__].preferences.tab_btbool_brush 
            if display_btbool_brush == 'on':
                
                layout.separator()  
 
                
                button_boolean_union_brush = icons.get("icon_boolean_union_brush")
                layout.menu("VIEW3D_TP_Brush_Menu", icon_value=button_boolean_union_brush.icon_id)  

                if (isCanvas(context.active_object)) or (isBrush(context.active_object)):
                  
                    layout.menu("VIEW3D_TP_BTools_Fix_Menu", icon="PANEL_CLOSE")

                    if 0 < len(bpy.context.selected_objects) < 2 and bpy.context.object.mode == "OBJECT":

                        layout.separator()  
                        
                        button_boolean_bevel = icons.get("icon_boolean_bevel")              
                        layout.menu("VIEW3D_TP_Bevel_Menu", icon_value=button_boolean_bevel.icon_id)                    
                        
                        button_boolean_apply = icons.get("icon_boolean_apply")  
                        layout.menu("VIEW3D_TP_Bevel_Fix_Menu", icon_value=button_boolean_apply.icon_id)
                   

            layout.separator() 

            obj = context.active_object
            if obj:
                active_wire = obj.show_wire 
                if active_wire == True:
                    button_wire_off = icons.get("icon_wire_off")
                    layout.operator("tp_ops.wt_selection_handler_toggle", "WireToggle", icon_value=button_wire_off.icon_id)              
                else:                       
                    button_wire_on = icons.get("icon_wire_on")
                    layout.operator("tp_ops.wt_selection_handler_toggle", "WireToggle", icon_value=button_wire_on.icon_id)
           
                layout.separator() 

            button_boolean_carver = icons.get("icon_boolean_carver")
            layout.operator("object.carver", text="3d Carver", icon_value=button_boolean_carver.icon_id)


            display_optimize = context.user_preferences.addons[__package__].preferences.tab_optimize
            if display_optimize == 'on':  

                layout.separator()
                
                #button_origin_obm = icons.get("icon_origin_obm")
                layout.operator_menu_enum("object.origin_set", "type", text="Set Origin", icon="LAYER_ACTIVE")



        if context.mode == 'EDIT_MESH':
                      

            display_bool_direct = context.user_preferences.addons[__package__].preferences.tab_bool_direct 
            if display_bool_direct == 'on':

                button_boolean_union = icons.get("icon_boolean_union")
                layout.operator("tp_ops.bool_union_edm_menu", text="Union", icon_value=button_boolean_union.icon_id) 

                button_boolean_intersect = icons.get("icon_boolean_intersect")
                layout.operator("tp_ops.bool_intersect_edm_menu",text="Intersect", icon_value=button_boolean_intersect.icon_id) 

                button_boolean_difference = icons.get("icon_boolean_difference")
                layout.operator("tp_ops.bool_difference_edm_menu",text="Difference", icon_value=button_boolean_difference.icon_id)  
              
                layout.separator() 


            display_bool_intersect = context.user_preferences.addons[__package__].preferences.tab_bool_intersect
            if display_bool_intersect == 'on':


                button_boolean_weld = icons.get("icon_boolean_weld")
                layout.operator("mesh.intersect", "Weld", icon_value=button_boolean_weld.icon_id).separate_mode = 'NONE'

                #button_boolean_isolate = icons.get("icon_boolean_isolate")
                #layout.operator("mesh.intersect", "Isolate", icon_value=button_boolean_isolate.icon_id).separate_mode = 'CUT'  

                button_boolean_isolate = icons.get("icon_boolean_isolate")
                layout.operator("mesh.intersect", "Isolate", icon_value=button_boolean_isolate.icon_id).separate_mode = 'ALL'  
                
                button_axis_xyz_planes = icons.get("icon_axis_xyz_planes")
                layout.menu("tp_menu.intersetion_planes", text ="Planes", icon_value=button_axis_xyz_planes.icon_id)      

                layout.separator()  


            display_bool_brush = context.user_preferences.addons[__package__].preferences.tab_btbool_brush 
            if display_bool_brush == 'on':

                button_boolean_bridge = icons.get("icon_boolean_bridge")
                layout.operator("mesh.edges_select_sharp", text="SharpEdges", icon_value=button_boolean_bridge.icon_id)    

                button_boolean_edge = icons.get("icon_boolean_edge")
                layout.operator("object.boolean_bevel_custom_edge", text="CustomEdges", icon_value=button_boolean_edge.icon_id)
                
                layout.operator("object.boolean_bevel_remove_objects", text="Rem.Guides", icon='GHOST_DISABLED')   
                 
                #button_boolean_bridge = icons.get("icon_boolean_bridge")
                #layout.operator("object.boolean_bevel_bridge", text="Bridge Edge", icon_value=button_boolean_bridge.icon_id)
                
                layout.separator()          



            obj = context.active_object
            if obj:
                active_wire = obj.show_wire 
                if active_wire == True:
                    button_wire_off = icons.get("icon_wire_off")
                    layout.operator("tp_ops.wt_selection_handler_toggle", "WireToggle", icon_value=button_wire_off.icon_id)              
                else:                       
                    button_wire_on = icons.get("icon_wire_on")
                    layout.operator("tp_ops.wt_selection_handler_toggle", "WireToggle", icon_value=button_wire_on.icon_id)
           
                layout.separator() 
           
            button_boolean_facemerge = icons.get("icon_boolean_facemerge")
            layout.operator("tp_ops.boolean_2d_union_edm_menu", text= "2d Union", icon_value=button_boolean_facemerge.icon_id)      



            display_optimize = context.user_preferences.addons[__package__].preferences.tab_optimize
            if display_optimize == 'on':  

                layout.separator()
                                    
                button_select_link = icons.get("icon_select_link")
                layout.operator("tp_ops.select_linked_edm",text="Select Linked", icon_value=button_select_link.icon_id)

                button_remove_double = icons.get("icon_remove_double")
                layout.operator("mesh.remove_doubles",text="Remove Doubles", icon_value=button_remove_double.icon_id)             

                layout.operator("mesh.normals_make_consistent", text="Recalc. Normals", icon="SNAP_NORMAL")

                layout.separator()          

                button_origin_edm = icons.get("icon_origin_edm")
                layout.operator("tp_ops.origin_edm",text="Set Origin", icon_value=button_origin_edm.icon_id)



# MENU #
class VIEW3D_TP_BTools_Fix_Menu(bpy.types.Menu):
    bl_label = "Delete / Apply"
    bl_idname = "VIEW3D_TP_BTools_Fix_Menu"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()


        if (isCanvas(context.active_object)):
           
            layout.separator()
            
            layout.operator("btool.to_mesh", icon="MOD_LATTICE", text="Apply All")
            Rem = layout.operator("btool.remove", icon="CANCEL", text="Remove All")
            Rem.thisObj = ""
            Rem.Prop = "CANVAS"

        if (isBrush(context.active_object)):
           
            layout.separator()
            
            layout.operator("btool.brush_to_mesh", icon="MOD_LATTICE", text="Apply Brush")
            Rem = layout.operator("btool.remove", icon="CANCEL", text="Remove Brush")
            Rem.thisObj = ""
            Rem.Prop = "BRUSH"


# REGISTERY # 
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()           


