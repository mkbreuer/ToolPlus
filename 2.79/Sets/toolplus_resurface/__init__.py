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



bl_info = {
"name": "T+ ReSurface", 
"author": "marivn.k.breuer (MKB)",
"version": (0, 1),
"blender": (2, 79, 0),
"location": "View3D > TAB T+ > ReSurface",
"description": "collection of toolplus setup",
"warning": "work in progress",
"wiki_url": "https://github.com/mkbreuer/ToolPlus/wiki",
"tracker_url": "",
"category": "ToolPlus"}



# LOAD MANUAL #
from toolplus_resurface.rsf_manual  import (VIEW3D_TP_ReSurface_Manual)

# LOAD PROPS #
from toolplus_resurface.properties.MeshBrushProps           import MeshBrushProps
from toolplus_resurface.properties.ShrinkwrapProps          import ShrinkwrapProps
from toolplus_resurface.properties.SmoothVerticesProps      import SmoothVerticesProps
from toolplus_resurface.properties.SurfaceConstraintProps   import SurfaceConstraintProps

from toolplus_resurface.ops_editing.bsurfaces         import (tp_bsurfacesProps)
from toolplus_resurface.ops_editing.looptools         import (tp_looptoolsProps)
from toolplus_resurface.ops_editing.meshcheck         import (MeshCheckCollectionGroup)
from toolplus_resurface.ops_editing.snapshot          import (VTOOLS_CC_snapShotMeshCollection)
from toolplus_resurface.ops_boolean.bool_carver       import (CarverPrefs)
from toolplus_resurface.ops_copy.copy_mifthcloning    import (MFTCloneProperties)
from toolplus_resurface.ops_copy.copy_to_meshtarget   import (ToTarget_Properties)

from toolplus_resurface.ops_align.align_auxiliary.oned_scripts    import (paul_managerProps)

# LOAD UI #
from toolplus_resurface.rsf_panel    import (VIEW3D_TP_ReSurface_Panel_TOOLS)
from toolplus_resurface.rsf_panel    import (VIEW3D_TP_ReSurface_Panel_UI)

# LOAD ICONS #
from . icons.icons   import load_icons
from . icons.icons   import clear_icons


# LOAD OPERATORS #

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_resurface'))

if "bpy" in locals():
    import importlib


    # # 
    importlib.reload(rsf_booltool)
    importlib.reload(rsf_reboot)
    importlib.reload(rsf_snapline)
    importlib.reload(keymap_ops)


    # ALIGN #  
    importlib.reload(align_mirror)
    importlib.reload(align_modifier) 
    importlib.reload(align_normal)   
    importlib.reload(align_orientation)   
    importlib.reload(align_pivot) 
    importlib.reload(align_snap_set)
    importlib.reload(align_snap_to)
    importlib.reload(align_transform) 
    importlib.reload(align_widget)

    importlib.reload(advanced)
    importlib.reload(center_cursor)
    importlib.reload(con_rotation)
    importlib.reload(distribute)     
    importlib.reload(distribute_obj)
    importlib.reload(face_to_face)
    importlib.reload(oned_scripts)
    importlib.reload(shrinksmooth) 
    importlib.reload(smoothdeform) 
    importlib.reload(snap_offset)
    importlib.reload(straighten) 
    importlib.reload(to_ground)
    importlib.reload(xyspread)     
    
    # BOOLEAN #
    importlib.reload(bool_action)
    importlib.reload(bool_bevel)
    importlib.reload(bool_boolean2d)
    importlib.reload(bool_carver)
    
    # BOUNDING #
    importlib.reload(boxes)    
    importlib.reload(copy)    
    importlib.reload(origin)    
    importlib.reload(recoplanar)    
    importlib.reload(relocal)    
    importlib.reload(rename)    
    importlib.reload(selection)    
    importlib.reload(spheres)    
    importlib.reload(tubes)    
    
    # COPY # 
    importlib.reload(copy_action)
    importlib.reload(copy_attributes)
    importlib.reload(copy_dupliset)
    importlib.reload(copy_fpath)    
    importlib.reload(copy_mifthcloning)
    importlib.reload(copy_multilinked)
    importlib.reload(copy_origin)
    importlib.reload(copy_replicator)
    importlib.reload(copy_to_all)
    importlib.reload(copy_to_cursor)
    importlib.reload(copy_to_meshtarget)
    
    # CURVE #
    
    importlib.reload(curve_actions)
    importlib.reload(curve_convert)
    importlib.reload(curve_copies)
    importlib.reload(curve_extend)
    importlib.reload(curve_merged)
    importlib.reload(curve_start)
    importlib.reload(curve_overlay)
    importlib.reload(curve_simplify)
    importlib.reload(curve_split)
    importlib.reload(curve_trim)
    importlib.reload(curve_outline)  
    importlib.reload(curve_remove) 
    importlib.reload(curve_draw) 

    importlib.reload(add_curves)
    importlib.reload(add_galore)
    importlib.reload(add_taper)
    importlib.reload(add_taper_bevel)
    importlib.reload(add_tube_edge)
    importlib.reload(add_tube_face)

    importlib.reload(__init__) 
    importlib.reload(internal) 
    importlib.reload(svg_export) 

    # EDITING #    
    importlib.reload(bsurfaces)
    importlib.reload(closer) 
    importlib.reload(create) 
    importlib.reload(cutfaces) 
    importlib.reload(reextrude)
    importlib.reload(fastloop)
    importlib.reload(filletinset)
    importlib.reload(filletplus)
    importlib.reload(looptools)
    importlib.reload(meshcheck)
    importlib.reload(meshlint)
    importlib.reload(mextrude)
    importlib.reload(mtbrush)
    importlib.reload(multiedit)
    importlib.reload(offsetedges)
    importlib.reload(snapshot)
    importlib.reload(unbevel)

    # DELETE #    
    importlib.reload(del_action)
    importlib.reload(del_all_scenes)
    importlib.reload(del_build_corner)
    importlib.reload(del_clear_all)
    importlib.reload(del_edgering)

    # IM-EXPORT #
    importlib.reload(io_export_selected)    

    # MIRATOOLS #
    importlib.reload(mi_color_manager)
    importlib.reload(mi_curve_guide)
    importlib.reload(mi_curve_main)
    importlib.reload(mi_curve_surfaces)
    importlib.reload(mi_curve_stretch)
    importlib.reload(mi_curve_test)
    importlib.reload(mi_deform)
    importlib.reload(mi_draw_extrude)
    importlib.reload(mi_inputs)
    importlib.reload(mi_linear_deformer)
    importlib.reload(mi_linear_widget)
    importlib.reload(mi_looptools)
    importlib.reload(mi_make_arc)
    importlib.reload(mi_noise)
    importlib.reload(mi_poly_loop)
    importlib.reload(mi_settings)
    importlib.reload(mi_utils_base)
    importlib.reload(mi_widget_curve)
    importlib.reload(mi_widget_linear_deform)
    importlib.reload(mi_widget_select)
    importlib.reload(mi_wrap_master)

    # MODIFIER #
    importlib.reload(mods)
    importlib.reload(mods_array)
    importlib.reload(mods_bevel)
    importlib.reload(mods_cast)
    importlib.reload(mods_copy)
    importlib.reload(mods_decimate)
    importlib.reload(mods_displace)
    importlib.reload(mods_display)
    importlib.reload(mods_easylattice)
    importlib.reload(mods_mirror)
    importlib.reload(mods_multires)
    importlib.reload(mods_remesh)
    importlib.reload(mods_remove)
    importlib.reload(mods_screw)
    importlib.reload(mods_sdeform)
    importlib.reload(mods_skin)
    importlib.reload(mods_smooth)
    importlib.reload(mods_solidifiy)
    importlib.reload(mods_subsurf)
    importlib.reload(mods_sym) 
    importlib.reload(mods_symcut) 
    importlib.reload(mods_toall) 

    # ORIGIN #
    importlib.reload(origin_action)
    importlib.reload(origin_align)
    importlib.reload(origin_batch)
    importlib.reload(origin_bbox)
    importlib.reload(origin_center)
    importlib.reload(origin_distribute)
    importlib.reload(origin_modal)
    importlib.reload(origin_operators)
    importlib.reload(origin_zero)
    
    # PENCIL #
    importlib.reload(pencil_action)  

    # SELECTION #
    importlib.reload(select_action)
    importlib.reload(select_ktools)
    importlib.reload(select_meshorder)
    importlib.reload(select_surface)
    importlib.reload(select_topokit2)
    importlib.reload(select_vismaya)

    # SCULPT #  
    importlib.reload(sculpt_displace)
    importlib.reload(sculpt_decimate)
    importlib.reload(sculpt_dyntopo)
    importlib.reload(sculpt_edit)
    importlib.reload(sculpt_load)
    importlib.reload(sculpt_masks)
    importlib.reload(sculpt_quickset)
    importlib.reload(sculpt_tools)

    importlib.reload(ops_brush)

    
    # SURFACE CONSTRAINT #
    importlib.reload(MeshBrush)
    importlib.reload(PickSurfaceConstraint)
    importlib.reload(Shrinkwrap)
    importlib.reload(SmoothVertices)
    importlib.reload(ResizeMeshBrush)
    importlib.reload(StrokeMove)
    importlib.reload(StrokeSmooth)
    importlib.reload(SurfaceConstraintToolsPrefs)   

    # VISUALS #
    importlib.reload(autowire)
    importlib.reload(delete)     
    importlib.reload(display)
    importlib.reload(fastnavi)
    importlib.reload(material)
    importlib.reload(matswitch)
    importlib.reload(normals)
    importlib.reload(normals_transfer)
    importlib.reload(normals_weighted)
    importlib.reload(opengl)
    importlib.reload(orphan) 
    importlib.reload(silhouette)


