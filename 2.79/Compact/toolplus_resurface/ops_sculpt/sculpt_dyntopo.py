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
import bmesh
from bpy import *
from bpy.props import *    


bpy.types.Scene.expand_mask = bpy.props.IntProperty(name="Expand Mask",  description="expand mask for dyntopo details", min=0, max=10, default=2) 

class VIEW3D_TP_Add_Dyntopo_Details(bpy.types.Operator):
    """add dyntopo details after boolean"""
    bl_idname = "tp_ops.add_dyntopo_details"
    bl_label = "Add Details"
    bl_options = {"REGISTER","UNDO"}


    def execute(self, context):
        
        obj = context.active_object
        paint = context.tool_settings.image_paint
       
        bpy.ops.object.mode_set(mode='OBJECT')             
       
        obj_list = [obj for obj in bpy.context.selected_objects]
        
        obj = context.active_object
        for obj in obj_list:  
            bpy.context.scene.objects.active = obj
            obj.select = True
            
            # remove groups
            for vgroup in obj.vertex_groups:
                if vgroup.name.startswith("B"):
                    obj.vertex_groups.remove(vgroup)
            
            bpy.ops.object.mode_set(mode='SCULPT')            
            bpy.ops.paint.hide_show(action='HIDE', area='MASKED')

            bpy.ops.object.mode_set(mode='EDIT')      
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.normals_make_consistent()
            bpy.ops.mesh.remove_doubles(threshold=0.05)
            
            scene = bpy.context.scene            
            for i in range(scene.expand_mask):
                bpy.ops.mesh.select_more()

            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.reveal()                           
            
            # add group
            obj.vertex_groups.new("Blob_Mask")
            for vgroup in obj.vertex_groups:
                if vgroup.name.startswith("B"):
                    bpy.ops.object.vertex_group_assign()
                    
            bpy.ops.object.mode_set(mode='OBJECT')        


        bpy.ops.sculpt.sculptmode_toggle()

        ###
        # create mask from vertgroup from masktools by Stanislav Blinov,Yigit Savtur           
        bmeshContainer = bmesh.new() # New bmesh container
        bmeshContainer.from_mesh(context.active_object.data) # Fill container with our object
        activeVertexGroup = context.active_object.vertex_groups.active  # Set active vgroup
        mask = bmeshContainer.verts.layers.paint_mask.verify() # get active mask layer
        bmeshContainer.verts.ensure_lookup_table() # Update vertex lookup table
       
        for x in context.active_object.data.vertices: # For each x vert
           
           bmeshContainer.verts[x.index] [mask] = 0.0 # Set mask to 0 weight
           
           if len(x.groups) > 0: # if vert is a member of a vgroup
            
            for y in x.groups: # For each y vgroup in group list
               
               if y.group == activeVertexGroup.index: # if y is active group x belongs to
                  
                  if activeVertexGroup.weight(x.index) > 0 :  # and x vert weight is not zero
                     
                     currVert = bmeshContainer.verts[x.index]  # current vert is x bmesh vert
                     maskWeight = activeVertexGroup.weight(x.index) # set weight from active vgroup                     
                     currVert[mask] = maskWeight # assign weight to custom data layer
                   
        bmeshContainer.to_mesh(context.active_object.data) # Fill obj data with bmesh data    
        bmeshContainer.free() # Release bmesh
        ###

        dynatopoEnabled = False
        if context.sculpt_object.use_dynamic_topology_sculpting:           
          dynatopoEnabled = True           

        if dynatopoEnabled == False:           
            bpy.ops.sculpt.dynamic_topology_toggle()
            bpy.context.scene.tool_settings.sculpt.detail_size = 4
            bpy.context.scene.tool_settings.sculpt.use_smooth_shading = True
        else:
            pass

        bpy.ops.paint.brush_select(sculpt_tool='BLOB')
        bpy.data.brushes["Blob"].strength = 0
        bpy.data.brushes["Smooth"].strength = 0.3
        
        return {"FINISHED"}   



# REGISTRY #        
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()