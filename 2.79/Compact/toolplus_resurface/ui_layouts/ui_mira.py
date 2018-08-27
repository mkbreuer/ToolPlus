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
import bpy, os
from bpy import *
from bpy.props import * 
from .. icons.icons import load_icons


# MIRATOOLS: COMPLETE EDIT #
types_mira = [("tp_mi0"   ," "   ,""   ,"COLLAPSEMENU"          ,0),
              ("tp_mi1"   ," "   ,""   ,"SNAP_SURFACE"          ,1), 
              ("tp_mi2"   ," "   ,""   ,"VPAINT_HLT"            ,2),
              ("tp_mi3"   ," "   ,""   ,"SURFACE_NCURVE"        ,3),
              ("tp_mi4"   ," "   ,""   ,"OUTLINER_OB_MESH"      ,4),
              ("tp_mi5"   ," "   ,""   ,"RNA"                   ,5),
              ("tp_mi6"   ," "   ,""   ,"STYLUS_PRESSURE"       ,6)]


bpy.types.Scene.tp_draw = bpy.props.EnumProperty(name = " ", default = "tp_mi0", items = types_mira)


def draw_miratools_ui(self, context, layout):

        tp = context.window_manager.mirawindow
    
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons() 

        scene = context.scene

        col = layout.column(align=True)
        
        box = col.box().column(1)
 
        row = box.row(1)  
        row.prop(context.scene, 'tp_draw',  emboss = False, expand = True) #icon_only=True,
 

        if scene.tp_draw == "tp_mi0": 
            pass


        if scene.tp_draw == "tp_mi1": 

            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("Settings", icon='SCRIPTWIN')

            
            box = col.box().column(1)
          
            row = box.row(1)
            row.prop(context.scene.mi_settings, "surface_snap", text='Surface Snapping', icon ="SNAP_SURFACE")

            row = box.row(1)
            row.prop(context.scene.mi_settings, "convert_instances", text='Convert Instances')

            box.separator() 

            row = box.column(1)
            row.prop(context.scene.mi_settings, "snap_objects", text='SnapObjects')

            box.separator() 


            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(context.scene.mi_settings, "spread_mode", text='Spread')

            box.separator() 

            row = box.column(1)
            row.prop(context.scene.mi_settings, "curve_resolution", text='Resolution')

            box.separator() 

            row = box.row(1)
            row.operator("mira.curve_test", text="Curve Test")
            row.prop(context.scene.mi_settings, "draw_handlers", text='Handlers')

            box.separator() 


   




        if scene.tp_draw == "tp_mi2": 

        
            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("Surface Mesh Drawing")
                
            box.separator()

            row = box.column(1)  
            row.operator("mira.draw_extrude", text="Draw Extrude", icon="VPAINT_HLT")

            row = box.row(1)
            if tp.display_help:                          
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://lh3.googleusercontent.com/-tIDzK8yFnjU/VbhVbn2cfSI/AAAAAAAAIPo/mYRzdjqOki0/w530-h749-p/%25231_Draw_Extrude.png"   

            if context.scene.mi_extrude_settings.extrude_step_type == 'Asolute':
                row.prop(context.scene.mi_extrude_settings, "absolute_extrude_step", text='')
            else:
                row.prop(context.scene.mi_extrude_settings, "relative_extrude_step", text='')

            box.separator()
            
            row = box.column(1)       
            row.prop(context.scene.mi_extrude_settings, "extrude_step_type", text='Step')

            box.separator()

            row = box.column(1)
            if context.scene.mi_settings.surface_snap is False:
                row.prop(context.scene.mi_extrude_settings, "do_symmetry", text='Symmetry')

                if context.scene.mi_extrude_settings.do_symmetry:
                    row.prop(context.scene.mi_extrude_settings, "symmetry_axys", text='Axys')

            box.separator() 
            
       
       
        if scene.tp_draw == "tp_mi3": 


            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("Create Surfaces")
          
            box.separator()
         
            row = box.row(1)
            
            if tp.display_help:                                        
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://lh3.googleusercontent.com/-0fzOvLD4EM8/Vb5CdYy5qKI/AAAAAAAAIVk/EkiLDYzwtVk/w780-h840-no/%25233_Poly_Loop.png"   
         
            row.operator("mira.poly_loop", text="Poly Loop", icon="MESH_GRID")
           
            box.separator()


            row = box.row(1)
            if tp.display_help:                                       
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://lh5.googleusercontent.com/-o3W-ypmbxI8/Vb5gyXLJ4tI/AAAAAAAAIXc/ZsNqJR5WiWw/w746-h840-no/%25234_Curve_Surface.png"             

            row.operator("mira.curve_surfaces", text="Curve Surface", icon="SURFACE_NCURVE")

            box.separator()

            row = box.column(1)
            row.prop(context.scene.mi_cur_surfs_settings, "spread_loops_type", text='Points')

            box.separator() 
            


        if scene.tp_draw == "tp_mi4": 

            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("Mesh Transformation")

            box.separator()
            
            row = box.row(1) 
            row.operator("mira.linear_deformer", text="LinearDeformer", icon="OUTLINER_OB_MESH")

            row = box.row(1)
            if tp.display_help:                                         
                row.operator("wm.url_open", text="", icon='QUESTION' ).url = "https://lh4.googleusercontent.com/-GTuGp92YHvc/VbruOKWUTTI/AAAAAAAAIUk/LbjhscUtqHI/w611-h840-no/%25232_Deform_Mesh.png"  

            row.prop(context.scene.mi_ldeformer_settings, "manual_update", text='ManualUpdate')

            box.separator()

            row = box.row(1)
            row.operator("screen.redo_last", text = "", icon="SETTINGS")            
            row.operator("mira.deformer", text="Deformer", icon="BLANK1")
            
            box.separator()
                        
            row = box.column(1)            
            row.operator("mira.noise", text="NoiseDeform", icon="RNDCURVE")

            box.separator()


        if scene.tp_draw == "tp_mi5": 
            
            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("CGuide")
            row.prop(context.scene.mi_settings, "surface_snap", text='', icon ="SNAP_SURFACE")                         
            
            box.separator()        

            row = box.column(1)
            row.operator("mira.curve_guide", text="CurveGuide", icon="RNA")

            row = box.row(1)
            if tp.display_help:                              
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://lh3.googleusercontent.com/WBih_PAVzmvuBWVuAv-iO6_ZAy1L9PdSaIm1C-AmkJkCeM8kl3te7DESf98kn3SAWVZWSLNAIg=w1920-h1080-no"    

            row.prop(context.scene.mi_curguide_settings, "points_number", text='LoopSpread')

            box.separator() 
            
            row = box.row(1)
            row.prop(context.scene.mi_curguide_settings, "deform_type", text='Type')
            
          
            box.separator() 



        if scene.tp_draw == "tp_mi5": 

            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("Arc Creation")
                         
            box.separator() 
           
            row = box.row(1)                             
            row.operator("mira.make_arc_get_axis", text="GetAxis", icon="OUTLINER_DATA_EMPTY")
            row.operator("mira.make_arc", text="MakeArc", icon="SPHERECURVE")
            
            box.separator()
            
            row = box.column()
            row.prop(context.scene.mi_makearc_settings, "arc_axis", text="ArcAxis")            
             
            box.separator() 

            if tp.display_help:            
            
                row = box.row(1)  
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://www.youtube.com/watch?v=00vyPu5JV2M&feature=youtu.be"           
                
                box.separator() 






        
        if scene.tp_draw == "tp_mi6": 

            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("CStretch")
            row.prop(context.scene.mi_settings, "surface_snap", text='', icon ="SNAP_SURFACE")                
            
            box.separator()        

            row = box.column(1)
            row.operator("mira.curve_stretch", text="CurveStretch", icon="STYLUS_PRESSURE")

            row = box.row(1)
            if tp.display_help:                              
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://lh3.googleusercontent.com/-pFQ0XaKlZY4/VcDyem3HKaI/AAAAAAAAIZI/oELrYw398oM/w530-h597-p/%25235_Curve_Stretch.png"  

            row.prop(context.scene.mi_cur_stretch_settings, "points_number", text='PointsNumber')

            box.separator() 