else:

    # # 
    from . import rsf_booltool  
    from . import rsf_reboot
    from . import rsf_snapline
    from . import keymap_ops


    # ALIGN #                              
    from .ops_align import align_mirror            
    from .ops_align import align_modifier   
    from .ops_align import align_normal   
    from .ops_align import align_orientation   
    from .ops_align import align_pivot        
    from .ops_align import align_snap_set         
    from .ops_align import align_snap_to                
    from .ops_align import align_transform     
    from .ops_align import align_widget  

    from .ops_align.align_auxiliary import advanced  
    from .ops_align.align_auxiliary import center_cursor  
    from .ops_align.align_auxiliary import con_rotation  
    from .ops_align.align_auxiliary import distribute
    from .ops_align.align_auxiliary import distribute_obj 
    from .ops_align.align_auxiliary import face_to_face   
    from .ops_align.align_auxiliary import oned_scripts  
    from .ops_align.align_auxiliary import snap_offset 
    from .ops_align.align_auxiliary import shrinksmooth
    from .ops_align.align_auxiliary import smoothdeform
    from .ops_align.align_auxiliary import straighten 
    from .ops_align.align_auxiliary import to_ground                                        
    from .ops_align.align_auxiliary import xyspread       

    # BOUNDING #
    from .ops_bounding import boxes    
    from .ops_bounding import copy    
    from .ops_bounding import origin    
    from .ops_bounding import recoplanar    
    from .ops_bounding import relocal    
    from .ops_bounding import rename    
    from .ops_bounding import selection    
    from .ops_bounding import spheres    
    from .ops_bounding import tubes    

    # BOOLEAN #
    from .ops_boolean import bool_action         
    from .ops_boolean import bool_bevel        
    from .ops_boolean import bool_boolean2d                                        
    from .ops_boolean import bool_carver    

    # COPY #
    from .ops_copy import copy_action         
    from .ops_copy import copy_attributes                          
    from .ops_copy import copy_dupliset              
    from .ops_copy import copy_fpath           
    from .ops_copy import copy_mifthcloning                
    from .ops_copy import copy_multilinked       
    from .ops_copy import copy_origin       
    from .ops_copy import copy_replicator 
    from .ops_copy import copy_to_all 
    from .ops_copy import copy_to_cursor 
    from .ops_copy import copy_to_meshtarget 

    # CURVE #
    from .ops_curve import curve_actions
    from .ops_curve import curve_convert
    from .ops_curve import curve_copies
    from .ops_curve import curve_extend
    from .ops_curve import curve_merged
    from .ops_curve import curve_start
    from .ops_curve import curve_overlay
    from .ops_curve import curve_outline
    from .ops_curve import curve_simplify
    from .ops_curve import curve_split
    from .ops_curve import curve_trim
    from .ops_curve import curve_remove
    from .ops_curve import curve_draw
    
    from .ops_curve import add_curves      
    from .ops_curve import add_galore      
    from .ops_curve import add_taper      
    from .ops_curve import add_taper_bevel          
    from .ops_curve import add_tube_edge      
    from .ops_curve import add_tube_face  

    from .ops_curve.curvetools import Properties
    from .ops_curve.curvetools import Operators
    from .ops_curve.curvetools import auto_loft 

    from .ops_curve.curvecad import __init__
    from .ops_curve.curvecad import internal
    from .ops_curve.curvecad import svg_export 

    # DELETE #    
    from .ops_delete import del_action
    from .ops_delete import del_all_scenes
    from .ops_delete import del_build_corner
    from .ops_delete import del_clear_all
    from .ops_delete import del_edgering
          
    # EDITING #    
    from .ops_editing import bsurfaces
    from .ops_editing import closer 
    from .ops_editing import create 
    from .ops_editing import cutfaces 
    from .ops_editing import reextrude
    from .ops_editing import fastloop
    from .ops_editing import filletinset
    from .ops_editing import filletplus
    from .ops_editing import looptools
    from .ops_editing import meshcheck
    from .ops_editing import meshlint
    from .ops_editing import mextrude
    from .ops_editing import mtbrush
    from .ops_editing import multiedit
    from .ops_editing import offsetedges
    from .ops_editing import snapshot
    from .ops_editing import unbevel

    # IM-EXPORT #
    from .ops_io import io_export_selected  

    # MIRATOOLS #
    from . import mi_color_manager
    from . import mi_curve_guide
    from . import mi_curve_main
    from . import mi_curve_surfaces
    from . import mi_curve_stretch
    from . import mi_curve_test
    from . import mi_deform
    from . import mi_draw_extrude
    from . import mi_inputs
    from . import mi_linear_deformer
    from . import mi_linear_widget
    from . import mi_looptools
    from . import mi_make_arc    
    from . import mi_noise
    from . import mi_poly_loop
    from . import mi_settings
    from . import mi_utils_base
    from . import mi_widget_curve
    from . import mi_widget_linear_deform
    from . import mi_widget_select
    from . import mi_wrap_master

    # MODIFIER #
    from .ops_modifier import mods
    from .ops_modifier import mods_array                
    from .ops_modifier import mods_bevel         
    from .ops_modifier import mods_cast         
    from .ops_modifier import mods_copy         
    from .ops_modifier import mods_decimate         
    from .ops_modifier import mods_displace         
    from .ops_modifier import mods_display         
    from .ops_modifier import mods_easylattice         
    from .ops_modifier import mods_mirror            
    from .ops_modifier import mods_multires            
    from .ops_modifier import mods_remesh            
    from .ops_modifier import mods_remove            
    from .ops_modifier import mods_screw                             
    from .ops_modifier import mods_sdeform                              
    from .ops_modifier import mods_skin                     
    from .ops_modifier import mods_smooth                     
    from .ops_modifier import mods_solidifiy                     
    from .ops_modifier import mods_subsurf       
    from .ops_modifier import mods_sym   
    from .ops_modifier import mods_symcut   
    from .ops_modifier import mods_toall   

    # ORIGIN #
    from .ops_origin import origin_action         
    from .ops_origin import origin_align         
    from .ops_origin import origin_batch               
    from .ops_origin import origin_bbox               
    from .ops_origin import origin_center                 
    from .ops_origin import origin_distribute                 
    from .ops_origin import origin_modal         
    from .ops_origin import origin_operators                 
    from .ops_origin import origin_zero  
    
    # PENCIL #
    from .ops_pencil import pencil_action

    # SELECTION #
    from .ops_select import select_action                
    from .ops_select import select_ktools                
    from .ops_select import select_meshorder                         
    from .ops_select import select_surface                
    from .ops_select import select_topokit2                
    from .ops_select import select_vismaya  

    # SCULPT #
    from .ops_sculpt import sculpt_displace
    from .ops_sculpt import sculpt_decimate
    from .ops_sculpt import sculpt_dyntopo
    from .ops_sculpt import sculpt_edit
    from .ops_sculpt import sculpt_load
    from .ops_sculpt import sculpt_masks
    from .ops_sculpt import sculpt_quickset
    from .ops_sculpt import sculpt_tools

    from .ops_brushes import ops_brush

    # SURFACE CONSTRAINT #
    from .ops_sfc import MeshBrush
    from .ops_sfc import PickSurfaceConstraint
    from .ops_sfc import Shrinkwrap
    from .ops_sfc import SmoothVertices    
    from .ops_sfc.internal import ResizeMeshBrush
    from .ops_sfc.internal import StrokeMove
    from .ops_sfc.internal import StrokeSmooth
    from .preferences import SurfaceConstraintToolsPrefs

    # VISUALS #
    from .ops_visuals import autowire
    from .ops_visuals import delete   
    from .ops_visuals import display
    from .ops_visuals import fastnavi
    from .ops_visuals import material
    from .ops_visuals import matswitch
    from .ops_visuals import normals
    from .ops_visuals import normals_transfer
    from .ops_visuals import normals_weighted
    from .ops_visuals import opengl    
    from .ops_visuals import orphan  
    from .ops_visuals import silhouette

    # LOAD MAPS #
    from .rsf_uimap               import*
    from .keymap_align            import*
    from .keymap_boolean          import*
    from .keymap_delete           import*
    from .keymap_editing          import*
    from .keymap_origin           import*
    from .keymap_relax            import*
    from .keymap_resurface        import*
    from .keymap_sculpt           import*
    from .keymap_selection        import*
    from .keymap_submenus         import*
    from .ops_editing.meshcheck   import*



###############################

# LOAD MODULS #

import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup



# REGISTRY TOOLS # 
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass 



