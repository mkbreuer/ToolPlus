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
    "name": "T+ Deform",
    "author": "Multi Authors (see URL), MKB",
    "version": (0, 1, 3),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] > Menu",
    "description": "Panel and Menu for Deform Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


from toolplus_deform.deform_batch  import (View3D_TP_Deform_Batch)

from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons

from .mesh_project import __init__
from .mesh_project import bound
from .mesh_project import funcs_blender
from .mesh_project import funcs_math
from .mesh_project import funcs_tri
from .mesh_project import mesh_mirror_script
from .mesh_project import partition_grid
from .mesh_project import proj_data
from .mesh_project import project
from .mesh_project import uv_project


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_deform'))

##################################
if "bpy" in locals():
    import imp
   
    imp.reload(deform_bounding)    
    imp.reload(deform_easylattice)    
    imp.reload(deform_meshcage)
    imp.reload(deform_modifier)  
    imp.reload(deform_pivot) 
    imp.reload(deform_transform)  

    print("Reloaded multifiles")
    
else:

    from . import deform_bounding    
    from . import deform_easylattice    
    from . import deform_meshcage
    from . import deform_modifier
    from . import deform_pivot
    from . import deform_transform

    print("Imported multifiles")


import deform_bounding    
import deform_easylattice    
import deform_meshcage
import deform_modifier
import deform_pivot
import deform_transform


import bpy
from bpy import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import* #(StringProperty, BoolProperty, FloatVectorProperty, FloatProperty, EnumProperty, IntProperty)


##################################



def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Deform_Panel_UI)
        
        bpy.utils.unregister_class(VIEW3D_TP_Deform_Panel_TOOLS)
        
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Deform_Panel_UI)

    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_Deform_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
       
        bpy.utils.register_class(VIEW3D_TP_Deform_Panel_TOOLS)

    else:
        bpy.utils.register_class(VIEW3D_TP_Deform_Panel_UI)



def update_display_tools(self, context):
   
    if context.user_preferences.addons[__name__].preferences.tab_meshcage == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_meshcage_menu == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_project == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_project_menu == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_vertgrp == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_vertgrp_menu == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_hook == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_hook_menu == 'on':
        return 
    elif context.user_preferences.addons[__name__].preferences.tab_history == 'on':
        return   
    elif context.user_preferences.addons[__name__].preferences.tab_history_menu == 'on':
        return   

    
    if context.user_preferences.addons[__name__].preferences.tab_meshcage == 'off':
        pass
    elif context.user_preferences.addons[__name__].preferences.tab_meshcage_menu == 'off':
        pass
    elif context.user_preferences.addons[__name__].preferences.tab_project == 'off':
        pass
    elif context.user_preferences.addons[__name__].preferences.tab_project_menu == 'off':
        pass
    elif context.user_preferences.addons[__name__].preferences.tab_vertgrp == 'off':
        pass
    elif context.user_preferences.addons[__name__].preferences.tab_vertgrp_menu == 'off':
        pass
    elif context.user_preferences.addons[__name__].preferences.tab_hook == 'off':
        pass   
    elif context.user_preferences.addons[__name__].preferences.tab_hook_menu == 'off':
        pass      
    elif context.user_preferences.addons[__name__].preferences.tab_history == 'off':
        pass
    elif context.user_preferences.addons[__name__].preferences.tab_history_menu == 'off':
        pass


    
addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(View3D_TP_Deform_Batch)
                
        # Keymapping
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        View3D_TP_Deform_Batch.bl_category = context.user_preferences.addons[__name__].preferences.tab_menu_view
    
        bpy.utils.register_class(View3D_TP_Deform_Batch)
    
        # Keymapping 
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('tp_batch.batch_deform', 'Y', 'PRESS', ctrl=True, shift=True) #,alt=True
        #kmi.properties.name = ''

    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass



