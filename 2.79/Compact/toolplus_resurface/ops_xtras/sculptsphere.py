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


# MAIN OPERATOR #

class VIEW3D_TP_Sculpt_Sphere(bpy.types.Operator):
    """create a sphere from a cube"""
    bl_idname = "tp_ops.sculpt_sphere"
    bl_label = "Sculpt Sphere"
    bl_options = {"REGISTER", 'UNDO'}

    cb_radius = bpy.props.FloatProperty(name="Radius",  description="cube radius", default=10, min=0.01, max=100)
    cuts = bpy.props.IntProperty(name="Subdivide",  description="subdivide ", min=0, max=100, default=5) 
    smooth = bpy.props.FloatProperty(name="Smoothness",  description="subdiv smooth", default=1.00, min=0.00, max=1.00)

    edit = bpy.props.BoolProperty(name="Edit",  description="editmode toggle", default=False, options={'SKIP_SAVE'})     
    shading = bpy.props.BoolProperty(name="Smooth",  description="editmode toggle", default=False, options={'SKIP_SAVE'})     
      
    def draw(self, layout):
        layout = self.layout
        
        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'cb_radius')   
        row.prop(self, 'cuts')
        row.prop(self, 'smooth')  

        row = box.row(1)
        row.prop(self, 'edit') # ,text=" ", icon="", expand =True)   
        row.prop(self, 'shading') # ,text=" ", icon="", expand =True)   

        box.separator()


    def execute(self, context):
            

        if context.mode == 'SCULPT' :
            
            oldmode = bpy.context.mode        
            bpy.ops.object.mode_set(mode='OBJECT')              
                   
#            selected = bpy.context.selected_objects
#            n = len(selected)                         
#            if n > 0:
#                bpy.ops.view3d.snap_cursor_to_selected()

            bpy.ops.mesh.primitive_cube_add(radius=self.cb_radius, view_align=False, enter_editmode=True)
            
            bpy.ops.mesh.subdivide(number_cuts=self.cuts, smoothness=self.smooth)
           
            bpy.ops.object.editmode_toggle()

            for i in range(self.edit):           
                bpy.ops.object.editmode_toggle()

            for i in range(self.shading):  
                if context.mode == 'EDIT_MESH' :
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.faces_shade_smooth()
                else:      
                    bpy.ops.object.shade_smooth()

            
            #bpy.ops.object.mode_set(mode=oldmode)


        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()