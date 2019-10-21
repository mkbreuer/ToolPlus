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


import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



class VIEW3D_TP_Spline_Type_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_spline_type"
    bl_label = "Spline Type"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        if context.mode == 'EDIT_CURVE':

            layout.operator("curve.spline_type_set", "Poly").type = 'POLY'     
            layout.operator("curve.spline_type_set", "Nurbs").type = 'NURBS'          
            layout.operator("curve.spline_type_set", "Bezier").type = 'BEZIER' 

        else:
            
            layout.operator("curve.to_poly","Poly")
            layout.operator("curve.to_nurbs","Nurbs")
            layout.operator("curve.to_bezier","Bezièr")


            

class VIEW3D_TP_Handle_Type_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_handle_type"
    bl_label = "Handle Type"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        

        if context.mode == 'EDIT_CURVE':

            layout.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
            layout.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'
            layout.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'  
            layout.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'

        else:
            
            layout.operator("curve.handle_to_automatic","Auto")                                                  
            layout.operator("curve.handle_to_free","Free") 
            layout.operator("curve.handle_to_vector","Vector") 
            layout.operator("curve.handle_to_aligned","Align")




# Define the "Extras" menu
class INFO_MT_curve_plants_add(bpy.types.Menu):
    bl_idname = "curve_plants_add"
    bl_label = "Plants"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.operator("curve.tree_add", text="Sapling 3")
       
        self.layout.operator("curve.ivy_gen", text="Add Ivy to Mesh").updateIvy = True



# Define the "Extras" menu
class INFO_MT_curve_knots_add(bpy.types.Menu):
    bl_idname = "curve_knots_add"
    bl_label = "Plants"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.operator("curve.torus_knot_plus", text="Torus Knot Plus")
        layout.operator("curve.celtic_links", text="Celtic Links")
        layout.operator("mesh.add_braid", text="Braid Knot")



# Define the "Extras" menu
class INFO_MT_curve_extras_add(bpy.types.Menu):    
    bl_idname = "curve_extra_objects_add"
    bl_label = "Extra Objects"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.operator("mesh.curveaceous_galore", text="Curves Galore!")
        layout.operator("curve.spirals", text="Spirals")
        layout.operator("curve.curlycurve", text="Curly Curve")
        layout.operator("curve.formulacurves", text="Formula Curve")
        layout.operator("curve.wires", text="Curve Wires")
        
        layout.separator()
        
        layout.label(text="Curve Utils")
        
        layout.operator("curve.simplify", text="Simplify Curves")
        layout.operator("curve.dial_scale", text="Dial/Scale")



# Define "Extras" menu
def menu(self, context):
    layout = self.layout
    
    col = layout.column()
    self.layout.separator()
    
    layout.label(text="AF: Curve Objects", icon="OUTLINER_OB_CURVE")
    
    self.layout.menu("curve_plants_add", text="Plants", icon="CURVE_DATA")
    self.layout.menu("curve_knots_add", text="Knots", icon='CURVE_DATA')
    self.layout.operator("mesh.curveaceous_galore", text="Curves Galore!", icon="CURVE_DATA")
    self.layout.operator("curve.spirals", text="Spirals", icon="CURVE_DATA")
    self.layout.operator("curve.curlycurve", text="Curly Curve", icon="CURVE_DATA")
    self.layout.operator("curve.formulacurves", text="Formula Curve", icon="CURVE_DATA")
    self.layout.operator("curve.wires", text="Curve Wires", icon="CURVE_DATA")
    self.layout.operator("curve.dial_scale", text="Dial/Scale", icon="CURVE_DATA")
    
    self.layout.separator()
    
    layout.label(text="Curve Utils")
    self.layout.operator("curve.simplify", text="Curve Simplify", icon="CURVE_DATA")




# Define the "Extras" menu
def menu_surface(self, context):
    layout = self.layout
    
    col = layout.column()
    self.layout.separator()
    
    layout.label(text="Surface Factory")
    
    self.layout.operator("object.add_surface_wedge", text="Wedge", icon="MOD_CURVE")
    self.layout.operator("object.add_surface_cone", text="Cone", icon="MOD_CURVE")
    self.layout.operator("object.add_surface_star", text="Star", icon="MOD_CURVE")
    self.layout.operator("object.add_surface_plane", text="Plane", icon="MOD_CURVE")
    self.layout.operator("curve.smooth_x_times", text="Special Smooth", icon="MOD_CURVE")


#add a menu to ui
def draw_beveled_curve(self, context):
    layout = self.layout
    
    col = layout.column()
    layout.separator() 

    if context.mode == 'OBJECT':      
        layout.operator("tp_ops.bevel_set","Beveled Setup", icon = "MOD_CURVE")
            
    show = bpy.context.object.data.dimensions
    if show == '3D':
         
        active_bevel = bpy.context.object.data.bevel_depth            
        if active_bevel == 0.0:              
            layout.operator("tp_ops.enable_bevel", text="CurveBevel on", icon='MOD_WARP')
        else:   
            layout.operator("tp_ops.enable_bevel", text="CurveBevel off", icon='MOD_WARP')  



# REGISTRY #        

def register():

    bpy.utils.register_module(__name__)

    # Add "Extras" menu to the "Add Primitiv" menu
    #bpy.types.INFO_MT_curve_add.append(menu)
    #bpy.types.INFO_MT_surface_add.append(menu_surface)
    #bpy.types.GRAPH_MT_channel.append(curve_simplify.menu_func)
    #bpy.types.DOPESHEET_MT_channel.append(curve_simplify.menu_func)


def unregister():

    bpy.utils.unregister_module(__name__)

    # Remove "Extras" menu from the "Add Primitiv" menu.
    #bpy.types.INFO_MT_curve_add.remove(menu)
    #bpy.types.INFO_MT_surface_add.remove(menu_surface)
    #bpy.types.GRAPH_MT_channel.remove(curve_simplify.menu_func)
    #bpy.types.DOPESHEET_MT_channel.remove(curve_simplify.menu_func)


if __name__ == "__main__":
    register()


