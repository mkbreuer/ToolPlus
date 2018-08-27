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




class VIEWD_TP_Batch_MiraTools(bpy.types.Operator):
    """Edit MiraTools"""
    #bl_idname = "View3D_Batch_MiraTools"
    bl_idname = "tp_ops.miratools"
    bl_label = "MiraTools :)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):      
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 225)  
 
    def check(self, context):
        return True

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'     
        layout.operator_context = 'INVOKE_REGION_WIN'  
        
        tp = context.window_manager.batchwindow
        
        box = layout.box().column(1) 

        row = box.row(1)

        if tp.display_batch_extrude:
            row.prop(tp, "display_batch_extrude", text="Extrude", icon="MOVE_UP_VEC")
        else:
            row.prop(tp, "display_batch_extrude", text="Extrude", icon="MOVE_DOWN_VEC")


        if tp.display_batch_surface:
            row.prop(tp, "display_batch_surface", text="Surface", icon="MOVE_UP_VEC")
        else:
            row.prop(tp, "display_batch_surface", text="Surface", icon="MOVE_DOWN_VEC")


        if tp.display_batch_deform:
            row.prop(tp, "display_batch_deform", text="Deform", icon="MOVE_UP_VEC")
        else:
            row.prop(tp, "display_batch_deform", text="Deform", icon="MOVE_DOWN_VEC") 
            
        row = box.row(1)

        if tp.display_batch_curves:
            row.prop(tp, "display_batch_curves", text="Curves", icon="MOVE_UP_VEC")
        else:
            row.prop(tp, "display_batch_curves", text="Curves", icon="MOVE_DOWN_VEC")

       
        if tp.display_batch_arc:
            row.prop(tp, "display_batch_arc", text="Arc", icon="MOVE_UP_VEC")
        else:
            row.prop(tp, "display_batch_arc", text="Arc", icon="MOVE_DOWN_VEC")

        if tp.display_batch_settings:
            row.prop(tp, "display_batch_settings", text="Settings", icon="MOVE_UP_VEC")
        else:
            row.prop(tp, "display_batch_settings", text="Settings", icon="MOVE_DOWN_VEC")
        
        
        row = box.row(1)

        if tp.display_batch_extrude:

            box = layout.box().column(1)         

            row = box.row(1)
            row.prop(context.scene.mi_settings, "surface_snap", text='', icon ="SNAP_SURFACE")
            row.label("New Mesh Drawing")
                
            box.separator() 

            row = box.row(1)                       
            row.operator("mira.draw_extrude", text="Draw Extrude", icon="VPAINT_HLT")

            box.separator()
            
            if context.scene.mi_extrude_settings.extrude_step_type == 'Asolute':
                row.prop(context.scene.mi_extrude_settings, "absolute_extrude_step", text='Step')
            else:
                row.prop(context.scene.mi_extrude_settings, "relative_extrude_step", text='Step')
     
            row = box.row(1) 
            row.prop(context.scene.mi_extrude_settings, "extrude_step_type", text='Step') 
                
            box.separator()

            row = box.row(1) 
            if context.scene.mi_settings.surface_snap is False:
                row.prop(context.scene.mi_extrude_settings, "do_symmetry", text='Symmetry')

                if context.scene.mi_extrude_settings.do_symmetry:
                    row.prop(context.scene.mi_extrude_settings, "symmetry_axys", text='Axys')

            box.separator()                     



        if tp.display_batch_surface:
            
            box = layout.box().column(1)

            row = box.row(1)
            row.prop(context.scene.mi_settings, "surface_snap", text='', icon ="SNAP_SURFACE")
            row.label("New Mesh Creation")
                
            box.separator()
            
            row = box.row(1)         
            row.operator("mira.poly_loop", text="Poly Loop", icon="MESH_GRID")
                
            box.separator()

            row = box.row(1)
                 
            row.operator("mira.curve_surfaces", text="CurveSurfaces", icon="SURFACE_NCURVE")
            
            box.separator()
            
            row = box.row(1)
            row.prop(context.scene.mi_cur_surfs_settings, "spread_loops_type", text='Points')       

            box.separator() 

            
            
        if tp.display_batch_deform:

            box = layout.box().column(1)  

            row = box.row(1)
            row.label("Mesh Transformation")
                
            box.separator() 
            
            row = box.row(1) 
            row.operator("screen.redo_last", text = "", icon="SETTINGS") 
            row.operator("mira.deformer", text="Deformer")
            row.operator("mira.noise", text="NoiseDeform", icon="RNDCURVE")
           
            box.separator() 
     
            row = box.row(1) 
            row.operator("mira.linear_deformer", text="LinearDeformer", icon="OUTLINER_OB_MESH")
            
            row = box.row(1) 
            row.prop(context.scene.mi_ldeformer_settings, "manual_update", text='ManualUpdate')

            box.separator() 
       
       
        if tp.display_batch_curves:
            
            box = layout.box().column(1)  

            row = box.row(1)
            row.prop(context.scene.mi_settings, "surface_snap", text='', icon ="SNAP_SURFACE")
            row.label("Loop Manipulation")
                
            box.separator()        
            
            row = box.row(1)        
            row.operator("mira.curve_stretch", text="CurveStretch", icon="STYLUS_PRESSURE")
            row.prop(context.scene.mi_cur_stretch_settings, "points_number", text='PointsNumber')       
            
            box.separator()
            
            row = box.row(1)     
            row.operator("mira.curve_guide", text="CurveGuide", icon="RNA")
            row.prop(context.scene.mi_curguide_settings, "points_number", text='LoopSpread')

            box.separator() 
            
            row = box.row(1)
            row.prop(context.scene.mi_curguide_settings, "deform_type", text='DeformType')      

            box.separator() 
        

        if tp.display_batch_arc:
            
            box = layout.box().column(1)         

            row = box.row(1)             
            row.label("Arc Creation")
                
            box.separator() 

            row = box.row(1)                             
            row.operator("mira.make_arc_get_axis", text="GetAxis")
            row.operator("mira.make_arc", text="MakeArc")

            box.separator() 
            
            row = box.column()
            row.prop(context.scene.mi_makearc_settings, "arc_axis", text="ArcAxis")

            box.separator() 
        

        if tp.display_batch_settings:

            box = layout.box().column(1)

            row = box.column(1)
            row.prop(context.scene.mi_settings, "surface_snap", text='Surface Snapping', icon ="SNAP_SURFACE")
            row.prop(context.scene.mi_settings, "convert_instances", text='Convert Instances')

            box.separator() 

            row = box.column(1)
            row.prop(context.scene.mi_settings, "snap_objects", text='SnapObjects')

            box.separator() 

            box = layout.box().column(1)

            row = box.column(1)
            row.prop(context.scene.mi_settings, "spread_mode", text='Spread')

            box.separator() 

            row = box.column(1)
            row.prop(context.scene.mi_settings, "curve_resolution", text='Resolution')

            box.separator() 

            row = box.row(1)
            row.operator("mira.curve_test", text="Curve Test")
            row.prop(context.scene.mi_settings, "draw_handlers", text='Handlers')

            box.separator() 
            
            box = layout.box().column(1)

            row = box.column(1)
            row.operator('wm.url_open', text = 'Wiki', icon='HELP').url = "https://github.com/mifth/mifthtools/wiki/Mira-Tools"

            row = box.row(1)           
            row.prop(tp, "display_help", text=" Help-URL-Buttons", icon='HELP')

            box.separator() 


        if context.mode == 'OBJECT':        
        
            box = layout.box().column(1)         

            row = box.column(1)
            row.operator("mira.wrap_object", text="WrapObject")
            row.operator("mira.wrap_master", text="WrapMaster")
            
            box.separator()         
        else:
            pass
        
        box = layout.box().column(1)    
                      
        row = box.row(1)                         
        row.operator("ed.undo", text = " ", icon="LOOP_BACK")
        row.operator("ed.redo", text = " ", icon="LOOP_FORWARDS") 
        
        box.separator() 



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()                            