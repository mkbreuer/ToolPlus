# ##### BEGIN GPL LICENSE BLOCK #####
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
__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *
from . icons.icons import load_icons



class TP_Header_Menus(bpy.types.Header):
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
        return 
       
    def draw(self, context):

        layout = self.layout

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        obj = context.active_object

        row = layout.row(1)
        row.scale_x = 1.2                            
        
        button_ruler_triangle = icons.get("icon_ruler_triangle") 
        row.operator("tp_ops.np_020_point_distance", text="", icon_value=button_ruler_triangle.icon_id) 

        # ADD
        display_header_custom_a = context.user_preferences.addons[__package__].preferences.tab_header_custom_a
        if display_header_custom_a == 'on':
  
            row = layout.row(1)
            row.label("Custom", icon = "INFO")   

                           
        # ALIGN
        display_header_align = context.user_preferences.addons[__package__].preferences.tab_header_align
        if display_header_align == 'on': 

            row = layout.row(1)
            row.operator("tp_header.snap_setup", text="", icon = "SNAP_SURFACE")           
           
            if context.mode == 'OBJECT': 
                          
                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:

                        button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                        row.operator("object.align_by_faces", text="", icon_value=button_snap_face_to_face.icon_id)  

                        button_snap_drop_down = icons.get("icon_snap_drop_down") 
                        row.operator("object.drop_on_active", text="", icon_value=button_snap_drop_down.icon_id) 

                        button_snap_offset = icons.get("icon_snap_offset")  
                        row.operator("view3d.xoffsets_main", "", icon_value=button_snap_offset.icon_id)   
 
                    else:
                        pass


            if context.mode == 'EDIT_MESH': 
                
                button_snap_offset = icons.get("icon_snap_offset")  
                row.operator("view3d.xoffsets_main", "", icon_value=button_snap_offset.icon_id)   
                
                button_align_con_face = icons.get("icon_align_con_face") 
                row.operator("mesh.rot_con", "", icon_value=button_align_con_face.icon_id) 
                          

        # NP Station
        display_header_np = context.user_preferences.addons[__package__].preferences.tab_header_np
        if display_header_np == 'on': 

            row = layout.row(1)

            if context.mode == 'OBJECT':  

                obj = context.active_object
                if obj:
                    obj_type = obj.type                       
                    if obj.type in {'MESH'}:

                        button_snap_abc = icons.get("icon_snap_abc") 
                        row.operator("tp_ops.np_020_point_align", text='', icon_value=button_snap_abc.icon_id) 
                    else:
                        pass

                button_snap_grab = icons.get("icon_snap_grab") 
                row.operator("tp_ops.np_020_point_move", text='', icon_value=button_snap_grab.icon_id)

                obj = context.active_object
                if obj:
                    obj_type = obj.type                        
                    if obj.type in {'MESH'}:
                       
                        button_snap_rotate = icons.get("icon_snap_rotate") 
                        row.operator("tp_ops.np_020_roto_move", text='', icon_value=button_snap_rotate.icon_id)
                    else:
                        pass
            
                button_snap_scale = icons.get("icon_snap_scale") 
                row.operator("tp_ops.np_020_point_scale", text='', icon_value=button_snap_scale.icon_id)


        # Zero
        display_header_zero = context.user_preferences.addons[__package__].preferences.tab_header_zero
        if display_header_zero == 'on': 
          
            row = layout.row(1)
            
            if context.mode == 'OBJECT': 

                button_align_advance = icons.get("icon_align_advance")
                row.operator("tp_origin.align_tools", "", icon_value=button_align_advance.icon_id)   


            button_align_zero = icons.get("icon_align_zero")  
            row.operator("tp_ops.zero_axis", text="", icon_value=button_align_zero.icon_id)  
 

        # AutoMirror
        display_header_automirror = context.user_preferences.addons[__package__].preferences.tab_header_automirror
        if display_header_automirror == 'on':  
            
            row = layout.row(1)
            
            button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
            row.operator("tp_batch.header_autom", text="",icon="MOD_WIREFRAME")  


        # SELECT
        display_header_select = context.user_preferences.addons[__package__].preferences.tab_header_select
        if display_header_select == 'on':

            row = layout.row(1)
            
            button_cursor = icons.get("icon_cursor")
            row.menu("tp_header.snap_to_cursor", " ", icon_value=button_cursor.icon_id)            
            row.menu("tp_header.snap_to_select", " ", icon="RESTRICT_SELECT_OFF")  


        # Mirror
        display_header_mirror = context.user_preferences.addons[__package__].preferences.tab_header_mirror
        if display_header_mirror == 'on':  
            
            button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
            row.menu("VIEW3D_MT_mirror",text="", icon_value=button_align_mirror_obm.icon_id)  


        # ORIGIN
        display_header_origin = context.user_preferences.addons[__package__].preferences.tab_header_origin
        if display_header_origin == 'on':

            row = layout.row(1)  
                  
            row.scale_x = 0.85         
            if context.mode == 'OBJECT':
                
                button_origin_center_view = icons.get("icon_origin_center_view")
                row.operator("object.transform_apply", text="", icon_value=button_origin_center_view.icon_id).location=True

                button_origin_cursor = icons.get("icon_origin_cursor")
                row.operator("tp_ops.origin_set_cursor", text="", icon_value=button_origin_cursor.icon_id)

                button_origin_tomesh = icons.get("icon_origin_tomesh")
                row.operator("tp_ops.origin_tomesh", text="", icon_value=button_origin_tomesh.icon_id)

                button_origin_meshto = icons.get("icon_origin_meshto")
                row.operator("tp_ops.origin_meshto", text="", icon_value=button_origin_meshto.icon_id)

                button_origin_mass = icons.get("icon_origin_mass")           
                row.operator("tp_ops.origin_set_mass", text="" , icon_value=button_origin_mass.icon_id)

            else:
                
                button_origin_center_view = icons.get("icon_origin_center_view")
                row.operator("tp_ops.origin_set_center", text="", icon_value=button_origin_center_view.icon_id)

                button_origin_cursor = icons.get("icon_origin_cursor")
                row.operator("tp_ops.origin_cursor_edm", text="", icon_value=button_origin_cursor.icon_id)            

                button_origin_edm = icons.get("icon_origin_edm")            
                row.operator("tp_ops.origin_edm","", icon_value=button_origin_edm.icon_id)       

                button_origin_obj = icons.get("icon_origin_obj")   
                row.operator("tp_ops.origin_obm","", icon_value=button_origin_obj.icon_id)             
           

            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:

                    if len(bpy.context.selected_objects) == 1: 
                      
                        if context.mode == 'OBJECT':
                            button_origin_bbox = icons.get("icon_origin_bbox")                               
                            row.operator("object.bbox_origin_modal_ops", text="", icon_value=button_origin_bbox.icon_id)                                
                    else:                            
                        button_origin_bbox = icons.get("icon_origin_bbox")   
                        row.operator("tp_ops.bbox_origin_set","", icon_value=button_origin_bbox.icon_id)
 
            #if context.mode == 'OBJECT':               

                #if bpy.context.scene.pivot_pro_enabled:
                    #row.prop(context.scene,"pivot_pro_enabled",text='Pro',icon='LAYER_ACTIVE')
                #else:
                    #row.prop(context.scene,"pivot_pro_enabled",text='Pro',icon='LAYER_ACTIVE') 
                                    

        # CUSTOM
        display_header_custom_b = context.user_preferences.addons[__package__].preferences.tab_header_custom_b
        if display_header_custom_b == 'on':  

            row = layout.row(1)
            row.label("Custom", icon = "INFO")                           


        # OBJECT
        display_header_object = context.user_preferences.addons[__package__].preferences.tab_header_object
        if display_header_object == 'on': 
            
            row = layout.row(1)
            
            obj = context.active_object
            if obj is None:                     
                pass
            else:
                row.prop(context.object, "show_x_ray", text="", icon="META_CUBE")
           
            row.prop(context.space_data, "show_backface_culling", text="", icon="MOD_LATTICE")
           
            if obj and obj.mode == 'EDIT' and context.space_data.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
                row.prop(context.space_data, "show_occlude_wire", text="", icon="OUTLINER_DATA_LATTICE")
                
            if obj and obj.mode == 'OBJECT':
                row.operator("object.shade_smooth", text="", icon="SMOOTH")
                row.operator("object.shade_flat", text="", icon="SOLID")                

            if obj and obj.mode == 'EDIT':
                row.operator("mesh.faces_shade_smooth", text="", icon="SMOOTH")
                row.operator("mesh.faces_shade_flat", text="", icon="SOLID") 

            #if not context.scene.render.use_shading_nodes:
                #row.prop(context.scene.game_settings, "material_mode", text="")

            if context.space_data.viewport_shade == 'SOLID':
                row.prop(context.space_data, "show_textured_solid", text="", icon="TEXTURE_SHADED")
                row.prop(context.space_data, "use_matcap", text="", icon="MATCAP_02")
               
                if context.space_data.use_matcap:
 
                    sub = row.row(1)
                    sub.scale_x = 0.2
                    sub.template_icon_view(context.space_data, "matcap_icon")

            elif context.space_data.viewport_shade == 'TEXTURED':
              
                if context.scene.render.use_shading_nodes or context.scene.game_settings .material_mode != 'GLSL':
                    row.prop(context.space_data, "show_textured_shadeless")    


        # HISTORY                
        display_header_history = context.user_preferences.addons[__package__].preferences.tab_header_history
        if display_header_history == 'on': 

            row = layout.row(1)
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.operator("ed.undo_history", text="", icon="RECOVER_LAST")


        # SAVE            
        display_header_save = context.user_preferences.addons[__package__].preferences.tab_header_save
        if display_header_save == 'on': 

            row = layout.row(1)
            row.operator("wm.save_mainfile",text="",icon="FILE_TICK") 
            row.operator("wm.save_as_mainfile",text="",icon="SAVE_AS")     
            

        # VIEW
        display_header_view = context.user_preferences.addons[__package__].preferences.tab_header_view
        if display_header_view == 'on': 

            row = layout.row(1)
            row.operator_context = 'INVOKE_REGION_WIN'                

            row.prop(context.space_data, "show_only_render", text="", icon ="SCENE")
            row.prop(context.space_data, "show_world", text="", icon ="WORLD")
            row.prop(context.space_data, "show_floor", text="", icon ="GRID")
              
            row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")                
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")

            if context.space_data.region_quadviews:
               
                region = context.space_data.region_quadviews[2]
               
                row = layout.row(1)
                row.prop(region, "lock_rotation")
               
                row = layout.row(1)
                row.enabled = region.lock_rotation
                row.prop(region, "show_sync_view")
                
                row = layout.row(1)
                row.enabled = region.lock_rotation and region.show_sync_view
                row.prop(region, "use_box_clip")     


         




### Registry
def register():

    bpy.utils.register_module(__name__)


def unregister():
   
    bpy.utils.unregister_module(__name__)
   
if __name__ == "__main__":
    register()  





