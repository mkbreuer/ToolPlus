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


import bpy
from bpy import *
from bpy.props import *



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


#class VIEW3D_TP_BoolTool_Config_TOOLS(bpy.types.Panel):
#    bl_category = "T+"
#    bl_idname = "VIEW3D_TP_BoolTool_Config_TOOLS"
#    bl_label = "BT Props"
#    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'TOOLS'
#    bl_context = "objectmode"
#    bl_options = {'DEFAULT_CLOSED'}

#    @classmethod
#    def poll(cls, context):
#        isModelingMode = not (
#        context.sculpt_object or 
#        context.vertex_paint_object
#        or context.weight_paint_object
#        or context.image_paint_object)
#        obj = context.active_object     
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM:        
#                return isModelingMode 
#    
#    @classmethod
#    def poll(cls, context):

#        result = False
#        actObj = bpy.context.active_object
#        if (isCanvas(actObj) or isBrush(actObj) or isPolyBrush(actObj)):
#            result = True
#        return result

#    def draw(self, context):
#        layout = self.layout.column_flow(1)  
#        layout.operator_context = 'INVOKE_REGION_WIN'

#        draw_bt_config_panel_layout(self, context, layout) 
#               


#class VIEW3D_TP_BoolTool_Config_UI(bpy.types.Panel):
#    bl_idname = "VIEW3D_TP_BoolTool_Config_UI"
#    bl_label = "BT Props"
#    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'UI'
#    bl_context = "objectmode"
#    bl_options = {'DEFAULT_CLOSED'}

#    @classmethod
#    def poll(cls, context):
#        isModelingMode = not (
#        context.sculpt_object or 
#        context.vertex_paint_object
#        or context.weight_paint_object
#        or context.image_paint_object)
#        obj = context.active_object     
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM:        
#                return isModelingMode 
#    
#    @classmethod
#    def poll(cls, context):

#        result = False
#        actObj = bpy.context.active_object
#        if (isCanvas(actObj) or isBrush(actObj) or isPolyBrush(actObj)):
#            result = True
#        return result


#    def draw(self, context):
#        layout = self.layout.column_flow(1)  
#        layout.operator_context = 'INVOKE_REGION_WIN'

#        draw_bt_config_panel_layout(self, context, layout) 



#def draw_bt_config_panel_layout(self, context, layout):
#    
#        actObj = bpy.context.active_object
#        icon = ""

#        box = layout.box().column(1)
#         
#        row = box.row(1)              
#        # CANVAS ---------------------------------------------------
#        if isCanvas(actObj):
#            row.label("CANVAS", icon="MESH_GRID")
#            
#            row = box.row()
#            row.prop(context.scene, 'BoolHide', text="Hide Bool objects")
#            
#            row = box.row(True)
#            row.operator("btool.to_mesh", icon="MOD_LATTICE", text="Apply All")

#            row = box.row(True)
#            Rem = row.operator("btool.remove", icon="CANCEL", text="Remove All")
#            Rem.thisObj = ""
#            Rem.Prop = "CANVAS"

#            if isBrush(actObj):
#                layout.separator()

#        # BRUSH ------------------------------------------------------
#        if isBrush(actObj):

#            if (actObj["BoolToolBrush"] == "UNION"):
#                icon = "ROTATECOLLECTION"
#            if (actObj["BoolToolBrush"] == "DIFFERENCE"):
#                icon = "ROTATECENTER"
#            if (actObj["BoolToolBrush"] == "INTERSECT"):
#                icon = "ROTACTIVE"
#            if (actObj["BoolToolBrush"] == "SLICE"):
#                icon = "ROTATECENTER"


#            row = box.row(True)
#            row.label("BRUSH", icon=icon)
#            # layout.separator()

#            icon = ""
#            if actObj["BoolTool_FTransform"] == "True":
#                icon = "PMARKER_ACT"
#            else:
#                icon = "PMARKER"
#            if isFTransf():
#                pass

