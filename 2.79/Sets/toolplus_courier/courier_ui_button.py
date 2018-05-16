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


def draw_buttons_mkb_layout(self, context, layout):

    panel_prefs = context.user_preferences.addons[__package__].preferences
        
    icons = load_icons()

    col = layout.column(align=True)
 
    box = col.box().column(1)  

    box.separator()    
  
    row = box.row(1)          
    row.scale_y = 1   
    row.label("Text Block", icon ="COLLAPSEMENU")  
    row.prop(panel_prefs, 'tab_view_mkb', text="", icon="SAVE_AS") 

    box.separator() 
    
    row = box.row(1)          
    row.scale_x = 1.3
    row.scale_y = 1.3
    row.alignment = 'CENTER' 

    sub = row.row(1)
    sub.label("B0")

    if context.user_preferences.addons[__package__].preferences.text_l0_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l0_mkb", text="", icon=ico_eye) 

    if context.user_preferences.addons[__package__].preferences.text_l1_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l1_mkb", text="", icon=ico_eye) 

    if context.user_preferences.addons[__package__].preferences.text_l2_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l2_mkb", text="", icon=ico_eye) 

    if context.user_preferences.addons[__package__].preferences.text_l3_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l3_mkb", text="", icon=ico_eye) 

    if context.user_preferences.addons[__package__].preferences.text_l4_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l4_mkb", text="", icon=ico_eye) 

    if context.user_preferences.addons[__package__].preferences.text_l5_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l5_mkb", text="", icon=ico_eye) 

    if context.user_preferences.addons[__package__].preferences.text_l6_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l6_mkb", text="", icon=ico_eye) 

    if context.user_preferences.addons[__package__].preferences.text_l7_mkb == True:
        ico_eye="RESTRICT_VIEW_OFF"
    else:
        ico_eye="RESTRICT_VIEW_ON" 
    row.prop(panel_prefs, "text_l7_mkb", text="", icon=ico_eye) 

    row.separator()
        
    if context.user_preferences.addons[__package__].preferences.tab_permanent_mkb == True:
        ico="UNLINKED"
    else:
        ico="LINKED"    
    row.prop(panel_prefs, "tab_permanent_mkb", text="", icon=ico)  

    button_run = icons.get("icon_run")         
    row.operator('tp_ops.do_text_draw_mkb', text="", icon_value=button_run.icon_id)

    box.separator()      


