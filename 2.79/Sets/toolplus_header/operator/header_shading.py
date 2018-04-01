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

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from bpy_extras import view3d_utils




class VIEW3D_TP_Header_AOCCL(bpy.types.Menu):
    """Ambient Occlusion"""
    bl_idname = "tp_ops.aoccl_ops"
    bl_label = " Ambient Occlusion"
    bl_options = {'REGISTER', 'UNDO'}


    def draw(self, context):
        layout = self.layout

        layout.prop(context.space_data.fx_settings.ssao, "factor")
        layout.prop(context.space_data.fx_settings.ssao, "distance_max")
        layout.prop(context.space_data.fx_settings.ssao, "attenuation")
        layout.prop(context.space_data.fx_settings.ssao, "samples")
        layout.prop(context.space_data.fx_settings.ssao, "color","")               
                

    


class VIEW3D_TP_Header_AOCCL_Set(bpy.types.Operator):
    """click: default ruler / shift+click: np distance point"""
    bl_idname = "tp_ops.aoccl_set"
    bl_label = " SSAO"
    bl_options = {'REGISTER', 'UNDO'}

#    @classmethod
#    def poll(cls, context):
#        return context.active_object is not None

    def invoke(self, context, event):

        ev = []
        ev.append("Click")  

        if event.shift:
            ev.append("Shift")
       
            active_ssao = bpy.context.space_data.fx_settings.use_ssao 
            if active_ssao == True:
                bpy.context.space_data.fx_settings.use_ssao = False
            else:
                bpy.context.space_data.fx_settings.use_ssao = True
            
            self.report({'INFO'}, "SSAO")


        else:
             

            bpy.ops.tp_ops.aoccl_ops()
 
            self.report({'INFO'}, "SSAO SET")      
 

        #self.report({'INFO'}, "+".join(ev))

        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()