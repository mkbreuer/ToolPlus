# ##### BEGIN GPL LICENSE BLOCK #####
#
#Copyright (C) 2017  Marvin.K.Breuer (MKB)]
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


bl_info = {
    "name": "T+ Origin",
    "author": "MKB",
    "version": (0, 1, 4),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N]> Menu",
    "description": "Panel and Menu for Origin Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


from toolplus_origin.origin_batch   import (View3D_TP_Origin_Batch)
from toolplus_origin.origin_menu    import (VIEW3D_TP_Origin_Menu)
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons

##################################

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_origin'))

if "bpy" in locals():
    import imp
    imp.reload(origin_action)
    imp.reload(origin_align)
    imp.reload(origin_batch)
    imp.reload(origin_distribute)
    imp.reload(origin_modal)
    imp.reload(origin_operators)
    imp.reload(origin_zero)


else:
    from . import origin_action         
    from . import origin_align         
    from . import origin_batch               
    from . import origin_distribute                 
    from . import origin_modal         
    from . import origin_operators                 
    from . import origin_zero         



import bpy
from bpy import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import* #(StringProperty, BoolProperty, FloatVectorProperty, FloatProperty, EnumProperty, IntProperty)

def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        VIEW3D_TP_Origin_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category

        bpy.utils.register_class(VIEW3D_TP_Origin_Panel_TOOLS)
    
    else:
        bpy.utils.register_class(VIEW3D_TP_Origin_Panel_UI)
  


def update_tools(self, context):

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass
    



addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        VIEW3D_TP_Origin_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Origin_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('wm.call_menu', 'D', 'PRESS', ctrl=True) #,alt=True, shift=True, 
        kmi.properties.name = "tp_menu.origin_base"


    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass



