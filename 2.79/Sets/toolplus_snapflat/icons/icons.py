import os
import bpy
import bpy.utils.previews

toolplus_icon_collections = {}
toolplus_icons_loaded = False

def load_icons():
    global toolplus_icon_collections
    global toolplus_icons_loaded

    if toolplus_icons_loaded: return toolplus_icon_collections["main"]

    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__))

    #--------------------------------------------

    mkb_icons.load("icon_snap_active", os.path.join(icons_dir, "snap_active.png"), 'IMAGE')
    mkb_icons.load("icon_snap_closest", os.path.join(icons_dir, "snap_closest.png"), 'IMAGE')
    mkb_icons.load("icon_snap_cursor", os.path.join(icons_dir, "snap_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid", os.path.join(icons_dir, "snap_grid.png"), 'IMAGE')
    mkb_icons.load("icon_snap_retopo", os.path.join(icons_dir, "snap_retopo.png"), 'IMAGE')
    mkb_icons.load("icon_snap_place", os.path.join(icons_dir, "snap_place.png"), 'IMAGE')
    mkb_icons.load("icon_snap_flat", os.path.join(icons_dir, "snap_flat.png"), 'IMAGE')
    mkb_icons.load("icon_snap_measure", os.path.join(icons_dir, "snap_measure.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate", os.path.join(icons_dir, "snap_annotate.png"), 'IMAGE')


    #--------------------------------------------

    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
    global toolplus_icons_loaded
    for icon in toolplus_icon_collections.values():
        bpy.utils.previews.remove(icon)
    toolplus_icon_collections.clear()
    toolplus_icons_loaded = False