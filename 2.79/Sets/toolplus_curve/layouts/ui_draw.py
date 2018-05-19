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
from .. icons.icons import load_icons    


def draw_draw_ui(self, context, layout):

    tp_props = context.window_manager.tp_props_curve  

    icons = load_icons()       
    my_button_one = icons.get("icon_image1")
    
    col = layout.column(1)

    box = col.box().column(1)                   

    box.separator()          
    box.separator() 

    row = box.row(1) 
    sub = row.row(1)
    sub.alignment = 'CENTER'    
    sub.scale_x = 2  
    sub.scale_y = 1.7   
  

    if context.mode == 'EDIT_CURVE':

        button_draw_bevel = icons.get("icon_draw_bevel")
        sub.operator("tp_ops.curve_draw", text="", icon_value=button_draw_bevel.icon_id)  
        
        button_draw_brush = icons.get("icon_draw_brush")
        sub.operator("curve.draw", text="", icon ="LINE_DATA") #icon_value=button_draw_brush.icon_id)  

    else:
        
        button_draw_lathe = icons.get("icon_draw_lathe")     
        sub.operator("tp_ops.curve_lathe", text="", icon_value=button_draw_lathe.icon_id)   

        button_draw_surface = icons.get("icon_draw_surface")     
        sub.operator("tp_ops.curve_draw", text="", icon_value=button_draw_surface.icon_id).mode ='surface' 

        button_draw_curve = icons.get("icon_draw_curve")     
        sub.operator("tp_ops.curve_draw", text="", icon_value=button_draw_curve.icon_id).mode ='cursor'      

        button_draw_bevel = icons.get("icon_draw_bevel")
        sub.operator("tp_ops.curve_draw", text="", icon_value=button_draw_bevel.icon_id)  


    box.separator()    
    box.separator()    

    row = box.row(1)
    row.scale_y = 1.2
    scene = context.scene  
    
    if tp_props.display_curve_options: 
        row.prop(tp_props, "display_curve_options", text="", icon="SCRIPTWIN", toggle=True)#, emboss = False)                        
    else:
        row.prop(tp_props, "display_curve_options", text="", icon="SCRIPTWIN", toggle=True)#, emboss = False)   
        
    row.label("Settings")

    row.operator("tp_ops.origin_2d", text="", icon='LAYER_ACTIVE')   

    button_curve_extrude = icons.get("icon_curve_extrude")        
    row.operator("tp_ops.curve_extrude", text="", icon_value=button_curve_extrude.icon_id)      

    obj = context.active_object     
    if obj:
       obj_type = obj.type
       if obj_type in {'CURVE'}:

        active_bevel = bpy.context.object.data.bevel_depth            
        if active_bevel == 0.0:              
            row.operator("tp_ops.enable_bevel", text="", icon='MOD_WARP')
        else:   
            row.operator("tp_ops.enable_bevel", text="", icon='MOD_WARP')    

    #row.prop(scene, "add_bevel", text ="", icon="MOD_WARP")   

    box.separator()

    row = box.row(1)
    row.scale_y = 1.2                  
    tool_settings = context.tool_settings
    cps = tool_settings.curve_paint_settings
    row.prop(cps, "radius_taper_start", text="Start")
    row.prop(cps, "radius_taper_end", text="End")

    box.separator()          
    box.separator()                           
                                                         
    row = box.row(1)
    row.scale_y = 1                             
    row.prop(scene.tp_props_insert, "add_mat", text ="")                 
    row.label(text="Add Color:")  
   
    row.prop(scene.tp_props_insert, "add_objmat", text ="", icon="GROUP_VCOL")                   
    
    obj = context.active_object
   
    if scene.tp_props_insert.add_random == False:       
        if scene.tp_props_insert.add_objmat == False:                     
            if bpy.context.scene.render.engine == 'CYCLES':
                row.prop(scene.tp_props_insert, "add_cyclcolor", text ="")        
            else:
                row.prop(scene.tp_props_insert, "add_color", text ="")       
        else:
            
            if obj:    
                if context.object.active_material:  
                    row.prop(context.object.active_material, "diffuse_color", text="")
                else:
                    row.label(text="")   
            else:
                pass               
    else:
       
        if scene.tp_props_insert.add_objmat == False:                            
            
            if bpy.context.scene.render.engine == 'CYCLES':
                row.prop(scene.tp_props_insert, "add_cyclcolor", text ="")        
            else:
                row.prop(scene.tp_props_insert, "add_color", text ="")                                                   
        
        else:                           
       
            if obj:   
                if context.object.active_material:  
                    row.prop(context.object.active_material, "diffuse_color", text="")
                else:
                    row.label(text="")            
            else:
                pass
                   
    row.prop(scene.tp_props_insert, "add_random", text ="", icon="FILE_REFRESH")
  
   
    obj = context.active_object     
    if obj:
       
        if len(context.object.material_slots) > 0:

            box.separator()
            
            row = box.row(1)
            row.scale_y = 1                                 
            row.label("Obj-Color")            
            if bpy.context.scene.render.engine == 'CYCLES':
                row.prop(context.object.active_material, "diffuse_color", text="")  
            else: 
                row.prop(context.object, "color", text="")                     
            
            active_objcolor = bpy.context.object.active_material.use_object_color
            if active_objcolor == True:
                row.prop(context.object.active_material, "use_object_color", text="", icon = 'OUTLINER_OB_LAMP')              
            else:                       
                row.prop(context.object.active_material, "use_object_color", text="", icon = 'OUTLINER_DATA_LAMP')  
                                
            box.separator()  

        else:
            pass   
    else:
        pass     
                         
    box.separator()
                       
  

    if tp_props.display_curve_options: 
        
        tool_settings = context.tool_settings
        cps = tool_settings.curve_paint_settings

        box = col.box().column(1)   

        box.separator()
       
        col = box.column()
        col.scale_y = 1.2
        col.prop(cps, "curve_type")
 
        if cps.curve_type == 'BEZIER':
            
            col.separator()            
            
            col.label("Bezier Options:")
            
            col.separator()
            
            col.prop(cps, "error_threshold")
            col.prop(cps, "fit_method")
            col.prop(cps, "use_corners_detect")
            col.active = cps.use_corners_detect
            col.prop(cps, "corner_angle")

        box.separator()
       
        col = box.column()
        col.label("Pressure Radius:")
        
        row = box.row(align=True)
        row.scale_y = 1.2
        rowsub = row.row(align=True)
        rowsub.prop(cps, "radius_min", text="Min")
        rowsub.prop(cps, "radius_max", text="Max")

        row.prop(cps, "use_pressure_radius", text="", icon_only=True)

        box.separator()

        col = box.column()
        col.label("Taper Radius:")
       
        row = box.row(align=True)
        row.scale_y = 1.2
        row.prop(cps, "radius_taper_start", text="Start")
        row.prop(cps, "radius_taper_end", text="End")


        box.separator()

        col = box.column()
        col.label("Projection Depth:")
        
        row = box.row(align=True)
        row.scale_y = 1.2
        row.prop(cps, "depth_mode", expand=True)

        col = box.column()
        col.scale_y = 1.2
        if cps.depth_mode == 'SURFACE':
            col.prop(cps, "surface_offset")
            col.prop(cps, "use_offset_absolute")
            col.prop(cps, "use_stroke_endpoints")
            
            if cps.use_stroke_endpoints:
                colsub = box.column(align=True)
                colsub.prop(cps, "surface_plane", expand=True)

        box.separator()

















class VIEW3D_TP_Curve_Draw_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Draw_Panel_TOOLS"
    bl_label = "Draw"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_draw_ui(self, context, layout)



class VIEW3D_TP_Curve_Draw_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Draw_Panel_UI"
    bl_label = "Draw"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'
         
         draw_draw_ui(self, context, layout)


