# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *  
from ..icons.icons import load_icons

from toolplus_resurface.rsf_booltool import *
from toolplus_resurface.ui_menus.menu_boolean import (VIEW3D_TP_Boolean_Menu)
from toolplus_resurface.ui_menus.menu_boolean import (VIEW3D_TP_Boolean_Direct_Menu, VIEW3D_TP_Boolean_Brush_Menu, VIEW3D_TP_Boolean_Bool_Menu)


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

def draw_boolean_ui(self, context, layout):
    
        tp_props = context.window_manager.tp_props_resurface   
           
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()

 
        col = layout.column(align=True)

        if not tp_props.display_boolean: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_boolean", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Boolean")  
               
            if bpy.context.mode == "OBJECT": 

                button_boolean_difference = icons.get("icon_boolean_difference")
                row.menu("tp_menu.boolean_direct_menu", text="", icon_value=button_boolean_difference.icon_id)

                button_boolean_union_brush = icons.get("icon_boolean_union_brush")
                row.menu("tp_menu.boolean_brush_menu", text="", icon_value=button_boolean_union_brush.icon_id)

                button_boolean_bevel = icons.get("icon_boolean_bevel")
                row.menu("tp_menu.boolean_bool_menu", text="", icon_value=button_boolean_bevel.icon_id)

            else:
                
                button_boolean_difference = icons.get("icon_boolean_difference")
                row.menu("tp_menu.boolean_direct_menu", text="", icon_value=button_boolean_difference.icon_id)

                button_boolean_facemerge = icons.get("icon_boolean_facemerge")
                row.operator("bpt.boolean_2d_union", text= "", icon_value=button_boolean_facemerge.icon_id)    

                button_boolean_bevel = icons.get("icon_boolean_bevel")
                row.menu("tp_menu.boolean_bool_menu", text="", icon_value=button_boolean_bevel.icon_id)                                                   

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_boolean", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Boolean")  

            
            button_boolean_difference = icons.get("icon_boolean_difference")
            row.menu("tp_menu.boolean_menu", text="", icon_value=button_boolean_difference.icon_id)
           

            if bpy.context.mode == "OBJECT": 

                box = col.box().column(1)
                
                row = box.column(1).column_flow(2)  
                
                button_boolean_union = icons.get("icon_boolean_union")
                row.operator("btool.direct_union", text="Union", icon_value=button_boolean_union.icon_id)

                button_boolean_intersect = icons.get("icon_boolean_intersect")
                row.operator("btool.direct_intersect", text="Intersect", icon_value=button_boolean_intersect.icon_id)

                button_boolean_difference = icons.get("icon_boolean_difference")
                row.operator("btool.direct_difference", text="Difference", icon_value=button_boolean_difference.icon_id)
                            
                row.separator()  

                button_boolean_substract = icons.get("icon_boolean_substract")
                row.operator("btool.direct_subtract", icon_value=button_boolean_substract.icon_id)              

                button_boolean_rebool = icons.get("icon_boolean_rebool")
                row.operator("btool.direct_slice", "Slice Rebool", icon_value=button_boolean_rebool.icon_id)        
                
                button_boolean_union_brush = icons.get("icon_boolean_union_brush")
                row.operator("tp_ops.tboolean_union", text="BT-Union", icon_value=button_boolean_union_brush.icon_id)            

                button_boolean_intersect_brush = icons.get("icon_boolean_intersect_brush")
                row.operator("tp_ops.tboolean_inters", text="BT-Intersect", icon_value=button_boolean_intersect_brush.icon_id)
                
                button_boolean_difference_brush = icons.get("icon_boolean_difference_brush")
                row.operator("tp_ops.tboolean_diff", text="BT-Difference", icon_value=button_boolean_difference_brush.icon_id)
                
                row.separator()

                button_boolean_rebool_brush = icons.get("icon_boolean_rebool_brush")
                row.operator("tp_ops.tboolean_slice", text="BT-SliceRebool", icon_value=button_boolean_rebool_brush.icon_id)

                layout.operator_context = 'INVOKE_REGION_WIN'
                button_boolean_draw = icons.get("icon_boolean_draw")
                row.operator("tp_ops.draw_polybrush", text="BT-DrawPoly", icon_value=button_boolean_draw.icon_id)


                if (isCanvas(context.active_object)) or (isBrush(context.active_object)):
                
                    box = col.box().column(1)
                    
                    row = box.column(1)  
     
                    if 0 < len(bpy.context.selected_objects) < 2 and bpy.context.object.mode == "OBJECT":
                                
                        button_boolean_bevel = icons.get("icon_boolean_bevel")
                        row.operator("object.boolean_bevel", text="BoolBevel", icon_value=button_boolean_bevel.icon_id)
                        
                        button_boolean_sym = icons.get("icon_boolean_sym")
                        row.operator("object.boolean_bevel_symmetrize", text="SymBevel", icon_value=button_boolean_sym.icon_id)
                       
                        button_boolean_pipe = icons.get("icon_boolean_pipe")                       
                        row.operator("object.boolean_bevel_make_pipe", text="BoolPipe", icon_value=button_boolean_pipe.icon_id)


                        if bpy.data.objects.find('BOOLEAN_BEVEL_CURVE') != -1 and bpy.data.objects.find('BOOLEAN_BEVEL_GUIDE') != -1:
                            button_boolean_custom = icons.get("icon_boolean_custom")
                            row.operator("object.boolean_custom_bevel", text="CustomBevel", icon_value=button_boolean_custom.icon_id)
                        
                        row.operator("tp_ops.cleanup_boolbevel", text="FinishBevel", icon='PANEL_CLOSE')

                    row.separator()


                    box.separator()

                    row = box.row()            
                    row.operator("object.boolean_bevel_remove_objects", text=" ", icon='GHOST_DISABLED')
                    row.operator("object.boolean_bevel_remove_pipes", text=" ", icon='IPO_CIRC')                
              
                    if len(bpy.context.selected_objects) > 0 and bpy.context.object.mode == "OBJECT":
                        
                        row.operator("object.boolean_bevel_remove_modifiers", text=" ", icon='X')
                        row.operator("object.boolean_bevel_apply_modifiers", text=" ", icon='FILE_TICK')

                    box.separator()

          

                box = col.box().column(1)
                
                row = box.column(1)
                   
                button_boolean_carver = icons.get("icon_boolean_carver")
                row.operator("object.carver", text="3d Carver", icon_value=button_boolean_carver.icon_id)

                box.separator()   

 
            if bpy.context.mode == "EDIT_MESH":


                box = col.box().column(1)                     

                row = box.column(1)                        

                button_boolean_union = icons.get("icon_boolean_union")
                row.operator("tp_ops.bool_union", text="Union", icon_value=button_boolean_union.icon_id) 

                button_boolean_intersect = icons.get("icon_boolean_intersect")
                row.operator("tp_ops.bool_intersect",text="Intersect", icon_value=button_boolean_intersect.icon_id) 

                button_boolean_difference = icons.get("icon_boolean_difference")
                row.operator("tp_ops.bool_difference",text="Difference", icon_value=button_boolean_difference.icon_id)  

                box.separator()  

                box = layout.box().column(1)                     

                row = box.column(1)  

                button_boolean_weld = icons.get("icon_boolean_weld")
                row.operator("mesh.intersect", "Weld", icon_value=button_boolean_weld.icon_id).separate_mode = 'NONE'

                #button_boolean_isolate = icons.get("icon_boolean_isolate")
                #row.operator("mesh.intersect", "Isolate", icon_value=button_boolean_isolate.icon_id).separate_mode = 'CUT'  

                button_boolean_isolate = icons.get("icon_boolean_isolate")
                row.operator("mesh.intersect", "Isolate", icon_value=button_boolean_isolate.icon_id).separate_mode = 'ALL'  
                
                box.separator()          
                
                row = box.row(1)           
                row.label("Planes")         

                button_axis_x = icons.get("icon_axis_x")
                row.operator("tp_ops.plane_x",text="", icon_value=button_axis_x.icon_id)      
              
                button_axis_y = icons.get("icon_axis_y")
                row.operator("tp_ops.plane_y",text="", icon_value=button_axis_y.icon_id)       

                button_axis_z = icons.get("icon_axis_z")
                row.operator("tp_ops.plane_z",text="", icon_value=button_axis_z.icon_id) 

                box.separator() 

                box = col.box().column(1)                     

                row = box.row(1) 
                
                button_boolean_facemerge = icons.get("icon_boolean_facemerge")
                row.operator("bpt.boolean_2d_union", text= "2d Union", icon_value=button_boolean_facemerge.icon_id)        
                
                box.separator() 

                
                box = col.box().column(1)
                
                row = box.column(1) 
                
                button_boolean_bridge = icons.get("icon_boolean_bridge")
                row.operator("mesh.edges_select_sharp", text="SharpEdges", icon_value=button_boolean_bridge.icon_id)    

                button_boolean_edge = icons.get("icon_boolean_edge")
                row.operator("object.boolean_bevel_custom_edge", text="CustomEdges", icon_value=button_boolean_edge.icon_id)
            
                row.operator("object.boolean_bevel_remove_objects", text="Remove Guides", icon='GHOST_DISABLED')        
                
                box.separator() 
