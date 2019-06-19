# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


 # RIGHT CLICK BUTTON TO ONLINE MANUAL
def VIEW3D_MT_OriginSet_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/ToolPlus/wiki"
    url_manual_mapping = (
        ("bpy.ops.tpc_ops.set_origin_to"                 , "/TP-Origin"),
        ("bpy.ops.tpc_ops.snaporigin_modal"              , "/TP-Origin"),
        ("bpy.ops.tpc_ops.origin_to_snap_helper"         , "/TP-Origin"),
        ("bpy.ops.tpc_ops.origin_ccc"                    , "/TP-Origin"),
        ("bpy.ops.tpc_ops.snap_to_bbox"                  , "/TP-Origin"),
        ("bpy.ops.tpc_ops.origin_to_bounding_box"        , "/TP-Origin"),
        ("bpy.ops.tp_ops.zero_axis"                     , "/TP-Origin"),
        ("bpy.ops.tpc_ops.distribute_objects"            , "/TP-Origin"),
        ("bpy.ops.tpc_ops.advanced_align_tools"          , "/TP-Origin"),
        ("bpy.ops.tpc_ops.origin_transform"              , "/TP-Origin"),
        ("bpy.data.window_managers.bbox_origin_window.display_origin_box"      , "/TP-Origin"),
        ("bpy.data.window_managers.bbox_origin_window.display_origin_editbox"  , "/TP-Origin"),
        )
    return url_manual_prefix, url_manual_mapping


