43# ##### BEGIN GPL LICENSE BLOCK #####
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
__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



def draw_curve_bevel_panel_layout(self, context, layout):

        icons = load_icons()       
        my_button_one = icons.get("icon_image1")
        
        if context.mode == 'EDIT_CURVE':

             box = layout.box().column(1)

             row = box.row(1)
             row.alignment = 'CENTER' 
             row.label("Bevel Curve") 
             
             row = box.row(1)        
             row.prop(context.object.data, "fill_mode", text="")           
             show = bpy.context.object.data.dimensions
             if show == '3D':
                 
                 active_bevel = bpy.context.object.data.bevel_depth            
                 if active_bevel == 0.0:              
                    row.operator("tp_ops.enable_bevel", text="Bevel on", icon='MOD_WARP')
                 else:   
                    row.operator("tp_ops.enable_bevel", text="Bevel off", icon='MOD_WARP')  
                 
             row = box.row(1)               
             row.prop(context.object.data, "use_fill_deform")

             box = layout.box().column(1)
             
             row = box.row(1)
 
             row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                               
             row.prop(context.object.data, "bevel_depth", text="Bevel")
             active_wire = bpy.context.object.show_wire 
             if active_wire == True:
                row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
             else:                       
                 row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID')   

             
             row = box.row(1)
             row.prop(context.object.data, "resolution_u", text="Rings")          
             row.prop(context.object.data, "bevel_resolution", text="Loops")

             row = box.row(1)
             row.prop(context.object.data, "offset")
             row.prop(context.object.data, "extrude","Height") 
            
             box.separator()  
                                   
             row = box.column_flow(2)
             row.label("Value Rings", icon = "MOD_CURVE")  
             row.label("1 = 4",) 
             row.label("2 = 8") 
             row.label("4 = 16") 
             row.label("8 = 32")
             row.label("(+4) Ring")          

             row.label("Value Loops", icon = "MOD_CURVE")  
             row.label("0 = 4",) 
             row.label("6 = 16") 
             row.label("10 = 24") 
             row.label("14 = 32")           
             row.label("(+2) Loop")    
                            
             box = layout.box().column(1)
             
             row = box.row(1) 
             row.label(text="Bevel Factor:")
         
             row.active = (context.object.data.bevel_depth > 0 or context.object.data.bevel_object is not None)

             row = box.row(1) 
             row.prop(context.object.data, "bevel_factor_start", text="Start") 
             row.prop(context.object.data, "bevel_factor_end", text="End")  

             row = box.row(1) 
             row.prop(context.object.data, "bevel_factor_mapping_start", text="")
             row.prop(context.object.data, "bevel_factor_mapping_end", text="")
                      
             row = box.row(1)                      
             sub = row.row()
             sub.active = context.object.data.taper_object is not None
             sub.prop(context.object.data, "use_map_taper")

             sub = row.row()
             sub.active = context.object.data.bevel_object is not None
             sub.prop(context.object.data, "use_fill_caps")

             box = layout.box().column(1)
             
             row = box.row(1)  
             row.label(text="Taper:")
             row.prop(context.object.data, "taper_object", text="")
             
             row = box.row(1) 
             row.label(text="Bevel:")
             row.prop(context.object.data, "bevel_object", text="")

             box = layout.box().column(1)

             row = box.row(1) 
             row.alignment = 'CENTER' 
             row.label(text="Path / Curve-Deform")

             row = box.row(1)
             row.prop(context.object.data, "use_radius")
             row.prop(context.object.data, "use_stretch")
             
             row = box.row(1)
             row.prop(context.object.data, "use_deform_bounds")
             
             row = box.row(1)
             row.alignment = 'CENTER' 
             row.label(text="Twisting")

             row = box.row(1) 
             row.active = (context.object.data.dimensions == '2D' or (context.object.data.bevel_object is None and context.object.data.dimensions == '3D'))
             row.prop(context.object.data,"twist_mode", text="")
             row.prop(context.object.data, "twist_smooth", text="Smooth")

             ###
             box.separator()   

        else:  
                      
             box = layout.box().column(1)   
         
             row = box.row(1)        
             row.prop(context.object.data, "fill_mode", text="")           
            
             show = bpy.context.object.data.dimensions
             if show == '3D':
                 
                 active_bevel = bpy.context.object.data.bevel_depth            
                 if active_bevel == 0.0:              
                    row.operator("tp_ops.enable_bevel", text="Bevel on", icon='MOD_WARP')
                 else:   
                    row.operator("tp_ops.enable_bevel", text="Bevel off", icon='MOD_WARP')                 
                          
             row = box.row(1)                          
             row.prop(context.object.data, "use_fill_deform")

             box = layout.box().column(1)   
             
             row = box.row(1) 
             row = box.row(1)
             active_wire = bpy.context.object.show_wire 
             row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
             row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
             if active_wire == True:
                row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
             else:                       
                 row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 
            
             row = box.row(1)
             row.prop(context.object.data, "resolution_u", text="Rings")          
             row.prop(context.object.data, "bevel_resolution", text="Loops")

             row = box.row(1)
             row.prop(context.object.data, "offset")
             row.prop(context.object.data, "extrude","Height")
            
             box.separator()  
                                   
             row = box.column_flow(2)
             row.label("Value Rings", icon = "PROP_CON")  
             row.label("1 = 4",) 
             row.label("2 = 8") 
             row.label("4 = 16") 
             row.label("8 = 32")
             row.label("(+4) Rings")          

             row.label("Value Loops", icon = "COLLAPSEMENU")  
             row.label("0 = 4",) 
             row.label("3 = 8") 
             row.label("4 = 12") 
             row.label("8 = 16")           
             row.label("(+2) Loop")                                 

             box.separator() 

             box = layout.box().column(1)

             row = box.row(1)              
             row.alignment = 'CENTER'
             row.label("Bevel & Taper", icon = "MOD_CURVE")    
            
             box.separator()
              
             row = box.row(1)
             row.operator("curve.bevelcurve", "C-Bevel", icon = "CURVE_BEZCIRCLE") 
             row.prop(context.object.data, "bevel_object", text = "")
             
             row = box.row(1)
             row.operator("curve.tapercurve", "C-Taper", icon = "CURVE_BEZCURVE") 
             row.prop(context.object.data, "taper_object", text = "")
     
             box.separator() 

             box = layout.box().column(1)

             row = box.row(1)              
             row.alignment = 'CENTER'
             row.label("Bevel Factor", icon = "MOD_CURVE")    
            
             box.separator()
            
             row = box.row(1) 
             row.prop(context.object.data, "bevel_factor_start", text="Start") 
             row.prop(context.object.data, "bevel_factor_end", text="End")  

             row = box.row(1) 
             row.prop(context.object.data, "bevel_factor_mapping_start", text="")
             row.prop(context.object.data, "bevel_factor_mapping_end", text="")    

             box.separator() 

             box = layout.box().column(1)  

             row = box.row(1) 
             row.alignment = 'CENTER'
             row.label(text="Path / Deform / Twist:")

             box.separator() 

             row = box.row(1)
             row.prop(context.object.data, "use_radius")
             row.prop(context.object.data, "use_stretch")
             row = box.row(1)
             row.prop(context.object.data, "use_deform_bounds")   
            
             row = box.row(1)                        
             row.prop(context.object.data,"twist_mode", text="")
             row.prop(context.object.data, "twist_smooth", text="Smooth")    
            
             ###
             box.separator()                                    
     




class VIEW3D_TP_Curve_Bevel_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Bevel_Panel_TOOLS"
    bl_label = "Bevel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_curve_bevel_panel_layout(self, context, layout)



class VIEW3D_TP_Curve_Bevel_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Bevel_Panel_UI"
    bl_label = "Bevel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'
         
         draw_curve_bevel_panel_layout(self, context, layout)






# Registry               

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


