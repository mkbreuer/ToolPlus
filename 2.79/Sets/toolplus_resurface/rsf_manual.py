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
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


 # RIGHT CLICK BUTTON TO ONLINE MANUAL
def VIEW3D_TP_ReSurface_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/ToolPlus/wiki"
    url_manual_mapping = (
        ("bpy.ops.object.transform_apply"               , "/TP-ReSurface"),


        # ALIGN #
        ("bpy.ops.object.align_location_all"          , "/TP-Align"),
        ("bpy.ops.object.align_location_x"            , "/TP-Align"),
        ("bpy.ops.object.align_location_y"            , "/TP-Align"),        
        ("bpy.ops.object.align_location_z"            , "/TP-Align"),
        ("bpy.ops.object.align_rotation_all"          , "/TP-Align"),
        ("bpy.ops.object.align_rotation_x"            , "/TP-Align"),
        ("bpy.ops.object.align_rotation_y"            , "/TP-Align"),
        ("bpy.ops.object.align_rotation_z"            , "/TP-Align"),
        ("bpy.ops.object.align_objects_scale_all"     , "/TP-Align"),
        ("bpy.ops.object.align_objects_scale_x"       , "/TP-Align"),
        ("bpy.ops.object.align_objects_scale_y"       , "/TP-Align"),
        ("bpy.ops.object.align_objects_scale_z"       , "/TP-Align"),

        ("bpy.ops.tp_origin.align_tools"              , "/TP-Align"),
        ("bpy.ops.object.distribute_osc"              , "/TP-Align"),
        ("bpy.ops.tp_ops.zero_axis_panel"             , "/TP-Align"),

        ("bpy.ops.tp_ops.np_020_point_move"             , "/TP-Align"),
        ("bpy.ops.tp_ops.np_020_roto_move"              , "/TP-Align"),
        ("bpy.ops.tp_ops.np_020_point_scale"            , "/TP-Align"),
        ("bpy.ops.tp_ops.np_020_point_align"            , "/TP-Align"),

        ("bpy.ops.object.align_by_faces"              , "/TP-Align"),
        ("bpy.ops.object.drop_on_active"              , "/TP-Align"),
        ("bpy.ops.view3d.xoffsets_main"               , "/TP-Align"),
        ("bpy.ops.view3d.xedit_rotate"                , "/TP-Align"),

        ("bpy.ops.mesh.wplsmthdef_snap"                , "/TP-Align"),
        
        ("bpy.ops.tp_ops.align_mesh_vertices"   , "/TP-Align"),
        ("bpy.ops.tp_ops.align_to_normal"       , "/TP-Align"),
        ("bpy.ops.mesh.rot_con"                 , "/TP-Align"),        
        ("bpy.ops.mesh.wplsmthdef_apply"        , "/TP-Align"),
        ("bpy.ops.mesh.vertex_align"            , "/TP-Align"),
        ("bpy.ops.mesh.vertex_distribute"       , "/TP-Align"),

        ("bpy.ops.mesh.looptools_space"         , "/TP-Align"),
        ("bpy.ops.mesh.looptools_curve"         , "/TP-Align"),
        ("bpy.ops.mesh.looptools_circle"        , "/TP-Align"),
        ("bpy.ops.mesh.looptools_flatten"       , "/TP-Align"),
        ("bpy.ops.mesh.looptools_relax"       , "/TP-Align"),
        ("bpy.ops.mesh.looptools_gstretch"      , "/TP-Align"),
        ("bpy.ops.tp_ops.surface_pencil"        , "/TP-Align"),
        ("bpy.ops.remove.gp"                    , "/TP-Align"),

        ("bpy.ops.mesh.vertices_smooth"               , "/TP-Align"),
        ("bpy.ops.mesh.vertices_smooth_laplacian"     , "/TP-Align"),        
        ("bpy.ops.mesh.shrinkwrap_smooth"             , "/TP-Align"),
        ("bpy.ops.tp_ops.mirror_over_edge"            , "/TP-Align"),
        ("bpy.ops.object.automirror"                  , "/TP-Align"),
        ("bpy.ops.mesh.align_operator"                  , "/TP-Align"),


        # BOOLEAN #
        ("bpy.ops.tp_ops.bool_union"        , "/TP-Boolean"),
        ("bpy.ops.tp_ops.bool_intersect"    , "/TP-Boolean"),
        ("bpy.ops.tp_ops.bool_difference"   , "/TP-Boolean"),        
        ("bpy.ops.tp_ops.tboolean_union"    , "/TP-Boolean"),
        ("bpy.ops.tp_ops.tboolean_inters"   , "/TP-Boolean"),
        ("bpy.ops.tp_ops.tboolean_diff"     , "/TP-Boolean"),
        ("bpy.ops.tp_ops.tboolean_slice"    , "/TP-Boolean"),
        ("bpy.ops.tp_ops.draw_polybrush"    , "/TP-Boolean"),
        ("bpy.ops.reset.exec"               , "/TP-Boolean"),
        ("bpy.ops.tool.exec"                , "/TP-Boolean"),
        ("bpy.ops.tp_ops.axis_plane"        , "/TP-Boolean"),
        ("bpy.ops.tp_ops.planefit"          , "/TP-Boolean"),
        ("bpy.ops.bpt.boolean_2d_union"     , "/TP-Boolean"),        
        ("bpy.ops.btool.direct_union"       , "/TP-Boolean"),
        ("bpy.ops.btool.direct_intersect"   , "/TP-Boolean"),
        ("bpy.ops.btool.direct_difference"  , "/TP-Boolean"),
        ("bpy.ops.btool.direct_subtract"    , "/TP-Boolean"),
        ("bpy.ops.btool.direct_slice"       , "/TP-Boolean"),
        ("bpy.ops.btool.remove"             , "/TP-Boolean"),
        ("bpy.ops.btool.to_mesh"            , "/TP-Boolean"),

        ("bpy.ops.object.boolean_bevel"                     , "/TP-Boolean"),
        ("bpy.ops.object.boolean_bevel_symmetrize"          , "/TP-Boolean"),
        ("bpy.ops.object.boolean_bevel_make_pipe"           , "/TP-Boolean"),
        ("bpy.ops.tp_ops.cleanup_boolbevel"                 , "/TP-Boolean"),
        ("bpy.ops.object.boolean_bevel_remove_objects"      , "/TP-Boolean"),
        ("bpy.ops.object.boolean_bevel_remove_pipes"        , "/TP-Boolean"),
        ("bpy.ops.object.boolean_bevel_remove_modifiers"    , "/TP-Boolean"),
        ("bpy.ops.object.boolean_bevel_remove_modifiers"    , "/TP-Boolean"),


        # BOUNDING #
        ("bpy.ops.tp_ops.bbox_cube"        , "/TP-Bounding"),
        ("bpy.ops.tp_ops.bbox_cylinder"    , "/TP-Bounding"),
        ("bpy.ops.tp_ops.bbox_sphere"      , "/TP-Bounding"),
        ("bpy.ops.tp_ops.bbox_select_box"  , "/TP-Bounding"),


        # COPY #
        ("bpy.ops.tp_ops.mft_radialclone"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.copy_to_cursor_panel"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.copy_to_meshtarget_pl"     , "/TP-Copy"),
        ("bpy.ops.tp_ops.origin_plus_z"             , "/TP-Copy"),
        ("bpy.ops.object.origin_set"                , "/TP-Copy"),
        ("bpy.ops.tp_ops.origin_minus_z"            , "/TP-Copy"),
        ("bpy.ops.tp_ops.x_array"                   , "/TP-Copy"),
        ("bpy.ops.tp_ops.y_array"                   , "/TP-Copy"),
        ("bpy.ops.tp_ops.z_array"                   , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_array"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_array_mods"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_curve"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_curve_mods"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_curve_array"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_curve_array_mods"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_circle_array"          , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_circle_array_mods"     , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_fpath_curve"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_fpath_con"             , "/TP-Copy"),


        # DEFORM #
        ("bpy.ops.tp_ops.easy_lattice_panel"         , "/TP-Deform"),
        ("bpy.ops.tp_ops.lattice_apply"              , "/TP-Deform"),

        
        # DELETE #
        ("bpy.ops.tp_ops.remove_double"              , "/TP-Delete"),
        ("bpy.ops.tp_ops.remove_all_material"        , "/TP-Delete"),
        ("bpy.ops.tp_ops.delete_data_obs"            , "/TP-Delete"),
        ("bpy.ops.tp_ops.build_corner"               , "/TP-Delete"),
        ("bpy.ops.tp_ops.dissolve_ring"              , "/TP-Delete"),

        # MODIFIER #
        ("bpy.ops.tp_ops.mod_mirror_x"             , "/TP-Modifier"),
        ("bpy.ops.tp_ops.mod_mirror_y"             , "/TP-Modifier"),
        ("bpy.ops.tp_ops.mod_mirror_z"             , "/TP-Modifier"),        
        
        
        # ORIGIN #
        ("bpy.ops.tp_ops.origin_set_center"             , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_set_cursor"             , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_tomesh"                 , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_meshto"                 , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_set_mass"               , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_edm"                    , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_obm"                    , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_ccc"                    , "/TP-Origin"),
        ("bpy.ops.object.bbox_origin_modal_ops"         , "/TP-Origin"),
        ("bpy.ops.tp_ops.zero_axis"                     , "/TP-Origin"),
        ("bpy.ops.object.distribute_osc"                , "/TP-Origin"),
        ("bpy.ops.tp_origin.align_tools"                , "/TP-Origin"),


        # RECOPLANAR #
        ("bpy.ops.tp_ops.set_new_local"          , "/TP-Recoplanar"),
        ("bpy.ops.tp_ops.recenter"               , "/TP-Recoplanar"),
        ("bpy.ops.tp_ops.reposition"             , "/TP-Recoplanar"),
        ("bpy.ops.tp_ops.copy_local_transform"   , "/TP-Recoplanar"),
        ("bpy.ops.object.transforms_to_deltas"   , "/TP-Recoplanar"),
        ("bpy.ops.tp_ops.relocate"               , "/TP-Recoplanar"),
        ("bpy.ops.tp_ops.delete_dummy"           , "/TP-Recoplanar"),


        # SELECTION / MESHCHECK #
        ("bpy.ops.tp_ops.cycle_selected"            , "/TP-Selection"),
        ("bpy.ops.tp_ops.unfreeze_selected"         , "/TP-Selection"),
        ("bpy.ops.tp_ops.freeze_selected"           , "/TP-Selection"),
        ("bpy.ops.object.mesh_all"                  , "/TP-Selection"),
        ("bpy.ops.object.lamp_all"                  , "/TP-Selection"),
        ("bpy.ops.object.curve_all"                 , "/TP-Selection"),
        ("bpy.ops.object.bone_all"                  , "/TP-Selection"),
        ("bpy.ops.object.particles_all"             , "/TP-Selection"),
        ("bpy.ops.object.camera_all"                , "/TP-Selection"),
        ("bpy.ops.tp_meshlint.live_toggle"          , "/TP-Selection"),
        ("bpy.ops.tp_meshlint.select"               , "/TP-Selection"),
        ("bpy.ops.object.face_type_select"          , "/TP-Selection"),

        
         # SNAPSET #       
        ("bpy.ops.tp_ops.place"           , "/TP-SnapSet"),
        ("bpy.ops.tp_ops.grid"            , "/TP-SnapSet"),
        ("bpy.ops.tp_ops.active_3d"       , "/TP-SnapSet"),
        ("bpy.ops.tp_ops.closest_snap"    , "/TP-SnapSet"),
        ("bpy.ops.tp_ops.closest_snap"    , "/TP-SnapSet"),
        ("bpy.ops.tp_ops.active_snap"     , "/TP-SnapSet"),


        )
    return url_manual_prefix, url_manual_mapping


