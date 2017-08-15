# BEGIN GPL LICENSE BLOCK #####
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
# END GPL LICENSE BLOCK #####

bl_info = {
    "name": "T+ Batch: MiraTools",
    "author": "MKB",
    "version": (2, 0, 0),
    "blender": (2, 78, 0),
    "location": "3D Viewport",
    "description": "Batch Operator Menu for MiraTools",
    "warning": "",
    "wiki_url": "https://github.com/mifth/mifthtools/wiki/Mira-Tools",
    "tracker_url": "https://github.com/mifth/mifthtools/issues",
    "category": "ToolPlus"}



import bpy
from bpy import*
from bpy.props import *
from bpy.types import AddonPreferences, PropertyGroup
import rna_keymap_ui

class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__


    prefs_tabs = EnumProperty(
        items=(('keymap',     "Keymap",     "Keymap"),
               ('url',        "URLs",       "URLs")),
               default='keymap')


    def draw(self, context):
        layout = self.layout

        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
        
        #Keymap
        if self.prefs_tabs == 'keymap':
            
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Batch Operator Menu for MiraTools:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Hotkey: CTRL+D")
  
            box.separator() 
            
            row = box.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")
      
            box.separator() 


        #Weblinks
        if self.prefs_tabs == 'url':
            box = layout.box()
          
            row = box.row(1)
            row.operator('wm.url_open', text = 'Wiki', icon = 'HELP').url = "https://github.com/mifth/mifthtools/wiki/Mira-Tools"
            row.operator('wm.url_open', text = 'Issues', icon = 'ERROR').url = "https://github.com/mifth/mifthtools/issues"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "http://blenderartists.org/forum/showthread.php?366107-MiraTools"             
            row.operator('wm.url_open', text = 'iskeyfree', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"
      
            box.separator() 






class Dropdown_Batch_MiraToolProps(bpy.types.PropertyGroup):

    display_batch_surface = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_curves = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)
    display_batch_deform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_extrude = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_arc = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_settings = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)



class View3D_Batch_MiraTools(bpy.types.Operator):
    """Edit MiraTools"""
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

                box.separator() 


        box = layout.box().column(1)    
                      
        row = box.row(1)                         
        row.operator("ed.undo", text = " ", icon="LOOP_BACK")
        row.operator("ed.redo", text = " ", icon="LOOP_FORWARDS") 





# register
addon_keymaps = []

def register():
    addon_keymaps.clear()

    #bpy.utils.register_class(View3D_Batch_MiraTools)
    bpy.utils.register_module(__name__)

    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type ='VIEW_3D')
        kmi = km.keymap_items.new('tp_ops.miratools', 'D', 'PRESS', ctrl=True)#, shift=True, alt=True, 
        #kmi.properties.name = 'tp_ops.miratools'
        addon_keymaps.append((km, kmi))


def unregister():
    #bpy.utils.unregister_class(View3D_Batch_MiraTools)
    bpy.utils.unregister_module(__name__)

    wm = bpy.context.window_manager

    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()        



          
