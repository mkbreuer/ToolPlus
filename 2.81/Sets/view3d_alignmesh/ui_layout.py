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

# ADDON CHECK #
import addon_utils   

def draw_ui_panel_align_mesh(context, layout):
    layout.scale_y = 1.15
    layout.operator_context = 'INVOKE_REGION_WIN'    

    addon_prefs = context.preferences.addons[__package__].preferences

    am_global = bpy.context.window_manager.alignmesh_global_props       
  
    icons = load_icons()      
  
    col = layout.row(align=True)
    if am_global.align_typ == 'align':                                                       
        col.operator("tpc_ops.mesh_align_help", text='', icon ='INFO').mode='align'
        col.label(text='Align: Direct')
    else:
        col.operator("tpc_ops.mesh_align_help", text='', icon ='INFO').mode='flatten'
        col.label(text='Modal: Linked Face') 
                                    
    col.prop_enum(am_global, "align_typ", "align", text="", icon ='CON_LOCLIMIT')
    col.prop_enum(am_global, "align_typ", "flatten", text="", icon ='MOD_MESHDEFORM')
 
    layout.separator()                                                   

    col = layout.column(align=True)                                                   
    box = layout.box().column(align=True)  

    if am_global.align_typ == 'align':

        row = box.row(align=True)

        button_align_x = icons.get("icon_align_x") 
        props = row.operator("tpc_ops.align_mesh", text="X", icon_value=button_align_x.icon_id)
        props.use_align_axis='axis_x'
        props.set_pivot='ACTIVE_ELEMENT'

        button_align_y = icons.get("icon_align_y")
        props = row.operator("tpc_ops.align_mesh",text="Y", icon_value=button_align_y.icon_id)
        props.use_align_axis='axis_y'
        props.set_pivot='ACTIVE_ELEMENT'

        button_align_z = icons.get("icon_align_z")
        props = row.operator("tpc_ops.align_mesh",text="Z", icon_value=button_align_z.icon_id)
        props.use_align_axis='axis_z'   
        props.set_pivot='ACTIVE_ELEMENT'

        box.separator()    

        row = box.row(align=True)

        button_align_xy = icons.get("icon_align_xy") 
        props = row.operator("tpc_ops.align_mesh", text="Xy", icon_value=button_align_xy.icon_id)
        props.use_align_axis='axis_xy'
        props.set_pivot='ACTIVE_ELEMENT'

        button_align_zy = icons.get("icon_align_zy") 
        props = row.operator("tpc_ops.align_mesh", text="Zy", icon_value=button_align_zy.icon_id)
        props.use_align_axis='axis_zy'
        props.set_pivot='ACTIVE_ELEMENT'

        button_align_zx = icons.get("icon_align_zx")
        props = row.operator("tpc_ops.align_mesh", text="Zx", icon_value=button_align_zx.icon_id)
        props.use_align_axis='axis_zx'
        props.set_pivot='ACTIVE_ELEMENT'

        box.separator()      
     
        row = box.row(align=True)

        button_align_n = icons.get("icon_align_n") 
        props = row.operator("tpc_ops.align_mesh", text="Align to Normal", icon_value=button_align_n.icon_id)
        props.use_align_axis='axis_n'
        props.set_pivot='ACTIVE_ELEMENT'

        box.separator()   
        
        row = box.column(align=True)
        icon_align_straigten = icons.get("icon_align_straigten") 
        row.operator('tpc_ot.vertex_align', text="Straight", icon_value=icon_align_straigten.icon_id)

        icon_align_distribute = icons.get("icon_align_distribute") 
        row.operator('tpc_ot.vertex_distribute', text="Evenly", icon_value=icon_align_distribute.icon_id)

        icon_align_both = icons.get("icon_align_both") 
        row.operator('tpc_ot.vertex_inline', text="Evenly Straight", icon_value=icon_align_both.icon_id)

        row.separator()  
        
        looptools_addon = "mesh_looptools" 
        looptools_state = addon_utils.check(looptools_addon)
        if not looptools_state[0]:
            row.operator("preferences.addon_show", text="Activate: LoopTools", icon="ERROR").module="mesh_looptools"                  
        else:           

            icon_align_space = icons.get("icon_align_space") 
            props = row.operator('mesh.looptools_space', text="LPT Space", icon_value=icon_align_space.icon_id)
            props.influence=100
            props.input='all'
            props.interpolation='cubic'
            props.lock_x=False
            props.lock_y=False
            props.lock_z=False

            icon_align_curve = icons.get("icon_align_curve") 
            props = row.operator('mesh.looptools_curve', text="LPT Curve", icon_value=icon_align_curve.icon_id)
            props.boundaries=True
            props.influence=100
            props.interpolation='cubic'
            props.lock_x=False
            props.lock_y=False
            props.lock_z=False 
            props.regular=True  
            props.restriction='none'

            icon_align_circle = icons.get("icon_align_circle") 
            props = row.operator('mesh.looptools_circle', text="LPT Circle", icon_value=icon_align_circle.icon_id)
            props.custom_radius=False
            props.fit='best'
            props.flatten=True
            props.influence=100
            props.lock_x=False
            props.lock_y=False
            props.lock_z=False 
            props.radius=1 
            props.regular=True 

            icon_align_flatten = icons.get("icon_align_flatten") 
            props = row.operator('mesh.looptools_flatten', text="LPT Flatten", icon_value=icon_align_flatten.icon_id)
            props.lock_x=False
            props.lock_y=False
            props.lock_z=False 
            props.plane='best_fit'
            props.restriction='none'

            row.separator()  

        
        icon_align_smooth = icons.get("icon_align_smooth") 
        row.operator('tpc_ot.shrinkwrap_smooth', text="Smooth Faces", icon_value=icon_align_smooth.icon_id)

        icon_align_vertices = icons.get("icon_align_vertices") 
        props = row.operator('mesh.vertices_smooth', text="Smooth Vertices", icon_value=icon_align_vertices.icon_id)
        props.factor=0.5
        props.repeat=1
        props.xaxis=True
        props.yaxis=True
        props.zaxis=True

        box.separator()  
     
        row = box.row(align=True)
        row.operator('tpc_ot.mirror_over_edge', text="Mirror over Edge", icon='ARROW_LEFTRIGHT')
        
        row = box.row(align=True)        
        row.operator_context = 'EXEC_REGION_WIN'       
        
        props = row.operator('transform.mirror', text="X-Mirror")
        props.orient_type=addon_prefs.orient
        props.constraint_axis=(True, False, False)

        props = row.operator('transform.mirror', text="Y-Mirror")
        props.orient_type=addon_prefs.orient
        props.constraint_axis=(False, True, False)

        props = row.operator('transform.mirror', text="Z-Mirror")
        props.orient_type=addon_prefs.orient
        props.constraint_axis=(False, False, True)
       
        box.separator()  
        
        row = box.row(align=True)
        row.label(text="Orientation")     
        row.prop(addon_prefs, 'orient', text="")     
       
        box.separator()  




    else:
        row = box.row(align=True)

        button_align_x = icons.get("icon_align_x") 
        props = row.operator("tpc_ops.snapflat_modal", text="X", icon_value=button_align_x.icon_id)
        props.mode='flatten_x'

        button_align_y = icons.get("icon_align_y")
        props = row.operator("tpc_ops.snapflat_modal",text="Y", icon_value=button_align_y.icon_id)
        props.mode='flatten_y'

        button_align_z = icons.get("icon_align_z")
        props = row.operator("tpc_ops.snapflat_modal",text="Z", icon_value=button_align_z.icon_id)
        props.mode='flatten_z'

        box.separator()    

        looptools_addon = "mesh_looptools" 
        looptools_state = addon_utils.check(looptools_addon)
        if not looptools_state[0]:
            row.operator("preferences.addon_show", text="Activate: LoopTools", icon="ERROR").module="mesh_looptools"                  
        else:   

            row = box.column(align=True)

            props = row.operator("tpc_ops.snapflat_modal", text="LPT Flatten*", icon='TRIA_DOWN_BAR')
            props.mode='flatten_lpt'
          
            row.separator()    
           
            row.prop(addon_prefs, "threshold", text="threshold linked face")        

            row.separator()    

            props = row.operator("tpc_ops.snapflat_modal", text="Region: Selection", icon='RESTRICT_SELECT_OFF')
            props.mode='snap_for_select'

            props = row.operator("tpc_ops.snapflat_modal", text="Region: UV Seam", icon='UV_FACESEL')
            props.mode='snap_for_uvs'

            props = row.operator("tpc_ops.snapflat_modal", text="Region: Mark Sharp", icon='SHADING_BBOX')
            props.mode='snap_for_sharp'

            box.separator()   

        row = box.row(align=True)
        row.label(text='Select Mode')   
        row.prop_enum(addon_prefs, "mesh_select_mode", "vertices", text="", icon ='VERTEXSEL')

        row = box.row(align=True)
        row.label(text='when finished')   
        row.prop_enum(addon_prefs, "mesh_select_mode", "edges", text="", icon ='EDGESEL')

        row = box.row(align=True)
        row.label(text='Modal Tools')   
        row.prop_enum(addon_prefs, "mesh_select_mode", "faces", text="", icon ='FACESEL')
    
        box.separator()   

    col = layout.row(align=True)
    col.scale_y = 0.65    
    col.operator("preferences.addon_show", text=" ", icon="LAYER_USED").module="view3d_alignmesh"

    if addon_prefs.show_history_tools == True:
        
        layout.separator()
        col = layout.row(align=True) 
        col.scale_y = 0.75
        col.alignment = 'CENTER' 
        col.operator("ed.undo", text="", icon="FRAME_PREV")
        col.operator("ed.undo_history", text="", icon="COLLAPSEMENU")
        col.operator("ed.redo", text="", icon="FRAME_NEXT") 


 