# ##### BEGIN GPL LICENSE BLOCK #####
#
#Copyright (C) 2017  Marvin.K.Breuer (MKB)]
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


bl_info = {
    'name': "T+ UV Image Tools",
    'author': "MKB",
    'version': (1, 0, 0),
    'blender': (2, 7, 8),
    'location': "Image Editor > TAB > Tools & Image",
    'description': "UV IMAGE TOOL",
    'category': 'ToolPlus'}

    # changes by russcript:tested 2.7 RC windows and linux	
    # added tabs organization (line 46)
    # toolbar now shows only in uv edit modes and not uv sculpt(line 51)
    # changed a few tooltips and labels, for clarity
    # made the Islands tools button show only in uv edit mode(line 622)
    # hope this helps, thanks for the addon
   


#from .uv_squares import *
from toolplus_uv_image_tools.uv_pie import (VIEW3D_TP_UV_EditSpace_Pie)
from toolplus_uv_image_tools.uv_pie import (VIEW3D_TP_UV_Sculpt_Pie)
from toolplus_uv_image_tools.uv_pie import register_icons, unregister_icons


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_uv_image_tools'))

if "bpy" in locals():
    import imp
    imp.reload(uv_action)
    imp.reload(uv_align)
    imp.reload(uv_pivot)
    imp.reload(uv_squares)

else:
    from . import uv_action         
    from . import uv_align         
    from . import uv_pivot         
    from . import uv_squares  



import bpy, re
from bpy import *
import bpy.utils.previews

from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import* #(StringProperty, BoolProperty, FloatVectorProperty, FloatProperty, EnumProperty, IntProperty)


