# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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


bl_info = {
    "name": "OriginSet",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 6),
    "blender": (2, 80, 0),
    "location": "3D View > Tool [T] or Property [N] Shelf Panel, Menus [CTRL+D], Special Menu [W], Header",
    "description": "collection of origin modal operators",
    "warning": "/",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "category": "ToolPlus",
}



# LOAD MODULES #
import bpy
import bpy.utils.previews
from bpy.props import *

# LOAD / RELOAD SUBMODULES #
import importlib
from . import developer_utils

# LOAD CUSTOM ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons


# LOAD OPERATORS #   
from .operators.ot_advance     import *
from .operators.ot_align       import *
from .operators.ot_bbox_modal  import *
from .operators.ot_bbox_multi  import *
from .operators.ot_center      import *
from .operators.ot_cursor      import *
from .operators.ot_distribute  import *
from .operators.ot_editor      import *
from .operators.ot_snappoint   import *
from .operators.ot_clickpoint  import *
from .operators.ot_nonmodal    import *
from .operators.ot_zero        import *


# LOAD UI # 
from .ui_panel          import *
from .ui_header         import *
from .ui_menu           import *
from .ui_menu_pie       import *
from .ui_menu_special   import *
from .ui_manual         import *
from .ui_keymap         import *


importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())


