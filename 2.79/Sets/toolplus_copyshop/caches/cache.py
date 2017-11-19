# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *



# MIFTHTOOLS #  
 
# LOAD CUSTOM TOOL SETTINGS #
def mft_settings_load(self):
    mft_props = bpy.context.window_manager.mifth_clone_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(mft_props, key))

# STORE CUSTOM TOOL SETTINGS #
def mft_settings_write(self):
    mft_props = bpy.context.window_manager.mifth_clone_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(mft_props, key, getattr(self, key))
 


# COPY TO TARGET # 

# LOAD CUSTOM TOOL SETTINGS #
def tot_settings_load(self):
    tot_props = bpy.context.window_manager.totarget_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tot_props, key))

# STORE CUSTOM TOOL SETTINGS #
def tot_settings_write(self):
    tot_props = bpy.context.window_manager.totarget_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tot_props, key, getattr(self, key))


# TO CURSOR # 

# LOAD CUSTOM TOOL SETTINGS #
def toc_settings_load(self):
    toc_props = bpy.context.window_manager.tocursor_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(toc_props, key))

# STORE CUSTOM TOOL SETTINGS #
def toc_settings_write(self):
    toc_props = bpy.context.window_manager.tocursor_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(toc_props, key, getattr(self, key))



# DUPLISET # 
 
# LOAD CUSTOM TOOL SETTINGS #
def dpl_settings_load(self):
    dpl_props = bpy.context.window_manager.dupliset_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(dpl_props, key))

# STORE CUSTOM TOOL SETTINGS #
def dpl_settings_write(self):
    dpl_props = bpy.context.window_manager.dupliset_props
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(dpl_props, key, getattr(self, key))               
 