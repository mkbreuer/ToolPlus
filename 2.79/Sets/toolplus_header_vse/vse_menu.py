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
from . icons.icons import load_icons    



class VIEW3D_TP_VSE_Options_Menu(bpy.types.Menu):
    bl_label = "VSE ICON UI"
    bl_idname = "VIEW3D_TP_VSE_Options_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5     
       
        wm = context.window_manager    
        layout.operator("wm.save_userpref", icon='FILE_TICK')   
 
        layout.separator() 

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
 
        layout.prop(panel_prefs, 'tab_vse_view')
        layout.prop(panel_prefs, 'tab_vse_add')
        layout.prop(panel_prefs, 'tab_vse_select')
        layout.prop(panel_prefs, 'tab_vse_move')
        layout.prop(panel_prefs, 'tab_vse_edit')
        layout.prop(panel_prefs, 'tab_vse_marker')
        layout.prop(panel_prefs, 'tab_vse_history')
        layout.prop(panel_prefs, 'tab_vse_custom')




class VIEW3D_TP_SEQUENCER_ADD(bpy.types.Menu):
    bl_label = "Add"
    bl_idname = "VIEW3D_TP_SEQUENCER_ADD"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("sequencer.movie_strip_add", text="Movie")
        layout.operator("sequencer.image_strip_add", text="Image")
        layout.operator("sequencer.sound_strip_add", text="Sound")

        if len(bpy.data.scenes) > 10:
            layout.operator_context = 'INVOKE_DEFAULT'
            layout.operator("sequencer.scene_strip_add", text="Scene...")
        else:
            layout.operator_menu_enum("sequencer.scene_strip_add", "scene", text="Scene...")

        if len(bpy.data.movieclips) > 10:
            layout.operator_context = 'INVOKE_DEFAULT'
            layout.operator("sequencer.movieclip_strip_add", text="Clips...")
        else:
            layout.operator_menu_enum("sequencer.movieclip_strip_add", "clip", text="Clip...")

        if len(bpy.data.masks) > 10:
            layout.operator_context = 'INVOKE_DEFAULT'
            layout.operator("sequencer.mask_strip_add", text="Masks...")
        else:
            layout.operator_menu_enum("sequencer.mask_strip_add", "mask", text="Mask...")



def act_strip(context):
    try:
        return context.scene.sequence_editor.active_strip
    except AttributeError:
        return None