# PANEL TO CONTAINING THE TOOLS #
class VIEW3D_PT_originset_panel_ui(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    bl_label = "OriginSet"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        #layout = self.layout.column(align=True)
        layout = self.layout.box().column(align=True)
         
        draw_originset_ui(self, context, layout)



# UPDATE TAB CATEGORY FOR PANEL IN THE TOOLSHELF #
panels = (
        VIEW3D_PT_originset_panel_ui,
        )

def update_panel(self, context):
    message = "Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            panel.bl_category = context.preferences.addons[__name__].preferences.category
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass



# ADDON PREFERENCES PANEL #
class Addon_Preferences_OriginSet(bpy.types.AddonPreferences):
    bl_idname = __name__

    # PANEL #          
    category : StringProperty(
              name="Tab Category",
              description="Choose a name for the category of the panel",
              default="Tools",
              update=update_panel
              )

    #------------------------------

    # INFO LIST #
    prefs_tabs : EnumProperty(
        items=(('info',  "Info",   "Info"),
               ('panel', "Panel",  "Panel"),
               ('menus', "Menus",  "Menus"),
               ('header',"Header", "Header")),
        default='info')

    #------------------------------

    # LAYOUT SCALE #
    ui_scale_y : bpy.props.FloatProperty(name="Scale Y",  description="scale layout space for menus", default=1.2, min=1.0, max=1.5, precision=2)

    # MENU #
    tab_origin_menu : EnumProperty(
        name = '3D View Menu',
        description = 'enable or disable menu for 3D View',
        items=(('menu',   'Use Menu', 'enable menu for 3D View'),
               ('pie',    'Use Pie',  'enable pie for 3D View'),
               ('remove', 'Disable',  'disable menus for 3D View')),
        default='menu', update = update_origin_menu)


    # SPECIAL W SUBMENUS #    
    tab_origin_special : EnumProperty(
        name = 'Append to Special Menu',
        description = 'menu for special menu',
        items=(('prepend', 'Menu Top',    'add menus to default special menus'),
               ('append',  'Menu Bottom', 'add menus to default special menus'),
               ('remove',  'Menu Remove', 'remove menus from default menus')),
        default='remove', update = update_origin_special)               

    toggle_special_origin_icon : bpy.props.BoolProperty(name="Use Icon", description="on / off", default=True)   
    toggle_special_origin_separator : bpy.props.BoolProperty(name="Use Separator", description="on / off", default=True)   


    # HEADER #    
    tab_origin_header : EnumProperty(
        name = 'Append to 3D View Header',
        description = 'menu for header',
        items=(('prepend', 'Add Menu',    'add menus to default header'),
               ('remove',  'Menu Remove', 'remove menus from header')),
        default='remove', update = update_origin_header)   
   
    tab_origin_header_text : bpy.props.BoolProperty(name="Show/Hide Menu Text", description="on / off", default=True)   


    # KEYMAP #      
    use_hotkey : StringProperty(name = 'Key', default="D", description = 'change hotkey / only capital letters allowed') 
    use_ctrl : BoolProperty(name= 'use Ctrl', description = 'enable key for menu', default=True) 
    use_alt : BoolProperty(name= 'use Alt', description = 'enable key for menu', default=False) 
    use_shift : BoolProperty(name= 'use Shift', description = 'enable key for menu', default=False) 
    use_event : EnumProperty(
        items=[('DOUBLE_CLICK',  "DOUBLE CLICK", "key event"),
               ('CLICK',         "CLICK",        "key event"),
               ('RELEASE',       "RELEASE",      "key event"),
               ('PRESS',         "PRESS",        "key event"),
               ('ANY',           "ANY",          "key event"),],
        name="",
        default='PRESS')
        

    #------------------------------

    # DISPLAY TOOLS IN LAYOUTS #
    
    # DEFAULT FOR ALL MODES #
    display_tpc_origin_to_cursor : bpy.props.BoolProperty(name="origin to cursor",  description="toggle button on or off", default=True) 
    display_tpc_origin_to_center : bpy.props.BoolProperty(name="origin to center",  description="toggle button on or off", default=True) 
    display_tpc_object_to_center : bpy.props.BoolProperty(name="object to center",  description="toggle button on or off", default=True) 
    display_tpc_origin_to_object : bpy.props.BoolProperty(name="origin to object",  description="toggle button on or off", default=True) 
    display_tpc_object_to_origin : bpy.props.BoolProperty(name="object to origin",  description="toggle button on or off", default=True)        
    display_tpc_mass_surface : bpy.props.BoolProperty(name="mass surface",  description="toggle button on or off", default=True) 
    display_tpc_mass_volume : bpy.props.BoolProperty(name="mass volume",  description="toggle button on or off", default=True) 

    # TOOLS #        
    display_tpc_origin_to_click_point : bpy.props.BoolProperty(name="Click Point",  description="toggle button on or off", default=True) 
    display_tpc_origin_to_snap_point : bpy.props.BoolProperty(name="Snap Point",  description="toggle button on or off", default=True) 
    display_tpc_3_vert_circle : bpy.props.BoolProperty(name="3Vert Circle",  description="toggle button on or off", default=True) 
    display_tpc_set_origin_to_edit : bpy.props.BoolProperty(name="Selected Edit",  description="toggle button on or off", default=True) 
    display_tpc_set_origin_to_edit_mesh : bpy.props.BoolProperty(name="Selected Edit (Mesh)",  description="toggle button on or off", default=True) 
    display_tpc_snap_to_bbox_modal : bpy.props.BoolProperty(name="BBox Modal",  description="toggle button on or off", default=True) 
    display_tpc_align_to_axis : bpy.props.BoolProperty(name="Advance Align (Edit)",  description="toggle button on or off", default=True) 
    display_tpc_advanced_align_tools : bpy.props.BoolProperty(name="Advance Align (Object)",  description="toggle button on or off", default=True) 

    # OPTIONAL # 
    display_tpc_snap_to_bbox_multi : bpy.props.BoolProperty(name="BBox Multi",  description="toggle button on or off", default=False) 
    display_tpc_zero_to_axis : bpy.props.BoolProperty(name="Zero to Axis",  description="toggle button on or off", default=False) 

    # ICONS #
    use_button_icons : bpy.props.BoolProperty(name="Toggle Icons",  description="toggle icons on or off", default=True) 

    #------------------------------
        
    # DRAW PREFENCES #
    def draw(self, context):
        layout = self.layout

        icons = load_icons()        
       
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)


        # INFO #
        if self.prefs_tabs == 'info':

            box = layout.box().column(align=True)
            box.separator() 
 
            row = box.column(align=False)
            row.label(text="Welcom to T+ Origin!")               
    
            box.separator()

            row = box.column(align=False)
            row.label(text="> This collection of tools allows to place the object's origin")               
            row.label(text="> in object mode and in edit mode as well.")               
            row.label(text="> There are different interface layouts to run the operators.")               
            row.label(text="> From panel, piemenu, header or from a full customizable context menu!")               
            row.label(text="> todo: more info")               

          
            row = box.column(align=False)                          
            row.label(text="(dft) > default operators like in [CTRL+ALT+SHIFT+C]")
            row.label(text="(obm) > only in object mode available")           
            row.label(text="(edm) > only in edit mode available")
            row.label(text="(edit) > in all edit mode except mesh edit mode available")
            row.label(text="(mesh) > only for mesh objects: obm-edm")
           
            box.separator() 
           
            row = box.column(align=False)                  
            row.label(text="(*) > Modal Operator = ...M")   
            row.label(text="(*) > Click on a vertex, edge or face to place the origin.")   
          
        
            row.separator()

            row.label(text="> Have Fun! ;)")               
    
            box.separator()


        # LOCATION #
        if self.prefs_tabs == 'panel':
            
            box = layout.box().column(align=True)
             
            row = box.row(align=True) 
            row.label(text="Panel Location:")
         
            box.separator() 
            row = box.row(align=True)              
            row.prop(self, "category")

            box.separator() 


        # APPEND #
        if self.prefs_tabs == 'menus':

            col = layout.column(align=True)   

            box = col.box().column(align=True)
         
            box.separator()
         
            row = box.row(align=True)  
            row.label(text="Add to Special Menu [W]", icon ="COLLAPSEMENU")         

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_origin_special', expand=True)


            if self.tab_origin_special == 'remove':
                pass
            else:

                box.separator() 

                row = box.row(align=True)  
                row.prop(self, 'toggle_special_origin_icon')
                row.prop(self, 'toggle_special_origin_separator')


            box.separator()
            box.separator()

            #-----------------------------------------------------

            box = col.box().column(align=True)

            box.separator()
            
            row = box.row(align=True)  
            row.label(text="Context Menu:", icon ="COLLAPSEMENU")        

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_origin_menu', expand=True)
         
            if self.tab_origin_menu == 'pie': 
               
                box.separator()   
              
                row = box.column(align=True)                                                  
                row.label(text="> This menu is always a proposal.")
                row.label(text="> Left or right, up or down, there are too many preferences,")
                row.label(text="> to create a pie menu for everyone.")
                row.label(text="> But it would be handy if you work with a bigger screen.")
      
            
            if self.tab_origin_menu == 'menu': 
 
                box.separator()
                box.separator()
             
                row = box.row(align=False)           
                row.label(text = '', icon='COLLAPSEMENU')   
                row.label(text="Tools in Panel & Context Menu")  
                
                box.separator() 
                box.separator()                

                row = box.row(align=True)  
                row.label(text="Layout Scale Y")                   
                row.prop(self, 'ui_scale_y')            

                box.separator()                                   
           
                row = box.row(align=False)        
                row.prop(self, 'use_button_icons')                               
        
                box.separator()           
                box.separator()           
               
                row = box.row(align=False)            
                row.prop(self, 'display_tpc_origin_to_cursor', text="")
                if self.use_button_icons ==True: 
                    button_origin_to_cursor = icons.get("icon_origin_cursor")                
                    row.label(text="", icon_value=button_origin_to_cursor.icon_id)   
                row.label(text="Origin to Cursor")

                box.separator()  
              
                row = box.row(align=False)  
                row.prop(self, 'display_tpc_origin_to_center', text="")  
                if self.use_button_icons ==True: 
                    button_origin_to_center_view = icons.get("icon_origin_to_center_view")               
                    row.label(text="", icon_value=button_origin_to_center_view.icon_id)          
                row.label(text="Origin to Center")

                box.separator()  

                row = box.row(align=False)  
                row.prop(self, 'display_tpc_origin_to_object', text="")     
                if self.use_button_icons ==True: 
                    button_origin_to_object = icons.get("icon_origin_to_object")               
                    row.label(text="", icon_value=button_origin_to_object.icon_id)         
                row.label(text="Origin to Object")

                box.separator() 
         
                row = box.row(align=False)  
                row.prop(self, 'display_tpc_object_to_origin', text="")  
                if self.use_button_icons ==True: 
                    button_object_to_origin = icons.get("icon_object_to_origin")               
                    row.label(text="", icon_value=button_object_to_origin.icon_id)                
                row.label(text="Object to Origin")

                box.separator()       
     
                row = box.row(align=False)  
                row.prop(self, 'display_tpc_mass_surface', text="")  
                if self.use_button_icons ==True: 
                    button_origin_to_surface = icons.get("icon_origin_to_surface")                
                    row.label(text="", icon_value=button_origin_to_surface.icon_id)            
                row.label(text="Mass (Surface)")
           
                box.separator() 
             
                row = box.row(align=False)  
                row.prop(self, 'display_tpc_mass_volume', text="")    
                if self.use_button_icons ==True: 
                    button_origin_to_volume = icons.get("icon_origin_to_volume")                
                    row.label(text="", icon_value=button_origin_to_volume.icon_id)        
                row.label(text="Mass (Volume)")

                box.separator()            
              
                row = box.row(align=False)
                row.prop(self, 'display_tpc_origin_to_click_point', text="")
                if self.use_button_icons ==True: 
                    button_origin_to_click_point = icons.get("icon_origin_to_click_point")                
                    row.label(text="", icon_value=button_origin_to_click_point.icon_id)   
                row.label(text="Click Point")               

                box.separator()       
                             
                row = box.row(align=False)
                row.prop(self, 'display_tpc_origin_to_snap_point', text="")     
                if self.use_button_icons ==True: 
                    button_origin_to_snap_point = icons.get("icon_origin_to_snap_point")                 
                    row.label(text="", icon_value=button_origin_to_snap_point.icon_id)       
                row.label(text="Snap Point")             

                box.separator()       

                row = box.row(align=False)  
                row.prop(self, 'display_tpc_3_vert_circle', text="")            
                if self.use_button_icons ==True: 
                    button_origin_to_cc = icons.get("icon_origin_to_cc")                
                    row.label(text="", icon_value=button_origin_to_cc.icon_id)  
                row.label(text="3Vert Circle")
           
                box.separator()       

                row = box.row(align=False)  
                row.prop(self, 'display_tpc_set_origin_to_edit', text="")            
                if self.use_button_icons ==True: 
                    button_origin_to_selected = icons.get("icon_origin_to_selected")                 
                    row.label(text="", icon_value=button_origin_to_selected.icon_id)  
                row.label(text="Selected Edit")
           
                box.separator()       

                row = box.row(align=False)  
                row.prop(self, 'display_tpc_set_origin_to_edit_mesh', text="")            
                if self.use_button_icons ==True: 
                    button_origin_to_selected = icons.get("icon_origin_to_selected")                 
                    row.label(text="", icon_value=button_origin_to_selected.icon_id)  
                row.label(text="Selected Edit (Mesh)")

                box.separator()  
                                
                row = box.row(align=False)  
                row.prop(self, 'display_tpc_snap_to_bbox_multi', text="")              
                if self.use_button_icons ==True: 
                    button_origin_to_bbox_multi = icons.get("icon_origin_to_bbox_multi")                
                    row.label(text="", icon_value=button_origin_to_bbox_multi.icon_id)  
                row.label(text="BBox Multi")      
               
                box.separator()  
                                
                row = box.row(align=False)  
                row.prop(self, 'display_tpc_snap_to_bbox_modal', text="")              
                if self.use_button_icons ==True: 
                    button_origin_to_bbox_modal = icons.get("icon_origin_to_bbox_modal")                
                    row.label(text="", icon_value=button_origin_to_bbox_modal.icon_id)  
                row.label(text="BBox Modal")          
           
                box.separator()  
                
                row = box.row(align=False)  
                row.prop(self, 'display_tpc_advanced_align_tools', text="")
                if self.use_button_icons ==True: 
                    button_origin_align_object = icons.get("icon_origin_align_object")                 
                    row.label(text="", icon_value=button_origin_align_object.icon_id)  
                row.label(text="Advanced Align (Object)")   

                box.separator()                     

                row = box.row(align=False)  
                row.prop(self, 'display_tpc_align_to_axis', text="")
                if self.use_button_icons ==True: 
                    button_origin_align_mesh = icons.get("icon_origin_align_mesh")                
                    row.label(text="", icon_value=button_origin_align_mesh.icon_id)  
                row.label(text="Advanced Align (Edit)")   

                box.separator()       

                row = box.row(align=False)  
                row.prop(self, 'display_tpc_zero_to_axis', text="")
                if self.use_button_icons ==True: 
                    button_align_to_zero = icons.get("icon_align_to_zero")                  
                    row.label(text="", icon_value=button_align_to_zero.icon_id)  
                row.label(text="Zero to XYZ Axis")   

                box.separator()     





            if self.tab_origin_menu == 'remove':
                box.separator()
            else: 
                box.separator()
                box = layout.box().column(align=True)
                box.separator()

                row = box.row(align=False)  
                row.prop(self, 'use_hotkey')
                row.prop(self, 'use_event')

                row = box.row(align=False)  
                row.prop(self, 'use_ctrl')
                row.prop(self, 'use_alt')
                row.prop(self, 'use_shift')
     
                box.separator()             
                box.separator()              

                # TIP #            
                row = box.row(align=True)             
                row.label(text="! Change Hotkeys !", icon ="INFO")

                row = box.column(align=True) 
                row.label(text="1 > Only capital letters for a new key allowed!", icon ="BLANK1")
                row.label(text="2 > Save preferences for a permanet use!", icon ="BLANK1")
                row.label(text="3 > Restarting blender ensure that the new key was attached!", icon ="BLANK1")
               
                box.separator() 

                row = box.row(align=False)              
                row.operator('wm.url_open', text = 'Type of Key-Events').url = "https://github.com/mkbreuer/Misc-Share-Archiv/blob/master/images/SHORTCUTS_Type%20of%20key%20event.png?raw=true"

                box.separator()  


        # HEADER #
        if self.prefs_tabs == 'header':
                        
            box = layout.box().column(align=True)         
            box.separator()
         
            row = box.row(align=True)  
            row.label(text="3D View Header", icon ="COLLAPSEMENU")         

            box.separator()            
         
            row = box.column(align=True)          
            row.label(text="A origin menu will be added to the header bar.")

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_origin_header', expand=True)

            if self.tab_origin_header == 'prepend':
                box.separator() 

                row = box.row(align=True)                  
                row.prop(self, 'tab_origin_header_text')
           
            box.separator()          
            box.separator()
 


