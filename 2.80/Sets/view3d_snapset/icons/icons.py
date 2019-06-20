import os
import bpy
import bpy.utils.previews

mkb_icon_collections = {}
mkb_icons_loaded = False

def load_icons():
    global mkb_icon_collections
    global mkb_icons_loaded

    if mkb_icons_loaded: return mkb_icon_collections["main"]

    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__))

    #--------------------------------------------

    mkb_icons.load("icon_snap_active", os.path.join(icons_dir, "snap_active.png"), 'IMAGE')
    mkb_icons.load("icon_snap_closest", os.path.join(icons_dir, "snap_closest.png"), 'IMAGE')
    mkb_icons.load("icon_snap_cursor", os.path.join(icons_dir, "snap_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid", os.path.join(icons_dir, "snap_grid.png"), 'IMAGE')
    mkb_icons.load("icon_snap_retopo", os.path.join(icons_dir, "snap_retopo.png"), 'IMAGE')
    mkb_icons.load("icon_snap_place", os.path.join(icons_dir, "snap_place.png"), 'IMAGE')
    mkb_icons.load("icon_snap_set", os.path.join(icons_dir, "snap_set.png"), 'IMAGE')
    mkb_icons.load("icon_snap_move", os.path.join(icons_dir, "snap_move.png"), 'IMAGE')
    mkb_icons.load("icon_snap_rotate", os.path.join(icons_dir, "snap_rotate.png"), 'IMAGE')
    mkb_icons.load("icon_snap_scale", os.path.join(icons_dir, "snap_scale.png"), 'IMAGE')
    mkb_icons.load("icon_snap_measure", os.path.join(icons_dir, "snap_measure.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate", os.path.join(icons_dir, "snap_annotate.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate_line", os.path.join(icons_dir, "snap_annotate_line.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate_polygon", os.path.join(icons_dir, "snap_annotate_polygon.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate_eraser", os.path.join(icons_dir, "snap_annotate_eraser.png"), 'IMAGE')

    #--------------------------------------------

    mkb_icon_collections["main"] = mkb_icons
    mkb_icons_loaded = True

    return mkb_icon_collections["main"]

def clear_icons():
    global mkb_icons_loaded
    for icon in mkb_icon_collections.values():
        bpy.utils.previews.remove(icon)
    mkb_icon_collections.clear()
    mkb_icons_loaded = False