def update_panel_position_uv(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_UV_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_UV_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_UV_Panel_UI)

    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_uv == 'tools':

        VIEW3D_TP_UV_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_uv
        bpy.utils.register_class(VIEW3D_TP_UV_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_uv == 'ui':
        bpy.utils.register_class(VIEW3D_TP_UV_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_uv == 'off':
        pass



def update_panel_position_image(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Image_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Image_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Image_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_image == 'tools':

        VIEW3D_TP_Image_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_image
        bpy.utils.register_class(VIEW3D_TP_Image_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_image == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Image_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_image == 'off':
        pass
        
        
        
addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_UV_EditSpace_Pie)
        bpy.utils.unregister_class(VIEW3D_TP_UV_Sculpt_Pie)
        
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        VIEW3D_TP_UV_EditSpace_Pie.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
        VIEW3D_TP_UV_Sculpt_Pie.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_UV_EditSpace_Pie)
        bpy.utils.register_class(VIEW3D_TP_UV_Sculpt_Pie)
    
        wm = bpy.context.window_manager

        km = wm.keyconfigs.addon.keymaps.new(name='Image', space_type='IMAGE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS') #shift=True, alt=True, ctrl=True 
        kmi.properties.name = 'tp_pie.uv_editspace'


        km = wm.keyconfigs.addon.keymaps.new(name='UV Sculpt')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS') #shift=True, alt=True, ctrl=True 
        kmi.properties.name = 'tp_pie.uv_sculpt'


    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass

    

#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),               
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location_uv = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'disable panel in the shelf')),
               default='tools', update = update_panel_position_uv)

    tab_location_image = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'disable panel in the shelf')),
               default='tools', update = update_panel_position_image)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)


    tools_category_uv = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_uv)
    tools_category_image = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_image)

    tools_category_menu = bpy.props.BoolProperty(name = "Pie Menu", description = "enable or disable menu", default=True, update = update_menu)


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            box = layout.box().column(1)
             
            row = box.column(1)   
            row.label(text="Welcome to T+ UV Image Tool Collection!")  
            row.label(text="This addon set is for editing uv in UV-Editor")   
            row.label(text="As changeable panel or menu")   
            row.label(text="Have Fun! :)")   


        #Location
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1) 
            
            row = box.row(1) 
            row.label("Location UV Tools Panel: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location_uv', expand=True)

            if self.tab_location_uv == 'tools':
                
                row = box.row()
                row.prop(self, "tools_category_uv")               
            
            box.separator()
        
            box = layout.box().column(1) 

            row = box.row(1) 
            row.label("Location Image Tools Panel: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location_image', expand=True)
            if self.tab_location_image == 'tools':

                row = box.row()                
                row.prop(self, "tools_category_image")
                            
            box.separator()

            row = layout.row()
            row.label(text="! please reboot blender after changing the panel location !", icon ="INFO")

            box.separator() 
            
        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Pie Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("UV Editor / UV Sculpt: SPACEBAR")
          
            box.separator() 
         
            row = box.column(1)  
            row.label("Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("UV Editor > UV Squares: ALT+E")
            row.label("UV Editor > Rip Faces: ALT+V")
            row.label("UV Editor > Join Faces: ALT+SHIFT+V")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
            
            row = layout.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")


        #Weblinks
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
             
            row = box.column_flow(2) 
            row.operator('wm.url_open', text = 'UV Align/Distribution', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/UV/UV_Align_Distribution"
            row.operator('wm.url_open', text = 'UV Square', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/UV/Uv_Squares"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?339842-Addon-UV-Image-Tools&highlight="
            row.operator('wm.url_open', text = 'iskeyfree', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"



class Dropdown_UVTool_Props(bpy.types.PropertyGroup):

    display_uvtransform = bpy.props.BoolProperty(name = "Transform", description = "Display UV Transfrom Tools", default = False)
    display_uvalign = bpy.props.BoolProperty(name = "Align", description = "Display UV Align Tools", default = False)
    display_uvselection = bpy.props.BoolProperty(name = "Selection", description = "Display UV Selection Tools", default = False)
    display_uvediting = bpy.props.BoolProperty(name = "Editing", description = "Display UV Editing Tools", default = False)
    display_uvisland = bpy.props.BoolProperty(name = "Island", description = "Display UV Island Tools", default = False)
    display_uvhide = bpy.props.BoolProperty(name = "Hidden", description = "Display UV Hide Tools", default = False)



def draw_uv_panel_layout(self, context, layout):
        
        tp_props = context.window_manager.uv_window
        scn = context.scene        

        icons = icon_collections["main"]
       
        # Selections
        if tp_props.display_uvselection:
            ###       
            box = layout.box()
            row = box.row()                    
            row.prop(tp_props, "display_uvselection", text="", icon='TRIA_DOWN')
         
        else:
            box = layout.box()
            row = box.row()        
            row.prop(tp_props, "display_uvselection", text="", icon='TRIA_RIGHT')
            
        row.label("Select...")        

        button_select_all = icons.get("icon_select_all") 
        row.operator("uv.select_all", text="", icon_value=button_select_all.icon_id).action='SELECT'

        button_select_box = icons.get("icon_select_box") 
        row.operator("uv.select_border", text="", icon_value=button_select_box.icon_id).pinned=True
   
        ###                  
        if tp_props.display_uvselection:

            ###        
            system = context.user_preferences.system
            inputs = context.user_preferences.inputs
            edit = context.user_preferences.edit
                        
            box = layout.box().column(1) 
            
            row = box.row(1)
            row.prop(inputs, "select_mouse", expand=True)
                        
            box.separator()

            row = box.row(1)

            button_select_invert = icons.get("icon_select_invert") 
            row.operator("uv.select_all", text="Invert", icon_value=button_select_invert.icon_id).action='INVERT'
            
            button_select_pinned = icons.get("icon_select_pinned") 
            row.operator("uv.select_pinned", text="Pinned", icon_value=button_select_pinned.icon_id) 

            row = box.row(1)

            button_select_link = icons.get("icon_select_link") 
            row.operator("uv.select_linked", text="Linked", icon_value=button_select_link.icon_id)
            
            button_select_split = icons.get("icon_select_split") 
            row.operator("uv.select_split", text="Split", icon_value=button_select_split.icon_id)

               
            box.separator()
            
            #--Snap

            box = layout.box().column(1) 

            row = box.row(1)  
            row.label('Selected to...')
                        
            row = box.row(1)
            row.operator("uv.snap_selected", text="-> Cursor").target="CURSOR"         
            row.operator("uv.snap_selected", text="-> Offset").target="CURSOR_OFFSET"

            box.separator()
            
            row = box.row(1)
            row.operator("uv.snap_selected", text="-> Pixel").target="PIXELS"         
            row.operator("uv.snap_selected", text="-> Adjacent").target="ADJACENT_UNSELECTED"
                       
            box.separator()

            row = box.row(1)  
            row.label('Cursor to...')
              
            row = box.row(1)  
            row.operator("uv.snap_cursor", text="-> Selected").target="SELECTED"
            row.operator("uv.snap_cursor", text="-> Pixel").target="PIXELS"
       
            box.separator()


        # Align UV
        if tp_props.display_uvalign:
            ###         
            box = layout.box()
            row = box.row()                    
            row.prop(tp_props, "display_uvalign", text="", icon='TRIA_DOWN')
         
        else:
            box = layout.box()
            row = box.row()        
            row.prop(tp_props, "display_uvalign", text="", icon='TRIA_RIGHT')
            
        row.label("Unwrap....")        

        button_uv_reset = icons.get("icon_uv_reset")   
        row.operator("uv.reset", text="", icon_value=button_uv_reset.icon_id)   
        row.operator("uv.unwrap", text="", icon = "GROUP_UVS")

        ###                   
        if tp_props.display_uvalign:
 
            box = layout.box().column(1) 
            
            ###
            row = box.row(1)
            row.label("Seams...")  
      
            row.separator()               
           
            button_edit_seams = icons.get("icon_edit_seams")               
            row.operator("uv.mark_seam", text="", icon_value=button_edit_seams.icon_id)
           
            row.separator()
            
            button_edit_seams_island = icons.get("icon_edit_seams_island")                                        
            row.operator("uv.seams_from_islands", text="", icon_value=button_edit_seams_island.icon_id)    

            box.separator() 
 
            ###
            row = box.row(1)
            row.label("Weld / Stitch...")   
            
            row.separator()  

            button_edit_weld = icons.get("icon_edit_weld")                                            
            row.operator("uv.weld", text="", icon_value=button_edit_weld.icon_id)

            row.separator()    
                
            button_edit_stitch = icons.get("icon_edit_stitch")                    
            row.operator("uv.stitch", text="", icon_value=button_edit_stitch.icon_id)            
            
            box.separator()                         
            
            ###
            row = box.row(1)
            row.label("Join / Rip...")   
            
            row.separator()  

            button_edit_join = icons.get("icon_edit_join")                
            row.operator("uv.uv_face_join", text="", icon_value=button_edit_join.icon_id) 

            row.separator() 
            
            button_edit_rip = icons.get("icon_edit_rip")            
            row.operator("uv.uv_face_rip", text="", icon_value=button_edit_rip.icon_id)

            box.separator()

            ###
            row = box.row(1)
            row.label("Un-/ Pin...")  
            
            row.separator()  

            row.operator("uv.pin", text="", icon="UNPINNED").clear=True                            
            
            row.separator()      
            row.operator("uv.pin", text="", icon="PINNED").clear=False

            box.separator()

            ###
            row = box.row(1) 
            row.label(text="Straight...")
           
            row.separator()  

            row.operator("uv.align", text="", icon ="AUTO").axis='ALIGN_S'

            row.separator()

            button_straighten_y = icons.get("icon_straighten_y")
            row.operator("uv.align", text="", icon_value=button_straighten_y.icon_id).axis='ALIGN_T'

            row.separator()

            button_straighten_x = icons.get("icon_straighten_x")
            row.operator("uv.align", text="", icon_value=button_straighten_x.icon_id).axis='ALIGN_U'

            box.separator()


            ###
            row = box.row(1)  
            row.label(text="Snap...")

            row.separator()            
           
            row.operator("uv.align", text="", icon ="AUTO").axis='ALIGN_AUTO'

            row.separator()

            button_align_y_axis = icons.get("icon_align_y_axis")
            row.operator("uv.align", text="", icon_value=button_align_y_axis.icon_id).axis='ALIGN_X'

            row.separator()
            
            button_align_x_axis = icons.get("icon_align_x_axis")
            row.operator("uv.align", text="", icon_value=button_align_x_axis.icon_id).axis='ALIGN_Y'
            
            #row.operator("uv.uv_snap_to_axis", text="Snap to X/Y-Axis")
            #row.operator("uv.uv_snap_to_axis_and_equal", text="Snap with Equal Distance")

            box.separator()    

            ###
            row = box.row(1)
            row.label("Relax...")  
          
            row.separator()
            
            button_uv_show_stretch = icons.get("icon_uv_show_stretch")   
            row.prop(context.space_data.uv_editor, "show_stretch",text="", icon_value=button_uv_show_stretch.icon_id)   

            row.separator()

            button_uv_stretch = icons.get("icon_uv_stretch")   
            row.operator("uv.minimize_stretch", text="", icon_value=button_uv_stretch.icon_id)            

            box.separator()


            ###
            row = box.row(1)  
            row.label(text="Match...")

            row.separator()
            
            button_edit_match = icons.get("icon_edit_match")            
            row.operator("uv.match_island", text="", icon_value=button_edit_match.icon_id)   

            box.separator()                      


            ###
            row = box.row(1)
            row.label("Remove...")  
          
            row.separator()

            button_edit_remove = icons.get("icon_edit_remove")                               
            row.operator("uv.remove_doubles", text="", icon_value=button_edit_remove.icon_id) 

            box.separator()

            ###
            box = layout.box().column(1) 

            row = box.row(1)  
            row.label(text="Grid...")
                        
            row.separator()

            button_snap_grid_noneq = icons.get("icon_snap_grid_noneq")
            row.operator("uv.uv_squares_by_shape", text="", icon_value=button_snap_grid_noneq.icon_id)

            row.separator()

            button_snap_grid_eq = icons.get("icon_snap_grid_eq")
            row.operator("uv.uv_squares", text="", icon_value=button_snap_grid_eq.icon_id)
                
            row.separator()
            
            button_snap_grid_pack = icons.get("icon_snap_grid_pack")
            row.operator("uv.pack_islands", text="", icon_value=button_snap_grid_pack.icon_id)

            box.separator()
  
            ###                       
            row = box.row(1)  
            row.label(text="Mirror...")
           
            row.separator()    
                    
            button_uv_mirror = icons.get("icon_uv_mirror")           
            row.operator("mesh.faces_mirror_uv", text="", icon_value=button_uv_mirror.icon_id)

            row.separator()
            
            button_mirror_y = icons.get("icon_mirror_y")
            row.operator("uv.rotateoneeighty", text="", icon_value=button_mirror_y.icon_id)    

            row.separator()

            button_mirror_x = icons.get("icon_mirror_x")
            row.operator("transform.mirror", text="", icon_value=button_mirror_x.icon_id).constraint_axis=(True, False, False)
          
            box.separator()

            ###
            row = box.row(1)  
            row.label(text="Rotation...")

            row.separator() 

            button_rotation_one_eighty = icons.get("icon_rotation_one_eighty")           
            row.operator("uv.align_rotation", text="", icon_value=button_rotation_one_eighty.icon_id)           
              
            row.separator()

            button_rotation_minus_ninety = icons.get("icon_rotation_minus_ninety")           
            row.operator("uv.rotatednineminus", text="", icon_value=button_rotation_minus_ninety.icon_id)           

            row.separator()

            button_rotation_plus_ninety = icons.get("icon_rotation_plus_ninety")
            row.operator("uv.rotatednine", text="", icon_value=button_rotation_plus_ninety.icon_id) 

            box.separator()

            ###
            row = box.row(1)  
            row.label(text="Scale...")

            row.separator() 
            
            row.operator("uv.average_islands_scale", text="", icon = "MAN_SCALE")  
           
            row.separator()            
           
            button_align_scale_eq = icons.get("icon_align_scale_eq")                       
            row.operator("uv.equalize_scale", text="", icon_value=button_align_scale_eq.icon_id)

            box.separator()            
            
            ###            
            box = layout.box().column(1) 
            
            row = box.row(1)  
            row.label(text="Align...")

            row.separator() 

            button_align_vertical_center = icons.get("icon_align_vertical_center")
            row.operator("uv.align_vertical_axis",text='', icon_value=button_align_vertical_center.icon_id)

            row.separator()            

            button_align_bottom = icons.get("icon_align_bottom")
            row.operator("uv.align_low_margin",text='', icon_value=button_align_bottom.icon_id)  

            row.separator() 

            button_align_right = icons.get("icon_align_right")
            row.operator("uv.align_right_margin",text='', icon_value=button_align_right.icon_id)  
            
            box.separator()
            
            ###
            
            row = box.row(1)  
            row.label(text="")

            row.separator()            

            button_align_horizontal_center = icons.get("icon_align_horizontal_center")
            row.operator("uv.align_horizontal_axis",text='', icon_value=button_align_horizontal_center.icon_id)
            
            row.separator()            

            button_align_top = icons.get("icon_align_top")
            row.operator("uv.align_top_margin",text='', icon_value=button_align_top.icon_id)

            row.separator()             

            button_align_left = icons.get("icon_align_left")
            row.operator("uv.align_left_margin",text='', icon_value=button_align_left.icon_id)     

            box.separator()
            
            ###

            row = box.column(1)  
            row.prop(scn,"relativeItems", text='Relativ')  
            row.prop(scn,"selectionAsGroup")
 
            box.separator()
                        
            ###            
            
            box = layout.box().column(1) 
            
            row = box.row(1) 
            row.label(text="Spread...")

            row.separator()

            button_distribute_vertical = icons.get("icon_distribute_vertical")
            row.operator("uv.equalize_vertical_gap", text='', icon_value=button_distribute_vertical.icon_id)

            row.separator()

            button_distribute_heights = icons.get("icon_distribute_heights")
            row.operator("uv.distribute_center_vertically", text='', icon_value=button_distribute_heights.icon_id)            

            row.separator() 

            button_distribute_down = icons.get("icon_distribute_down")
            row.operator("uv.distribute_bedges_vertically", text='', icon_value=button_distribute_down.icon_id)

            row.separator() 

            button_distribute_right = icons.get("icon_distribute_right")
            row.operator("uv.distribute_redges_horizontally", text='', icon_value=button_distribute_right.icon_id)

            box.separator()            
          
            ###
            
            row = box.row(1) 
            row.label(text=" ")

            row.separator()

            button_distribute_horizontal = icons.get("icon_distribute_horizontal")
            row.operator("uv.equalize_horizontal_gap", text='', icon_value=button_distribute_horizontal.icon_id)

            row.separator()

            button_distribute_widths = icons.get("icon_distribute_widths")
            row.operator("uv.distribute_center_horizontally", text='', icon_value=button_distribute_widths.icon_id)

            row.separator() 

            button_distribute_up = icons.get("icon_distribute_up")
            row.operator("uv.distribute_tedges_vertically", text='', icon_value=button_distribute_up.icon_id)

            row.separator() 

            button_distribute_left = icons.get("icon_distribute_left")              
            row.operator("uv.distribute_ledges_horizontally", text='', icon_value=button_distribute_left.icon_id)
 


            box.separator()            
          
            ###

            #button_triangle_up = icons.get("icon_triangle_up")            
            #button_triangle_left = icons.get("icon_triangle_left")
            #button_triangle_corner_left_up = icons.get("icon_triangle_corner_left_up")
            #button_triangle_corner_right_down = icons.get("icon_triangle_corner_right_down")
            #button_triangle_right = icons.get("icon_triangle_right")
            #button_triangle_down = icons.get("icon_triangle_down")            
            #text='', icon_value=button_triangle_up.icon_id)     



        # Hidden            
        if tp_props.display_uvhide:
            ###         
            box = layout.box()
            row = box.row()                    
            row.prop(tp_props, "display_uvhide", text="", icon='TRIA_DOWN')
         
        else:
            box = layout.box()
            row = box.row()        
            row.prop(tp_props, "display_uvhide", text="", icon='TRIA_RIGHT')
                   
        row.label("View...")  
        row.operator("ed.undo", text="", icon="LOOP_BACK")
        row.operator("ed.redo", text="", icon="LOOP_FORWARDS")                 

        ###                   
        if tp_props.display_uvhide:
            ###           
            box = layout.box().column(1) 
            
            row = box.row(1)         
            row.operator("uv.reveal", text="Show All", icon="VISIBLE_IPO_ON") 
            row.operator("ed.undo_history", text="History", icon="SCRIPTPLUGINS")
        
            row = box.row(1)     
            row.operator("uv.hide", text="UnHide", icon ="RESTRICT_VIEW_OFF").unselected=True            
            row.operator("uv.hide", text="Hide", icon="RESTRICT_VIEW_ON").unselected=False

            box.separator() 


        # Save                        
        box = layout.box().column(1) 
        
        row = box.row(1)
        row.operator("uv.export_layout", text="Export UV Layout")
        
        row.separator()                
        row.operator("wm.save_mainfile",text="",icon="FILE_TICK")

        row.separator()   
        row.operator("wm.save_as_mainfile",text="",icon="SAVE_AS")

        box.separator()        


    


class VIEW3D_TP_UV_Panel_TOOLS(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_UV_Panel_TOOLS"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'UvTools'
    bl_label = "UV Tools"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        sima = context.space_data
        return sima.show_uvedit and not context.tool_settings.use_uv_sculpt

  
    def draw(self, context):
        tp_props = context.window_manager.uv_window
        scn = context.scene
        layout = self.layout.column(1) 
        
        draw_uv_panel_layout(self, context, layout) 




class VIEW3D_TP_UV_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_UV_Panel_UI"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_label = "UV Tools"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        sima = context.space_data
        return sima.show_uvedit and not context.tool_settings.use_uv_sculpt

  
    def draw(self, context):
        tp_props = context.window_manager.uv_window
        scn = context.scene
        layout = self.layout.column(1) 

        draw_uv_panel_layout(self, context, layout) 

        




def draw_image_panel_layout(self, context, layout) :
        scn = context.scene
        
        icons = icon_collections["main"]
        
        # Image                                  
        box = layout.box().column(1) 
        
        row = box.row(1)

        my_button_one = icons.get("my_image1")
        row.label(text="", icon_value=my_button_one.icon_id)  
        
        row.label(text="Image...")
        
        row = box.row(1)
        row.operator("image.open", text="Open", icon="FILESEL")
        row.operator("image.new", text="New")
        
        row = box.row(1)
        row.operator("image.reload", text="Reload")
        row.operator("image.replace", text="Replace")
        
        box.separator()   

        row = box.row(1)
        row.prop(context.user_preferences.filepaths, "image_editor", text="")
        row.operator("image.external_edit",text="External Edit ") 
        
        box.separator()
        
        # Image Pack                
        box = layout.box().column(1) 
        
        row = box.row(1)
        row.label(text="Pack into File...")

        row = box.row(1)
        row.operator("image.pack", text="Pack", icon="PACKAGE")
        row.operator("image.pack", text="Pack as PNG").as_png=True
               
        box.separator()     
           
        # Save             
        box = layout.box().column(1) 
        
        row = box.row(1)
        row.label(text="Save...")

        row = box.row(1)
        row.operator("image.save", text="Save", icon="FILE_TICK")
        row.operator("image.save_as", text="Save as" , icon="SAVE_AS")
        row.operator("image.save_as", text="Save Copy").copy=True
       
        box.separator()


    
class VIEW3D_TP_Image_Panel_TOOLS(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Image_Panel_TOOLS"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'UvTools'
    bl_label = "Image Tools"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        sima = context.space_data
        return sima.show_uvedit and not context.tool_settings.use_uv_sculpt

  
    def draw(self, context):
        tp_props = context.window_manager.uv_window
        scn = context.scene
        layout = self.layout.column(1) 
        
        draw_image_panel_layout(self, context, layout) 



class VIEW3D_TP_Image_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Image_Panel_UI"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Image Tools"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        sima = context.space_data
        return sima.show_uvedit and not context.tool_settings.use_uv_sculpt

  
    def draw(self, context):
        tp_props = context.window_manager.uv_window
        scn = context.scene
        layout = self.layout.column(1) 

        draw_image_panel_layout(self, context, layout) 






def menu_func_uv_squares(self, context): self.layout.operator('uv.uv_squares')
def menu_func_uv_squares_by_shape(self, context): self.layout.operator('uv.uv_squares_by_shape')
def menu_func_face_rip(self, context): self.layout.operator('uv.uv_face_rip')
def menu_func_face_join(self, context): self.layout.operator('uv.uv_face_join')


###################################
# register

import traceback

icon_collections = {}

def register():
    register_icons()
    
    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    mkb_icons.load("my_image1", os.path.join(icons_dir, "icon_image1.png"), 'IMAGE')
    mkb_icons.load("my_image2", os.path.join(icons_dir, "icon_image2.png"), 'IMAGE')

    mkb_icons.load("icon_triangle_left", os.path.join(icons_dir, "triangle_left.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_right", os.path.join(icons_dir, "triangle_right.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_up", os.path.join(icons_dir, "triangle_up.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_down", os.path.join(icons_dir, "triangle_down.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_left_up", os.path.join(icons_dir, "triangle_corner_left_up.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_right_up", os.path.join(icons_dir, "triangle_corner_right_up.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_left_down", os.path.join(icons_dir, "triangle_corner_left_down.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_right_down", os.path.join(icons_dir, "triangle_corner_right_down.png"), 'IMAGE')

    mkb_icons.load("icon_align_bottom", os.path.join(icons_dir, "align_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_align_horizontal_center", os.path.join(icons_dir, "align_horizontal_center.png"), 'IMAGE')
    mkb_icons.load("icon_align_left", os.path.join(icons_dir, "align_left.png"), 'IMAGE')
    mkb_icons.load("icon_align_right", os.path.join(icons_dir, "align_right.png"), 'IMAGE')
    mkb_icons.load("icon_align_scale_eq", os.path.join(icons_dir, "align_scale_eq.png"), 'IMAGE')
    mkb_icons.load("icon_align_top", os.path.join(icons_dir, "align_top.png"), 'IMAGE')
    mkb_icons.load("icon_align_vertical_center", os.path.join(icons_dir, "align_vertical_center.png"), 'IMAGE')

    mkb_icons.load("icon_align_x_axis", os.path.join(icons_dir, "align_x_axis.png"), 'IMAGE')
    mkb_icons.load("icon_align_y_axis", os.path.join(icons_dir, "align_y_axis.png"), 'IMAGE')

    mkb_icons.load("icon_distribute_down", os.path.join(icons_dir, "distribute_down.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_heights", os.path.join(icons_dir, "distribute_heights.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_horizontal", os.path.join(icons_dir, "distribute_horizontal.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_left", os.path.join(icons_dir, "distribute_left.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_right", os.path.join(icons_dir, "distribute_right.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_up", os.path.join(icons_dir, "distribute_up.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_vertical", os.path.join(icons_dir, "distribute_vertical.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_widths", os.path.join(icons_dir, "distribute_widths.png"), 'IMAGE')
    
    mkb_icons.load("icon_edit_join", os.path.join(icons_dir, "edit_join.png"), 'IMAGE')
    mkb_icons.load("icon_edit_match", os.path.join(icons_dir, "edit_match.png"), 'IMAGE')
    mkb_icons.load("icon_edit_remove", os.path.join(icons_dir, "edit_remove.png"), 'IMAGE')
    mkb_icons.load("icon_edit_rip", os.path.join(icons_dir, "edit_rip.png"), 'IMAGE')
    mkb_icons.load("icon_edit_seams", os.path.join(icons_dir, "edit_seams.png"), 'IMAGE')
    mkb_icons.load("icon_edit_seams_island", os.path.join(icons_dir, "edit_seams_island.png"), 'IMAGE')
    mkb_icons.load("icon_edit_stitch", os.path.join(icons_dir, "edit_stitch.png"), 'IMAGE')
    mkb_icons.load("icon_edit_weld", os.path.join(icons_dir, "edit_weld.png"), 'IMAGE')

    mkb_icons.load("icon_mirror_x", os.path.join(icons_dir, "mirror_x.png"), 'IMAGE')
    mkb_icons.load("icon_mirror_y", os.path.join(icons_dir, "mirror_y.png"), 'IMAGE')

    mkb_icons.load("icon_rotation_minus_ninety", os.path.join(icons_dir, "rotation_minus_ninety.png"), 'IMAGE')
    mkb_icons.load("icon_rotation_one_eighty", os.path.join(icons_dir, "rotation_one_eighty.png"), 'IMAGE')
    mkb_icons.load("icon_rotation_plus_ninety", os.path.join(icons_dir, "rotation_plus_ninety.png"), 'IMAGE')

    mkb_icons.load("icon_select_all", os.path.join(icons_dir, "select_all.png"), 'IMAGE')
    mkb_icons.load("icon_select_box", os.path.join(icons_dir, "select_box.png"), 'IMAGE')
    mkb_icons.load("icon_select_invert", os.path.join(icons_dir, "select_invert.png"), 'IMAGE')
    mkb_icons.load("icon_select_link", os.path.join(icons_dir, "select_link.png"), 'IMAGE')
    mkb_icons.load("icon_select_pinned", os.path.join(icons_dir, "select_pinned.png"), 'IMAGE')
    mkb_icons.load("icon_select_split", os.path.join(icons_dir, "select_split.png"), 'IMAGE')

    mkb_icons.load("icon_snap_grid_eq", os.path.join(icons_dir, "snap_grid_eq.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid_noneq", os.path.join(icons_dir, "snap_grid_noneq.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid_pack", os.path.join(icons_dir, "snap_grid_pack.png"), 'IMAGE')

    mkb_icons.load("icon_straighten_x", os.path.join(icons_dir, "straighten_x.png"), 'IMAGE')
    mkb_icons.load("icon_straighten_y", os.path.join(icons_dir, "straighten_y.png"), 'IMAGE')

    mkb_icons.load("icon_uv_mirror", os.path.join(icons_dir, "uv_mirror.png"), 'IMAGE')
    mkb_icons.load("icon_uv_reset", os.path.join(icons_dir, "uv_reset.png"), 'IMAGE')
    mkb_icons.load("icon_uv_show_stretch", os.path.join(icons_dir, "uv_show_stretch.png"), 'IMAGE')
    mkb_icons.load("icon_uv_stretch", os.path.join(icons_dir, "uv_stretch.png"), 'IMAGE')
    
    icon_collections['main'] = mkb_icons


    #UV Square Menu
    bpy.types.IMAGE_MT_uvs.append(menu_func_uv_squares)
    bpy.types.IMAGE_MT_uvs.append(menu_func_uv_squares_by_shape)
    bpy.types.IMAGE_MT_uvs.append(menu_func_face_rip)
    bpy.types.IMAGE_MT_uvs.append(menu_func_face_join)


    bpy.utils.register_class(Dropdown_UVTool_Props)
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        

    bpy.types.WindowManager.uv_window = bpy.props.PointerProperty(type = Dropdown_UVTool_Props)


    update_panel_position_uv(None, bpy.context)
    update_panel_position_image(None, bpy.context)

    update_menu(None, bpy.context)





def unregister():
    for icon in icon_collections.values():
        bpy.utils.previews.remove(icon)
    icon_collections.clear()

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    unregister_icons()

    #UV Square Menu
    bpy.types.IMAGE_MT_uvs.remove(menu_func_uv_squares)
    bpy.types.IMAGE_MT_uvs.remove(menu_func_uv_squares_by_shape)
    bpy.types.IMAGE_MT_uvs.remove(menu_func_face_rip)
    bpy.types.IMAGE_MT_uvs.remove(menu_func_face_join)



if __name__ == "__main__":
    register()
