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




def draw_curve_convert_panel_layout(self, context, layout):
    
        icons = load_icons()     
        my_button_one = icons.get("icon_image1")
        
        obj = context.active_object  
        
        box = layout.box().column(1) 
                
        row = box.row(1)                                                          
        row.operator("tp_ops.wire_all", text="Wire all", icon='WIRE')
        
        obj = context.active_object
        if obj:
            active_wire = obj.show_wire 
            if active_wire == True:
                row.operator("tp_ops.wire_off", "Wire Select", icon = 'MESH_PLANE')              
            else:                       
                row.operator("tp_ops.wire_on", "Wire Select", icon = 'MESH_GRID')
        else:
            row.label("", icon="BLANK1")            
       
        row = box.row(1)
        
        obj = context.active_object
        if obj:               
            if obj.draw_type == 'WIRE':
                row.operator("tp_ops.draw_solid", text="Solid on", icon='GHOST_DISABLED')     
            else:
                row.operator("tp_ops.draw_wire", text="Solid off", icon='GHOST_ENABLED')        
        else:
            row.label("", icon="BLANK1")  
 
        ob = context.object
        if ob: 
            row.prop(ob, "draw_type", text="")
            
            row = box.row(1)
            row.prop(ob, "show_bounds", text="ShowBounds", icon='STICKY_UVS_LOC') 
            row.prop(ob, "draw_bounds_type", text="")    
       
        else:
            row.label("", icon="BLANK1") 

        
        if context.mode == 'EDIT_MESH':          
            
            box.separator() 
            
            row = box.row(1)  
            row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
            row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 
            
            row = box.row(1)  
            row.operator("mesh.normals_make_consistent", text="Consistent Normals", icon="SNAP_NORMAL")  
        
        else:            
            
            box.separator() 
            
            if context.mode == 'OBJECT': 
                
                row = box.row(1)  
                row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
           
            row = box.row(1)  
            row.operator("tp_ops.rec_normals", text="Consistent Normals", icon="SNAP_NORMAL")  

        box.separator() 



class VIEW3D_TP_Curve_Convert_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Convert_Panel_TOOLS"
    bl_label = "Convert"
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
            return (isModelingMode)

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_curve_convert_panel_layout(self, context, layout)


class VIEW3D_TP_Curve_Convert_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Convert_Panel_UI"
    bl_label = "Convert"
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
            return (isModelingMode)

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'         

         draw_curve_convert_panel_layout(self, context, layout)



# Registry               

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


