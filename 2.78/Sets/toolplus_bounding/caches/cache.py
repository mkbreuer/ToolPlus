# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *



    
# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    tp = bpy.context.window_manager.tp_props_bbox
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, key))



# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp = bpy.context.window_manager.tp_props_bbox
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, key, getattr(self, key))
 
