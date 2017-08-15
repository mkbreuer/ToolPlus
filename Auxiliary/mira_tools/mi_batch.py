import bpy
from bpy import*
from bpy.props import *



class View3D_Batch_MiraTools(bpy.types.Operator):
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
        
        mt = context.window_manager.batchwindow
        

        if context.mode == 'OBJECT':

            box = layout.box().column(1) 

            row = box.column(1)
            row.label("Wrap over UV")
            
            row = box.column(1)
            row.operator("mira.wrap_object", text="WrapObject", icon="MOD_LATTICE")
            row.operator("mira.wrap_scale", text="WrapScale", icon="MAN_SCALE")
            row.operator("mira.wrap_master", text="WrapMaster", icon ="MOD_SHRINKWRAP")
            
            box.separator()

        else:
            
            box = layout.box().column(1) 

            row = box.row(1)

            if mt.display_batch_extrude:
                row.prop(mt, "display_batch_extrude", text="Extrude", icon="MOVE_UP_VEC")
            else:
                row.prop(mt, "display_batch_extrude", text="Extrude", icon="MOVE_DOWN_VEC")


            if mt.display_batch_surface:
                row.prop(mt, "display_batch_surface", text="Surface", icon="MOVE_UP_VEC")
            else:
                row.prop(mt, "display_batch_surface", text="Surface", icon="MOVE_DOWN_VEC")


            if mt.display_batch_deform:
                row.prop(mt, "display_batch_deform", text="Deform", icon="MOVE_UP_VEC")
            else:
                row.prop(mt, "display_batch_deform", text="Deform", icon="MOVE_DOWN_VEC") 
                
            row = box.row(1)

            if mt.display_batch_curves:
                row.prop(mt, "display_batch_curves", text="Curves", icon="MOVE_UP_VEC")
            else:
                row.prop(mt, "display_batch_curves", text="Curves", icon="MOVE_DOWN_VEC")

           
            if mt.display_batch_arc:
                row.prop(mt, "display_batch_arc", text="Arc", icon="MOVE_UP_VEC")
            else:
                row.prop(mt, "display_batch_arc", text="Arc", icon="MOVE_DOWN_VEC")

            if mt.display_batch_settings:
                row.prop(mt, "display_batch_settings", text="Settings", icon="MOVE_UP_VEC")
            else:
                row.prop(mt, "display_batch_settings", text="Settings", icon="MOVE_DOWN_VEC")
            
            
            row = box.row(1)

            if mt.display_batch_extrude:

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



            if mt.display_batch_surface:
                
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

                
                
            if mt.display_batch_deform:

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
           
           
            if mt.display_batch_curves:
                
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
            

            if mt.display_batch_arc:
                
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
            

            if mt.display_batch_settings:

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
                row.prop(mt, "display_help", text=" Help-URL-Buttons", icon='HELP')

                box.separator() 


        box = layout.box().column(1)    
                      
        row = box.row(1)                         
        row.operator("ed.undo", text = " ", icon="LOOP_BACK")
        row.operator("ed.redo", text = " ", icon="LOOP_FORWARDS") 
                    