# MIRATOOLS: CURVE GUIDE #

def draw_miraguide_ui(self, context, layout):

        tp = context.window_manager.mirawindow     

        icons = load_icons() 

        col = layout.column(align=True)

        if not tp.display_miraguide:
            
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp, "display_miraguide", text="", icon='TRIA_RIGHT', emboss = False)
            row.label("CGuide")

            sub = row.row(1)
            sub.scale_x = 0.2
            sub.prop(context.scene.mi_curguide_settings, "points_number", text='')
            row.operator("mira.curve_guide", text='', icon="RNA")

        else:
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp, "display_miraguide", text="", icon='TRIA_DOWN', emboss = False)

            row.label("CGuide")

            sub = row.row(1)
            sub.scale_x = 0.2
            sub.prop(context.scene.mi_curguide_settings, "points_number", text='')
            row.operator("mira.curve_guide", text='', icon="RNA")

            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("Guided Loop Shift")
            row.prop(context.scene.mi_settings, "surface_snap", text='', icon ="SNAP_SURFACE")                         
            
            box.separator()        

            row = box.column(1)
            row.operator("mira.curve_guide", text="CurveGuide", icon="RNA")

            row = box.row(1)
            if tp.display_help:                              
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://lh3.googleusercontent.com/WBih_PAVzmvuBWVuAv-iO6_ZAy1L9PdSaIm1C-AmkJkCeM8kl3te7DESf98kn3SAWVZWSLNAIg=w1920-h1080-no"    

            row.prop(context.scene.mi_curguide_settings, "points_number", text='LoopSpread')

            box.separator() 
            
            row = box.row(1)
            row.prop(context.scene.mi_curguide_settings, "deform_type", text='Type')
            
          
            box.separator() 




