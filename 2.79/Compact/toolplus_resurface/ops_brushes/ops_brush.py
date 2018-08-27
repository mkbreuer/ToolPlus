# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

from bpy.types import Operator
from bpy.types import Menu, Panel, UIList

import os

root = bpy.utils.script_path_user()
sep = os.sep

    

def execscript(listebrush = []):
    lien = root + sep + "addons" + sep + "toolplus_resurface" + sep + "ops_brushes" + sep + "ops_brush.py"
    bpy.ops.script.python_file_run( filepath = lien )

class VIEW3D_TP_Reload_Brushes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "tp_ops.reload_brushes"
    bl_label = "Reload"
 
    def execute(self, context):
        execscript()
        return {'FINISHED'}



def execscriptik():
    lien = root + sep + "addons" + sep + "toolplus_resurface" + sep + "ops_brushes" + sep + "ops_load.py"
    bpy.ops.script.python_file_run( filepath = lien )

class VIEW3D_TP_Load_Brushes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "tp_ops.load_brushes"
    bl_label = "Load IK Brushes"
 
    def execute(self, context):
        execscriptik()
        return {'FINISHED'}





if __name__ == "__main__":  # only for live edit.
    bpy.utils.register_module(__name__)  
    