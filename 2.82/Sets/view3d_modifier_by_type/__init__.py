# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2020 MKB
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


bl_info = {
    "name": "Modifier by Type",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 6),
    "blender": (2, 82, 0),
    "location": "3D View Editor > Tab: Modifier by Type / Properties Editor > Tab: Modifier > on Top",
    "description": "modifier function processing for all selected object",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User Tools"}


# LOAD MODULES #
import bpy
import bpy.utils.previews
from bpy.props import *
from bpy.types import AddonPreferences, PropertyGroup


# ADDON CHECK #
import addon_utils   
from . ui_utils import addon_exists

# LOAD / RELOAD SUBMODULES #
import importlib
from . import developer_utils

# LOAD OPERATORS #   
from .ot_copy     import *
from .ot_process  import *
from .ui_utils    import *

# LOAD UI # 
from .ui_keymap  import *
from .ui_layout  import *
from .ui_layout  import VIEW3D_PT_modifier_by_type_panel_ui

importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())


# UPDATE TAB CATEGORY FOR PANEL IN THE TOOLSHELF #
panels = (
        VIEW3D_PT_modifier_by_type_panel_ui,
        )

def update_panel(self, context):
    addon_prefs = context.preferences.addons[__name__].preferences                                        
    message = "Updating Panel locations has failed"
    try:
        for panel in panels:             
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
      
        for panel in panels: 
            panel.bl_category = addon_prefs.category 
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass



class AddonPreferences(AddonPreferences):
    bl_idname = __name__
        
    category : StringProperty(name="", description="Choose a name for the category of the panel", default="Modifier by Type", update=update_panel)
    #toggle_sidebar_panel : BoolProperty(name="Sidebar Panel", description="enable or disable", default = True, update=update_panel)
    ui_scale_y : bpy.props.FloatProperty(name="Scale Y",  description="scale layout space", default=1.1, min=1.0, max=1.5, precision=2)
    toggle_name_dropdowns : BoolProperty(name="", default=True, description="enable/disable layout separator")
    toggle_name_buttons : BoolProperty(name="", default=True, description="enable/disable layout separator")
    toggle_display_custom1 : BoolProperty(name="", default=False, description="enable/disable custom string")

    toggle_layout_type : EnumProperty(
        name = 'Layout Type',
        description = 'toggle layout type',
        items=[('type_a', 'Layout A', 'layout position'),
               ('type_b', 'Layout B', 'layout position'),
               ('type_c', 'Layout C', 'layout position'),
               ('type_d', 'Layout D', 'layout position'),
               ('type_e', 'Layout E', 'layout position')],
               default='type_a')


    toggle_layout_properties : BoolProperty(name="Property Menu", description="enable or disable", default = True, update=update_properties)
    ui_scale_y_properties : bpy.props.FloatProperty(name="Scale Y",  description="scale layout space", default=1.0, min=1.0, max=1.5, precision=2)
    toggle_name_dropdowns_properties : BoolProperty(name="", default=True, description="enable/disable layout separator")
    toggle_name_buttons_properties : BoolProperty(name="", default=True, description="enable/disable layout separator")
    toggle_display_custom2 : BoolProperty(name="", default=False, description="enable/disable custom string")

    toggle_layout_type_properties : EnumProperty(
        name = 'Layout Type',
        description = 'toggle layout type',
        items=[('type_a', 'Layout A', 'layout position'),
               ('type_b', 'Layout B', 'layout position'),
               ('type_c', 'Layout C', 'layout position'),
               ('type_d', 'Layout D', 'layout position')],
               default='type_a')
               

    toggle_popover : EnumProperty(
        name = 'Menu Location',
        description = 'save user settings',
        items=(('prepend', 'Top/Left',     'menu layout position'),
               ('append',  'Bottom/Right', 'menu layout position'),
               ('off',     'Off',    'disable menu for 3d view')),
               default='off', update = update_menu)

    toggle_MT_menu : EnumProperty(
        name = 'Menu Location',
        description = 'save user settings',
        items=[('menu_special',  'Special Menu ',  'Keys: [W]'),
               ('menu_header',   '3D View Header', 'Keys: none')],
               default='menu_special')

    toggle_MT_menu_location : EnumProperty(
        name = 'Header Location',
        description = 'save user settings',
        items=[('header_editor_menus',  'Editor Menu', 'header layout position'),
               ('header_main_menus',    'Header Menu', 'header layout position')],
               default='header_editor_menus')

    toggle_popover_icon : BoolProperty(name="", default=True, description="enable/disable layout separator")
    toggle_popover_separator : BoolProperty(name="", default=True, description="enable/disable layout separator")

    toggle_addon_modifier_tools : BoolProperty(name="Modifier Tools", default=True, description="enable/disable")

    def draw(self, context):
        layout = self.layout.column(align=True)
       
        box = layout.box().column(align=True)
        box.separator()                                   
       
        row = box.row(align=True) 
        row.label(text="Tab Category:")             
        row.prop(self, "category", text="")    
    
        box.separator() 

        row = box.row(align=True)  
        row.label(text="Layout Type:")                   
        row.prop(self, 'toggle_layout_type', text="")   

        box.separator() 

        row = box.row(align=True)  
        row.label(text="Layout Scale:")                   
        row.prop(self, 'ui_scale_y')            
      
        box.separator() 

        row = box.row(align=True)  
        row.label(text="Menu Panel:")                   
        row.popover(panel="VIEW3D_PT_modifier_by_type_panel_ui", text="VIEW3D_PT_modifier_by_type_panel_ui")    
 
        box.separator() 

        row = box.row(align=True)  
        row.label(text="Name Dropdowns:")                   
        row.prop(self, 'toggle_name_dropdowns')  

        box.separator() 

        row = box.row(align=True)  
        row.label(text="Name Buttons:")                   
        row.prop(self, 'toggle_name_buttons')  
      
        box.separator()     

        row = box.row(align=True)  
        row.label(text="Display Custom:")                   
        row.prop(self, 'toggle_display_custom1')  
      
        box.separator()  

        row = box.row(align=True) 
        row.label(text="! Refesh category with 3D View panel button > dis-/enable!", icon ="INFO")  

        box.separator()                    
        box = layout.box().column(align=True)
        box.separator()            

        row = box.row(align=True)  
        row.label(text="Property Menu:")                   
        row.prop(self, 'toggle_layout_properties', text="")  

        box.separator() 

        row = box.row(align=True)  
        row.label(text="Layout Type:")                   
        row.prop(self, 'toggle_layout_type_properties', text="")   

        box.separator() 

        row = box.row(align=True)  
        row.label(text="Layout Scale:")                   
        row.prop(self, 'ui_scale_y_properties')            
      
        box.separator()

        if self.toggle_layout_type_properties !='type_b':
            
            row = box.row(align=True)  
            row.label(text="Name Dropdowns:")                   
            row.prop(self, 'toggle_name_dropdowns_properties')  

            box.separator()

            row = box.row(align=True)  
            row.label(text="Name Buttons:")                   
            row.prop(self, 'toggle_name_buttons_properties')  

            box.separator()

        row = box.row(align=True)  
        row.label(text="Display Custom:")                   
        row.prop(self, 'toggle_display_custom2')     

        box.separator()                    
        box = layout.box().column(align=True)
        box.separator()    

        row = box.row(align=True)  
        row.label(text="Add to Special Menu:")        

        row = box.column(align=True)    
        row.prop(self, 'toggle_popover_icon', text='toggle menu icon')
        row.prop(self, 'toggle_popover_separator', text='toggle menu separator')

        box.separator()
       
        row = box.row(align=True)  
        row.prop(self, 'toggle_popover', expand=True)
                    
        if self.toggle_popover == 'off':
            
            box.separator() 
            
            row = box.row(align=True) 
            row.label(text="! menu hidden with next blender start durably!", icon ="INFO")  
       
        else:

            box.separator()

            row = box.row(align=True)  
            row.prop(self, 'toggle_MT_menu', expand=True)  
      
            box.separator() 
            
            if self.toggle_MT_menu == 'menu_header': 

                row = box.row(align=True)  
                row.prop(self, 'toggle_MT_menu_location', expand=True)  
          
                box.separator()  
          
            row = box.row(align=True) 
            row.label(text="! Refesh with Top/Left - Bottom/Right buttons!", icon ="INFO")  


        box.separator()                    
        box = layout.box().column(align=True)
        box.separator()    

        row = box.row(align=True)  
        row.label(text="Recommended Addon:", icon='PLUGIN')
        
        row = box.row(align=True)
        row.prop(self, 'toggle_addon_modifier_tools', text="")  
        row.label(text="Modifier Tools")
        
        if self.toggle_addon_modifier_tools == True:  
            modifier_tools_addon = "space_view3d_modifier_tools" 
            modifier_tools_state = addon_utils.check(modifier_tools_addon)
            if not modifier_tools_state[0]:
                row.operator("preferences.addon_show", text="Activate: Modifier Tools", icon="ERROR").module="space_view3d_modifier_tools"    
            else:
                row.label(text="Tools are available!", icon ="INFO")  
        else:
            row.label(text="Tools are hidden!", icon ="ERROR")  
   
        box.separator()                    