# MIRATOOLS: CURVE STRETCH #
def draw_mirastretch_ui(self, context, layout):

        tp = context.window_manager.mirawindow     

        icons = load_icons()    
    
        col = layout.column(align=True)

        if not tp.display_mirastretch:
      
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp, "display_mirastretch", text="", icon='TRIA_RIGHT', emboss = False)

            row.label("CStretch")
            sub = row.row(1)
            sub.scale_x = 0.2
            sub.prop(context.scene.mi_cur_stretch_settings, "points_number", text='')
            row.operator("mira.curve_stretch", text="", icon="STYLUS_PRESSURE")

        else:
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp, "display_mirastretch", text="", icon='TRIA_DOWN', emboss = False)
            row.label("CStretch")
            sub = row.row(1)
            sub.scale_x = 0.2
            sub.prop(context.scene.mi_cur_stretch_settings, "points_number", text='')
            row.operator("mira.curve_stretch", text="", icon="STYLUS_PRESSURE")

            box = col.box().column(1)
            
            row = box.row(1)  
            row.label("Free Loop Shift")
            row.prop(context.scene.mi_settings, "surface_snap", text='', icon ="SNAP_SURFACE")                
            
            box.separator()        

            row = box.column(1)
            row.operator("mira.curve_stretch", text="CurveStretch", icon="STYLUS_PRESSURE")

            row = box.row(1)
            if tp.display_help:                          
                row.operator("wm.url_open", text="", icon='QUESTION').url = "https://lh3.googleusercontent.com/-pFQ0XaKlZY4/VcDyem3HKaI/AAAAAAAAIZI/oELrYw398oM/w530-h597-p/%25235_Curve_Stretch.png"  

            row.prop(context.scene.mi_cur_stretch_settings, "points_number", text='PointsNumber')

            box.separator() 




            
# MIRATOOLS: WRAP #
def draw_mirawrap_ui(self, context, layout):

        tp = context.window_manager.mirawindow     

        icons = load_icons()

        col = layout.column(align=True)

        if not tp.display_mira_wrap:
                        
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp, "display_mira_wrap", text="", icon='TRIA_RIGHT', emboss = False)
          
            row.label("WrapTool")               
            row.operator("mira.wrap_object", text="", icon ="MOD_LATTICE")
            row.operator("mira.wrap_scale", text="", icon ="MAN_SCALE")
            row.operator("mira.wrap_master", text="", icon ="MOD_SHRINKWRAP")

            
        else:

            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp, "display_mira_wrap", text="", icon='TRIA_DOWN', emboss = False)
            row.label("WrapTool")               

            box.separator() 

            row = box.column(1)  
            row.operator("mira.wrap_object", text="WrapObject", icon ="MOD_LATTICE")
            row.operator("mira.wrap_scale", text="WrapScale", icon ="MAN_SCALE")
            row.operator("mira.wrap_master", text="WrapMaster", icon ="MOD_SHRINKWRAP")

