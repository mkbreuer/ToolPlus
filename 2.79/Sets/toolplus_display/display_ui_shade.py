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

class draw_layout_shade:

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
        ob = context.object  
        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene 
        gs = scene.game_settings
       
        box = layout.box().column(1)                                                  

        row = box.row(1)
        row.alignment = 'CENTER'           
        row.operator("tp_ops.toggle_silhouette", text="", icon ="MATCAP_08")      
        row.prop(bpy.context.space_data, 'viewport_shade', text='', expand=True)

        box.separator()   
        box.separator()   

        row = box.row()
        row.prop(context.space_data, "show_world", "World")# ,icon ="WORLD")

        if context.space_data.show_world:        
       
            if tp_props.display_world_set:            
                row.prop(tp_props, "display_world_set", text="", icon="TRIA_UP_BAR")
            else:
                row.prop(tp_props, "display_world_set", text="", icon="TRIA_DOWN_BAR")    

            sub = row.row(1)
            sub.scale_x = 0.1 
            sub.prop(context.scene.world, "horizon_color", "")
                           
            box.separator() 

            if tp_props.display_world_set: 
                
                box.separator()            

                row = box.column(1)
                row.label("Lamp Settings")  
                row.prop(context.scene.world, "exposure")
                row.prop(context.scene.world, "color_range")
                row.prop(context.scene.world, "horizon_color", "")

                box.separator() 



        col = box.column()
        if view.viewport_shade == 'SOLID':
            
            col = box.row()
            col.prop(view, "use_matcap")
            if view.use_matcap:
                sub = col.row(1)
                sub.scale_y = 0.2
                sub.scale_x = 1
                sub.template_icon_view(context.space_data, "matcap_icon")
                
                box.separator()

        fx_settings = view.fx_settings
        if view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:

            col = box.row()
            col.prop(context.space_data.fx_settings, "use_ssao", text="Ambient Occlusion")
            
            if context.space_data.fx_settings.use_ssao:

                if tp_props.display_aoccl:            
                    col.prop(tp_props, "display_aoccl", text="", icon="TRIA_UP_BAR")
                else:  
                    col.prop(tp_props, "display_aoccl", text="", icon="TRIA_DOWN_BAR")    

                sub = col.row(1)
                sub.scale_x = 0.1           
                sub.prop(context.space_data.fx_settings.ssao, "color","")
            
                if tp_props.display_aoccl:

                    box.separator()
                    
                    col = box.column(1)
                    col.prop(context.space_data.fx_settings.ssao, "factor")
                    col.prop(context.space_data.fx_settings.ssao, "distance_max")
                    col.prop(context.space_data.fx_settings.ssao, "attenuation")
                    col.prop(context.space_data.fx_settings.ssao, "samples")
                    col.prop(context.space_data.fx_settings.ssao, "color","")               
                
                box.separator()


        row = box.row()
        if view.viewport_shade == 'SOLID':
            row.prop(view, "show_textured_solid")
            
        if view.viewport_shade == 'TEXTURED' or context.mode == 'PAINT_TEXTURE':
            if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                row.prop(view, "show_textured_shadeless")

        if not scene.render.use_shading_nodes:
            row = box.row(1)  
            row.prop(gs, "material_mode", text="")
        
        box.separator()


        box = layout.box().column(1)   

        row = box.row(1)  
        row.menu("VIEW3D_MT_opengl_lights_presets", text=bpy.types.VIEW3D_MT_opengl_lights_presets.bl_label, icon = "COLLAPSEMENU")
        row.operator("scene.opengl_lights_preset_add", text="", icon='ZOOMIN')
        row.operator("scene.opengl_lights_preset_add", text="", icon='ZOOMOUT').remove_active = True      
                     
        system = bpy.context.user_preferences.system
        
        def opengl_lamp_buttons(column, lamp):
           
            split = column.split(percentage=0.1)
            split.prop(lamp, "use", text="", icon='OUTLINER_OB_LAMP' if lamp.use else 'LAMP_DATA')
            
            col = split.column()
            col.active = lamp.use
            
            row = col.row()
            row.label(text="Diffuse:")
            row.prop(lamp, "diffuse_color", text="")
            
            row = col.row()
            row.label(text="Specular:")
            row.prop(lamp, "specular_color", text="")
            
            col = split.column()           
            col.active = lamp.use
            col.prop(lamp, "direction", text="")
        
        row = box.row(1) 
        p = context.scene.opengl_lights_properties
        row.prop(p, "edit", "edit opengl light", icon = "LIGHTPAINT")
        
        if(p.edit):
            box.separator()   
            
            box = layout.box().column(1)  
            
            column = box.column()
            
            split = column.split(percentage=0.1)
            split.label()
            split.label(text="Colors:")
            split.label(text="Direction:")
            
            lamp = system.solid_lights[0]
            opengl_lamp_buttons(column, lamp)
            
            lamp = system.solid_lights[1]
            opengl_lamp_buttons(column, lamp)
            
            lamp = system.solid_lights[2]
            opengl_lamp_buttons(column, lamp)


        box.separator() 



class VIEW3D_TP_Shade_Panel_TOOLS(bpy.types.Panel, draw_layout_shade):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Shade_Panel_TOOLS"
    bl_label = "3D Shade"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_Shade_Panel_UI(bpy.types.Panel, draw_layout_shade):
    bl_idname = "VIEW3D_TP_Shade_Panel_UI"
    bl_label = "3D Shade"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}