# ADDON PREFERNCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
 
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('tools',      "Tools",      "Tools"),
               ('keymap',     "Keymap",     "Keymap"), 
               ('menus',       "Menus",      "Menus"), 
               ('snapline',   "Snapline",   "Snapline"), 
               ('carver',     "Caver",      "Carver"), 
               ('url',        "URLs",       "URLs")),
               default='info')
      
    #----------------------------
 
 
    # KEY INPUT #   
      
    key_inputs = EnumProperty(
        name = "Key Inputs Style",
        items = (('Blender', 'Blender', ''),
                ('Maya', 'Maya', '')
                ),
        default = 'Blender')


    #----------------------------

    
    # PANEL RESURFACE  #  
           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_position)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)


    #----------------------------


    # MENUS #  
        
    tab_menu_resurface = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_resurface)


    tab_menu_align = EnumProperty(
        name = 'Pie Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on',  'enable menu'),
               ('pie',  'Pie on',   'enable pie menu'),
               ('off',  'Menu off', 'disable menus')),
               default='off', update = update_menu_align)
       

    tab_menu_boolean = EnumProperty(
        name = 'Boolean Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_boolean)               


    tab_menu_closer = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_closer)


    tab_menu_delete = EnumProperty(
        name = 'Boolean Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_delete) 
 

    tab_menu_vert_edit = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_vert_edit)


    tab_menu_edge_edit = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_edge_edit)
               

    tab_menu_edge_visual = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_edge_visual)               


    tab_menu_face_edit = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_face_edit)


    tab_menu_face_visual = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_face_visual)


    tab_menu_special_edit = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_special_edit)

               
    tab_menu_origin = EnumProperty(
        name = 'Origin Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_origin)

    
    tab_menu_relax = EnumProperty(
        name = 'Relax Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_relax)


    tab_menu_selection = EnumProperty(
        name = 'Selection Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_selection) 

               
    tab_menu_submenus = EnumProperty(
        name = 'Submenus',
        description = 'add submenus to default blender menus',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_submenus)               


    #----------------------------


    # UI #
    expand_panel_tools = bpy.props.BoolProperty(name="Expand", description="Expand, to display the settings", default=False)          
    
    tab_add_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Add on', 'enable tools in panel'), ('off', 'Add off', 'disable tools in panel')), default='on', update = update_display_tools)
    
    tab_title_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)
    
    tab_pivot_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Pivots on', 'enable tools in panel'), ('off', 'Pivots off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_create_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Insert on', 'enable tools in panel'), ('off', 'Insert off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_align_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Align on', 'enable tools in panel'), ('off', 'Align off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_boolean_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Boolean on', 'enable tools in panel'), ('off', 'Boolean off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_copy_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Copy on', 'enable tools in panel'), ('off', 'Copy off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_convert_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Convert on', 'enable tools in panel'), ('off', 'Convert off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_origin_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Origin on', 'enable tools in panel'), ('off', 'Origin off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_snapshot_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapShot on', 'enable tools in panel'), ('off', 'SnapShot off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_edit_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'EditTools on', 'enable tools in panel'), ('off', 'EditTools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_symdim_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SymDim on', 'enable tools in panel'), ('off', 'PivotTools off', 'disable tools in panel')), default='on', update = update_display_tools)
 
    tab_pencil_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Pencil on', 'enable tools in panel'), ('off', 'Pencil off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_spacing_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Spacing on', 'enable tools in panel'), ('off', 'Spacing off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_biped_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Biped on', 'enable tools in panel'), ('off', 'Biped off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_recoplanar_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ReCoPlanar on', 'enable tools in panel'), ('off', 'ReCoPlanar off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_relax_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Relax on', 'enable tools in panel'), ('off', 'Relax off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_check_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Check on', 'enable tools in panel'), ('off', 'Check off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_modifier_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Modifier on', 'enable tools in panel'), ('off', 'Modifier off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_transform_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Transform on', 'enable tools in panel'), ('off', 'Transform off', 'disable tools in panel')), default='on', update = update_display_tools)      
      
    tab_visual_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Visuals on', 'enable tools in panel'), ('off', 'Visuals off', 'disable tools in panel')), default='on', update = update_display_tools)
      
    tab_history_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'Historyoff', 'disable tools in panel')), default='on', update = update_display_tools)
  

    # CURVETOOLS 2#
    tab_curve_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'CurveTools on', 'enable tools in panel'), ('off', 'CurveTools off', 'disable tools in panel')), default='on', update = update_display_tools)


    # MIRATOOLS #
    tab_miratools_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'MiraTools on', 'enable tools in panel'), ('off', 'MiraTools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_mirawrap_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mira Wrap on', 'enable tools in panel'), ('off', 'Mira Wrap off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_miraguide_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mira Guide on', 'enable tools in panel'), ('off', 'Mira Guide off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_mirastretch_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mira Stretch on', 'enable tools in panel'), ('off', 'Mira Stretch off', 'disable tools in panel')), default='on', update = update_display_tools)
                  

    # SURFACE CONSTRAINT #
    tab_surface_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Surface Constraint on', 'enable tools in panel'), ('off', 'Surface Constraint off', 'disable tools in panel')), default='on', update = update_display_tools)


    # CUTSOM #
    tab_custom_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Custom on', 'enable tools in panel'), ('off', 'Custom off', 'disable tools in panel')), default='on', update = update_display_tools)


    #----------------------------


    # PREFERNCES SCULPT #         
    
    tab_location_sculpt = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_sculpt)

    tools_category_sculpt = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = '(WIP)', update = update_panel_sculpt)


    tab_brush_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SculptBrush on', 'change settings with rightmouse button'), ('off', 'SculptBrush off', 'select with rightmouse button')), default='on', update = update_display_tools)

    tab_brush_quickset = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'QuickBrush on', 'change settings with rightmouse button'), ('off', 'QuickBrush off', 'select with rightmouse button')), default='on', update = update_display_tools)

    tab_sculpt_edit = EnumProperty(name = 'Display Tools', description = 'on / off',
                 items=(('on', 'SculptEdit on', 'enable tools in panel'), ('off', 'SculptEdit off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_sculpt_mask = EnumProperty(name = 'Display Tools', description = 'on / off',
                 items=(('on', 'SculptMask on', 'enable tools in panel'), ('off', 'SculptMask off', 'disable tools in panel')), default='on', update = update_display_tools)

 
    tab_modsculpt_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Modifier on', 'enable tools in panel'), ('off', 'Modifier off', 'disable tools in panel')), default='on', update = update_display_tools)


    #----------------------------


    # PREFERNCES BOOELAN #
    
    make_vertex_groups = bpy.props.BoolProperty(name="Make Vertex Groups", default=False, description="When Apply a Brush to de Object it will create a new vertex group of the new faces" )
    make_boundary = bpy.props.BoolProperty(name="Make Boundary", default=False, description="When Apply a Brush to de Object it will create a new vertex group of the bondary boolean area")
    use_wire = bpy.props.BoolProperty(name="Use Bmesh", default=False, description="Use The Wireframe Instead Of Boolean")
   
    tab_direct_keys = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Direct Boolean on', 'enable tools'), 
                         ('off', 'Direct Boolean off', 'disable tools')), 
                         default='on', update = update_display_tools)

    tab_brush_keys = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Brush Boolean on', 'enable tools'), 
                         ('off', 'Brush Boolean off', 'disable tools')), 
                         default='on', update = update_display_tools)

    tab_brush_fast = EnumProperty(name = 'Display Tools', description="Replace the Transform HotKeys (G,R,S) for a custom version that can optimize the visualization of Brushes",
                  items=(('on', 'Fast Transformations on', 'enable tools'), 
                         ('off', 'Fast Transformations off', 'disable tools')), 
                         default='off', update = update_display_tools)                        

    tab_custom_sculpt_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Custom on', 'enable tools in panel'), ('off', 'Custom off', 'disable tools in panel')), default='on', update = update_display_tools)


    #----------------------------


    # PREFERNCES SURFACE CONSTRAINT #
    
    mesh_brush = bpy.props.PointerProperty(type = MeshBrushProps) 
    shrinkwrap = bpy.props.PointerProperty(type = ShrinkwrapProps)
    smooth_vertices = bpy.props.PointerProperty(type = SmoothVerticesProps)
    surface_constraint = bpy.props.PointerProperty(type = SurfaceConstraintProps)


    tab_surface_ui = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Surface Constraint on', 'enable tools in panel'), ('off', 'Surface Constraint off', 'disable tools in panel')), default='on', update = update_display_tools)


    #----------------------------


    # PREFERNCES SNAPLINE #
    
    expand_snap_settings = bpy.props.BoolProperty(name="Expand", description="Expand, to display the settings", default=False)      

    intersect = bpy.props.BoolProperty(name="Intersect", description="intersects created line with the existing edges, even if the lines do not intersect.", default=True)
    create_new_obj = bpy.props.BoolProperty(name="Create a new object", description="If have not a active object, or the active object is not in edit mode, it creates a new object.", default=False)
    create_face = bpy.props.BoolProperty(name="Create faces", description="Create faces defined by enclosed edges.", default=False)
    outer_verts = bpy.props.BoolProperty(name="Snap to outer vertices", description="The vertices of the objects are not activated also snapped.", default=True)      
    increments_grid = bpy.props.BoolProperty(name="Increments of Grid", description="Snap to increments of grid", default=False)
    incremental = bpy.props.FloatProperty(name="Incremental", description="Snap in defined increments", default=0, min=0, step=1, precision=3)
    relative_scale = bpy.props.FloatProperty(name="Relative Scale", description="Value that divides the global scale.", default=1, min=0, step=1, precision=3)

    out_color = bpy.props.FloatVectorProperty(name="OUT", default=(0.0, 0.0, 0.0, 0.5), size=4, subtype="COLOR", min=0, max=1)
    face_color = bpy.props.FloatVectorProperty(name="FACE", default=(1.0, 0.8, 0.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    edge_color = bpy.props.FloatVectorProperty(name="EDGE", default=(0.0, 0.8, 1.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    vert_color = bpy.props.FloatVectorProperty(name="VERT", default=(1.0, 0.5, 0.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    center_color = bpy.props.FloatVectorProperty(name="CENTER", default=(1.0, 0.0, 1.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    perpendicular_color = bpy.props.FloatVectorProperty(name="PERPENDICULAR", default=(0.1, 0.5, 0.5, 1.0), size=4, subtype="COLOR", min=0, max=1)
    constrain_shift_color = bpy.props.FloatVectorProperty(name="SHIFT CONSTRAIN", default=(0.8, 0.5, 0.4, 1.0), size=4, subtype="COLOR", min=0, max=1)


    #----------------------------


    # PREFERNCES CARVER #
    
    Enable_Tab_01 = BoolProperty(name="Info", description="Some general information and settings about the add-on", default=False)
    Enable_Tab_02 = BoolProperty(name="Hotkeys",  description="List of the shortcuts used during carving", default=False )
    bpy.types.Scene.Key_Create = StringProperty(name="Object creation", description="Object creation",  maxlen=1, default="C")
    bpy.types.Scene.Key_Update = StringProperty(name="Auto Bevel Update", description="Auto Bevel Update", maxlen=1, default="A")
    bpy.types.Scene.Key_Bool = StringProperty(name="Boolean type", description="Boolean operation type", maxlen=1, default="T")
    bpy.types.Scene.Key_Brush = StringProperty(name="Brush Mode", description="Brush Mode", maxlen=1, default="B")
    bpy.types.Scene.Key_Help = StringProperty(name="Help display",  description="Help display", maxlen=1, default="H")
    bpy.types.Scene.Key_Instant = StringProperty(name="Instantiate",  description="Instantiate object", maxlen=1, default="I")
    bpy.types.Scene.Key_Close = StringProperty(name="Close polygonal shape", description="Close polygonal shape", maxlen=1, default="X")
    bpy.types.Scene.Key_Apply = StringProperty( name="Apply operation", description="Apply operation", maxlen=1, default="Q")
    bpy.types.Scene.Key_Scale = StringProperty(name="Scale object", description="Scale object", maxlen=1, default="S")
    bpy.types.Scene.Key_Gapy = StringProperty(name="Gap rows", description="Scale gap between columns", maxlen=1, default="J")
    bpy.types.Scene.Key_Gapx = StringProperty(name="Gap columns", description="Scale gap between columns", maxlen=1, default="U")
    bpy.types.Scene.Key_Depth = StringProperty(name="Depth", description="Cursor depth or solidify pattern", maxlen=1, default="D")
    bpy.types.Scene.Key_BrushDepth = StringProperty(name="Brush Depth", description="Brush depth", maxlen=1, default="C")
    bpy.types.Scene.Key_Subadd = StringProperty(name="Add subdivision", description="Add subdivision", maxlen=1, default="X")
    bpy.types.Scene.Key_Subrem = StringProperty( name="Remove subdivision", description="Remove subdivision", maxlen=1, default="W")
    bpy.types.Scene.Key_Randrot = StringProperty(name="Random rotation", description="Random rotation", maxlen=1, default="R")
    bpy.types.Scene.Key_Solver = StringProperty(name="Solver", description="Switch between Carve and BMesh Boolean solverdepending on a specific use case", maxlen=1, default="V")
    bpy.types.Scene.ProfilePrefix = StringProperty(name="Profile prefix", description="Prefix to look for profiles with", default="Carver_Profile-")
    bpy.types.Scene.CarverSolver = EnumProperty(name="Boolean Solver", description="Boolean solver to use by default\n", default="CARVE",
                items=(
                ('CARVE', 'Carve', "Carve solver, as the legacy one, can handle basic coplanar but can often fail with non-closed geometry"),
                ('BMESH', 'BMesh', "BMesh solver is faster, but cannot handle coplanar and self-intersecting geometry")
                ))


    #----------------------------


    # DRAW RESURFACE PREFERNCES #
    
    def draw(self, context):
        layout = self.layout
        icons = load_icons()         

        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            row = layout.row()
            row.label(text="T+ ReSurface! (WIP)")

            row = layout.row()
            row.label(text="Tool collection for retopology and sculpting adventure")
           


        # LOCATION #
        if self.prefs_tabs == 'location':
         
            box = layout.box().column(1)

            row = box.row()
            row.label("Panel: ReSurface")
            
            row = box.row()
            row.prop(self, 'tab_location', expand=True)

            row = box.row()
            if self.tab_location == 'tools':
                row.prop(self, "tools_category")

            box.separator()

            row = box.row()
            row.label("Panel: Sculpt")
            
            row = box.row()
            row.prop(self, 'tab_location_sculpt', expand=True)
            
            row = box.row()        
            if self.tab_location_sculpt == 'tools':
                row.prop(self, "tools_category_sculpt")

            box.separator()


        #Tools
        if self.prefs_tabs == 'tools':
          

            box = layout.box().column(1)

            row = box.row()
            row.label("Panel Tools", icon ="INFO")            

            row = box.column_flow(4)                                       
            row.prop(self, 'tab_add_ui', expand=True)                                       
            row.prop(self, 'tab_title_ui', expand=True)                                       
            row.prop(self, 'tab_pivot_ui', expand=True)                                       
            row.prop(self, 'tab_create_ui', expand=True)                                       
            row.prop(self, 'tab_origin_ui', expand=True)                                       
            row.prop(self, 'tab_surface_ui', expand=True)
            row.prop(self, 'tab_snapshot_ui', expand=True)
            row.prop(self, 'tab_boolean_ui', expand=True)
            row.prop(self, 'tab_align_ui', expand=True)
            row.prop(self, 'tab_symdim_ui', expand=True)
            row.prop(self, 'tab_copy_ui', expand=True)
            row.prop(self, 'tab_edit_ui', expand=True)
            row.prop(self, 'tab_mirastretch_ui', expand=True)
            row.prop(self, 'tab_miraguide_ui', expand=True)                        
            row.prop(self, 'tab_pencil_ui', expand=True)
            row.prop(self, 'tab_spacing_ui', expand=True)
            row.prop(self, 'tab_relax_ui', expand=True)
            row.prop(self, 'tab_check_ui', expand=True)     
            row.prop(self, 'tab_mirawrap_ui', expand=True)        
            row.prop(self, 'tab_biped_ui', expand=True)          
            row.prop(self, 'tab_recoplanar_ui', expand=True)          
            row.prop(self, 'tab_transform_ui', expand=True)          
            row.prop(self, 'tab_custom_ui', expand=True)
            row.prop(self, 'tab_convert_ui', expand=True)
            row.prop(self, 'tab_miratools_ui', expand=True)
            row.prop(self, 'tab_modifier_ui', expand=True)
            row.prop(self, 'tab_visual_ui', expand=True)          
            row.prop(self, 'tab_history_ui', expand=True)
             
            row.prop(self, 'tab_brush_quickset', expand=True) 
            row.prop(self, 'tab_sculpt_edit', expand=True) 
            row.prop(self, 'tab_sculpt_mask', expand=True) 
        
            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 



        # KEYMAP #
        if self.prefs_tabs == 'keymap':


            # BOOLEAN #
            box = layout.box().column(1)
             
            row = box.row(1)              
            row.label("Direct Boolean:", icon ="INFO") 
            row.prop(self, 'tab_direct_keys', expand=True)
                                   
            box.separator()
            box.separator()

            row = box.column_flow(2)              
            
            # column 1
            row.label("Objectmode:")
            
            button_boolean_union = icons.get("icon_boolean_union")            
            row.label("Direct_Union: [CTR+NUMPAD PLUS]", icon_value=button_boolean_union.icon_id)
            
            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.label("Intersect: [CTRL+NUMPAD ASTERIX]", icon_value=button_boolean_intersect.icon_id)

            button_boolean_difference = icons.get("icon_boolean_difference")
            row.label("Difference: [CTRL+NUMPAD MINUS]", icon_value=button_boolean_difference.icon_id)

            button_boolean_rebool = icons.get("icon_boolean_rebool")
            row.label("SliceRebool: [CTRL+NUMPAD_SLASH]", icon_value=button_boolean_rebool.icon_id)

            # column 2
            row.label("Editmode:")
     
            button_boolean_union = icons.get("icon_boolean_union")
            row.label("Union: [SHIFT+NUMPAD _PLUS]", icon_value=button_boolean_union.icon_id)
            
            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.label("Intersect: [SHIFT+NUMPAD_ASTERIX]", icon_value=button_boolean_intersect.icon_id)
            
            button_boolean_difference = icons.get("icon_boolean_difference")
            row.label("Difference: [SHIFT+NUMPAD_MINUS]", icon_value=button_boolean_difference.icon_id)
            
            button_boolean_rebool = icons.get("icon_boolean_rebool")
            row.label("SliceRebool: [SHIFT+NUMPAD_SLASH]", icon_value=button_boolean_rebool.icon_id)
       
            box.separator()



            # BOOLEAN #
            box = layout.box().column(1)

            row = box.row(1)              
            row.label("Brush Boolean", icon ="INFO") 
            row.prop(self, 'tab_brush_keys', expand=True)
                                   
            box.separator()
            box.separator()

 
            # column 1
            row = box.column(1)               
            split = row.split(percentage=0.5)

            col = split.column()            
            button_boolean_union_brush = icons.get("icon_boolean_union_brush")
            col.label("BT-Union: [CTRL+SHIFT+NUMPAD PLUS]", icon_value=button_boolean_union_brush.icon_id)
            
            button_boolean_intersect_brush = icons.get("icon_boolean_intersect_brush")
            col.label("BT-Intersect: [CTRL+SHIFT+NUMPAD ASTERIX]", icon_value=button_boolean_intersect_brush.icon_id)
            
            button_boolean_difference_brush = icons.get("icon_boolean_difference_brush")
            col.label("BT-Difference: [CTRL+SHIFT+NUMPAD MINUS]", icon_value=button_boolean_difference_brush.icon_id)
            
            button_boolean_rebool_brush = icons.get("icon_boolean_rebool_brush")
            col.label("BT-SliceRebool: [CTRL+SHIFT+NUMPAD SLASH]", icon_value=button_boolean_rebool_brush.icon_id)
                      
            col.separator()

            col.label("Apply Brush: [CTRL+NUMPAD ENTER]", icon = 'MOD_LATTICE')
            col.label("Apply All: [CTRL+SHIFT+NUMPAD ENTER]", icon = 'MOD_LATTICE')

            
            # column 2
            split = split.split(percentage=0.5)
           
            col = split.column()              
            col.label("Experimental BoolTool Features:")
            
            col.separator()
            col.prop(self, 'tab_brush_fast')#, expand=True)                      
            col.prop(self, "use_wire", text="Use Wire Instead Of BBox")
         
            box.separator()
                
       

      
        # MENUS #
        if self.prefs_tabs == 'menus':

  
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Menu: [SHIFT+X]", icon ="COLLAPSEMENU") 

            row = box.row(1)          
            row.prop(self, 'tab_menu_resurface', expand=True)
                
            box.separator() 

            if self.tab_menu_resurface == 'off':
                row = box.row(1) 
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")

            box.separator()
            box.separator()
          
            # TIP #            
            row = box.row(1)             
            row.label(text="! For key change you can go also to > User Preferences > TAB: Input !", icon ="INFO")

            row = box.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. bool menu: shift x", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_ReSurface_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = box.row(1)             
            row.label(text="! Other way to change the default key is to edit the keymap script !", icon ="INFO")
             
            row = box.row(1) 
            row.operator("tp_ops.key_map_resurface", text = 'Open KeyMap (Text Editor)', icon ="TEXT")
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()  
            box.separator()  
            box.separator()  



            # ALIGN #  
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Align Menu: [CTRL+D] ", icon ="COLLAPSEMENU")                      
            row.prop(self, 'tab_menu_align', expand=True)
            row.operator("tp_ops.key_map_align", text = '', icon ="TEXT")            
        
            if self.tab_menu_align == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator() 



            # BOOLEAN #               
            row = box.row(1)  
            row.label("BoolMenu: [SHIFT+T]", icon ="COLLAPSEMENU")         
            row.prop(self, 'tab_menu_boolean', expand=True)
            row.operator("tp_ops.key_map_boolean", text = '', icon ="TEXT")
            
            if self.tab_menu_boolean == 'off':

                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator()

 
            # ORIGIN #     
            row = box.row(1)  
            row.label(" Menu: Origin [CTRL+D]", icon ="COLLAPSEMENU")          
            row.prop(self, 'tab_menu_origin', expand=True)
            row.operator("tp_ops.key_map_origin", text = '', icon ="TEXT")            
         
            if self.tab_menu_origin == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")
                
            box.separator()  
          

            # SELECTION #
            row = box.row(1)          
            row.label("Menu: Selection [ALT+Q]", icon ="COLLAPSEMENU")        
            row.prop(self, 'tab_menu_selection', expand=True)
            row.operator("tp_ops.key_map_selection", text = '', icon ="TEXT")            
            
            if self.tab_menu_selection == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot !", icon ="INFO")
           
            box.separator()

           
            ### EDITMODE MENUS ###
            box = layout.box().column(1)
            
            # VERTICES EDIT #
            row = box.row(1)  
            row.label("Menu: Vertices Edit [CTL+V]", icon ="COLLAPSEMENU")         
            row.prop(self, 'tab_menu_vert_edit', expand=True)
                        
            if self.tab_menu_vert_edit == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator()


            # EDGE EDIT #
            row = box.row(1)  
            row.label("Menu: Edge Edit [SHIFT+E]", icon ="COLLAPSEMENU")       
            row.prop(self, 'tab_menu_edge_edit', expand=True)  
                        
            if self.tab_menu_edge_edit == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator()


            # EDGE VISUAL #
            row = box.row(1)  
            row.label("Menu: Edge Visual [CTL+E]", icon ="COLLAPSEMENU")          
            row.prop(self, 'tab_menu_edge_visual', expand=True)
            
            if self.tab_menu_edge_visual == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator()


            # FACE EDIT #
            row = box.row(1)  
            row.label("Menu: Face Edit [SHIFT+F]", icon ="COLLAPSEMENU")        
            row.prop(self, 'tab_menu_face_edit', expand=True)
            
            if self.tab_menu_face_edit == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator()


            # FACE VISUAL #
            row = box.row(1)  
            row.label("Menu: Face Visual [CTL+F]", icon ="COLLAPSEMENU")        
            row.prop(self, 'tab_menu_face_visual', expand=True)
            
            if self.tab_menu_face_visual == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator()


            # SPECIAL EDIT #
            row = box.row(1)  
            row.label("Menu: Special Menu [W]", icon ="COLLAPSEMENU")       
            row.prop(self, 'tab_menu_special_edit', expand=True)
            
            if self.tab_menu_special_edit == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator()


            # CLOSER TO #
            row = box.row(1)  
            row.label("Menu: CloserTo [CTL+V]", icon ="COLLAPSEMENU") 
            row.operator("tp_ops.key_map_editing", text = '', icon ="TEXT")                       
            row.prop(self, 'tab_menu_closer', expand=True)    
         
            if self.tab_menu_closer == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            box.separator()



            # RELAX #             
            row = box.row(1)  
            row.label("Menu: Relax [CTRL+SHIFT+W]", icon ="COLLAPSEMENU")         
            row.prop(self, 'tab_menu_relax', expand=True)
            row.operator("tp_ops.key_map_relax", text = '', icon ="TEXT")
                        
            if self.tab_menu_relax == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")
    
            box.separator()



            # DELETE #
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Menu: Delete [X]", icon ="COLLAPSEMENU")        
            row.prop(self, 'tab_menu_delete', expand=True)
            row.operator("tp_ops.key_map_delete", text = '', icon ="TEXT")

            if self.tab_menu_delete == 'off':
                row = box.row(1) 
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")

            else:            
                row = box.column(1)             
                row.label(text="! To use the delete menu > go to TAB: Input !", icon ="INFO")
                row.label(text="! Change search to key-bindig and insert the hotkey: [x] !", icon ="BLANK1")
                row.label(text="! Now disable all the delete menus you want to replace !", icon ="BLANK1")
                row.label(text="! Example for editmode replace: disable Call Menu (VIEW3D_MT_edit_mesh_delete) ", icon ="BLANK1")
                
            box.separator()    








        # SNAPLINE #
        if self.prefs_tabs == 'snapline':

            box = layout.box().column(1)

            row = box.row()
            row.label("Snapline Colors", icon ="LINE_DATA")    
            row.prop(self, "out_color")

            split = box.split()

            col = split.column()
            col.prop(self, "constrain_shift_color")
        
            col = split.column()
            col.prop(self, "face_color")
          
            col = split.column()
            col.prop(self, "edge_color")        
          
            col = row.column()

            col = split.column()
            col.prop(self, "vert_color")
          
            col = split.column()
            col.prop(self, "center_color")
          
            col = split.column()
            col.prop(self, "perpendicular_color")

            row = box.row()
           
            col.separator()
           
            col = row.column()
            
            col.prop(self, "incremental")
            col.prop(self, "increments_grid")
         
            if self.increments_grid:
                col.prop(self, "relative_scale")

            col.prop(self, "outer_verts")
            row.separator()

            col = row.column()
            col.label(text="Line Tool:")
            col.prop(self, "intersect")
            col.prop(self, "create_face")
            col.prop(self, "create_new_obj")



        # CARVER #
        if self.prefs_tabs == 'carver':
           
            scene = context.scene
          
            box = layout.box().column(1)

            row = box.row()
            button_draw_carver = icons.get("icon_draw_carver")
            row.label("CARVER", icon_value=button_draw_carver.icon_id) 

            row = box.column()                        
            row.prop(self, "Enable_Tab_01", text="Info and Settings", icon="QUESTION")
            if self.Enable_Tab_01:
               
                row.label(text="Carver Operator:", icon="LAYER_ACTIVE")
                row.label(text="Select a mesh to carve", icon="LAYER_USED")
                row.label(text="Run Carver (HotKey or Panel)", icon="LAYER_USED")
                row.label(text="To finish press [ESC] or [RIGHT CLICK]", icon="LAYER_USED")
                
                row.separator()                
                                                
                row.prop(scene, "ProfilePrefix", text="Profile prefix")
                row.prop(scene, "CarverSolver", text="Solver")

                box.separator()             
            
            box.separator()             
 
            row = box.column()
            row.prop(self, "Enable_Tab_02", text="Keys", icon="KEYINGSET")
            if self.Enable_Tab_02:
                
                split = box.split()
                
                col = split.column()
                col.label("Object Creation:")
                col.prop(scene, "Key_Create", text="")
                col.label("Auto bevel update:")
                col.prop(scene, "Key_Update", text="")
                col.label("Boolean operation type:")
                col.prop(scene, "Key_Bool", text="")
                col.label("Solver:")
                col.prop(scene, "Key_Solver", text="")

                col = split.column()
                col.label("Brush Mode:")
                col.prop(scene, "Key_Brush", text="")
                col.label("Help display:")
                col.prop(scene, "Key_Help", text="")
                col.label("Instantiate object:")
                col.prop(scene, "Key_Instant", text="")
                col.label("Brush Depth:")
                col.prop(scene, "Key_BrushDepth", text="")

                col = split.column()
                col.label("Close polygonal shape:")
                col.prop(scene, "Key_Close", text="")
                col.label("Apply operation:")
                col.prop(scene, "Key_Apply", text="")
                col.label("Scale object:")
                col.prop(scene, "Key_Scale", text="")

                col = split.column()
                col.label("Gap rows:")
                col.prop(scene, "Key_Gapy", text="")
                col.label("Gap columns:")
                col.prop(scene, "Key_Gapx", text="")
                col.label("Depth / Solidify:")
                col.prop(scene, "Key_Depth", text="")

                col = split.column()
                col.label("Subdiv add:")
                col.prop(scene, "Key_Subadd", text="")
                col.label("Subdiv Remove:")
                col.prop(scene, "Key_Subrem", text="")
                col.label("Random rotation:")
                col.prop(scene, "Key_Randrot", text="")




        # WEB #
        if self.prefs_tabs == 'url':
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = '', icon = 'INFO').url = "#"            







# PROPERTY MENU: MIRATOOLS #
class Dropdown_Batch_MiraToolProps(bpy.types.PropertyGroup):

    display_batch_surface = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_curves = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)
    display_batch_deform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_extrude = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_arc = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_settings = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)


# PROPERTY TOOLS: MIRATOOLS #
class DropdownMiraToolProps(bpy.types.PropertyGroup):

    display_miraarc = bpy.props.BoolProperty(name="Make Arc", description="UI Make Arc Tools", default=False)
    display_mirastretch = bpy.props.BoolProperty(name="Curve Stretch", description="UI Curve Stretch Tools", default=False)
    display_mirasface = bpy.props.BoolProperty(name="Curve Surface", description="UI Curve Surface Tools", default=False)
    display_miraguide = bpy.props.BoolProperty(name="Curve Guide", description="UI Curve Guide Tools", default=False)
    display_miramodify = bpy.props.BoolProperty(name="Modify Tools", description="UI Modify Tools", default=False)
    display_miradeform = bpy.props.BoolProperty(name="Deform Tools", description="UI Deform Tools", default=False)
    display_miraextrude = bpy.props.BoolProperty(name="Draw Extrude", description="UI Draw Extrude", default=False)
    display_mirasettings = bpy.props.BoolProperty(name="Settings", description="UI Settings", default=False)
    display_mira_wrap = bpy.props.BoolProperty(name="WrapTools", description="UI WrapTools", default=False)
 

# PROPERTY DISPLAY: VISUALS #
class Dropdown_TP_Visual_Props(bpy.types.PropertyGroup):

    display_world_set = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_aoccl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_grid = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_fastnav = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_more_mat = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_more = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_lens = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_navi = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    mat_mode = bpy.props.StringProperty(default="")
    index_count_sw = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)     
    mat_switch = bpy.props.EnumProperty(
                              items = [("tp_mat_00", "Light", "", 1),
                                       ("tp_mat_01", "Darken",  "", 2)],
                                       name = "",
                                       default = "tp_mat_00",  
                                       description="material index switch") 

    new_swatch = FloatVectorProperty(name = "Color", default=[0.0,1.0,1.0], min = 0, max = 1,  subtype='COLOR')
    index_count = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)  
    matrandom = bpy.props.BoolProperty(name="ID-Switch / ID-Random", description="enable random material", default=False)  


# PROPERTY TOOLS: VISUALS #
class Display_Tools_Props(bpy.types.PropertyGroup):
    
    Delay = BoolProperty(default=False, description="Activate delay return to normal viewport mode")
    DelayTime = IntProperty(default=30, min=0, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    DelayTimeGlobal = IntProperty(default=30, min=1, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    EditActive = BoolProperty(default=True, description="Activate for fast navigate in edit mode too")
    FastNavigateStop = BoolProperty(name="Fast Navigate Stop", description="Stop fast navigate mode", default=False)    
    ShowParticles = BoolProperty(name="Show Particles", description="Show or hide particles on fast navigate mode", default=True)  
    ParticlesPercentageDisplay = IntProperty(name="Display", default=25, min=0, max=100, soft_min=0, soft_max=100, subtype='FACTOR', description="Display only a percentage of particles")
    InitialParticles = IntProperty( name="Count for initial particle setting before entering fast navigate", description="Display a percentage value of particles", default=100, min=0, max=100, soft_min=0, soft_max=100)
    ScreenStart = IntProperty(name="Left Limit", default=0, min=0, max=1024, subtype='PIXEL', description="Limit the screen active area width from the left side\n changed values will take effect on the next run")
    ScreenEnd = IntProperty( name="Right Limit", default=0, min=0, max=1024, subtype='PIXEL', description="Limit the screen active area width from the right side\n changed values will take effect on the next run")
    FastMode = EnumProperty(items=[('WIREFRAME', 'Wireframe', 'Wireframe display'), ('BOUNDBOX', 'Bounding Box', 'Bounding Box display')], name="Fast")
    OriginalMode = EnumProperty(items=[('TEXTURED', 'Texture', 'Texture display mode'), ('SOLID', 'Solid', 'Solid display mode')], name="Normal", default='SOLID')

    WT_handler_enable = BoolProperty(default=False)
    WT_handler_previous_object = StringProperty(default="")


# PROPERTY DELETE: VISUALS #
class Orphan_Tools_Props(bpy.types.PropertyGroup):
   
    mod_list = bpy.props.EnumProperty(
                       items = [tuple(["meshes"]*3),        tuple(["armatures"]*3), 
                                tuple(["cameras"]*3),       tuple(["curves"]*3),
                                tuple(["fonts"]*3),         tuple(["grease_pencil"]*3),
                                tuple(["groups"]*3),        tuple(["images"]*3),
                                tuple(["lamps"]*3),         tuple(["lattices"]*3),
                                tuple(["libraries"]*3),     tuple(["materials"]*3),
                                tuple(["actions"]*3),       tuple(["metaballs"]*3),
                                tuple(["node_groups"]*3),   tuple(["objects"]*3),
                                tuple(["sounds"]*3),        tuple(["texts"]*3), 
                                tuple(["textures"]*3),      tuple(["speakers"]*3)],
                                name = "",
                                default = "meshes", 
                                description="Target: Module choice made for orphan deletion")




# PROPS FOR PANEL: BOUNDING #
class Dropdown_BBox_Panel_Props(bpy.types.PropertyGroup):

    ### BOUNDING CUBE ###
    tp_geom_box = bpy.props.EnumProperty(
        items=[("tp_bb1"    ,"Grid"   ,"add grid plane"  ),
               ("tp_bb2"    ,"Cube"    ,"add a cube"     )],
               name = "ObjectType",
               default = "tp_bb2",    
               description = "choose objecttype")

    # GRID #
    subX = bpy.props.IntProperty(name="X Subdiv", description="set vertices value",  min=2, max=100, default=0, step=1)
    subY = bpy.props.IntProperty(name="Y Subdiv", description="set vertices value",  min=2, max=100, default=0, step=1)
    subR = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)            

    bgrid_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bgrid_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bgrid_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CUBE #
    scale = FloatVectorProperty(name="scale", default=(1.0, 1.0, 1.0), subtype='TRANSLATION', description="scaling" )
    scale_all = FloatProperty(name="Scale XYZ",  default=1.0, min=0.00, max=100, description="xyz scaling" )
    rotation = FloatVectorProperty(name="Rotation", subtype='EULER')

    bcube_rad = FloatProperty(name="Radius",  default=1.0, min=0.01, max=100, description="xyz scaling")

    bcube_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcube_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcube_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # generic transform props
    view_align = BoolProperty(name="Align to View", default=False)
    location = FloatVectorProperty(name="Location", subtype='TRANSLATION')
    rotation = FloatVectorProperty(name="Rotation",subtype='EULER')
    layers = BoolVectorProperty(name="Layers", size=20, subtype='LAYER', options={'HIDDEN', 'SKIP_SAVE'}) 
            
    # TOOLS #
    box_subdiv_use = bpy.props.BoolProperty(name="Subdivide",  description="activate subdivide", default=False) 
    box_subdiv = bpy.props.IntProperty(name="Loops", description="How many?", default=1, min=0, max=20, step=1)                   
    box_subdiv_smooth = bpy.props.FloatProperty(name="Smooth",  description="smooth subdivide", default=0.0, min=0.0, max=1.0)                    

    box_sphere_use = bpy.props.BoolProperty(name="Use Sphere",  description="activate to sphere", default=False) 
    box_sphere = bpy.props.FloatProperty(name="Sphere",  description="transform to sphere", default=1, min=0, max=1) 

    box_bevel_use = bpy.props.BoolProperty(name="Use Bevel",  description="activate bevel", default=False) 
    box_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    box_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1, min=0, max=1)
    box_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=1.5, min=0, max=100)
    box_verts_use = bpy.props.BoolProperty(name="Use Vertices",  description="activate vertex extrusion", default=False)     


    # BOX #
    box_dim = bpy.props.BoolProperty(name="Copy",  description="deactivate scale", default=True) 
    box_dim_apply = bpy.props.BoolProperty(name="Apply",  description="applyscale", default=True) 

    box_rota = bpy.props.BoolProperty(name="Copy Rotation",  description="deactivate copy rotation", default=True) 

    box_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )], 
               name = "MeshType",
               default = "tp_00",    
               description = "change meshtype")

    box_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    box_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    box_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    box_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)  

    # MATERIAL #
    box_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    box_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    box_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    box_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Widget Orientation",
               default = "tp_w0",    
               description = "widget orientation")



    ### BOUNDING CYLINDER ###
    tp_geom_tube = bpy.props.EnumProperty(
        items=[("tp_add_cyl"   ,"Tube"   ,"add cylinder" ),
               ("tp_add_cone"  ,"Cone"   ,"add cone"     ),
               ("tp_add_circ"  ,"Circle" ,"add circle"   ),
               ("tp_add_tor"  ,"Torus"  ,"add torus"  )],
               name = "ObjectType",
               default = "tp_add_cyl",    
               description = "change objecttype")

    tube_fill = bpy.props.EnumProperty(
        items=[("NOTHING"   ,"Nothing"  ,""   ),
               ("NGON"      ,"Ngon"     ,""   ),
               ("TRIFAN"    ,"Triangle" ,""   )],
               name = "",
               default = "NGON",    
               description = "change fill type")
                   
    # CIRCLE #
    bcirc_res = bpy.props.IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bcirc_rad = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)

    bcirc_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcirc_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcirc_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CYLINDER #
    bcyl_res = bpy.props.IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bcyl_rad = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)
    bcyl_dep = bpy.props.FloatProperty(name="Depth", description="set depth value", default=1.0, min=0.01, max=100)

    bcyl_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcyl_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcyl_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CONE #
    bcon_res = bpy.props.IntProperty(name="Verts", description="vertices value",  min=3, max=80, default=12)
    bcon_res1 = bpy.props.FloatProperty(name="Bottom", description="set bottom value",  min=0.01, max=100, default=2.5)
    bcon_res2 = bpy.props.FloatProperty(name="Top", description="set top value",  min=0.01, max=100, default=1.0)
    bcon_depth = bpy.props.FloatProperty(name="Depth", description="set depth value",  min=1, max=100, default=2)

    bcon_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcon_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcon_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # TORUS #
    btor_seg1 = bpy.props.IntProperty(name="Major Segments", description="set value",  min=1, max=100, default=51) 
    btor_seg2 = bpy.props.IntProperty(name="Minor Segments", description="set value",  min=1, max=100, default=15)
    btor_siz1 = bpy.props.FloatProperty(name="Major Radius", description="set value", default=1.13, min=0.01, max=1000)
    btor_siz2 = bpy.props.FloatProperty(name="Minor Radius", description="set value", default=0.78, min=0.01, max=1000)

    btor_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    btor_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    btor_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)


    # TOOLS #
    bvl_pipe_use = bpy.props.BoolProperty(name="Use Pipe",  description="activate pipe", default=False) 
    bvl_pipe_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=1.5, min=0.01, max=1000)

    bvl_bevel_use = bpy.props.BoolProperty(name="Use Bevel",  description="activate bevel", default=False) 
    bvl_select_all = bpy.props.BoolProperty(name="All",  description="use bevel on each edge", default=False) 
    bvl_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    bvl_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1, min=0, max=1)
    bvl_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=1.5, min=0, max=1000) 
    bvl_verts_use = bpy.props.BoolProperty(name="Vertices",  description="activate vertex extrusion", default=False) 

    bvl_extrude_use = bpy.props.BoolProperty(name="Use Extrude",  description="activate extrusion", default=False) 
    bvl_extrude_offset = bpy.props.FloatProperty(name="Extrude",  description="extrude on local z axis", default=10, min=0.01, max=1000) 

    # TUBE #
    tube_dim = bpy.props.BoolProperty(name="Copy",  description="deactivate scale", default=True) 
    tube_dim_apply = bpy.props.BoolProperty(name="Apply",  description="apply scale", default=True) 

    tube_rota = bpy.props.BoolProperty(name="Rotation",  description="deactivate copy rotation", default=True)

    tube_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )],
               name = "MeshType",
               default = "tp_00",    
               description = "change meshtype")

    tube_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    tube_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    tube_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    tube_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)  

    # MATERIAL #
    tube_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    tube_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    tube_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    tube_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Widget Orientation",
               default = "tp_w0",    
               description = "widget orientation")



    ### BOUNDING SPHERE ###
    tp_geom_sphere = bpy.props.EnumProperty(
        items=[("tp_add_sph"  ,"Sphere" ,"add sphere" ),
               ("tp_add_ico"  ,"Ico"    ,"add ico"    )],
               name = "ObjectType",
               default = "tp_add_sph",    
               description = "change objectype")

    # SPHERE #
    bsph_seg = bpy.props.IntProperty(name="Segments",  description="set value", min=1, max=100, default=32) 
    bsph_rig = bpy.props.IntProperty(name="Rings",  description="set value",  min=1, max=100, default=16) 
    bsph_siz = bpy.props.FloatProperty(name="Size",  description="set value", default=1.00, min=0.01, max=100) 

    bsph_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bsph_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bsph_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # ICO #
    bico_div = bpy.props.IntProperty(name="Subdiv",  description="set value", min=1, max=5, default=2) 
    bico_siz = bpy.props.FloatProperty(name="Size",  description="set value", default=1.00, min=0.01, max=100) 

    bico_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bico_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bico_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # TOOLS # 
    sphere_dim = bpy.props.BoolProperty(name="Copy Scale",  description="deactivate copy scale", default=True) 
    sphere_dim_apply = bpy.props.BoolProperty(name="Apply Scale",  description="apply copied scale", default=True) 

    sphere_rota = bpy.props.BoolProperty(name="Copy Rotation",  description="deactivate copy rotation", default=True) 

    sphere_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )],
               name = "MeshType",
               default = "tp_00",    
               description = "change meshtype")

    sphere_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    sphere_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    sphere_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    sphere_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)    

    # MATERIAL #
    sph_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    sph_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    sph_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    sph_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Widget Orientation",
               default = "tp_w0",    
               description = "widget orientation")
               

    ### BOUNDING SELECTIONS ###
    types_sel =  [("tp_01"  ,"Box"     ," "   ,""  ,1),
                  ("tp_02"  ,"Grid"    ," "   ,""  ,2), 
                  ("tp_03"  ,"Circle"  ," "   ,""  ,3),
                  ("tp_04"  ,"Tube"    ," "   ,""  ,4),
                  ("tp_05"  ,"Cone"    ," "   ,""  ,5),
                  ("tp_06"  ,"Sphere"  ," "   ,""  ,6),
                  ("tp_06"  ,"Ico"     ," "   ,""  ,7),
                  ("tp_06"  ,"Torus"   ," "   ,""  ,8)]
    
    tp_sel = bpy.props.EnumProperty(name = "Select ObjectType", default = "tp_01", description = "select all bounding geometry in the scene", items = types_sel)

    types_meshtype =[("tp_01"   ,"Shaded"      ,"select shaded"     ),
                     ("tp_02"   ,"Shadeless"   ,"select shadeless"  ),
                     ("tp_03"   ,"Wired"       ,"select wired mesh" )]
         
    tp_sel_meshtype = bpy.props.EnumProperty(name = "Select MeshType", default = "tp_01", description = "select choosen meshtype", items = types_meshtype)

    tp_extend = bpy.props.BoolProperty(name="Extend Selection",  description="extend selection", default=False) 

    tp_link = bpy.props.BoolProperty(name="LinkData",  description="activate link object data", default=False) 

    ### BOUNDING ACTIONS ###
    lock_mode = bpy.props.StringProperty(default="")
    select_mode = bpy.props.StringProperty(default="")