#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('toolsets',   "Tools",      "Tools"),
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


    tab_meshcage = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'MeshCage on', 'enable tools in panel'), ('off', 'MeshCage off', 'disable tools in panel')), default='off', update = update_display_tools)

    tab_project = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Project on', 'enable tools in menu'), ('off', 'Project off', 'disable tools in menu')), default='off', update = update_display_tools)

    tab_vertgrp = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'VertexGroup on', 'enable tools in panel'), ('off', 'VertexGroup off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_hook = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Hook on', 'enable tools in menu'), ('off', 'Hook off', 'disable tools in menu')), default='off', update = update_display_tools)

    tab_history = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='off', update = update_display_tools)

 
    tab_meshcage_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'MeshCage on', 'enable tools in panel'), ('off', 'MeshCage off', 'disable tools in panel')), default='off', update = update_display_tools)

    tab_project_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Project on', 'enable tools in menu'), ('off', 'Project off', 'disable tools in menu')), default='off', update = update_display_tools)

    tab_vertgrp_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'VertexGroup on', 'enable tools in panel'), ('off', 'VertexGroup off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_hook_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Hook on', 'enable tools in menu'), ('off', 'Hook off', 'disable tools in menu')), default='off', update = update_display_tools)

    tab_history_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='off', update = update_display_tools)
 
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)


    def draw(self, context): 

        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            row = layout.row()
            row.label(text="Welcome to T+ Deform Collection")
            
            row = layout.column()
            row.label(text="This setup helps to make fast adjustment to an finished object. etc.")
            row.label(text=" for your own workflow you can enable or disable the functions in the panel or in the menu") 
            row.label(text="Have Fun! ;) ")     
            

        #Tools
        if self.prefs_tabs == 'toolsets':

            box = layout.box().column(1)

            row = box.row()
            row.prop(self, 'tab_meshcage', expand=True)
            row.prop(self, 'tab_project', expand=True)
            row.prop(self, 'tab_vertgrp', expand=True)
           
            box.separator()               
           
            row = box.row()
            row.prop(self, 'tab_hook', expand=True)
            row.prop(self, 'tab_history', expand=True)

            row = box.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 


        #Location
        if self.prefs_tabs == 'location':
          
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location Deform:")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            box.separator() 

            row = layout.row()
            row.label(text="! please reboot blender after changing the panel location !", icon ="INFO")
            
            
        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Deform Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: CTRL+SHIFT+Y")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
             
            row.operator('wm.url_open', text = 'tip: iskeyfree', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"

            box.separator() 
        
            row = box.row()  
            row.prop(self, 'tab_meshcage_menu', expand=True)
            row.prop(self, 'tab_project_menu', expand=True)
            row.prop(self, 'tab_vertgrp_menu', expand=True)
        
            box.separator()             
          
            row = box.row()              
            row.prop(self, 'tab_hook_menu', expand=True)
            row.prop(self, 'tab_history_menu', expand=True)

            box.separator() 
            
            row = box.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")


        #Weblinks
        if self.prefs_tabs == 'url':

            row = layout.row()
            row.operator('wm.url_open', text = 'Easy Lattice', icon = 'INFO').url = "http://wiki.blender.org/index.php/Easy_Lattice_Editing_Addon"
            row.operator('wm.url_open', text = 'MDeform', icon = 'INFO').url = "http://airplanes3d.net/scripts-256_e.xml"
            row.operator('wm.url_open', text = 'Projection Ops', icon = 'CLIP').url = "https://www.youtube.com/watch?v=ipr53QH6iyQ"
            row.operator('wm.url_open', text = 'THREAD', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?409575-Addon-T-Deform&p=3114846#post3114846"


class DropdownDeformToolProps(bpy.types.PropertyGroup):

    display_mod_hook = bpy.props.BoolProperty(name="Hook Props", description="open / close", default=False)



#--- ### Helper functions
DEBUG = 0 
MID = "MDeformer"

def assigned_objects(deformer):

    return list(filter(lambda obj: obj.modifiers.get(MID, None) and obj.modifiers[MID].object == deformer, bpy.context.scene.objects))

def is_deformer_object(obj):

    if obj.modifiers.get(MID, None): 
        return False
    else:
        return assigned_objects(obj) != []

def is_bound(deformer):

    return (deformer.get(MID, None) != None)



# Panel Layout
def draw_deform_panel_layout(self, context, layout):
                        
        tpw = context.window_manager.tpw_defom_window

        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'


        if context.mode == 'EDIT_LATTICE':
            
            box = layout.box().column(1)                    

            row = box.row(1)
            row.prop(context.object.data, "use_outside")
            row.prop_search(context.object.data, "vertex_group", context.object, "vertex_groups", text="")   

            box.separator()                       

            row = box.row(1)
            row.prop(context.object.data, "points_u", text="X")
            row.prop(context.object.data, "points_v", text="Y")
            row.prop(context.object.data, "points_w", text="Z")
         
            row = box.row(1)
            row.prop(context.object.data, "interpolation_type_u", text="")
            row.prop(context.object.data, "interpolation_type_v", text="")
            row.prop(context.object.data, "interpolation_type_w", text="")  

            box.separator()                       

            row = box.row(1)
            row.operator("lattice.make_regular", "Make Regular", icon ="LATTICE_DATA")
             
            ###
            box.separator()   


        if context.mode == 'OBJECT':

            obj = context.active_object     
            if obj:
               obj_type = obj.type

               if obj_type in {'LATTICE'}:
                    box = layout.box().column(1)                    

                    row = box.row(1)

                    row.prop(context.object.data, "use_outside")
                    row.prop_search(context.object.data, "vertex_group", context.object, "vertex_groups", text="")   

                    box.separator()                       

                    row = box.row(1)
                    row.prop(context.object.data, "points_u", text="X")
                    row.prop(context.object.data, "points_v", text="Y")
                    row.prop(context.object.data, "points_w", text="Z")
                 
                    row = box.row(1)
                    row.prop(context.object.data, "interpolation_type_u", text="")
                    row.prop(context.object.data, "interpolation_type_v", text="")
                    row.prop(context.object.data, "interpolation_type_w", text="")  

                    box.separator()                       

                    row = box.column(1)
                    row.operator("lattice.make_regular", "Make Regular", icon ="LATTICE_DATA")
                    row.operator("tp_ops.zero_rotation", "Set zero rotation", icon ="MAN_ROT")
                    
                    box.separator()   

               else:
                    box = layout.box().column(1)   

                    row = box.row(1)
                    row.alignment = 'CENTER'
                    row.label("Easy Lattice")
                   
                    box.separator()   
                    
                    row = box.row(1) 
                    
                    button_lattice_create = icons.get("icon_lattice_create")                                                               
                    row.operator("object.easy_lattice_panel", text="Create", icon_value=button_lattice_create.icon_id)  

                    button_lattice_apply = icons.get("icon_lattice_apply")    
                    row.operator("tp_ops.lattice_apply", text = "Apply", icon_value=button_lattice_apply.icon_id)                       
                        
                    box.separator()   
                    
                    row = box.row(1) 
                    row.prop(context.scene, "lat_u", text="X")
                    row.prop(context.scene, "lat_w", text="Y")
                    row.prop(context.scene, "lat_m", text="Z")
                    
                    box.separator()           
                    
                    row = box.row(1)
                    row.prop(context.scene, "lat_type", text = "Type")

                    box.separator()                    


            Display_MeshCage = context.user_preferences.addons[__name__].preferences.tab_meshcage
            if Display_MeshCage == 'on':   
                
                box = layout.box().column(1)   

                row = box.row(1)
                row.alignment = 'CENTER'
                row.label("MeshCage Deform")
               
                box.separator()   
                
                row = box.row(1)         
                row.operator("tp_ops.add_bound_meshcage", "Add CageBox", icon ="MOD_MESHDEFORM")            

                
                obj = context.object
                if obj:
                    if obj.draw_type == 'WIRE':
                        row.operator("tp_ops.draw_solid", text="", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text="", icon='GHOST_ENABLED') 
              
                row = box.row(1)  
                obj = context.object
                if obj:                    
                    MID = "MDeformer"
                    if obj.modifiers.get(MID, None):
                        row.operator("mesh.deformer_clear", "", icon ="PANEL_CLOSE")
                    else:
                        row.operator("mesh.deformer_set", "Set Deformer", icon ="CONSTRAINT_DATA")

                box.separator()  


            Display_Project = context.user_preferences.addons[__name__].preferences.tab_project
            if Display_Project == 'on':   
 
                box = layout.box().column(1)   

                row = box.row(1)
                row.alignment = 'CENTER'
                row.label("Project to active Surface")
               
                box.separator()   
                
                row = box.column(1)                           
                row.operator("mesh.project_onto_uvmapped_mesh", text="to UVs", icon ="MOD_LATTICE")  
                row.operator("mesh.project_onto_selected_mesh", text = "to Mesh", icon="MOD_SHRINKWRAP")    
                row.operator("mesh.mirror_mesh_along_mirrormesh_normals", text = "Normals Mirror", icon="MOD_MIRROR")    

                ###
                box.separator()                                     


            Display_VertexGroups = context.user_preferences.addons[__name__].preferences.tab_vertgrp
            if Display_VertexGroups == 'on':   
                     
                box = layout.box().column(1)   

                row = box.row(1)              
                row.alignment = 'CENTER'
                row.label("VertexGroups", icon='STICKY_UVS_LOC')     
                
                box.separator()                                       
                
                row = box.row()
                obj = context.object
                if obj:
                    row.template_list("MESH_UL_vgroups", "", obj, "vertex_groups", obj.vertex_groups, "active_index", rows=4)           

                col = row.column()
                sub = col.column(1)
                sub.operator("object.vertex_group_add", icon='ZOOMIN', text="")
                sub.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
                sub.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
                sub.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                sub.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                
                
                ###
                box.separator()    



            Display_Hook = context.user_preferences.addons[__name__].preferences.tab_hook
            if Display_Hook == 'on':   
                
                obj = context.active_object
                if obj:
                    for mo in obj.modifiers:
                        if mo.type == 'HOOK':
                         
                            row = box.row()
                            if tpw.display_mod_hook:
                                row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')            
                            else:                
                                row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')

                            if tpw.display_mod_hook: 

                                row = box.column(1)                                 
                                mo_types = []
                                append = mo_types.append

                                for mo in obj.modifiers:
                                    if mo.type == 'HOOK':
                                        
                                        append(mo.type)

                                        box = layout.box().column(1)  

                                        row = box.column(1)                                  
                                        row.label(mo.name)

                                        row = box.column(1)
                                        row.prop(mo, "object", text="")
                                        obj = context.object
                                        if obj:
                                            row.prop_search(mo, "vertex_group", obj, "vertex_groups", text="")

                                        box.separator()

                                        row = box.column(1)
                                        row.prop(mo, "falloff_radius")
                                        row.prop(mo, "strength", slider=True)
                                        
                                        box.separator()
                                        
                                        row = box.column(1)
                                        row.prop(mo, "use_falloff_uniform")
                                        row.prop(mo, "falloff_type", text="")                                                        

                                        ###
                                        box.separator()   



        if context.mode == 'EDIT_MESH':

            box = layout.box().column(1)   

            row = box.row(1)
            row.alignment = 'CENTER'
            row.label("Easy Lattice")
    
            box.separator()               
     
            row = box.row(1)                           

            button_lattice_create = icons.get("icon_lattice_create")                                                               
            row.operator("object.easy_lattice_panel", text="Create", icon_value=button_lattice_create.icon_id)  
          
            button_lattice_apply = icons.get("icon_lattice_apply")    
            row.operator("tp_ops.lattice_apply", text = "Apply", icon_value=button_lattice_apply.icon_id)                               
                      
            box.separator()   
            
            row = box.row(1) 
            row.prop(context.scene, "lat_u", text="X")
            row.prop(context.scene, "lat_w", text="Y")
            row.prop(context.scene, "lat_m", text="Z")
            
            box.separator()           
            
            row = box.row(1)
            row.prop(context.scene, "lat_type", text = "Type")

            ###
            box.separator()     

            Display_Project = context.user_preferences.addons[__name__].preferences.tab_project
            if Display_Project == 'on':   

                box = layout.box().column(1)   

                row = box.row(1)
                row.alignment = 'CENTER'
                row.label("MeshCage Deform")
               
                box.separator()   
                
                row = box.column(1)
                obj = context.object
                if obj:
                    objects = assigned_objects(context.object)
                    
                    if len(objects) > 0:
                        info = "%d associated objects"  % len(objects)
                        
                        row.label(text=info)

                        if is_bound(context.object):
                            
                            row.operator("mesh.deformer_bind", text = "Unbind objects") 
                            
                            box.separator() 
                            
                            row = box.row(1)
                            row.operator("mesh.deformer_clear", text= "Remove").apply=False
                            row.operator("mesh.deformer_clear", text= "Apply").apply=True
                       
                        else:   
                            row.operator("mesh.deformer_bind", text = "Bind objects")
                            
                            row = box.row()
                            row.operator("mesh.deformer_clear", text= "Remove").apply=False

                    else: 
                        row.label(text="no associated objects", icon = "INFO")                   
                                                
                ###
                box.separator()                                     



            Display_VertexGroups = context.user_preferences.addons[__name__].preferences.tab_vertgrp
            if Display_VertexGroups == 'on':   

                box = layout.box().column(1)   

                row = box.row(1)              
                row.alignment = 'CENTER'
                row.label("VertexGroups", icon='STICKY_UVS_LOC')     
                
                box.separator()                                       
                
                row = box.row()
                obj = context.object
                if obj:                                
                    row.template_list("MESH_UL_vgroups", "", obj, "vertex_groups", obj.vertex_groups, "active_index", rows=4)           

                col = row.column()
                sub = col.column(1)
                sub.operator("object.vertex_group_add", icon='ZOOMIN', text="")
                sub.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
                sub.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
                sub.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                sub.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                

                box.separator()  
                
                row = box.row(1)
                row.operator("object.vertex_group_assign", text="Assign", icon="ZOOMIN") 
                row.operator("object.vertex_group_remove_from", text="Remove", icon="ZOOMOUT") 

                row = box.row(1)                    
                row.operator("object.vertex_group_select", text="Select", icon="RESTRICT_SELECT_OFF")
                row.operator("object.vertex_group_deselect", text="Deselect", icon="RESTRICT_SELECT_ON")
                
                row = box.row(1)
                row.prop(context.tool_settings, "vertex_group_weight", text="Weight")
            
                ###
                box.separator()    

           
            Display_Hook = context.user_preferences.addons[__name__].preferences.tab_hook
            if Display_Hook == 'on':   
                
                box = layout.box().column(1)   

                row = box.row(1)              
                row.alignment = 'CENTER'
                row.label("HOOK", icon='HOOK')     
                
                box.separator()
                      
                row = box.row(1)   
                row.operator_context = 'EXEC_AREA'
                row.operator("object.hook_add_newob", text="to New")
                row.operator("object.hook_add_selob", text="to Selected").use_bone = False
                    
                row = box.row(1)
                row.operator("object.hook_add_selob", text="to Selected Object Bone").use_bone = True

                box.separator()
                
                obj = context.active_object
                if obj:
                    for mo in obj.modifiers:
                        if mo.type == 'HOOK':
                                
                            row = box.row(1)
                            row.operator_menu_enum("object.hook_assign", "modifier", text="Assign")
                            row.operator_menu_enum("object.hook_remove", "modifier", text="Remove")
                                
                            row = box.row(1)
                            row.operator_menu_enum("object.hook_select", "modifier", text="Select")
                            row.operator_menu_enum("object.hook_reset", "modifier", text="Reset")
                            
                            row = box.row(1)
                            row.operator_menu_enum("object.hook_recenter", "modifier", text="Recenter")                            

                            box.separator()  
                                        
                            if tpw.display_mod_hook:
                                row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')            
                            else:                
                                row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')

                            if tpw.display_mod_hook: 

                                row = box.column(1)                                 
                                mo_types = []
                                append = mo_types.append

                                for mo in context.active_object.modifiers:
                                    if mo.type == 'HOOK':
                                        
                                        append(mo.type)

                                        box = layout.box().column(1)  

                                        row = box.column(1)                                  
                                        row.label(mo.name)

                                        row = box.column(1)
                                        row.prop(mo, "object", text="")
                                        
                                        obj = context.object
                                        if obj:      
                                            row.prop_search(mo, "vertex_group", obj, "vertex_groups", text="")

                                        box.separator()

                                        row = box.column(1)
                                        row.prop(mo, "falloff_radius")
                                        row.prop(mo, "strength", slider=True)
                                        
                                        box.separator()
                                        
                                        row = box.column(1)
                                        row.prop(mo, "use_falloff_uniform")
                                        row.prop(mo, "falloff_type", text="")                                                        

                                        ###
                                        box.separator()   


        obj = context.active_object
        if obj:
            if obj.modifiers:  
                                      
                box = layout.box().column(1)  

                row = box.row(1)  
                row.operator("tp_ops.remove_mod", text="Clear All", icon='X') 
                row.operator("tp_ops.apply_mod", text="Apply All", icon='FILE_TICK')  
                
                row = box.row(1)
                row.operator("tp_ops.modifier_on", "View on",icon = 'RESTRICT_VIEW_OFF')     
                row.operator("tp_ops.modifier_off","View off",icon = 'VISIBLE_IPO_OFF')  
          
                box.separator() 
                   
            else:
                pass
            


        Display_History = context.user_preferences.addons[__name__].preferences.tab_history 
        if Display_History == 'on':
            
            box = layout.box().column(1)  

            row = box.row(1)        
            row.operator("view3d.ruler", text="Ruler")   
             
            row.operator("ed.undo_history", text="History")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
           
            box.separator()   
            
        


class VIEW3D_TP_Deform_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Deform"
    bl_idname = "VIEW3D_TP_Deform_Panel_TOOLS"
    bl_label = "Deform"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'    
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)        
        if context.mode == 'OBJECT' or context.mode == 'EDIT_MESH' or context.mode == 'EDIT_LATTICE':            
            return isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_deform_panel_layout(self, context, layout)         
        


class VIEW3D_TP_Deform_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Deform_Panel_UI"
    bl_label = "Deform"
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
        if context.mode == 'OBJECT' or context.mode == 'EDIT_MESH' or context.mode == 'EDIT_LATTICE':            
            return isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_deform_panel_layout(self, context, layout) 



# register

icon_collections = {}

addon_keymaps = []

def register():
    
    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    mkb_icons.load("my_image1", os.path.join(icons_dir, "icon_image1.png"), 'IMAGE')
    mkb_icons.load("my_image2", os.path.join(icons_dir, "icon_image2.png"), 'IMAGE')

    icon_collections['main'] = mkb_icons
    
    deform_easylattice.register()    
    deform_meshcage.register()
    deform_modifier.register()
    deform_transform.register()

    bpy.utils.register_module(__name__)

    bpy.types.WindowManager.tpw_defom_window = bpy.props.PointerProperty(type = DropdownDeformToolProps)

    update_menu(None, bpy.context)
    update_panel_position(None, bpy.context)


def unregister():

    for icon in icon_collections.values():
        bpy.utils.previews.remove(icon)
    icon_collections.clear()

    deform_easylattice.unregister()    
    deform_meshcage.unregister()
    deform_modifier.unregister()
    deform_transform.unregister()

    bpy.utils.unregister_module(__name__)

    del bpy.types.WindowManager.tpw_defom_window
    
if __name__ == "__main__":
    register()
        
        



            



