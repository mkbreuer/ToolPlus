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


from toolplus_boolean.bool_booltools3   import *


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from bpy.types import WindowManager
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


# Object is a Poly Brush Tool Bool collection
def isPolyBrush(_obj):
    try:
        if _obj["BoolToolPolyBrush"]:
            return True
    except:
        return False
    

def draw_bt_config_panel_layout(context, layout):
    
        icons = load_icons()

        actObj = bpy.context.active_object
        icon = ""
            
        # CANVAS ---------------------------------------------------
        if isCanvas(actObj):

            box = layout.box().column(1)
             
            row = box.row(1)   

            row.label("CANVAS", icon="MESH_GRID")

            obj = context.active_object
            if obj:
                active_wire = obj.show_wire 
                if active_wire == True:
                    button_wire_off = icons.get("icon_wire_off")
                    row.operator("tp_ops.wt_selection_handler_toggle", "", icon_value=button_wire_off.icon_id)              
                else:                       
                    button_wire_on = icons.get("icon_wire_on")
                    row.operator("tp_ops.wt_selection_handler_toggle", "", icon_value=button_wire_on.icon_id)
            
            row.prop(context.scene, 'BoolHide', text="", icon="VISIBLE_IPO_ON")
         
            row = box.row(1)
            Rem = row.operator("btool.remove", icon="PANEL_CLOSE", text="Remove All")
            Rem.thisObj = ""
            Rem.Prop = "CANVAS"
            
            
            button_boolean_apply = icons.get("icon_boolean_apply")
            row.operator("btool.to_mesh", text="Apply All", icon_value=button_boolean_apply.icon_id)

            if isBrush(actObj):
                layout.separator()

        # BRUSH ------------------------------------------------------
        if isBrush(actObj):

            box = layout.box().column(1)
             
            row = box.row(1)   

            if (actObj["BoolToolBrush"] == "UNION"):
                icon = "ROTATECOLLECTION"
            if (actObj["BoolToolBrush"] == "DIFFERENCE"):
                icon = "ROTATECENTER"
            if (actObj["BoolToolBrush"] == "INTERSECT"):
                icon = "ROTACTIVE"
            if (actObj["BoolToolBrush"] == "SLICE"):
                icon = "ROTATECENTER"

            row = box.row(True)
            row.label("BRUSH", icon=icon)
            
            obj = context.active_object
            if obj:
                active_wire = obj.show_wire 
                if active_wire == True:
                    button_wire_off = icons.get("icon_wire_off")
                    row.operator("tp_ops.wt_selection_handler_toggle", "", icon_value=button_wire_off.icon_id)              
                else:                       
                    button_wire_on = icons.get("icon_wire_on")
                    row.operator("tp_ops.wt_selection_handler_toggle", "", icon_value=button_wire_on.icon_id)


            icon = ""
            if actObj["BoolTool_FTransform"] == "True":
                icon = "PMARKER_ACT"
            else:
                icon = "PMARKER"
            if isFTransf():
                pass

            if isFTransf():
                row.operator("btool.enable_ftransf", text="", icon=icon)
                Enable = row.operator("btool.enable_this_brush", text="", icon="VISIBLE_IPO_ON")
            else:                               
                Enable = row.operator("btool.enable_this_brush", icon="VISIBLE_IPO_ON")

        if isPolyBrush(actObj):
            
            #box = layout.box().column(1)
              
            row = box.row()            
            row.label("POLY BRUSH", icon="LINE_DATA")
            mod = actObj.modifiers["BTool_PolyBrush"]
           
            row = box.row()
            row.prop(mod, "thickness", text="Size")
            
            layout.separator()

        if isBrush(actObj):

            row = box.row(1)
            Rem = row.operator("btool.remove", icon="PANEL_CLOSE", text="Remove All")
            Rem.thisObj = ""
            Rem.Prop = "BRUSH"
            
            button_boolean_apply = icons.get("icon_boolean_apply")
            row.operator("btool.to_mesh", text="Apply All", icon_value=button_boolean_apply.icon_id)




bpy.types.Scene.tp_sublocal = bpy.props.BoolProperty(default=False)


EDIT = ["OBJECT", "EDIT_MESH"]
GEOM = ['MESH']

class draw_boolean_layout:
    
    @classmethod
    def poll(cls, context):
       
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)

        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                