# PROPERTY GROUP: MIFTHTOOLS #
class MFTCloneProperties(bpy.types.PropertyGroup):

    # RADIAL CLONE #
    mft_create_last_clone = BoolProperty(name="Create Last Clone",description="create last clone...",default=False)
    mft_radialClonesAngle = FloatProperty(default=360.0, min=-360.0,max=360.0)
    mft_clonez = IntProperty(default=8,min=2, max=300)
    mft_radialClonesAxis = EnumProperty(items=(('X', 'X', ''),('Y', 'Y', ''),('Z', 'Z', '')),default = 'Z')
    mft_radialClonesAxisType = EnumProperty(items=(('Global', 'Global', ''),('Local', 'Local', '')),default = 'Global')

    # RELATIONS #    
    mft_single = bpy.props.BoolProperty(name="Unlink",  description="Unlink Clones", default=False)    
    mft_join = bpy.props.BoolProperty(name="Join",  description="Join Clones", default=False)    
    mft_edit = bpy.props.BoolProperty(name="Edit",  description="Editmode", default=False)    

    # TRANSFORM #
    copy_transform_use = bpy.props.BoolProperty(name="Transform",  description="enable transform tools", default=False)  
    mft_origin = bpy.props.BoolProperty(name="Set Origin back",  description="set origin back to previuos postion", default=False)  

    # TRANSFORM LOCATION #
    copy_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})

    # TRANSFORM ROTATE #
    copy_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})

    # TRANSFORM SCALE #
    copy_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})