class Global_Property_Group(bpy.types.PropertyGroup):

    mod_mode : StringProperty(default="", options={'HIDDEN'})
    mod_string : StringProperty(name="None", description="Use name of modifier", default="")
    
    mod_processing : bpy.props.EnumProperty(                            
      items = [("ADD",     "Add",       "",    "ADD",                   0),                                  
               ("RENDER",  "Render",    "",    "RESTRICT_RENDER_OFF",   1), 
               ("UNHIDE",  "(Un)Hide",  "",    "RESTRICT_VIEW_OFF",     2), 
               ("EDIT",    "Edit",      "",    "EDITMODE_HLT",          3), 
               ("CAGE",    "Cage",      "",    "MESH_DATA",             4), 
               ("DOWN",    "Down",      "",    "TRIA_DOWN",             5),
               ("UP",      "Up",        "",    "TRIA_UP",               6),  
               ("APPLY",   "Apply",     "",    "CHECKMARK",             7),                                 
               ("REMOVE",  "Remove",    "",    "X",                     8),
               ("STACK",   "Stack",     "",    "FULLSCREEN_ENTER",      9),
               ("NONE",    "None",      "",    "INFO",                  10)],
               name = "Process All", 
               default = "NONE", 
               description="change modifier processing type")


    mod_list : EnumProperty(                         
      items = [
               ("DATA_TRANSFER",            "Data Transfer",            "", "MOD_DATA_TRANSFER",  101),       
               ("MESH_CACHE",               "Mesh Cache",               "", "MOD_MESHDEFORM",     102),                                   
               ("MESH_SEQUENCE_CACHE",      "Mesh Sequence Cache",      "", "MOD_MESHDEFORM",     103),                                            
               ("NORMAL_EDIT",              "Normal Edit",              "", "MOD_UVPROJECT",      104),               
               ("WEIGHTED_NORMAL",          "Weighted Normal",          "", "MOD_UVPROJECT",      105),               
               ("UV_PROJECT",               "UV Project",               "", "MOD_UVPROJECT",      106),               
               ("UV_WARP",                  "UV Warp",                  "", "MOD_UVPROJECT",      107),                                                                      
               ("VERTEX_WEIGHT_EDIT",       "Vertex Weight Edit",       "", "MOD_VERTEX_WEIGHT",  108),
               ("VERTEX_WEIGHT_MIX",        "Vertex Weight Mix",        "", "MOD_VERTEX_WEIGHT",  109),          
               ("VERTEX_WEIGHT_PROXIMITY",  "Vertex Weight Proximity",  "", "MOD_VERTEX_WEIGHT",  110),      
      
               ("WELD",                     "Weld",                     "", "AUTOMERGE_OFF",      200),  
               ("WIREFRAME",                "Wireframe",                "", "MOD_WIREFRAME",      201),  
               ("TRIANGULATE",              "Triangulate",              "", "MOD_TRIANGULATE",    202),                                 
               ("SUBSURF",                  "Subsurf",                  "", "MOD_SUBSURF",        203),  
               ("SOLIDIFY",                 "Solidify",                 "", "MOD_SOLIDIFY",       204),                             
               ("SKIN",                     "Skin",                     "", "MOD_SKIN",           205),                              
               ("SCREW",                    "Screw",                    "", "MOD_SCREW",          206),                               
               ("REMESH",                   "Remesh",                   "", "MOD_REMESH",         207),                                  
               ("MULTIRES",                 "Multires",                 "", "MOD_MULTIRES",       208),                                  
               ("MIRROR",                   "Mirror",                   "", "MOD_MIRROR",         209),                                                                   
               ("MASK",                     "Mask",                     "", "MOD_MASK",           210),                                  
               ("EDGE_SPLIT",               "Edge Split",               "", "MOD_EDGESPLIT",      211),                                   
               ("DECIMATE",                 "Decimate",                 "", "MOD_DECIM",          212),                                  
               ("BUILD",                    "Build",                    "", "MOD_BUILD",          213), 
               ("BOOLEAN",                  "Boolean",                  "", "MOD_BOOLEAN",        214),  
               ("BEVEL",                    "Bevel",                    "", "MOD_BEVEL",          215), 
               ("ARRAY",                    "Array",                    "", "MOD_ARRAY",          216),                                   
             
               ("WAVE",                     "Wave",                     "", "MOD_WAVE",           301),                                   
               ("WARP",                     "Warp",                     "", "MOD_WARP",           302),                                   
               ("SURFACE_DEFORM",           "Smooth Deform",            "", "MOD_SMOOTH",         303),
               ("LAPLACIANSMOOTH",          "Smooth Laplacian",         "", "MOD_SMOOTH",         304),
               ("CORRECTIVE_SMOOTH",        "Smooth Corrective",        "", "MOD_SMOOTH",         305),
               ("SMOOTH",                   "Smooth",                   "", "MOD_SMOOTH",         306),                                   
               ("SIMPLE_DEFORM",            "Simple Deform",            "", "MOD_SIMPLEDEFORM",   307),                                   
               ("SHRINKWRAP",               "Shrinkwrap",               "", "MOD_SHRINKWRAP",     308),                                   
               ("MESH_DEFORM",              "Mesh Deform",              "", "MOD_MESHDEFORM",     309),                                   
               ("LATTICE",                  "Lattice",                  "", "MOD_LATTICE",        310),
               ("LAPLACIANDEFORM",          "Laplacian Deform",         "", "MOD_MESHDEFORM",     311),
               ("HOOK",                     "Hook",                     "", "HOOK",               312),  
               ("DISPLACE",                 "Displace",                 "", "MOD_DISPLACE",       313),
               ("CURVE",                    "Curve",                    "", "MOD_CURVE",          314),
               ("CAST",                     "Cast",                     "", "MOD_CAST",           315),                                    
               ("ARMATURE",                 "Armature",                 "", "MOD_ARMATURE",       316),                                   
             
               ("NONE",                     "None",                     "", "INFO",               400),
               ("SOFT_BODY",                "Soft Body",                "", "MOD_SOFT",           401),
               ("SMOKE",                    "Smoke",                    "", "MOD_SMOKE",          402),
               ("PARTICLE_SYSTEM",          "Particle System",          "", "MOD_PARTICLES",      403),
               ("PARTICLE_INSTANCE",        "Particle Instance",        "", "MOD_PARTICLES",      404),
               ("OCEAN",                    "Ocean",                    "", "MOD_OCEAN",          405),
               ("FLUID",                    "Fluid Simulation",         "", "MOD_FLUIDSIM",       406),
               ("EXPLODE",                  "Explode",                  "", "MOD_EXPLODE",        407),
               ("DYNAMIC_PAINT",            "Dynamic Paint",            "", "MOD_DYNAMICPAINT",   408),
               ("COLLISION",                "Collision",                "", "MOD_PHYSICS",        409),
               ("CLOTH",                    "Cloth",                    "", "MOD_CLOTH",          410)], 
            
              #(identifier,                 name,              description, icon,                 number)   
             
               name = "Modifier Type", 
               default = "NONE", 
               description="change modifier type",
               options={'SKIP_SAVE'}) 
               
               
    mod_list_lock : BoolProperty(name="Lock ModType", description="lock modifier type for custom", default = False)
    mod_list_stack : BoolProperty(name="Modifier Stack", description="show modifier stack", default = False)
 


# REGISTER #
classes = (
    VIEW3D_MT_add_modifier_mbt,
    VIEW3D_OT_modifier_add_mbt,
    VIEW3D_OT_execute_direct,
    VIEW3D_OT_modifier_by_type,
    VIEW3D_OT_modifier_copy,
    VIEW3D_OT_modifier_tools,
    VIEW3D_OT_clear_string,
    VIEW3D_OT_reset_all,
    VIEW3D_PT_modifier_by_type_panel_ui,
    AddonPreferences,
    Global_Property_Group,
    )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.WindowManager.global_props_modbytype = bpy.props.PointerProperty(type=Global_Property_Group)   

    update_panel(None, bpy.context)
    update_menu(None, bpy.context)
    update_properties(None, bpy.context)


def unregister():
    try:
        del bpy.types.WindowManager.global_props_modbytype
    except Exception as e:
        print('unregister fail:\n', e)
        pass

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()



              
