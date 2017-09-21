#
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

__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2016"



# LOAD MODULS #

import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



# HEADER #

class VSE_HEADER(bpy.types.Header):
    bl_space_type = 'SEQUENCE_EDITOR'

    @classmethod
    def poll(self, context):
       return 
       

    def draw(self, context):
        tp = context.window_manager.tp_vse_window
       
        layout = self.layout

        icons = load_icons()
        
        if context.space_data.view_type in {'SEQUENCER', 'SEQUENCER_PREVIEW'}:

            layout.operator_context = 'INVOKE_REGION_WIN'
            layout.operator_context = 'INVOKE_REGION_PREVIEW'
            layout.operator_context = 'INVOKE_DEFAULT'


            if tp.display_vse_view:

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


            if tp.display_vse_add: 

                row = layout.row(1)   
                   
                add_strips = icons.get("add_strips")  
                row.menu("tp_vse.add", text="", icon_value=add_strips.icon_id)  
                
                add_effects = icons.get("add_effects")      
                row.menu("SEQUENCER_MT_add_effect", text="", icon_value=add_effects.icon_id)  


            if tp.display_vse_select:  
                
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
                    

            if tp.display_vse_move:
                
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



            if tp.display_vse_edit:

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

                            
            if tp.display_vse_marker:
                
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

                marker_lock = icons.get("marker_lock")           
                row.prop(bpy.context.tool_settings, "lock_markers", text="", icon_value=marker_lock.icon_id)

                marker_delete = icons.get("marker_delete")
                row.operator("marker.delete", text="", icon_value=marker_delete.icon_id)
                    

            if tp.display_vse_edit:
                
                row = layout.row(1)
                
                strip = context.scene.sequence_editor.active_strip
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
                

                row = layout.row(1)
                row.operator("ed.undo", text="", icon="LOOP_BACK")
                row.operator("ed.redo", text="", icon="LOOP_FORWARDS")




class SEQUENCER_FTH_ADD(bpy.types.Menu):
    bl_label = "Add"
    bl_idname = "tp_vse.add"

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



class Enable_All(bpy.types.Operator):
    """Enable all Icon Tools"""
    bl_idname = "tp_vse.enable_all"
    bl_label = "Enable All"
    bl_options = {'REGISTER', 'UNDO'}    

    def execute(self, context):

        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_add = True
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_view = True
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_select = True
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_move = True
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_marker = True
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_edit = True

        return {'FINISHED'} 

class Disable_All(bpy.types.Operator):
    """Disable all Icon Tools"""
    bl_idname = "tp_vse.disable_all"
    bl_label = "Disable All"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_add = False
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_view = False
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_select = False
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_move = False
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_marker = False
        bpy.data.window_managers["WinMan"].tp_vse_window.display_vse_edit = False

        return {'FINISHED'} 



# REGISTRY #

def register():

    bpy.utils.register_class(VSE_HEADER)
    bpy.utils.register_class(SEQUENCER_FTH_ADD)
    bpy.utils.register_class(Enable_All)
    bpy.utils.register_class(Disable_All)


def unregister():

    bpy.utils.unregister_class(VSE_HEADER)  
    bpy.utils.unregister_class(SEQUENCER_FTH_Add)                
    bpy.utils.unregister_class(Enable_All)       
    bpy.utils.unregister_class(Disable_All)       

if __name__ == "__main__":
    register()  