# PROPERTY GROUP: COPY TO CURSOR #
class ToCursor_Properties(bpy.types.PropertyGroup):
    
    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)


# PROPERTY GROUP: DUPLISET #
class DupliSet_Properties(bpy.types.PropertyGroup):
    
    dupli_align = bpy.props.BoolProperty(name="Align Source",  description="Align Object Location", default=False)       
    dupli_single = bpy.props.BoolProperty(name="Make Real",  description="Single Dupli-Instances", default=False)    
    dupli_separate = bpy.props.BoolProperty(name="Separate all",  description="Separate Objects", default=False)    
    dupli_link = bpy.props.BoolProperty(name="Link separted",  description="Link separated Objects", default=False)  


# PROPERTY GROUP: REMESH #
class Sculpt_Remesh_Properties(bpy.types.PropertyGroup):

    bpy.types.Object.frozen = BoolProperty(name="frozen", default = False)
        
    remeshDepthInt = IntProperty(min = 2, max = 10, default = 4)
    remeshSubdivisions = IntProperty(min = 0, max = 6, default = 0)
    remeshPreserveShape = BoolProperty(default = True)

    extractDepthFloat = bpy.props.FloatProperty(min = -10.0, max = 10.0, default = 0.1)
    extractOffsetFloat = bpy.props.FloatProperty(min = -10.0, max = 10.0, default = 0.0)
    extractSmoothIterationsInt = bpy.props.IntProperty(min = 0, max = 50, default = 5)    
    extractStyleEnum = bpy.props.EnumProperty(name="Extract style", 
               items = [("SOLID",    "Solid",        "", 1), 
                        ("SINGLE",   "Single Sided", "", 2), 
                        ("FLAT",     "Flat",         "", 3), 
                        ("CUT",      "Cut",          "", 4), 
                        ("COPY",     "Copy",         "", 5), 
                        ("DELETE",   "Delete",       "", 6)], 
                        default = "SOLID")
                             

