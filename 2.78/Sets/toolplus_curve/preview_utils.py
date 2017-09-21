import bpy, os
from os import listdir
from os.path import isfile, join
from bpy.props import *
from bpy.types import WindowManager

from . curve_insert import tp_curve_preview_insert


TP_Curves_Insert_Preview_collections = {}

def enumPreviewsFromDirectoryItems(self, context):
    """EnumProperty callback"""
    enum_items = []
 
    if context is None:
        return enum_items
   
    directory = join(os.path.dirname(__file__), "icons","tp_insert") 
    # Get the preview collection (defined in register func).
    pcoll = TP_Curves_Insert_Preview_collections["main"]
 
    if directory == pcoll.TP_Curves_Insert_Previews_dir:
        return pcoll.TP_Curves_Insert_Previews
 
    if directory and os.path.exists(directory):
        # Scan the directory for png files
        image_paths = []
        for fn in os.listdir(directory):
            if fn.lower().endswith(".png"):
                image_paths.append(fn)
 
        for i, name in enumerate(image_paths):
            # generates a thumbnail preview for a file.
            filepath = os.path.join(directory, name)
            thumb = pcoll.load(filepath, filepath, 'IMAGE')
            enum_items.append((name, name, "", thumb.icon_id, i))
 
    pcoll.TP_Curves_Insert_Previews = enum_items
    pcoll.TP_Curves_Insert_Previews_dir = directory
 
    return pcoll.TP_Curves_Insert_Previews


 
def register_TP_Curve_pcoll():  
 
    WindowManager.TP_Curves_Insert_Previews = EnumProperty(items=enumPreviewsFromDirectoryItems, update=tp_curve_preview_insert)
 
    import bpy.utils.previews
    wm = bpy.context.window_manager
    pcoll = bpy.utils.previews.new()
    pcoll.TP_Curves_Insert_Previews_dir = ""
    pcoll.TP_Curves_Insert_Previews = ()

    TP_Curves_Insert_Preview_collections["main"] = pcoll
 
 
def unregister_TP_Curve_pcoll():
    from bpy.types import WindowManager
 
    del WindowManager.TP_Curves_Insert_Previews
 
    for pcoll in TP_Curves_Insert_Preview_collections.values():
        bpy.utils.previews.remove(pcoll)

    TP_Curves_Insert_Preview_collections.clear()    