# UI: MAIN MENU # 
class VIEW3D_TP_VSE_HEADER_Menu(bpy.types.Header):
    bl_space_type = 'SEQUENCE_EDITOR'

    @classmethod
    def poll(self, context):
       return 
   
    def draw(self, context):
        layout = self.layout

        #tp_props = context.window_manager.tp_vse_window
      
        icons = load_icons()
        
        if context.space_data.view_type in {'SEQUENCER', 'SEQUENCER_PREVIEW'}:

            layout.operator_context = 'INVOKE_REGION_WIN'
            layout.operator_context = 'INVOKE_REGION_PREVIEW'
            layout.operator_context = 'INVOKE_DEFAULT'

            row = layout.row(1)

            row.separator() 

            row.menu("VIEW3D_TP_VSE_Options_Menu", text="", icon="SCRIPTWIN")  



            # CUSTOM #
            display_vse_custom = context.user_preferences.addons[__package__].preferences.tab_vse_custom
            if display_vse_custom == True:  
                            

                row = layout.row(1)
                row.label(text="Custom", icon="LAMP") 


            
            
            # VIEW #            
            display_vse_view = context.user_preferences.addons[__package__].preferences.tab_vse_view
            if display_vse_view == True:  

                row = layout.row(1)
                row.operator_context = 'INVOKE_REGION_WIN'

                view_all = icons.get("view_all") 
                row.operator("sequencer.view_all", text="", icon_value=view_all.icon_id)                    

                view_selected = icons.get("view_selected")     
                row.operator("sequencer.view_selected", text="", icon_value=view_selected.icon_id)

                row = layout.row(1)

                range_clear = icons.get("range_clear")             
                row.operator("anim.previewrange_clear", text="", icon_value=range_clear.icon_id)

                range_set = icons.get("range_set") 
                row.operator("anim.previewrange_set", text="", icon_value=range_set.icon_id)
          
            
            # ADD #            
            display_vse_add = context.user_preferences.addons[__package__].preferences.tab_vse_add
            if display_vse_add == True:  

                row = layout.row(1)   
                   
                add_strips = icons.get("add_strips")  
                row.menu("tp_vse.add", text="", icon_value=add_strips.icon_id)  
                
                add_effects = icons.get("add_effects")      
                row.menu("SEQUENCER_MT_add_effect", text="", icon_value=add_effects.icon_id)  


            # SELECT #          
            display_vse_select = context.user_preferences.addons[__package__].preferences.tab_vse_select
            if display_vse_select == True: 
 
                row = layout.row(1)
                
                select_all_left = icons.get("select_all_left")             
                props = row.operator("sequencer.select", text="", icon_value=select_all_left.icon_id)
                props.left_right = 'LEFT'
                props.linked_time = True
                
                select_left = icons.get("select_left")  
                row.operator("sequencer.select_active_side", text="", icon_value=select_left.icon_id).side = 'LEFT'

                select_handle_left = icons.get("select_handle_left")              
                row.operator("sequencer.select_handles", text="", icon_value=select_handle_left.icon_id).side = 'LEFT'

                select_handle_both = icons.get("select_handle_both")  
                row.operator("sequencer.select_handles", text="", icon_value=select_handle_both.icon_id).side = 'BOTH'

                select_handle_right = icons.get("select_handle_right")  
                row.operator("sequencer.select_handles", text="", icon_value=select_handle_right.icon_id).side = 'RIGHT'

                select_right = icons.get("select_right")  
                row.operator("sequencer.select_active_side", text="", icon_value=select_right.icon_id).side = 'RIGHT'
                
                select_all_right = icons.get("select_all_right")  
                props = row.operator("sequencer.select", text="", icon_value=select_all_right.icon_id)
                props.left_right = 'RIGHT'
                props.linked_time = True
                        
    
            # MOVE #
            display_vse_move = context.user_preferences.addons[__package__].preferences.tab_vse_move
            if display_vse_move == True: 

                row = layout.row(1)

                swap_left = icons.get("swap_left")                  
                row.operator("sequencer.swap", text="", icon_value=swap_left.icon_id).side = 'LEFT'             
     
                row.operator("transform.transform", text="", icon = "MAN_TRANS").mode = 'TRANSLATION'
                
                snap = icons.get("snap")
                row.operator("sequencer.snap", text="", icon_value=snap.icon_id)
                
                swap_right = icons.get("swap_right")      
                row.operator("sequencer.swap", text="", icon_value=swap_right.icon_id).side = 'RIGHT'

                row = layout.row(1)  
               
                row.operator("sequencer.slip", text="", icon = "SNAP_INCREMENT")

                time_extend = icons.get("time_extend")
                row.operator("transform.transform", text="", icon_value=time_extend.icon_id).mode = 'TIME_EXTEND'   

                clear_offset = icons.get("clear_offset")
                row.operator("sequencer.offset_clear", text="", icon_value=clear_offset.icon_id)
               
                row = layout.row(1)   
                            
                row.operator("sequencer.duplicate_move", text="", icon = "PASTEFLIPDOWN")

           
            # EDIT #
            display_vse_edit = context.user_preferences.addons[__package__].preferences.tab_vse_edit
            if display_vse_edit == True: 

                row = layout.row(1) 

                cut_soft = icons.get("cut_soft")
                row.operator("sequencer.cut", text="", icon_value=cut_soft.icon_id).type = 'HARD'

                cut_hard = icons.get("cut_hard")
                row.operator("sequencer.cut", text="", icon_value=cut_hard.icon_id).type = 'SOFT'

                row = layout.row(1)  
                
                gap_insert = icons.get("gap_insert")
                row.operator("sequencer.gap_insert", text="", icon_value=gap_insert.icon_id)

                gap_remove = icons.get("gap_remove")
                row.operator("sequencer.gap_remove", text="", icon_value=gap_remove.icon_id).all = False

                row = layout.row(1)

                meta_make = icons.get("meta_make")
                row.operator("sequencer.meta_make", text="", icon_value=meta_make.icon_id)

                meta_separate = icons.get("meta_separate")
                row.operator("sequencer.meta_separate", text="", icon_value=meta_separate.icon_id)

                row = layout.row(1)
                row.operator("sequencer.unmute", text="", icon = "VISIBLE_IPO_ON").unselected = False
                row.operator("sequencer.mute", text="", icon = "VISIBLE_IPO_OFF").unselected = False

                mute_unselected = icons.get("mute_unselected")
                row.operator("sequencer.mute", text="", icon_value=mute_unselected.icon_id).unselected = True

                row = layout.row(1)
                row.operator("sequencer.lock", text="", icon = "LOCKED")
                row.operator("sequencer.unlock", text="", icon = "UNLOCKED")

                row = layout.row(1)
                row.operator("sequencer.images_separate", text="", icon = "RENDERLAYERS")

                deinterlace = icons.get("deinterlace")
                row.operator("sequencer.deinterlace_selected_movies", text="",icon_value=deinterlace.icon_id)
                row.operator("sequencer.rebuild_proxy", text="", icon = "FILE_REFRESH")   

 
            # MARKER # 
            display_vse_marker = context.user_preferences.addons[__package__].preferences.tab_vse_marker
            if display_vse_marker == True:    

                row = layout.row(1)
                
                marker_add = icons.get("marker_add")
                row.operator("marker.add",  text="", icon_value=marker_add.icon_id)

                marker_rename = icons.get("marker_rename")
                row.operator("marker.rename", text="", icon_value=marker_rename.icon_id)

                marker_dupli = icons.get("marker_dupli")
                row.operator("marker.duplicate", text="", icon_value=marker_dupli.icon_id)            
                  
                row = layout.row(1)  

                marker_jump_left = icons.get("marker_jump_left")                     
                row.operator("screen.marker_jump", text="", icon_value=marker_jump_left.icon_id).next = False

                marker_move = icons.get("marker_move")
                row.operator("marker.move", text="", icon_value=marker_move.icon_id)

                marker_jump_right = icons.get("marker_jump_right")
                row.operator("screen.marker_jump", text="", icon_value=marker_jump_right.icon_id).next = True

                row = layout.row(1)            
              
                #if len(bpy.data.scenes) > 10:                
                   # marker_dupli_scene = icons.get("marker_dupli_scene")   
                    #row.operator_context = 'INVOKE_DEFAULT'
                   # row.operator("marker.make_links_scene", text="", icon_value=marker_dupli_scene.icon_id)
                #else:
                   # marker_dupli_scene = icons.get("marker_dupli_scene")  
                    #row.operator_context = 'INVOKE_DEFAULT'
                    #row.operator_menu_enum("marker.make_links_scene", "scene", text="", icon_value=marker_dupli_scene.icon_id)

                marker_lock = icons.get("marker_lock")           
                row.prop(bpy.context.tool_settings, "lock_markers", text="", icon_value=marker_lock.icon_id)

                marker_delete = icons.get("marker_delete")
                row.operator("marker.delete", text="", icon_value=marker_delete.icon_id)
                
            
            # EDIT #
            display_vse_edit = context.user_preferences.addons[__package__].preferences.tab_vse_edit
            if display_vse_edit == True: 

                row = layout.row(1)
                strip = act_strip(context)    
                            
                if strip:
                    stype = strip.type
                    
                    if stype == 'EFFECT':
                        pass
                    
                    elif stype == 'IMAGE':         
                        row.operator("sequencer.rendersize", text="", icon = "AXIS_TOP")
                   
                    elif stype == 'SCENE':
                        pass
                   
                    elif stype == 'MOVIE':
                        row.operator_context = 'INVOKE_REGION_WIN'
                        row.operator("sequencer.rendersize", text="", icon = "AXIS_TOP")
                    
                    elif stype == 'SOUND':
                        row.operator_context = 'INVOKE_REGION_WIN'
                        row.operator("sequencer.crossfade_sounds", text="", icon = "SOUND")        

            
            # HISTORY #
            display_vse_history = context.user_preferences.addons[__package__].preferences.tab_vse_history
            if display_vse_history == True: 
                
                row = layout.row(1)
                row.operator("ed.undo", text="", icon="FRAME_PREV")
                row.operator("ed.redo", text="", icon="FRAME_NEXT")