# BOOLTOOL: HIDE BOOLEAN OBJECTS #
def update_BoolHide(self, context):
    ao = context.scene.objects.active
    objs = [i.object for i in ao.modifiers if i.type == 'BOOLEAN']
    hide_state = context.scene.BoolHide
    for o in objs:
        o.hide = hide_state
        


# PROPERTY CURVETOOLS 2 # 
def UpdateDummy(object, context):
    pass
   
class CurveTools2_Props(bpy.types.PropertyGroup):
    # selection
    SelectedObjects = CollectionProperty(type = Properties.CurveTools2SelectedObject)
    NrSelectedObjects = IntProperty(name = "NrSelectedObjects", default = 0, description = "Number of selected objects", update = UpdateDummy)

    # curve
    CurveLength = FloatProperty(name = "CurveLength", default = 0.0, precision = 6)
        
    # splines
    SplineResolution = IntProperty(name = "SplineResolution", default = 64, min = 2, max = 1024, soft_min = 2, description = "Spline resolution will be set to this value")
    
    SplineRemoveLength = FloatProperty(name = "SplineRemoveLength", default = 0.001, precision = 6, description = "Splines shorter than this threshold length will be removed")
    SplineJoinDistance = FloatProperty(name = "SplineJoinDistance", default = 0.001, precision = 6, description = "Splines with starting/ending points closer to each other than this threshold distance will be joined")
    SplineJoinStartEnd = BoolProperty(name = "SplineJoinStartEnd", default = False, description = "Only join splines at the starting point of one and the ending point of the other")

    splineJoinModeItems = (('At midpoint', 'At midpoint', 'Join splines at midpoint of neighbouring points'), ('Insert segment', 'Insert segment', 'Insert segment between neighbouring points'))
    SplineJoinMode = EnumProperty(items = splineJoinModeItems, name = "SplineJoinMode", default = 'At midpoint', description = "Determines how the splines will be joined")
    
    # curve intersection
    LimitDistance = FloatProperty(name = "LimitDistance", default = 0.0001, precision = 6, description = "Displays the result of the curve length calculation")

    intAlgorithmItems = (('3D', '3D', 'Detect where curves intersect in 3D'), ('From View', 'From View', 'Detect where curves intersect in the RegionView3D'))
    IntersectCurvesAlgorithm = EnumProperty(items = intAlgorithmItems, name = "IntersectCurvesAlgorithm", description = "Determines how the intersection points will be detected", default = '3D')

    intModeItems = (('Insert', 'Insert', 'Insert points into the existing spline(s)'), ('Split', 'Split', 'Split the existing spline(s) into 2'), ('Empty', 'Empty', 'Add empty at intersections'))
    IntersectCurvesMode = EnumProperty(items = intModeItems, name = "IntersectCurvesMode", description = "Determines what happens at the intersection points", default = 'Split')

    intAffectItems = (('Both', 'Both', 'Insert points into both curves'), ('Active', 'Active', 'Insert points into active curve only'), ('Other', 'Other', 'Insert points into other curve only'))
    IntersectCurvesAffect = EnumProperty(items = intAffectItems, name = "IntersectCurvesAffect", description = "Determines which of the selected curves will be affected by the operation", default = 'Both')
 