# REGISTER #
classes = (
    VIEW3D_PT_originset_panel_ui,
    VIEW3D_MT_originset_menu_special,
    VIEW3D_MT_originset_menu_header,
    VIEW3D_OT_advanced_align_tools,
    VIEW3D_OT_cycle_through,
    VIEW3D_OT_align_to_axis,
    VIEW3D_OT_snap_to_bbox_multi,
    VIEW3D_OT_move_origin_to_bbox,
    VIEW3D_OT_snap_origin_to_bbox,
    VIEW3D_OT_origin_to_circle_center,
    VIEW3D_OT_origin_cursor_align,
    VIEW3D_OT_distribute_objects,
    VIEW3D_OT_distribute_objects_menu,
    VIEW3D_OT_keymap_texteditor_origin,
    VIEW3D_OT_snap_origin_to_click_point,
    VIEW3D_OT_snap_origin_to_click_point_mode,
    VIEW3D_OT_set_origin_to,
    VIEW3D_OT_set_origin_to_edit,
    VIEW3D_OT_set_origin_to_edit_mesh,
    VIEW3D_OT_origin_to_snap_point,
    VIEW3D_OT_zero_to_global_axis_menu,
    Addon_Preferences_OriginSet,
)



## REGISTER #

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
   
    update_origin_menu(None, bpy.context)
    update_origin_header(None, bpy.context)
    update_origin_special(None, bpy.context)
    update_panel(None, bpy.context)
   
    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_MT_OriginSet_Manual)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
  
    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_MT_OriginSet_Manual) 

if __name__ == "__main__":
    register()



