# ##### BEGIN GPL LICENSE BLOCK #####
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
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    

class draw_layout_screen:

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode 

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator_context = 'INVOKE_AREA'

        tp_props = context.window_manager.tp_props_display  
                
        icons = load_icons()

        wm = context.window_manager 
        view = context.space_data
        scene = context.scene
        gs = scene.game_settings
        obj = context.object

        box = layout.box().column(1)  

        row = box.row(1)  
        row.operator_context = 'INVOKE_REGION_WIN'  
        row.operator("wm.window_fullscreen_toggle", text = "Full Screen", icon = "FULLSCREEN_ENTER")    
        row.operator("screen.screen_full_area", text = "Full Area", icon = "GO_LEFT")    
       
        row = box.row(1) 
        row.operator("wm.window_duplicate", text="Dupli View", icon = "SCREEN_BACK")
        row.operator("screen.region_quadview", text="Quad View", icon = "SPLITSCREEN")

        if context.space_data.region_quadviews:
        
            row.operator_context = 'INVOKE_REGION_WIN'
        
            box.separator()        
          
            row = box.row(1)          
            region = context.space_data.region_quadviews[2]
            row.prop(region, "lock_rotation")
            sub = row.row(1)        
            sub.enabled = region.lock_rotation
            sub.prop(region, "show_sync_view")
            sub1 = row.row(1)  
            sub1.enabled = region.lock_rotation and region.show_sync_view
            sub1.prop(region, "use_box_clip")

        box.separator()

        row = box.row(1)              
        if tp_props.display_lens:            
            row.prop(tp_props, "display_lens", text="Clip/Lens", icon="CHECKBOX_HLT")
        else:
            row.prop(tp_props, "display_lens", text="Clip/Lens", icon="CHECKBOX_DEHLT")   

        if tp_props.display_navi:            
            row.prop(tp_props, "display_navi", text="Navigation", icon="CHECKBOX_HLT")
        else:
            row.prop(tp_props, "display_navi", text="Navigation", icon="CHECKBOX_DEHLT")    

        box.separator()

        
        if tp_props.display_lens: 
            
            box = layout.box().column(1)  

            row = box.column(1)
            row.prop(context.space_data, "lens")

            box.separator() 
            
            row = box.column(1)
            row.prop(context.space_data, "clip_start", text="ClipStart")
            row.prop(context.space_data, "clip_end", text="ClipEnd")


        if tp_props.display_navi: 

            box = layout.box().column(1) 

            row = box.row(1)
            row.alignment = 'CENTER'     
            row.operator("view3d.viewnumpad", text=" ", icon='CAMERA_DATA').type = 'CAMERA'
            row.operator("view3d.view_selected", text=" ", icon='ZOOM_SELECTED')
            row.operator("view3d.view_center_cursor", text=" ", icon='FORCE_FORCE')        
            row.operator("view3d.view_all", text=" ", icon='MANIPUL').center = True
         
            box.separator() 

            row = box.row(1) 

            box = row.box()

            box.label(text='Pan:')
            rowr = box.row(1)
            rowr.operator('opr.pan_up_view1', text='', icon='TRIA_DOWN')
            rowr.operator('opr.pan_down_view1', text='', icon='TRIA_UP')

            rowr = box.row(1)
            rowr.operator('opr.pan_right_view1', text='', icon='BACK')
            rowr.operator('opr.pan_left_view1', text='', icon='FORWARD')

            rowr = box.row(1)
            rowr.label(text='Zoom:')
            
            rowr = box.row(1)
            rowr.operator('opr.zoom_in_view1', text='', icon='ZOOMIN')
            rowr.operator('opr.zoom_out_view1', text='', icon='ZOOMOUT')

            box.separator()     

            rowr = box.row(1)

            rowr = box.row()

            box = row.box()
            box.label(text='Orbit:')

            rowr = box.row(1)
            rowr.operator('opr.orbit_up_view1', text='', icon='TRIA_DOWN')
            rowr.operator('opr.orbit_down_view1', text='', icon='TRIA_UP')  

            rowr = box.row(1)
            rowr.operator('opr.orbit_right_view1', text='', icon='BACK')
            rowr.operator('opr.orbit_left_view1', text='', icon='FORWARD')

            rowr = box.row(1)
            rowr.label(text='Roll:')
            
            rowr = box.row(1)
            rowr.operator('opr.roll_left_view1', text='', icon='ZOOMIN')
            rowr.operator('opr.roll_right_view1', text='', icon='ZOOMOUT')

            box.separator()     
                              
            rowr = box.row(1)

            rowr = box.row()

            box = row.box()
            box.label(text='View:')
            
            rowr = box.column(1)        
            rowr.operator("view3d.viewnumpad", text="Front").type='FRONT'
            rowr.operator("view3d.viewnumpad", text="Back").type='BACK'
            rowr.operator("view3d.viewnumpad", text="Left").type='LEFT'
            rowr.operator("view3d.viewnumpad", text="Right").type='RIGHT'
            rowr.operator("view3d.viewnumpad", text="Top").type='TOP'
            rowr.operator("view3d.viewnumpad", text="Bottom").type='BOTTOM'

            box.separator()       

            box = layout.box().column(1)  
            
            row = box.row(1)  
            row.operator("view3d.localview", text="Global/Local", icon='WORLD')
            row.operator("view3d.view_persportho", text="Persp/Ortho", icon='VIEW3D')             

            box.separator()                             

            row = box.column(1)
            row.prop(context.space_data, "lock_object", text="View to:")

            box.separator() 


        box = layout.box().column(1)     

        row = box.row(1)           
        row.prop(context.scene.render, "use_simplify", text="", icon='MESH_ICOSPHERE')    
        row.label("Simplify")
        
        row.label("")
        
        if tp_props.display_simplify: 
            row.prop(tp_props, "display_simplify", text="", icon='TRIA_UP_BAR')    
        else:
            row.prop(tp_props, "display_simplify", text="", icon='TRIA_DOWN_BAR')                                   
                       
        box.separator()
        
        if tp_props.display_simplify:
                             
            if bpy.context.scene.render.use_simplify == True:

                rd = context.scene.render   
                             
                if bpy.context.scene.render.engine == 'CYCLES':

                    box.active = context.scene.render.use_simplify
     
                    row = box.column(1) 
                    row.label(text="Viewport:")
                    row.prop(context.scene.render, "simplify_subdivision", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles", text="Child Particles")

                    box.separator()

                    row = box.column(1) 
                    row.label(text="Render:")

                    row.prop(context.scene.render, "simplify_subdivision_render", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles_render", text="Child Particles")

                    col = box.column()
                    col.prop(context.scene.cycles, "use_camera_cull")
                   
                    subsub = col.column()
                    subsub.active = context.scene.cycles.use_camera_cull
                    subsub.prop(context.scene.cycles, "camera_cull_margin")

                else:

                    box.active = context.scene.render.use_simplify

                    row = box.column(1) 
                    row.label(text="Viewport:")
                    row.prop(context.scene.render, "simplify_subdivision", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles", text="Child Particles")

                    box.separator()

                    row = box.column(1) 
                    row.label(text="Render:")
                    row.prop(context.scene.render, "simplify_subdivision_render", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles_render", text="Child Particles")
                    row.prop(context.scene.render, "simplify_shadow_samples", text="Shadow Samples")
                    row.prop(context.scene.render, "simplify_ao_sss", text="AO and SSS")                
                    row.prop(context.scene.render, "use_simplify_triangulate")    

                box.separator()
           
            else:      
                row = box.column(1) 
                row.label(text="Not active!")
               
                box.separator()



        box = layout.box().column(1)     

        row = box.row()
        row.prop(context.space_data, "show_floor", text="", icon ="GRID")  
        row.label(text="Grid Floor") 

        if tp_props.display_grid:            
            row.prop(tp_props, "display_grid", text="", icon="TRIA_UP_BAR")
        else:
            row.prop(tp_props, "display_grid", text="", icon="TRIA_DOWN_BAR")    

        box.separator()
 
        if tp_props.display_grid: 
            
            row = box.row(1)
            row.label("Axis")
            row.prop(context.space_data, "show_axis_x", text="X", toggle=True)
            row.prop(context.space_data, "show_axis_y", text="Y", toggle=True)
            row.prop(context.space_data, "show_axis_z", text="Z", toggle=True)

            box.separator() 

            if context.space_data.show_floor:  
           
                row = box.column(1)
                row.prop(context.space_data, "grid_lines", text="Lines")
                row.prop(context.space_data, "grid_scale", text="Scale")
                row.prop(context.space_data, "grid_subdivisions", text="Subdivisions")
               
                box.separator() 




class VIEW3D_TP_Screen_Panel_TOOLS(bpy.types.Panel, draw_layout_screen):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Screen_Panel_TOOLS"
    bl_label = "3D Screen"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_Screen_Panel_UI(bpy.types.Panel, draw_layout_screen):
    bl_idname = "VIEW3D_TP_Screen_Panel_UI"
    bl_label = "3D Screen"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}