#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_position)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)

    tab_display_tools = EnumProperty(
        name = 'Display Tools', 
        description = 'on / off',
        items=(('on', 'Batch on', 'enable tools in panel'), 
               ('off', 'Batch off', 'disable tools in panel')), 
               default='off', update = update_tools)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)

    tools_category_menu = bpy.props.BoolProperty(name = "Origin Menu", description = "enable or disable menu", default=True, update = update_menu)


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Origin Collection!")  
            row.label(text="The addon set allows you to:") 
            row.label(text="1. set your origin")   
            row.label(text="2. zero to a choosen axis > object or origin or cursor")   
            row.label(text="3. align your object or origin or cursor")     
            row.label(text="Have Fun! :)")         


        #Tools
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)

            row = box.row()
            row.prop(self, 'tab_display_tools', expand=True)

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 
            

        #Location
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location Origin:")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            row = layout.row()
            row.label(text="! please reboot blender after changing the panel location !", icon ="INFO")

            box.separator() 


        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Origin Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: CTRL+D ")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
             
            row.operator('wm.url_open', text = '! tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"

            box.separator() 
            
            row = layout.row(1) 
            row.label(text="! for key change go to > User Preferences > TAB: Input !", icon ="INFO")


        #Weblinks
        if self.prefs_tabs == 'url':
            row = layout.row()
            row.operator('wm.url_open', text = 'Distribute', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Oscurart_Tools"
            row.operator('wm.url_open', text = 'Modal Origin', icon = 'HELP').url = "http://blenderlounge.fr/forum/viewtopic.php?f=18&t=1438"
            row.operator('wm.url_open', text = 'Advance Align', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?256114-Add-on-Advanced-align-tools"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?410351-Addon-T-Origin&p=3119318#post3119318"



class DropdownOriginToolProps(bpy.types.PropertyGroup):

    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)




def draw_origin_panel_layout(self, context, layout):
    
        lt = context.window_manager.bbox_origin_window     
          
        icons = load_icons()

        if context.mode == 'OBJECT':

            box = layout.box().column(1)                         
            
            row = box.column(1)
            
            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("object.transform_apply", text="Center", icon_value=button_origin_center_view.icon_id).location=True

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_set_cursor", text="Cursor", icon_value=button_origin_cursor.icon_id)

            row.separator()
            
            button_origin_tomesh = icons.get("icon_origin_tomesh")
            row.operator("tp_ops.origin_tomesh", text="Origin to Mesh", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            row.operator("tp_ops.origin_meshto", text="Mesh to Origin", icon_value=button_origin_meshto.icon_id)

            row.separator()
            
            button_origin_mass = icons.get("icon_origin_mass")           
            row.operator("tp_ops.origin_set_mass", text="Center of Mass", icon_value=button_origin_mass.icon_id)

            Display_Dynamics = context.user_preferences.addons[__name__].preferences.tab_display_tools
            if Display_Dynamics == 'on':       
                box = layout.box().column(1)                         
            
                row = box.column(1)
                row.operator("tp_batch.origin_batch", text="Origin Batch", icon="SETTINGS")   

                box.separator() 


            

            box = layout.box().column(1)
            row = box.row(1)
            
            if lt.display_origin_bbox:                     
                
                button_origin_bbox = icons.get("icon_origin_bbox")            
                row.prop(lt, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)                     
               
                row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
          
            else:
               
                button_origin_bbox = icons.get("icon_origin_bbox")                
                row.prop(lt, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)
                
                row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
                            
            if bpy.context.object.type == 'MESH':
                if lt.display_origin_bbox: 
                 
                     box = layout.box().row(1)

                     row = box.column(1) 
                     row.label("+Y") 
                     row.label("Axis") 
                     row.label("Back") 
                     
                     #Top
                     row = box.column(1)
                     
                     button_origin_left_top = icons.get("icon_origin_left_top")                  
                     row.operator("tp_ops.cubeback_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)#"Back- Left -Top")

                     button_origin_left = icons.get("icon_origin_left")
                     row.operator("tp_ops.cubefront_edgemiddle_minus_x", "", icon_value=button_origin_left.icon_id)#"Back- Left")

                     button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                     row.operator("tp_ops.cubeback_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)# "Back- Left -Bottom")
                      
                     #Middle
                     row = box.column(1)

                     button_origin_top = icons.get("icon_origin_top")                     
                     row.operator("tp_ops.cubeback_edgetop_minus_y", "", icon_value=button_origin_top.icon_id)#"Back - Top")                            

                     button_origin_cross = icons.get("icon_origin_cross")
                     row.operator("tp_ops.cubefront_side_plus_y","", icon_value=button_origin_cross.icon_id)# "Back")                 

                     button_origin_bottom = icons.get("icon_origin_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_plus_y","", icon_value=button_origin_bottom.icon_id)#"Back - Bottom") 
                      
                     #Bottom
                     row = box.column(1) 

                     button_origin_right_top = icons.get("icon_origin_right_top")
                     row.operator("tp_ops.cubeback_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)# "Back- Right -Top ")                 

                     button_origin_right = icons.get("icon_origin_right")
                     row.operator("tp_ops.cubefront_edgemiddle_plus_x","", icon_value=button_origin_right.icon_id)#"Back- Right")      

                     button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                     row.operator("tp_ops.cubeback_cornerbottom_plus_xy","", icon_value=button_origin_right_bottom.icon_id)# "Back- Right -Bottom")  

                
                     box.separator()
                     box.separator()
                     box.separator()
                     
                     row.separator()
                     
                     ############################

                     box = layout.box().row(1)

                     row = box.column(1) 
                     row.label("XZ") 
                     row.label("Axis") 
                     row.label("Center") 
                     
                     #Top
                     row = box.column(1)
                     
                     button_origin_left_top = icons.get("icon_origin_left_top")   
                     row.operator("tp_ops.cubefront_edgetop_minus_x","", icon_value=button_origin_left_top.icon_id)#"Middle - Left Top")
                     
                     button_origin_left = icons.get("icon_origin_left")
                     row.operator("tp_ops.cubefront_side_minus_x","", icon_value=button_origin_left.icon_id)# "Left")         
                     
                     button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_minus_x","", icon_value=button_origin_left_bottom.icon_id)#"Middle - Left Bottom")
                      
                     #Middle
                     row = box.column(1) 
                     
                     button_origin_top = icons.get("icon_origin_top")
                     row.operator("tp_ops.cubefront_side_plus_z", "", icon_value=button_origin_top.icon_id)#"Top")  
                     
                     button_origin_diagonal = icons.get("icon_origin_diagonal")
                     row.operator("object.origin_set", text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'                    
                     
                     button_origin_bottom = icons.get("icon_origin_bottom")
                     row.operator("tp_ops.cubefront_side_minus_z","", icon_value=button_origin_bottom.icon_id)# "Bottom")    

                     #Bottom
                     row = box.column(1) 
                     
                     button_origin_right_top = icons.get("icon_origin_right_top")
                     row.operator("tp_ops.cubefront_edgetop_plus_x","", icon_value=button_origin_right_top.icon_id)#"Middle - Right Top")  
                     
                     button_origin_right = icons.get("icon_origin_right")
                     row.operator("tp_ops.cubefront_side_plus_x","", icon_value=button_origin_right.icon_id)# "Right")            
                     
                     button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_plus_x","", icon_value=button_origin_right_bottom.icon_id)#"Middle - Right Bottom")  

                     box.separator()
                     box.separator()
                     box.separator()
                     
                     row.separator()

                     ############################
                     
                     box = layout.box().row(1)

                     row = box.column(1) 
                     row.label("-- Y") 
                     row.label("Axis") 
                     row.label("Front") 
                    
                     #Top
                     row = box.column(1) 
                     
                     button_origin_left_top = icons.get("icon_origin_left_top") 
                     row.operator("tp_ops.cubefront_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)# "Front- Left -Top"
                     
                     button_origin_left = icons.get("icon_origin_left")
                     row.operator("tp_ops.cubefront_edgemiddle_minus_y","", icon_value=button_origin_left.icon_id)# "Front- Left"  
                     
                     button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                     row.operator("tp_ops.cubefront_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)# "Front- Left -Bottom"  
                               
                     #Middle
                     row = box.column(1) 
                     
                     button_origin_top = icons.get("icon_origin_top")
                     row.operator("tp_ops.cubeback_edgetop_plus_y","", icon_value=button_origin_top.icon_id)# "Front - Top"                                      
                     
                     #button_origin_center = icons.get("icon_origin_center")
                     
                     button_origin_cross = icons.get("icon_origin_cross")
                     row.operator("tp_ops.cubefront_side_minus_y","", icon_value=button_origin_cross.icon_id)#  "Front"           
                     
                     button_origin_bottom = icons.get("icon_origin_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_minus_y","", icon_value=button_origin_bottom.icon_id)# "Front - Bottom"           

                     #Bottom
                     row = box.column(1) 
                     
                     button_origin_right_top = icons.get("icon_origin_right_top")
                     row.operator("tp_ops.cubefront_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)#  "Front- Right -Top"
                     
                     button_origin_right = icons.get("icon_origin_right")
                     row.operator("tp_ops.cubefront_edgemiddle_plus_y","", icon_value=button_origin_right.icon_id)# "Front- Right"    
                     
                     button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                     row.operator("tp_ops.cubefront_cornerbottom_plus_xy", "", icon_value=button_origin_right_bottom.icon_id)# "Front- Right -Bottom") 

                     box.separator()
                     box.separator()
                     box.separator()
                     
                     row.separator()


            box = layout.box().column(1) 
             
            row = box.row(1)
            
            if lt.display_origin_zero:                     
                button_align_zero = icons.get("icon_align_zero")          
                row.prop(lt, "display_origin_zero", text="", icon_value=button_align_zero.icon_id)                             
               
                row.operator("tp_ops.zero_axis_panel", "   Execute Zero")  
           
            else:
                button_align_zero = icons.get("icon_align_zero")              
                row.prop(lt, "display_origin_zero", text="", icon_value=button_align_zero.icon_id)               
               
                row.operator("tp_ops.zero_axis", "   ZeroAxis")  
                    
            if lt.display_origin_zero: 

                box.separator()   
                
                row = box.row(1)
                row.prop(context.scene, 'tp_switch', expand=True)

                row = box.row()
                row.prop(context.scene, 'tp_switch_axis', expand=True)
                
            box.separator()    

            box = layout.box().column(1) 
            
            row = box.column(1)

            button_origin_distribute = icons.get("icon_origin_distribute")  
            row.operator("object.distribute_osc", "Distribute", icon_value=button_origin_distribute.icon_id)

            button_origin_align = icons.get("icon_origin_align")                
            row.operator("tp_origin.align_tools", "Advanced", icon_value=button_origin_align.icon_id)    
  

            box.separator()                                     

        else:

            box = layout.box().column(1) 
            
            row = box.column(1) 

            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_cursor_edm", text="Cursor", icon_value=button_origin_cursor.icon_id)            

            row.separator()

            button_origin_edm = icons.get("icon_origin_edm")            
            row.operator("tp_ops.origin_edm","Edm-Select", icon_value=button_origin_edm.icon_id)       

            button_origin_obj = icons.get("icon_origin_obj")   
            row.operator("tp_ops.origin_obm","Obm-Select", icon_value=button_origin_obj.icon_id)             
     
            box.separator() 
            
            if context.mode == 'EDIT_MESH':

                box = layout.box().column(1)
                row = box.row(1)
                
                if lt.display_origin_editbox:                     
                    button_origin_bbox = icons.get("icon_origin_bbox")            
                    row.prop(lt, "display_origin_editbox", text="BBoxOrigin", icon_value=button_origin_bbox.icon_id)                     
                else:
                    button_origin_bbox = icons.get("icon_origin_bbox")                
                    row.prop(lt, "display_origin_editbox", text="BBoxOrigin", icon_value=button_origin_bbox.icon_id)
                    
                if lt.display_origin_editbox:        

                     box = layout.box().row(1)

                     row = box.column(1) 
                     row.label("+Y") 
                     row.label("Axis") 
                     row.label("Back") 
                     
                     #Top
                     row = box.column(1)
                     
                     button_origin_left_top = icons.get("icon_origin_left_top")                  
                     row.operator("tp_ops.cubeback_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)#"Back- Left -Top")

                     button_origin_left = icons.get("icon_origin_left")
                     row.operator("tp_ops.cubefront_edgemiddle_minus_x", "", icon_value=button_origin_left.icon_id)#"Back- Left")

                     button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                     row.operator("tp_ops.cubeback_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)# "Back- Left -Bottom")
                      
                     #Middle
                     row = box.column(1)

                     button_origin_top = icons.get("icon_origin_top")                     
                     row.operator("tp_ops.cubeback_edgetop_minus_y", "", icon_value=button_origin_top.icon_id)#"Back - Top")                            

                     button_origin_cross = icons.get("icon_origin_cross")
                     row.operator("tp_ops.cubefront_side_plus_y","", icon_value=button_origin_cross.icon_id)# "Back")                 

                     button_origin_bottom = icons.get("icon_origin_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_plus_y","", icon_value=button_origin_bottom.icon_id)#"Back - Bottom") 
                      
                     #Bottom
                     row = box.column(1) 

                     button_origin_right_top = icons.get("icon_origin_right_top")
                     row.operator("tp_ops.cubeback_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)# "Back- Right -Top ")                 

                     button_origin_right = icons.get("icon_origin_right")
                     row.operator("tp_ops.cubefront_edgemiddle_plus_x","", icon_value=button_origin_right.icon_id)#"Back- Right")      

                     button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                     row.operator("tp_ops.cubeback_cornerbottom_plus_xy","", icon_value=button_origin_right_bottom.icon_id)# "Back- Right -Bottom")  

                
                     box.separator()
                     box.separator()
                     box.separator()
                     
                     row.separator()
                     
                     ############################

                     box = layout.box().row(1)

                     row = box.column(1) 
                     row.label("XZ") 
                     row.label("Axis") 
                     row.label("Center") 
                     
                     #Top
                     row = box.column(1)
                     
                     button_origin_left_top = icons.get("icon_origin_left_top")   
                     row.operator("tp_ops.cubefront_edgetop_minus_x","", icon_value=button_origin_left_top.icon_id)#"Middle - Left Top")
                     
                     button_origin_left = icons.get("icon_origin_left")
                     row.operator("tp_ops.cubefront_side_minus_x","", icon_value=button_origin_left.icon_id)# "Left")         
                     
                     button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_minus_x","", icon_value=button_origin_left_bottom.icon_id)#"Middle - Left Bottom")
                      
                     #Middle
                     row = box.column(1) 
                     
                     button_origin_top = icons.get("icon_origin_top")
                     row.operator("tp_ops.cubefront_side_plus_z", "", icon_value=button_origin_top.icon_id)#"Top")  
                        
                     button_origin_diagonal = icons.get("icon_origin_diagonal")
                     row.operator("tp_ops.origin_set_editcenter", text="", icon_value=button_origin_diagonal.icon_id) 
                                     
                     button_origin_bottom = icons.get("icon_origin_bottom")
                     row.operator("tp_ops.cubefront_side_minus_z","", icon_value=button_origin_bottom.icon_id)# "Bottom")    

                     #Bottom
                     row = box.column(1) 
                     
                     button_origin_right_top = icons.get("icon_origin_right_top")
                     row.operator("tp_ops.cubefront_edgetop_plus_x","", icon_value=button_origin_right_top.icon_id)#"Middle - Right Top")  
                     
                     button_origin_right = icons.get("icon_origin_right")
                     row.operator("tp_ops.cubefront_side_plus_x","", icon_value=button_origin_right.icon_id)# "Right")            
                     
                     button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_plus_x","", icon_value=button_origin_right_bottom.icon_id)#"Middle - Right Bottom")  

                     box.separator()
                     box.separator()
                     box.separator()
                     
                     row.separator()

                     ############################
                     
                     box = layout.box().row(1)

                     row = box.column(1) 
                     row.label("-- Y") 
                     row.label("Axis") 
                     row.label("Front") 
                    
                     #Top
                     row = box.column(1) 
                     
                     button_origin_left_top = icons.get("icon_origin_left_top") 
                     row.operator("tp_ops.cubefront_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)# "Front- Left -Top"
                     
                     button_origin_left = icons.get("icon_origin_left")
                     row.operator("tp_ops.cubefront_edgemiddle_minus_y","", icon_value=button_origin_left.icon_id)# "Front- Left"  
                     
                     button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                     row.operator("tp_ops.cubefront_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)# "Front- Left -Bottom"  
                               
                     #Middle
                     row = box.column(1) 
                     
                     button_origin_top = icons.get("icon_origin_top")
                     row.operator("tp_ops.cubeback_edgetop_plus_y","", icon_value=button_origin_top.icon_id)# "Front - Top"                                      
                     
                     #button_origin_center = icons.get("icon_origin_center")
                     
                     button_origin_cross = icons.get("icon_origin_cross")
                     row.operator("tp_ops.cubefront_side_minus_y","", icon_value=button_origin_cross.icon_id)#  "Front"           
                     
                     button_origin_bottom = icons.get("icon_origin_bottom")
                     row.operator("tp_ops.cubefront_edgebottom_minus_y","", icon_value=button_origin_bottom.icon_id)# "Front - Bottom"           

                     #Bottom
                     row = box.column(1) 
                     
                     button_origin_right_top = icons.get("icon_origin_right_top")
                     row.operator("tp_ops.cubefront_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)#  "Front- Right -Top"
                     
                     button_origin_right = icons.get("icon_origin_right")
                     row.operator("tp_ops.cubefront_edgemiddle_plus_y","", icon_value=button_origin_right.icon_id)# "Front- Right"    
                     
                     button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                     row.operator("tp_ops.cubefront_cornerbottom_plus_xy", "", icon_value=button_origin_right_bottom.icon_id)# "Front- Right -Bottom") 

                     box.separator()
                     box.separator()
                     box.separator()
                     
                     row.separator()


            box = layout.box().column(1)
            row = box.row(1)         

            if lt.display_origin_zero_edm:                     
                button_align_zero = icons.get("icon_align_zero")          
                row.prop(lt, "display_origin_zero_edm", text="", icon_value=button_align_zero.icon_id)                             
               
                row.operator("tp_ops.zero_axis_panel", "   Execute Zero")  
           
            else:
                button_align_zero = icons.get("icon_align_zero")              
                row.prop(lt, "display_origin_zero_edm", text="", icon_value=button_align_zero.icon_id)               
               
                row.operator("tp_ops.zero_axis_panel", "   ZeroAxis")  
                    
            if lt.display_origin_zero_edm: 

                box.separator()   

                row = box.row(1)
                row.prop(context.scene, 'tp_switch', expand=True)

                row = box.row()
                row.prop(context.scene, 'tp_switch_axis', expand=True)       

            box.separator()



class VIEW3D_TP_Origin_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Origin"
    bl_idname = "VIEW3D_TP_Origin_Panel_TOOLS"
    bl_label = "Origin"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_origin_panel_layout(self, context, layout) 



class VIEW3D_TP_Origin_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Origin_Panel_UI"
    bl_label = "Origin"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'  

        draw_origin_panel_layout(self, context, layout) 




# register

import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.bbox_origin_window = bpy.props.PointerProperty(type = DropdownOriginToolProps)
    
    update_tools(None, bpy.context)
    update_menu(None, bpy.context)
    update_panel_position(None, bpy.context)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    del bpy.types.WindowManager.bbox_origin_window
 
if __name__ == "__main__":
    register()
        
        




              
