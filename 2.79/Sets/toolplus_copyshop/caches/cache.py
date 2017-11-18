# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *



    
# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    mft_props = bpy.context.window_manager.mifth_clone_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(mft_props, key))



# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    mft_props = bpy.context.window_manager.mifth_clone_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(mft_props, key, getattr(self, key))
 
