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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *

# BOUNDING #  
    
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
 