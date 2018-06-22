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


# MENUS #  

class VIEW3D_TP_Curve_Add_2D_Curves(bpy.types.Menu):
    bl_idname = "tp_menu.curve_add_2d"
    bl_label = "2D Curves"

    def draw(self, context):
        layout = self.layout        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()       

        col = split.column()
        col.scale_y = 1.2     
        col.operator("tp_ops.edge_profil", text="Profils")
        col.operator("curve.simple", text="Point").Simple_Type="Point"
        col.operator("curve.simple", text="Distance").Simple_Type="Distance"    
        col.operator("curve.simple", text="Circle").Simple_Type="Circle"        
        col.operator("curve.simple", text="Arc").Simple_Type="Arc"       
        col.operator("curve.simple", text="Segment").Simple_Type="Segment"    
        col.operator("curve.simple", text="Rhomb").Simple_Type="Rhomb"
        col.operator("curve.simple", text="PolygonAB").Simple_Type="Polygon_ab"


        col = split.column()
        col.scale_y = 1.2    
        col.operator("mesh.curveaceous_galore", text="Galore")
        col.operator("curve.simple", text="Line").Simple_Type="Line"    
        col.operator("curve.simple", text="Angle").Simple_Type="Angle"        
        col.operator("curve.simple", text="Ellipse").Simple_Type="Ellipse"
        col.operator("curve.simple", text="Sector").Simple_Type="Sector"
        col.operator("curve.simple", text="Rectangle").Simple_Type="Rectangle"
        col.operator("curve.simple", text="Polygon").Simple_Type="Polygon"
        col.operator("curve.simple", text="Trapezoid").Simple_Type="Trapezoid"


class VIEW3D_TP_Curve_Add_2D_Curves_Profils(bpy.types.Menu):
    bl_idname = "tp_menu.curve_add_2d_profils"
    bl_label = "2D Profils"

    def draw(self, context):
        layout = self.layout        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()       

        col = split.column()
        col.scale_y = 1.2     
        col.operator("tp_ops.edge_profil", text="Bevel_1").profil_typ="profil_01"
        col.operator("tp_ops.edge_profil", text="Car").profil_typ="profil_03"
        col.operator("tp_ops.edge_profil", text="Double").profil_typ="profil_05"        
        col.operator("tp_ops.edge_profil", text="Inlay_2").profil_typ="profil_07"       
        col.operator("tp_ops.edge_profil", text="Norman").profil_typ="profil_09"    
        col.operator("tp_ops.edge_profil", text="Nose_2").profil_typ="profil_11"
        col.operator("tp_ops.edge_profil", text="Round_50").profil_typ="profil_13"
        col.operator("tp_ops.edge_profil", text="Round_100").profil_typ="profil_15"
        col.operator("tp_ops.edge_profil", text="Shoe").profil_typ="profil_17"


        col = split.column()
        col.scale_y = 1.2    
        col.operator("tp_ops.edge_profil", text="Bevel_2").profil_typ="profil_02"
        col.operator("tp_ops.edge_profil", text="Cornice").profil_typ="profil_04"    
        col.operator("tp_ops.edge_profil", text="Inlay_1").profil_typ="profil_06"        
        col.operator("tp_ops.edge_profil", text="Inlay_3").profil_typ="profil_08"
        col.operator("tp_ops.edge_profil", text="Nose_1").profil_typ="profil_10"
        col.operator("tp_ops.edge_profil", text="Quad").profil_typ="profil_12"
        col.operator("tp_ops.edge_profil", text="Round_75").profil_typ="profil_14"
        col.operator("tp_ops.edge_profil", text="Round_Up").profil_typ="profil_16"
        col.operator("tp_ops.edge_profil", text="Smooth").profil_typ="profil_18"



class VIEW3D_TP_Curve_Add_3D_Curves(bpy.types.Menu):
    bl_idname = "tp_menu.curve_add_3d"
    bl_label = "3D Curves"

    def draw(self, context):
        layout = self.layout        
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()
      
        split = layout.split()       

        col = split.column()
        col.scale_y = 1.2     
        col.operator("curve.spirals", text="Spirals")
        col.operator("curve.wires", text="Wires")
        col.operator("object.pipe_nightmare", text="PipeTech")
        col.operator("object.add_catenary_curve", text="Catenary")
        col.operator("mesh.primitive_tube_add", text="Tupe")  
            
        col = split.column()
        col.scale_y = 1.2   
        col.operator("curve.curlycurve", text="Curly") 
        col.operator("curve.formulacurves", text="Formula")
        col.operator("curve.dial_scale", text="Dial/Scale")            
        col.operator("mesh.primitive_pipe_add", text="Pipe")    
        col.operator("mesh.convert_pipe_to_mesh", text="Apply Pipe")    



class VIEW3D_TP_Curve_Add_Plants(bpy.types.Menu):
    bl_idname = "tp_menu.curve_add_plants"
    bl_label = "Plants"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("curve.tree_add", text="Sapling Tree")       
        layout.operator("mesh.add_iterative_tree", text="Iterative Tree")

        obj = context.active_object
        if obj:
            obj_type = obj.type                
            if obj.type in {'CURVE'}: 
                
                show = bpy.context.object.data.dimensions
                if show == '3D':
                     
                    active_bevel = bpy.context.object.data.bevel_depth            
                    if active_bevel == 0.0:         
                       pass
                    else:      
                      layout.operator("mesh.addleaves", text="Iterative Leaves")   


        layout.operator("curve.ivy_gen", text="Ivy to Mesh").updateIvy = True   



class VIEW3D_TP_Curve_Add_Knots(bpy.types.Menu):    
    bl_idname = "tp_menu.curve_add_knots"
    bl_label = "Knots"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

                 
        layout.operator("curve.torus_knot_plus", text="Torus")
        layout.operator("mesh.add_braid", text="Braid")
        
        layout.operator("curve.celtic_links", text="Celtic")
        layout.operator("object.add_bounce_spline", text="Bounce")
        
        layout.operator("object.add_spirofit_spline", text="SpiroFit")            
        

        
class VIEW3D_TP_Surface_Add_Factory(bpy.types.Menu):    
    bl_idname = "tp_menu.curve_add_factory"
    bl_label = "Factory"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
            
        layout.operator("object.add_surface_wedge", text="Wedge")
        layout.operator("object.add_surface_cone", text="Cone")
        layout.operator("object.add_surface_star", text="Star")
        layout.operator("object.add_surface_plane", text="Plane")

        layout.separator()
        
        layout.operator("curve.smooth_x_times", text="nSmooth")


                   
                                             