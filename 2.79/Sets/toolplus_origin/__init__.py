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
    "name": "T+ Origin",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 1),
    "blender": (2, 79, 0),
    "location": "3D View > Tool [T] or Property [N] Shelf Panel, Menus [CTRL+D], Special Menu [W], Header",
    "description": "collection of origin modal operators",
    "warning": "/",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "category": "ToolPlus",
}



# LOAD CUSTOM ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons


# LOAD MODULES #
import bpy
import bpy.utils.previews
import traceback
from bpy.props import *

# LOAD / RELOAD SUBMODULES #
import importlib
from . import developer_utils

# LOAD OPERATORS #   
from .ot_advance       import *
from .ot_align         import *
from .ot_bbox          import *
from .ot_bboxM         import *
from .ot_center        import *
from .ot_cursor        import *
from .ot_distribute    import *
from .ot_editor        import *
from .ot_helper        import *
from .ot_modal         import *
from .ot_nonmodal      import *
from .ot_zero          import *

# LOAD OPERATORS #           
from .ui_manual        import *            
from .ui_panel         import *            
from .ui_menu          import *         
from .ui_header        import *     
from .ui_menu_pie      import *     
from .ui_menu_special  import * 
from .ui_keymap        import*


importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())



# PANEL TO CONTAINING THE TOOLS #
class VIEW3D_PT_Origin_Panel_TOOLS(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'T+'
    bl_label = "Set Origin"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_origin_ui(self, context, layout)


class VIEW3D_PT_Origin_Panel_UI(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Set Origin"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_origin_ui(self, context, layout)



# UPDATE TAB CATEGORY FOR PANEL IN THE TOOLSHELF #
panels = (VIEW3D_PT_Origin_Panel_UI, VIEW3D_PT_Origin_Panel_TOOLS)

def update_panel(self, context):
    message = "Template: Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_origin_location == 'tools':
         
            VIEW3D_PT_Origin_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.category
            bpy.utils.register_class(VIEW3D_PT_Origin_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_origin_location == 'ui':
            
            bpy.utils.register_class(VIEW3D_PT_Origin_Panel_UI)

        if context.user_preferences.addons[__name__].preferences.tab_origin_location == 'off':  
            return None

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass




# ADDON PREFERENCES PANEL #
class Addon_Preferences_Origin(bpy.types.AddonPreferences):
    bl_idname = __name__

    # INFO LIST #
    prefs_tabs=EnumProperty(
        items=(('info',  "Info",   "Info"),
               ('panel', "Panel",  "Panel"),
               ('menus', "KeyMap", "KeyMap"),
               ('header',"Header", "Header")),
        default='info')

    #------------------------------

    # PANEL #          
    tab_origin_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf',      'place panel in the tool shelf [T]'),
               ('ui',    'Property Shelf',  'place panel in the property shelf [N]'),
               ('off',   'Remove Panel',    'remove the panel')),
               default='tools', update = update_panel)

    category=StringProperty(
              name="Tab Category",
              description="Choose a name for the category of the panel",
              default="Tools",
              update=update_panel
              )

    #------------------------------

    # LAYOUT SCALE #
    scale_y = bpy.props.FloatProperty(name="Scale Y",  description="scale layout space for menus", default=1.2, min=1, max=1.5)

    # MENU #
    tab_origin_menu=EnumProperty(
        name = '3D View Menu',
        description = 'enable or disable menu for 3D View',
        items=(('menu',   'Use Menu', 'enable menu for 3D View'),
               ('pie',    'Use Pie',  'enable pie for 3D View'),
               ('remove', 'Disable',  'disable menus for 3D View')),
        default='menu', update = update_origin_menu)


    # SUBMENUS #    
    tab_origin_special=EnumProperty(
        name = 'Append to Special Menu',
        description = 'menu for special menu',
        items=(('prepend', 'Menu Top',    'add menus to default special menus'),
               ('append',  'Menu Bottom', 'add menus to default special menus'),
               ('remove',  'Menu Remove', 'remove menus from default menus')),
        default='remove', update = update_origin_special)               

    # HEADER #    
    tab_origin_header=EnumProperty(
        name = 'Append to 3D View Header',
        description = 'menu for header',
        items=(('prepend', 'Add Menu',    'add menus to default header'),
               ('remove',  'Menu Remove', 'remove menus from header')),
        default='remove', update = update_origin_header)   
   
    tab_origin_header_text = bpy.props.BoolProperty(name="Show/Hide Menu Text", description="on / off", default=True)   
        
    #------------------------------

    # TOOLS #
    tab_display_tools = bpy.props.BoolProperty(name="Advanced", description="on / off", default=False)   

    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="align origin to the boundtyp: box (4x vertice / 12x edge / 6x face)", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="align origin to the boundtyp: box (4x vertice / 12x edge / 6x face)", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="align origin, object or cursor to an axis", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="align only origin, object or cursor to an axis", default=False)
    display_origin_active = bpy.props.BoolProperty(name="Align to Active", description="align origin to active object", default=False)

    loc_x = BoolProperty (name = "Align to X axis", default= False, description= "Enable X axis alignment")
    loc_y = BoolProperty (name = "Align to Y axis", default= False, description= "Enable Y axis alignment")                               
    loc_z = BoolProperty (name = "Align to Z axis", default= False, description= "Enable Z axis alignment")

    loc_offset = FloatVectorProperty(name="Location Offset", description="Offset for location align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)       

    #------------------------------
   
    # ZERO AXIS #
    tp_switch = bpy.props.EnumProperty(
        items=[("tp_obj"    ,"Object"    ,"01"),
               ("tp_org"    ,"Origin"    ,"02"),
               ("tp_crs"    ,"Cursor"    ,"03")],
               name = "ZeroFor",
               default = "tp_org",    
               description = "zero object or cursor")

    align_x = BoolProperty (name = "X", default= False, description= "enable X axis alignment")
    align_y = BoolProperty (name = "Y", default= False, description= "enable Y axis alignment")                               
    align_z = BoolProperty (name = "Z", default= False, description= "enable Z axis alignment")

    tp_origin_offset = FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)
    tp_align_offset = FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)

    #------------------------------

    # DISPLAY TOOLS IN LAYOUTS #
    
    # ALL MODES #
    display_origin_to_cursor = bpy.props.BoolProperty(name="origin to cursor",  description="toggle button on or off", default=True) 
    display_origin_to_center = bpy.props.BoolProperty(name="origin to center",  description="toggle button on or off", default=True) 
    display_object_to_center = bpy.props.BoolProperty(name="object to center",  description="toggle button on or off", default=True) 
    display_origin_to_object = bpy.props.BoolProperty(name="origin to object",  description="toggle button on or off", default=True) 
    display_object_to_origin = bpy.props.BoolProperty(name="object to origin",  description="toggle button on or off", default=True)        
    display_mass_surface = bpy.props.BoolProperty(name="mass surface",  description="toggle button on or off", default=True) 
    display_mass_volume = bpy.props.BoolProperty(name="mass volume",  description="toggle button on or off", default=True) 
    display_zero_to_axis = bpy.props.BoolProperty(name="zero to axis",  description="toggle button on or off", default=True) 

    # MODE OBJECT #        
    display_origin_to_snap = bpy.props.BoolProperty(name="origin_to_snap",  description="toggle button on or off", default=True) 
    display_origin_to_select = bpy.props.BoolProperty(name="origin to select",  description="toggle button on or off", default=True) 
    display_origin_to_active = bpy.props.BoolProperty(name="origin to active",  description="toggle button on or off", default=True) 
    display_boundbox_m = bpy.props.BoolProperty(name="boundbox m",  description="toggle button on or off", default=True) 
    display_boundbox_x = bpy.props.BoolProperty(name="boundbox x",  description="toggle button on or off", default=True)         
    display_distribute = bpy.props.BoolProperty(name="distribute",  description="toggle button on or off", default=True) 
    display_advance_obm = bpy.props.BoolProperty(name="advance align tools",  description="toggle button on or off", default=True) 

    # MODE EDIT #
    display_linked_mesh = bpy.props.BoolProperty(name="linked mesh",  description="toggle button on or off", default=True) 
    display_selected_mesh = bpy.props.BoolProperty(name="selected mesh",  description="toggle button on or off", default=True) 
    display_mselect_edm = bpy.props.BoolProperty(name="mselect edm",  description="toggle button on or off", default=True) 
    display_mselect_obm = bpy.props.BoolProperty(name="mselect obm",  description="toggle button on or off", default=True) 
    display_select_edm = bpy.props.BoolProperty(name="select edm",  description="toggle button on or off", default=True) 
    display_select_obm = bpy.props.BoolProperty(name="select obm",  description="toggle button on or off", default=True) 
    display_3_point_circle = bpy.props.BoolProperty(name="3point circle",  description="toggle button on or off", default=True) 
    display_advance_edm = bpy.props.BoolProperty(name="advance align to axis",  description="toggle button on or off", default=True) 

    # LAYOUT SEPARATOR #
    display_layout_separator_a = bpy.props.BoolProperty(name="Separator 01",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_b = bpy.props.BoolProperty(name="Separator 02",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_c = bpy.props.BoolProperty(name="Separator 03",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_d = bpy.props.BoolProperty(name="Separator 04",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_e = bpy.props.BoolProperty(name="Separator 05",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_f = bpy.props.BoolProperty(name="Separator 06",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_g = bpy.props.BoolProperty(name="Separator 07",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_h = bpy.props.BoolProperty(name="Separator 08",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_i = bpy.props.BoolProperty(name="Separator 09",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_j = bpy.props.BoolProperty(name="Separator 10",  description="toggle layout separator on or off", default=True) 
    display_layout_separator_k = bpy.props.BoolProperty(name="Separator 11",  description="toggle layout separator on or off", default=True) 

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
            row.label(text="Set Origin Collection")               
          
            row.separator() 

            row.label(text="> (*) Modal Operator = click on a vertex, edge or face to place the origin.")   
            row.label(text="> Checkbox = toggle tools in the cascade menu on or off.")    
 
            box.separator() 
            
            box.separator() 
            box = layout.box().column(align=True)
            box.separator() 
           
            row = box.column(align=False)           
            row.label(text="Default Operators from [CTRL+ALT+SHIFT+C]")            
          
            box.separator()           
           
            row = box.row(align=False)            
            row.prop(self, 'display_origin_to_cursor', text="")
            row.label(text="> Origin to Cursor = set origin to cursor.")
  
            row = box.row(align=False)  
            row.prop(self, 'display_origin_to_center', text="")              
            row.label(text="> Origin to Center = set origin to 3D view center.")

            row = box.row(align=False)  
            row.prop(self, 'display_origin_to_object', text="")            
            row.label(text="> Origin to Object = set origin to geometry.")
         
            row = box.row(align=False)  
            row.prop(self, 'display_object_to_origin', text="")               
            row.label(text="> Object to Origin = set geometry to origin. ")

            row = box.row(align=False)  
            row.prop(self, 'display_mass_surface', text="")            
            row.label(text="> Mass (Surface) = set origin to center of surface mass.")

            row = box.row(align=False)  
            row.prop(self, 'display_mass_volume', text="")            
            row.label(text="> Mass (Volume) = set origin to center of volume mass.")
           

            box.separator() 
            box = layout.box().column(align=True)
            box.separator() 
         
            row = box.column(align=False)
            row.label(text="Available for Object and Edit Mode:")

            box.separator() 

            row = box.row(align=False)
            row.prop(self, 'display_origin_to_select', text="")            
            row.label(text="> Origin to Select: snap origin to mesh geometry (*)")
           
            row = box.row(align=False)
            row.prop(self, 'display_object_to_center', text="")
            row.label(text="> Object to Center: set origin to mesh and relocate object to 3D view center. (*)")   

            row = box.row(align=False)  
            row.prop(self, 'display_origin_to_active', text="")                        
            row.label(text="> Origin to Active: align origin for all selected to a active object.")

            row = box.row(align=False)  
            row.prop(self, 'display_boundbox_x', text="")              
            row.label(text="> BoundBoxX = set origin to a point on the bounding box for all selected.")          

            row = box.row(align=False)  
            row.prop(self, 'display_zero_to_axis', text="")            
            row.label(text="> Zero to Axis = align object, origin or cursor to one of the 3d view axis.")

          
            box.separator() 
            box = layout.box().column(align=True)
            box.separator() 
           
            row = box.column(align=False)
            row.label(text="Only in Object Mode: ")

            box.separator() 

            row = box.row(align=False)
            row.prop(self, 'display_origin_to_snap', text="")
            row.label(text="> Object to Snap: snap origin with a emtpty to snap point [CTRL]. (*)")  

            row = box.row(align=False)  
            row.prop(self, 'display_boundbox_m', text="")            
            row.label(text="> BoundBoxM = set origin to a point on a wrapped bounding box. (*)")

            row = box.row(align=False)  
            row.prop(self, 'display_distribute', text="")            
            row.label(text="> Distribute: even spacing between selected objects origin with xyz axis and offset.")   

            row = box.row(align=False)  
            row.prop(self, 'display_advance_obm', text="")
            row.label(text="> Advanced: align object, origin or cursor to active with max, mid or min values and offset.")   

            box.separator() 
            box = layout.box().column(align=True)           
            box.separator() 

            row = box.column(align=False)
            row.label(text="Only in Edit Mode: Mesh")

            box.separator() 

            row = box.row(align=False)  
            row.prop(self, 'display_linked_mesh', text="")            
            row.label(text="> Linked Mesh = select linked mesh and set origin to selected.")

            row = box.row(align=False)  
            row.prop(self, 'display_selected_mesh', text="")
            row.label(text="> Selected Mesh = set origin to selected geometry, vertices, edges or faces.")            

            row = box.row(align=False)  
            row.prop(self, 'display_mselect_edm', text="")            
            row.label(text="> M-Select-EdM = set origin to active or selected mesh and stay in editmode. (*)")                   

            row = box.row(align=False)  
            row.prop(self, 'display_mselect_obm', text="")            
            row.label(text="> M-Select-ObM = set origin to active or selected mesh and stay in editmode. (*)")                   

            row = box.row(align=False)  
            row.prop(self, 'display_3_point_circle', text="")            
            row.label(text="> 3P-Circle = set origin to a circle center of 3 selected vertices")

            row = box.row(align=False)  
            row.prop(self, 'display_advance_edm', text="")
            row.label(text="> Advanced: align vertices, edges or faces to axis or normal direction, etc.")   
                    
            box.separator() 
            box = layout.box().column(align=True)           
            box.separator() 
            
            row = box.column(align=False)
            row.label(text="Only in Edit Mode:")

            box.separator() 

            row = box.row(align=False) 
            row.prop(self, 'display_select_edm', text="")
            row.label(text="> Edm-Select = set origin to active or selected mesh and stay in editmode.")

            row = box.row(align=False) 
            row.prop(self, 'display_select_obm', text="")
            row.label(text="> Obm-Select = set origin to active or selected mesh and toggle to objectmode.")

            row = box.row(align=False) 
            row.prop(self, 'display_advance_edm', text="")            
            row.label(text="> Advanced: align vertices, edges or faces to axis or normal direction, etc.")   
                    
            box.separator() 
            box = layout.box().column(align=True)           
            box.separator() 
        
            row = box.column(align=False) 
            row.label(text="Checkbox = toggle menu layout separator on or off.")   
          
            box.separator() 
            
            row = box.column_flow(2) 
            row.prop(self, 'display_layout_separator_a', text="Separator 01")
            row.prop(self, 'display_layout_separator_b', text="Separator 02")
            row.prop(self, 'display_layout_separator_c', text="Separator 03")
            row.prop(self, 'display_layout_separator_d', text="Separator 04")
            row.prop(self, 'display_layout_separator_e', text="Separator 05")
            row.prop(self, 'display_layout_separator_f', text="Separator 06")
            row.prop(self, 'display_layout_separator_g', text="Separator 07")
            row.prop(self, 'display_layout_separator_h', text="Separator 08")
            row.prop(self, 'display_layout_separator_i', text="Separator 09")
            row.prop(self, 'display_layout_separator_j', text="Separator 10")
            row.prop(self, 'display_layout_separator_k', text="Separator 11")
                    
            box.separator()       
            box = layout.box().column(align=True)         
            box.separator()
         
            row = box.row(align=True)  
            row.label(text="Menu Layout Scale Y", icon ="COLLAPSEMENU")         
            
            box.separator()   
           
            row = box.column(align=True)               
            row.prop(self, 'scale_y')            
         
            box.separator()



        # LOCATION #
        if self.prefs_tabs == 'panel':
            
            box = layout.box().column(align=True)
             
            row = box.row(1) 
            row.label("Panel Location:")
         
            box.separator()             
         
            row = box.row(1)
            row.prop(self, 'tab_origin_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_origin_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "category")

            box.separator() 
            box.separator() 



        # APPEND #
        if self.prefs_tabs == 'menus':

            col = layout.column(align=True)   

            box = col.box().column(align=True)

            box.separator()
            
            row = box.row(align=True)  
            row.label(text="Cascade Menu: [CTRL+D] ", icon ="COLLAPSEMENU")        

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_origin_menu', expand=True)
         
            if self.tab_origin_menu == 'pie': 
               
                box.separator()   
              
                row = box.column(align=True)                                                  
                row.label(text="> This menu is work in progress and always a proposal.")
                row.label(text="> Left or right, up or down, there are too many preferences,")
                row.label(text="> to create a pie menu for everyone.")
                row.label(text="> But it would be handy if you work with a bigger screen.")

 
            box.separator()
            box.separator()

            #-----------------------------------------------------

            box = col.box().column(align=True)
         
            box.separator()
         
            row = box.row(align=True)  
            row.label(text="Special Menu [W]", icon ="COLLAPSEMENU")         

            box.separator()            
         
            row = box.column(align=True)          
            row.label(text="A origin menu will be added to the default special menu.")

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_origin_special', expand=True)

            box.separator()
            box.separator()


            #-----------------------------------------------------

            box = col.box().column(align=True)
           
            box.separator()              
            box.separator()              

            # TIP #            
            row = box.row(align=True)             
            row.label(text="! For key change go to > Edit: Preferences > Keymap !", icon ="INFO")

            row = box.column(align=True) 
            row.label(text="1 > change search to key-bindig and insert the hotkey: ctrl d", icon ="BLANK1")
            row.label(text="2 > go to 3D View > Call Menu [CTRL+D]: VIEW3D_MT_Origin_Menu /_Pie!", icon ="BLANK1")
            row.label(text="3 > choose a new key configuration and save preferences !", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)             
            row.label(text="Or edit the keymap script directly:", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)  
            row.label(text="", icon ="BLANK1")
            row.operator("tpc_ot.keymap_origin", text = 'Open KeyMap in Text Editor')
            row.operator('wm.url_open', text = 'Type of Events').url = "https://github.com/mkbreuer/Misc-Share-Archiv/blob/master/images/SHORTCUTS_Type%20of%20key%20event.png?raw=true"
            
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
 





## REGISTER #

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()


    update_panel(None, bpy.context)
    update_origin_menu(None, bpy.context)
    update_origin_header(None, bpy.context)
    update_origin_special(None, bpy.context)


    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_MT_Origin_Manual)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
 
    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_MT_Origin_Manual) 

if __name__ == "__main__":
    register()