def run_auto_loft(self, context):
    if self.auto_loft:
        bpy.ops.wm.auto_loft_curve()
    return None

 
# PROPERTY INSERTS # 
class Insert_Props(bpy.types.PropertyGroup):

    radius = bpy.props.FloatProperty(name="Radius",  description=" ", default=10, min=0.01, max=1000)
    depth = bpy.props.FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)

    ring = bpy.props.IntProperty(name="Ring",  description=" ", min=0, max=100, default=1) 
    nring = bpy.props.IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop = bpy.props.IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 

    offset = bpy.props.FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height = bpy.props.FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

    wire = bpy.props.BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})    

    curve_type = bpy.props.EnumProperty(
        items=[("tp_bezier"     ,"Bezier Curve"     ,"Bezier Curve"),
               ("tp_circle"     ,"Circle Curve"     ,"Circle Curve"),
               ("tp_nurbs"      ,"Nurbs Curve"      ,"Nurbs Curve"),
               ("tp_ncircle"    ,"Nurbs Circle"     ,"Nurbs Circle")],
               name = "Type",
               default = "tp_bezier",    
               description = "add geometry")

   
    add_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    add_objmat = bpy.props.BoolProperty(name="Use Object Color",  description="add material and enable object color", default=False)  
    add_random = bpy.props.BoolProperty(name="Add Random",  description="add random materials", default=False, options={'SKIP_SAVE'})    
    add_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)

    add_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    mode = bpy.props.StringProperty(default="")    
    convert = bpy.props.BoolProperty(name="Convert to Mesh",  description=" ", default=False, options={'SKIP_SAVE'})   




# PROPERTY DISPLAY: RESURFACE #
class Dropdown_TP_ReSurface_Props(bpy.types.PropertyGroup):

    # HELP/DOCU/FILE #
    display_title = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)     
    display_pathes = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_help = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False) 
    display_docu = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # ADD #
    display_addset = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_insert = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # ALIGN #
    display_align = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_align_help = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # BOOLEAN #
    display_boolean = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # BOUNDING #
    display_bbox = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_bbox_set = bpy.props.BoolProperty(name = "Display Setting", description = "Display Setting", default = False)
    display_bcyl_set = bpy.props.BoolProperty(name = "Display Setting", description = "Display Setting", default = False)
    display_bext_set = bpy.props.BoolProperty(name = "Display Setting", description = "Display Setting", default = False)

    # BRUSHES #
    display_brushes = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_brushes_obm = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_meshbrush = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_retopo_mt = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_carver_util = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_snap_util = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_polymesh = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_knife = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_cdraw = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # COPY #
    display_copy = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_copy_to_faces = bpy.props.BoolProperty(name = "Copy to Faces Tools", description = "open / close props", default = False)
    display_toall = bpy.props.BoolProperty(name = "Copy to All", description = "open / close props", default = False)
    display_pfath = bpy.props.BoolProperty(name = "Follow Path Array", description = "open / close props", default = False)
    display_empty = bpy.props.BoolProperty(name = "Empty Array", description = "open / close props", default = False)
    display_array = bpy.props.BoolProperty(name = "Curve Array", description = "open / close props", default = False)
    display_axis_array = bpy.props.BoolProperty(name = "Axis Array", description = "open / close props", default = False)
    display_array_tools = bpy.props.BoolProperty(name = "Array Tools", description = "open / close props", default = False)
    display_apply = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_dupli = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_optimize_tools = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_copy_to_cursor = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # CONVERT #
    display_convert = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # CURVE #
    display_curve_info = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_insert = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_select = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_edit = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_bevel = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_bevel_reso = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_taper = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_utility = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_type = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_options = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_draw = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_custom = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  

    # EDITING #
    display_deform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_snapshot = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_symdim = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_divide = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_relax = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_spacing = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_rename = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # GREASE PENCIL #
    display_pencil_obm = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)       
    display_pencil_edm = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_gstretch_edm = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_bsurface_edm = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
 
    # MESHCHECK #
    display_mcheck = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_meshlint_toggle = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # MODIFIER #
    display_symdim = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_subsurf = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_automirror = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_apply = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_rename = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_recoplanar = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_divide = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_xtras = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_addmods = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_sdeform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_array = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_mirror = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_bevel = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_skin = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_solidify = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_screw = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False) 
    display_cast = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False) 
    display_lattice = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False) 
    display_subsurf = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_vertgrp = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_smooth = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_remesh = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_decimate = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_multires = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    display_multiresset = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   

    # ORIGIN #
    display_origin = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)
    
    # SELECTION #
    display_select = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_transform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   
    
    # SCULPT # 
    display_sculpt_edit = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_sculpt_mask = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_sculpt_noise = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_sculpt_displace = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_sculpt_decimate = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  

    # Transform #
    display_copydim = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)   

    # VISUALS #
    display_smooth = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_visual = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_grid = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_aoccl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_world_set = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)      

    # CUSTOM #
    display_custom = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)      





 


    
# REGISTER #
import traceback