#            if isFTransf():
#                row = box.row(True)
#                row.operator(BTool_EnableFTransform.bl_idname, text="Fast Vis", icon=icon)
#                Enable = row.operator(BTool_EnableThisBrush.bl_idname, text="Enable", icon="VISIBLE_IPO_ON")
#                row = box.row(True)
#            else:
#                Enable = row.operator(BTool_EnableThisBrush.bl_idname, icon="VISIBLE_IPO_ON")
#                row = box.row(True)

#        if isPolyBrush(actObj):
#            row = box.row(False)
#            row.label("POLY BRUSH", icon="LINE_DATA")
#            mod = actObj.modifiers["BTool_PolyBrush"]
#            row = box.row(False)
#            row.prop(mod, "thickness", text="Size")
#            layout.separator()

#        if isBrush(actObj):
#            row = box.row(True)
#            row.operator("btool.brush_to_mesh", icon="MOD_LATTICE", text="Apply Brush")
#            row = box.row(True)
#            Rem = row.operator("btool.remove", icon="CANCEL", text="Remove Brush")
#            Rem.thisObj = ""
#            Rem.Prop = "BRUSH"

#        box.separator()












# LOAD UI: PANEL #

GEOM = ['MESH']

class draw_bool_panel_layout:
    
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
                return isModelingMode 
    
    @classmethod
    def poll(cls, context):
        actObj = bpy.context.active_object

        if isCanvas(actObj):
            return context.scene.tp_sublocal
            #return True 
        else:
            return False


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        actObj = bpy.context.active_object
        icon = ""

        if isCanvas(actObj):

            for mod in actObj.modifiers:
                container = self.layout.box()
                row = container.row(True)
                icon = ""
                if ("BTool_" in mod.name):
                  
                    if (mod.operation == "UNION"):

                        icon = "ROTATECOLLECTION"
                   
                    if (mod.operation == "DIFFERENCE"):

                        icon = "ROTATECENTER"
                   
                    if (mod.operation == "INTERSECT"):

                        icon = "ROTACTIVE"
                   
                    if (mod.operation == "SLICE"):

                        icon = "ROTATECENTER"


                    objSelect = row.operator("btool.find_brush", text=mod.object.name, icon=icon, emboss=False)
                    objSelect.obj = mod.object.name

                    EnableIcon = "RESTRICT_VIEW_ON"
                    if (mod.show_viewport):
                        EnableIcon = "RESTRICT_VIEW_OFF"
                    Enable = row.operator(BTool_EnableBrush.bl_idname, icon=EnableIcon, emboss=False)
                    Enable.thisObj = mod.object.name

                    Remove = row.operator("btool.remove", icon="CANCEL", emboss=False)
                    Remove.thisObj = mod.object.name
                    Remove.Prop = "THIS"

                    # Stack Changer
                    Up = row.operator("btool.move_stack", icon="TRIA_UP", emboss=False)
                    Up.modif = mod.name
                    Up.direction = "UP"

                    Dw = row.operator("btool.move_stack", icon="TRIA_DOWN", emboss=False)
                    Dw.modif = mod.name
                    Dw.direction = "DOWN"

                else:
                    row.label(mod.name)
                    # Stack Changer
                    Up = row.operator("btool.move_stack", icon="TRIA_UP", emboss=False)
                    Up.modif = mod.name
                    Up.direction = "UP"

                    Dw = row.operator("btool.move_stack", icon="TRIA_DOWN", emboss=False)
                    Dw.modif = mod.name
                    Dw.direction = "DOWN"


                    


class VIEW3D_TP_BoolTool_BViewer_TOOLS(bpy.types.Panel, draw_bool_panel_layout):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_BoolTool_BViewer_TOOLS"
    bl_label = "BT-Brushes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_BoolTool_BViewer_UI(bpy.types.Panel, draw_bool_panel_layout):
    bl_idname = "VIEW3D_TP_BoolTool_BViewer_UI"
    bl_label = "BT-Brushes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}