#                result = False                
#                if (isCanvas(obj) or isBrush(obj) or isPolyBrush(obj)):
#                    result = True                
                     
                return isModelingMode and context.mode in EDIT #and result
    
    icons = load_icons()
    types_bool =  [("tp_01"    ,"Direct"  ,"direct boolean"  ,icons["icon_boolean_rebool"].icon_id          ,0),
                   ("tp_02"    ,"Brush"   ,"brush boolean"   ,icons["icon_boolean_rebool_brush"].icon_id    ,1), 
                   ("tp_03"    ,"Multi"   ,"multi boolean"   ,"MOD_ARRAY" ,2)]                   
    bpy.types.Scene.tp_bool = bpy.props.EnumProperty(name = " ", default = "tp_01", items = types_bool)

    icons = load_icons()
    types_bool_edm =  [("tp_01"    ,"Direct"  ,"direct boolean"  ,icons["icon_boolean_rebool"].icon_id       ,0),
                       ("tp_02"    ,"Brush"   ,"brush boolean"   ,icons["icon_boolean_rebool_brush"].icon_id ,1)]                   
    bpy.types.Scene.tp_bool_edm = bpy.props.EnumProperty(name = " ", default = "tp_01", items = types_bool_edm)


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
                
        icons = load_icons()

        scene = context.scene
               

        col = layout.column(1)

        box = col.box().column(1) 
        
        if context.mode == "OBJECT":
           
            row = box.row(1)  
            row.prop(scene, 'tp_bool', emboss = False, expand = True) #icon_only=True,


            # DIRECT BOOLEAN #
            if scene.tp_bool == "tp_01": 

                box = layout.box().column(1)                                                   

                row = box.column(1) 
                
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

                Display_Optimize = context.user_preferences.addons[__package__].preferences.tab_optimize
                if Display_Optimize == 'on':  

                    box.separator()         

                    box = layout.box().column(1)   

                    row = box.column(1) 
                    
                    button_origin_obm = icons.get("icon_origin_obm")
                    row.operator("object.origin_set", "Set Origin", icon_value=button_origin_obm.icon_id).type='ORIGIN_GEOMETRY'
                
                box.separator()         

                box = layout.box().column(1)               

                row = box.column(1)   

                button_boolean_carver = icons.get("icon_boolean_carver")
                row.operator("object.carver", text="3d Carver", icon_value=button_boolean_carver.icon_id)

                box.separator()         
      


            # BRUSH BOOLEAN #
            if scene.tp_bool == "tp_02": 

                box = layout.box().column(1)

                row = box.column(1) 
                
                button_boolean_union_brush = icons.get("icon_boolean_union_brush")
                row.operator("tp_ops.tboolean_union", text="BT-Union", icon_value=button_boolean_union_brush.icon_id)            
                
                display_btbool_brush_simple = context.user_preferences.addons[__package__].preferences.tab_btbool_brush_simple_pl 
                if display_btbool_brush_simple == 'on':

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


                    row.separator()
                    row.prop(bpy.context.scene, "tp_sublocal", text="Open BT-Brush-Viewer", icon="RESTRICT_VIEW_OFF")         


                box.separator()

                
                draw_bt_config_panel_layout(context, layout) 


#                is_boolean = False   
#                            
#                for mode in bpy.context.object.modifiers :
#                    if mode.type == 'BOOLEAN' :
#                        is_boolean = True