def register():  

    meshcheck.register()     
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    # UI #
    update_panel_position(None, bpy.context)
    update_panel_sculpt(None, bpy.context)
    update_display_tools(None, bpy.context)

    # MENUS #
    update_menu_align(None, bpy.context) 
    update_menu_boolean(None, bpy.context) 
    update_menu_delete(None, bpy.context)
    update_menu_origin(None, bpy.context) 
    update_menu_relax(None, bpy.context)
    update_menu_resurface(None, bpy.context)
    update_menu_selection(None, bpy.context)
    update_menu_submenus(None, bpy.context)

    update_menu_closer(None, bpy.context)
    update_menu_vert_edit(None, bpy.context)
    update_menu_edge_edit(None, bpy.context)
    update_menu_edge_visual(None, bpy.context)
    update_menu_face_edit(None, bpy.context)
    update_menu_face_visual(None, bpy.context)
    update_menu_special_edit(None, bpy.context)


    # RESURFACE #
    bpy.types.WindowManager.tp_props_resurface = bpy.props.PointerProperty(type = Dropdown_TP_ReSurface_Props)

    # BOOLTOOL #
    bpy.types.Scene.BoolHide = bpy.props.BoolProperty(default=False, description='Hide boolean objects', update=update_BoolHide)

    # BOUNDING #
    bpy.types.WindowManager.tp_props_bbox = bpy.props.PointerProperty(type = Dropdown_BBox_Panel_Props)  

    # BSURFACE #
    bpy.types.Scene.tp_bsurfaces = bpy.props.PointerProperty(type = tp_bsurfacesProps) 

    # CARVER #
    bpy.types.Scene.DepthCursor = bpy.props.BoolProperty(name="DepthCursor", default=False)
    bpy.types.Scene.OInstanciate = bpy.props.BoolProperty(name="Obj_Instantiate", default=False)
    bpy.types.Scene.ORandom = bpy.props.BoolProperty(name="Random_Rotation", default=False)
    bpy.types.Scene.DontApply = bpy.props.BoolProperty(name="Dont_Apply", default=False)
    bpy.types.Scene.nProfile = bpy.props.IntProperty(name="Num_Profile", default=0)

    # COPY # 
    bpy.types.WindowManager.tocursor_props = PointerProperty(type = ToCursor_Properties)
    bpy.types.WindowManager.dupliset_props = PointerProperty(type = DupliSet_Properties)
    bpy.types.WindowManager.mifth_clone_props = PointerProperty(type = MFTCloneProperties)
    bpy.types.WindowManager.totarget_props = PointerProperty(type = ToTarget_Properties)

    # CURVE # 
    bpy.types.Scene.curve_vertcolor = bpy.props.FloatVectorProperty(name="OUT", default=(0.2, 0.9, 0.9, 1), size=4, subtype="COLOR", min=0, max=1)

    # CURVETOOLS 2 # 
    bpy.types.Scene.curvetools = bpy.props.PointerProperty(type=CurveTools2_Props)      
    bpy.types.WindowManager.auto_loft = BoolProperty(default=False, name="Auto Loft", update=run_auto_loft)
    bpy.context.window_manager.auto_loft = False

    # INSERT #
    bpy.types.Scene.tp_props_insert = bpy.props.PointerProperty(type=Insert_Props)   
    bpy.types.WindowManager.tp_props_insert = bpy.props.PointerProperty(type=Insert_Props)   

    # LOOPTOOLS #
    bpy.types.WindowManager.tp_props_looptools = bpy.props.PointerProperty(type = tp_looptoolsProps) 

    # MESCH CHECK #
    bpy.types.WindowManager.mesh_check = bpy.props.PointerProperty(type=MeshCheckCollectionGroup)
    
    # MIRATOOLS #
    bpy.types.Scene.mi_settings = PointerProperty(name="Global Settings", type=mi_settings.MI_Settings, description="Global Settings.")
    bpy.types.Scene.mi_cur_stretch_settings = PointerProperty(name="Curve Stretch Settings",type=mi_curve_stretch.MI_CurveStretchSettings,description="Curve Stretch Settings.")
    bpy.types.Scene.mi_cur_surfs_settings = PointerProperty(name="Curve Surfaces Settings", type=mi_curve_surfaces.MI_CurveSurfacesSettings, description="Curve Surfaces Settings.")
    bpy.types.Scene.mi_extrude_settings = PointerProperty(name="Extrude Variables", type=mi_draw_extrude.MI_ExtrudeSettings, description="Extrude Settings")
    bpy.types.Scene.mi_ldeformer_settings = PointerProperty(name="Linear Deformer Variables", type=mi_linear_deformer.MI_LDeformer_Settings, description="Linear Deformer Settings")
    bpy.types.Scene.mi_curguide_settings = PointerProperty(name="Curve Guide Variables", type=mi_curve_guide.MI_CurGuide_Settings, description="Curve Guide Settings")
    bpy.types.Scene.mi_makearc_settings = PointerProperty(name="Make Arc Variables", type=mi_make_arc.MI_MakeArc_Settings, description="Make Arc Settings")
    bpy.types.WindowManager.mirawindow = bpy.props.PointerProperty(type = DropdownMiraToolProps)

    bpy.types.Object.BrushSize  = bpy.props.FloatProperty(default = 1.0, min = 0.0, max = 100.0)
    bpy.types.Object.BrushCut   = bpy.props.FloatProperty(default = 6.0, min = 0.0, max = 100.0)
    bpy.types.Object.CTNCut     = bpy.props.FloatProperty(default = 6.0, min = 0.0, max = 100.0)
    bpy.types.Object.AutoMerge  = bpy.props.BoolProperty(default = True)    
    
    # MULTI EDIT #
    bpy.types.Scene.Keep_Origin_Point = bpy.props.BoolProperty ( name = "Keep Origin Point", description = "Keep origin points", default = True)

    # RENAME #
    bpy.types.Scene.rno_list_selection_ordered = bpy.props.EnumProperty(name="selection orderer", items=[])    
    bpy.types.Scene.rno_str_new_name = bpy.props.StringProperty(name="New name", default='')
    bpy.types.Scene.rno_str_old_string = bpy.props.StringProperty(name="Old string", default='')
    bpy.types.Scene.rno_str_new_string = bpy.props.StringProperty(name="New string", default='')
    bpy.types.Scene.rno_str_numFrom = bpy.props.StringProperty(name="from", default='')
    bpy.types.Scene.rno_str_prefix = bpy.props.StringProperty(name="Prefix", default='')
    bpy.types.Scene.rno_str_subfix = bpy.props.StringProperty(name="Subfix", default='')    
    bpy.types.Scene.rno_bool_numbered = bpy.props.BoolProperty(name='numbered', default=True)
    bpy.types.Scene.rno_bool_keepOrder = bpy.props.BoolProperty(name='keep selection order')
    bpy.types.Scene.rno_bool_keepIndex = bpy.props.BoolProperty(name='keep object Index', default=True)

    # SCULPT #
    brush_quickset = context.user_preferences.addons[__name__].preferences.tab_brush_quickset
    if brush_quickset == 'on':
        
        cfg = bpy.context.window_manager.keyconfigs.addon
        if not cfg.keymaps.__contains__('Sculpt'):
            cfg.keymaps.new('Sculpt', space_type='EMPTY', region_type='WINDOW')
        kmi = cfg.keymaps['Sculpt'].keymap_items
        kmi.new('brush.modal_quickset', 'RIGHTMOUSE', 'PRESS')

    bpy.types.Scene.mask_cavity_angle = bpy.props.IntProperty(name = "Cavity Angle", default = 82, min = 45, max = 90)
    bpy.types.Scene.mask_cavity_strength = bpy.props.FloatProperty(name = "Mask Strength", default = 1.0, min = 0.1, max = 1.0)     
    bpy.types.Scene.mask_edge_angle = bpy.props.IntProperty(name = "Sharp Angle", default = 82, min = 45, max = 90)
    bpy.types.Scene.mask_edge_strength = bpy.props.FloatProperty(name = "Mask Strength", default = 1.0, min = 0.1, max = 1.0)     
    bpy.types.Scene.mask_smooth_strength = bpy.props.FloatProperty(name = "Mask Smooth Strength", default = 0.25, min = 0.1, max = 1.0)
    bpy.types.WindowManager.tp_props_remesh = PointerProperty(type = Sculpt_Remesh_Properties)    

    # SCRIPTS 1D #
    bpy.types.WindowManager.paul_manager = bpy.props.PointerProperty(type = paul_managerProps) 
    bpy.context.window_manager.paul_manager.display_align = False
    bpy.context.window_manager.paul_manager.align_dist_z = True
    bpy.context.window_manager.paul_manager.align_lock_z = False
    bpy.context.window_manager.paul_manager.step_len = 1.0
    bpy.context.window_manager.paul_manager.edge_idx_store = -1
    bpy.context.window_manager.paul_manager.object_name_store = ''
    bpy.context.window_manager.paul_manager.object_name_store_c = ''
    bpy.context.window_manager.paul_manager.object_name_store_v = ''
    bpy.context.window_manager.paul_manager.active_edge1_store = -1
    bpy.context.window_manager.paul_manager.active_edge2_store = -1
    bpy.context.window_manager.paul_manager.coner_edge1_store = -1
    bpy.context.window_manager.paul_manager.coner_edge2_store = -1

    # SNAPSHOT #
    bpy.types.Object.snapShotMesh_ID_index = bpy.props.IntProperty()
    bpy.types.Object.snapShotMeshes = bpy.props.CollectionProperty(type=VTOOLS_CC_snapShotMeshCollection)

    # VISUALS #  
    bpy.types.WindowManager.tp_props_visual = bpy.props.PointerProperty(type = Dropdown_TP_Visual_Props)      
    bpy.types.Scene.display_props = bpy.props.PointerProperty(type=Display_Tools_Props)
    bpy.types.Scene.orphan_props = bpy.props.PointerProperty(type=Orphan_Tools_Props)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_ReSurface_Manual)





def unregister():
  
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # RESURFACE #
    del bpy.types.WindowManager.tp_props_resurface

    # BOOLTOOL #
    del bpy.types.Scene.BoolHide
    
    # BOUNDING #
    del bpy.types.WindowManager.tp_props_bbox

    # BSURFACE #
    del bpy.types.Scene.tp_bsurfaces
    
    # CARVER #
    del bpy.types.Scene.DepthCursor
    del bpy.types.Scene.OInstanciate
    del bpy.types.Scene.ORandom
    del bpy.types.Scene.DontApply
    del bpy.types.Scene.nProfile    

    # COPY # 
    del bpy.types.WindowManager.tocursor_props
    del bpy.types.WindowManager.dupliset_props
    del bpy.types.WindowManager.mifth_clone_props      
    del bpy.types.WindowManager.totarget_props 

    # CURVE #
    del bpy.types.Scene.curve_vertcolor   
     
    # CURVETOOLS 2 # 
    del bpy.types.Scene.curvetools     
    del bpy.types.WindowManager.auto_loft

    # INSERT #
    del bpy.types.Scene.tp_props_insert 
    del bpy.types.WindowManager.tp_props_insert 

    # LOOPTOOLS #
    del bpy.types.WindowManager.tp_props_looptools

    # MESCH CHECK #
    del bpy.types.WindowManager.mesh_check    

    # MIRATOOLS #
    del bpy.types.Scene.mi_settings
    del bpy.types.Scene.mi_cur_stretch_settings
    del bpy.types.Scene.mi_cur_surfs_settings
    del bpy.types.Scene.mi_extrude_settings
    del bpy.types.Scene.mi_ldeformer_settings
    del bpy.types.Scene.mi_curguide_settings
    del bpy.types.Scene.mi_makearc_settings
    del bpy.types.WindowManager.mirawindow    

    # MULTI EDIT #
    del bpy.types.Scene.Keep_Origin_Point

    # RENAME # 
    del bpy.types.Scene.rno_str_new_name
    del bpy.types.Scene.rno_str_old_string
    del bpy.types.Scene.rno_str_new_string
    del bpy.types.Scene.rno_bool_keepOrder
    del bpy.types.Scene.rno_bool_numbered
    del bpy.types.Scene.rno_list_selection_ordered
    del bpy.types.Scene.rno_str_prefix
    del bpy.types.Scene.rno_str_subfix
    del bpy.types.Scene.rno_bool_keepIndex 


    # SCULPT #
    cfg = bpy.context.window_manager.keyconfigs.addon
    if cfg.keymaps.__contains__('Sculpt'):
        for kmi in cfg.keymaps['Sculpt'].keymap_items:
            if kmi.idname == 'brush.modal_quickset':
                cfg.keymaps['Sculpt'].keymap_items.remove(kmi)
                break

    del bpy.types.Scene.mask_cavity_angle
    del bpy.types.Scene.mask_cavity_strength
    del bpy.types.Scene.mask_edge_angle
    del bpy.types.Scene.mask_smooth_strength 
    del bpy.types.WindowManager.tp_props_remesh 

    # SCRIPTS 1D #
    del bpy.types.WindowManager.paul_manager
      
    # SNAPSHOT #
    del bpy.types.Object.snapShotMeshes
    del bpy.types.Object.snapShotMesh_ID_index

    # VISUALS #  
    del bpy.types.WindowManager.tp_props_visual
    del bpy.types.Scene.display_props
    del bpy.types.Scene.orphan_props

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_ReSurface_Manual)



 
if __name__ == "__main__":
    register()      
    

                 




