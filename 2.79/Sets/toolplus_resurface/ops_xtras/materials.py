# ##### BEGIN GPL LICENSE BLOCK #####
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


# LOAD MODULE #
import bpy, random
from bpy import*
from bpy.props import *

    

# remove all materials slots   
def remove_material_slots():
    bpy.ops.object.mode_set(mode='OBJECT')

    obj = bpy.context.object

    for i in range(0,len(obj.material_slots)):
        obj.active_material_index = 0
        bpy.ops.object.material_slot_remove()

    for i in range(0,len(obj.material_slots)):
        obj.active_material_index = 1
        bpy.ops.object.material_slot_remove()

    for i in range(0,len(obj.material_slots)):
        obj.active_material_index = 2
        bpy.ops.object.material_slot_remove()

    for i in range(0,len(obj.material_slots)):
        obj.active_material_index = 3
        bpy.ops.object.material_slot_remove()

    for i in range(0,len(obj.material_slots)):
        obj.active_material_index = 4
        bpy.ops.object.material_slot_remove()

    bpy.ops.object.mode_set(mode='EDIT')



def tbhl_create_material_0():

    # Get material
    mat = bpy.data.materials.get("XMat_idx0")

    #if it doesnt exist, create it.
    if mat is None:
        
        if bpy.context.scene.render.engine == 'BLENDER_RENDER':
            mat_name = "XMat_idx0"
            mat = bpy.data.materials.new(mat_name)
            mat.diffuse_shader = 'MINNAERT'
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            mat.darkness = 0.8       
            bpy.context.space_data.viewport_shade = 'SOLID'

        else:
            mat_name = "XMat_idx0"
            materials = bpy.data.materials        
            mat = materials.get(mat_name) or materials.new(mat_name)           
            mat.use_nodes = True
            nodes = mat.node_tree.nodes 
            node = nodes.new('ShaderNodeBsdfDiffuse')
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            node.location = (100,100)
            bpy.context.space_data.viewport_shade = 'MATERIAL'
    
    return mat
 

def tbhl_create_material_1():

    # Get material
    mat = bpy.data.materials.get("XMat_idx1")

    #if it doesnt exist, create it.
    if mat is None:
        
        if bpy.context.scene.render.engine == 'BLENDER_RENDER':
            mat_name = "XMat_idx1"
            mat = bpy.data.materials.new(mat_name)
            mat.diffuse_shader = 'MINNAERT'
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            mat.darkness = 0.8       
            bpy.context.space_data.viewport_shade = 'SOLID'

        else:
            mat_name = "XMat_idx1"
            materials = bpy.data.materials        
            mat = materials.get(mat_name) or materials.new(mat_name)           
            mat.use_nodes = True
            nodes = mat.node_tree.nodes 
            node = nodes.new('ShaderNodeBsdfDiffuse')
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            node.location = (100,100)
            bpy.context.space_data.viewport_shade = 'MATERIAL'
       
    return mat


def tbhl_create_material_2():

    # Get material
    mat = bpy.data.materials.get("XMat_idx2")

    #if it doesnt exist, create it.
    if mat is None:
        
        if bpy.context.scene.render.engine == 'BLENDER_RENDER':
            mat_name = "XMat_idx2"
            mat = bpy.data.materials.new(mat_name)
            mat.diffuse_shader = 'MINNAERT'
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            mat.darkness = 0.8       
            bpy.context.space_data.viewport_shade = 'SOLID'

        else:
            mat_name = "XMat_idx2"
            materials = bpy.data.materials        
            mat = materials.get(mat_name) or materials.new(mat_name)           
            mat.use_nodes = True
            nodes = mat.node_tree.nodes 
            node = nodes.new('ShaderNodeBsdfDiffuse')
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            node.location = (100,100)
            bpy.context.space_data.viewport_shade = 'MATERIAL'
       
    return mat



def tbhl_create_material_3():

    # Get material
    mat = bpy.data.materials.get("XMat_idx3")

    #if it doesnt exist, create it.
    if mat is None:
        
        if bpy.context.scene.render.engine == 'BLENDER_RENDER':
            mat_name = "XMat_idx3"
            mat = bpy.data.materials.new(mat_name)
            mat.diffuse_shader = 'MINNAERT'
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            mat.darkness = 0.8       
            bpy.context.space_data.viewport_shade = 'SOLID'

        else:
            mat_name = "XMat_idx3"
            materials = bpy.data.materials        
            mat = materials.get(mat_name) or materials.new(mat_name)           
            mat.use_nodes = True
            nodes = mat.node_tree.nodes 
            node = nodes.new('ShaderNodeBsdfDiffuse')
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            node.location = (100,100)
            bpy.context.space_data.viewport_shade = 'MATERIAL'
       
    return mat



def tbhl_create_material_4():

    # Get material
    mat = bpy.data.materials.get("XMat_idx4")

    #if it doesnt exist, create it.
    if mat is None:
        
        if bpy.context.scene.render.engine == 'BLENDER_RENDER':
            mat_name = "XMat_idx4"
            mat = bpy.data.materials.new(mat_name)
            mat.diffuse_shader = 'MINNAERT'
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            mat.darkness = 0.8       
            bpy.context.space_data.viewport_shade = 'SOLID'

        else:
            mat_name = "XMat_idx4"
            materials = bpy.data.materials        
            mat = materials.get(mat_name) or materials.new(mat_name)           
            mat.use_nodes = True
            nodes = mat.node_tree.nodes 
            node = nodes.new('ShaderNodeBsdfDiffuse')
            #mat.diffuse_color = (0.5, 0.5, 0.5)
            mat.diffuse_color = (random.random(), random.random(), random.random())
            node.location = (100,100)
            bpy.context.space_data.viewport_shade = 'MATERIAL'
       
    return mat



    