#                if is_boolean == True:                            

                if (isCanvas(context.active_object)) or (isBrush(context.active_object)):
                
                    if 0 < len(bpy.context.selected_objects) < 2 and bpy.context.object.mode == "OBJECT":

                        box = layout.box().column(1)

                        row = box.column(1) 
                        
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




        # MULTI BOOLEAN #
            if scene.tp_bool == "tp_03": 

                tp_props = context.window_manager.tp_props_multibool 

                box = layout.box().column(1) 
               
                row = box.column(1)
                row.prop_search(tp_props, "Target", bpy.data, "objects",icon="TRIA_DOWN")
                row.prop_search(tp_props, "Tool", bpy.data, "objects",icon="TRIA_DOWN")
                
                row.separator()         
               
                row.prop(tp_props, "MMAction", text="Action")      
                row.prop(tp_props, "MMMove", text="Move")      

                row.separator() 
                
                row.prop(tp_props, "MMToolXVal", text="X")
                row.prop(tp_props, "MMToolYVal", text="Y")
                row.prop(tp_props, "MMToolZVal", text="Z")
               
                row.separator() 

                row.prop(tp_props, "NumSteps", text="Num. Steps")
                row.prop(tp_props, "StartSteps", text="Start at Step")

                box.separator() 
                
                box = layout.box().column(1) 
               
                row = box.column(1)
                row.prop(tp_props, "MMPreStep", text="Pre-Move")
                
                row.separator()         
                
                row.prop(tp_props, "MMPreStepXVal", text="X")
                row.prop(tp_props, "MMPreStepYVal", text="Y")
                row.prop(tp_props, "MMPreStepZVal", text="Z")
                
                box.separator() 

                box = layout.box().column(1) 
               
                row = box.column(1)
                row.prop(tp_props, "RepeaterCnt", text="Repeat")
                row.separator() 
                row.prop(tp_props, "ReturnToLoc", text="ReturnToLoc")

                row.separator() 
                
                row = box.row(1)        
                row.operator("reset.exec", text="Reset")       
                row.operator("tool.exec", text="Execute")
              
                box.separator() 




        if context.mode == "EDIT_MESH":
           
            row = box.row(1)  
            row.prop(scene, 'tp_bool_edm', emboss = False, expand = True) #icon_only=True,


            # DIRECT BOOLEAN #        
            if scene.tp_bool_edm == "tp_01": 

                box = layout.box().column(1)                     

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
                row.label("Planes / Circles")         

                button_axis_x = icons.get("icon_axis_x")
                row.operator("tp_ops.axis_plane",text="", icon_value=button_axis_x.icon_id).pl_axis = "axis_x"       
              
                button_axis_y = icons.get("icon_axis_y")
                row.operator("tp_ops.axis_plane",text="", icon_value=button_axis_y.icon_id).pl_axis = "axis_y"        

                button_axis_z = icons.get("icon_axis_z")
                row.operator("tp_ops.axis_plane",text="", icon_value=button_axis_z.icon_id).pl_axis = "axis_z"  

                button_axis_n = icons.get("icon_axis_n")
                row.operator("tp_ops.planefit",text="", icon_value=button_axis_n.icon_id) 

                box.separator() 

                box = layout.box().column(1)                     

                row = box.row(1) 
                
                button_boolean_facemerge = icons.get("icon_boolean_facemerge")
                row.operator("bpt.boolean_2d_union", text= "2d Union", icon_value=button_boolean_facemerge.icon_id)        
                
                box.separator() 


                display_optimize = context.user_preferences.addons[__package__].preferences.tab_optimize
                if display_optimize == 'on':   

                    box = layout.box().column(1)                          

                    row = box.column(1)  
                    
                    button_select_link = icons.get("icon_select_link")
                    row.operator("mesh.select_linked",text="Select Linked", icon_value=button_select_link.icon_id)

                    button_remove_double = icons.get("icon_remove_double")
                    row.operator("mesh.remove_doubles",text="Remove Doubles", icon_value=button_remove_double.icon_id)             

                    row.operator("mesh.normals_make_consistent", text="Recalc. Normals", icon="SNAP_NORMAL")

                    row.separator() 

                    button_origin_edm = icons.get("icon_origin_edm")
                    row.operator("tp_ops.origin_edm",text="Set Origin", icon_value=button_origin_edm.icon_id)
                   
                    box.separator()



            # BRUSH BOOLEAN #
            if scene.tp_bool_edm == "tp_02": 

                box = layout.box().column(1)

                row = box.column(1) 
                
                button_boolean_bridge = icons.get("icon_boolean_bridge")
                row.operator("mesh.edges_select_sharp", text="SharpEdges", icon_value=button_boolean_bridge.icon_id)    

                button_boolean_edge = icons.get("icon_boolean_edge")
                row.operator("object.boolean_bevel_custom_edge", text="CustomEdges", icon_value=button_boolean_edge.icon_id)
            
                row.operator("object.boolean_bevel_remove_objects", text="Remove Guides", icon='GHOST_DISABLED')        
                
                #button_boolean_bridge = icons.get("icon_boolean_bridge")
                #row.operator("object.boolean_bevel_bridge", text="Bridge Edge", icon_value=button_boolean_bridge.icon_id)
                



# LOAD UI #
class VIEW3D_TP_Edit_Boolean_Panel_TOOLS(bpy.types.Panel,draw_boolean_layout):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Edit_Boolean_Panel_TOOLS"
    bl_label = "Boolean"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}    

class VIEW3D_TP_Edit_Boolean_Panel_UI(bpy.types.Panel,draw_boolean_layout):
    bl_idname = "VIEW3D_TP_Edit_Boolean_Panel_UI"
    bl_label = "Boolean"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

