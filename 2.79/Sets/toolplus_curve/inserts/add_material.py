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
import random




class VIEW3D_TP_Curve_Extrude(bpy.types.Operator):
    """create 2d bevel extrude on curve"""
    bl_idname = "tp_ops.curve_extrude"
    bl_label = "Curve Extrude"
    bl_options = {"REGISTER", "UNDO"}


    # MATERIAL #
    add_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)        
    add_random = bpy.props.BoolProperty(name="Add Random",  description="add random material", default=False, options={'SKIP_SAVE'})    
    add_objmat = bpy.props.BoolProperty(name="Add Material",  description="add material", default=False, options={'SKIP_SAVE'})    
    add_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    add_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    def draw(self, context):      
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(1)             

        box.separator()        
       
        row = box.row(1)                                                                                                                                                                                                                    
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(self, 'depth')
 
        if self.wire == True:
            row.prop(self, 'wire', "", icon = 'MESH_PLANE')              
        else:                       
           row.prop(self, 'wire', "", icon = 'MESH_GRID') 
                    
        row = box.row(1)
        row.prop(self, 'ring')  
        row.prop(self, 'loop')

        row = box.row(1)
        row.prop(self, 'offset')  
        row.prop(self, 'height')
    
        box.separator()
                    
        row = box.row(1) 
        row.prop(self, "add_mat", text ="")                    
        row.label(text="Color:") 
     
        row.prop(self, "add_objmat", text ="", icon="GROUP_VCOL")
        if self.add_random == False:                   
            if self.add_objmat == False:
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(self, "add_cyclcolor", text ="")        
                else:
                    row.prop(self, "add_color", text ="")          
            else:
                row.prop(context.object.active_material, "diffuse_color", text="")  
        else:
            row.prop(context.object.active_material, "diffuse_color", text="")
       
        row.prop(self, "add_random", text ="", icon="FILE_REFRESH")
       
        box.separator()



    def execute(self, context):

        settings_write(self) 
 
        # add material
        for i in range(self.add_mat):
            bpy.ops.object.mode_set(mode = 'OBJECT')
           
            # Get material
            active = bpy.context.active_object
            mat = bpy.data.materials.get("Mat_Lathe")
            if mat is None:
                # create material
                mat = bpy.data.materials.new(name="Mat_Lathe")
            else:
                bpy.ops.object.material_slot_remove()
                mat = bpy.data.materials.new(name="Mat_Lathe")
                     
            # Assign it to object
            if len(active.data.materials):
                # assign to 1st material slot
                active.data.materials[0] = mat
            else:
                # no slots
                active.data.materials.append(mat)
                        

            # toggle random
            if self.add_random == False:            
                                
                # toggle color target
                if self.add_objmat == False: 
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        mat.diffuse_color = (self.add_cyclcolor)                        
                    else:
                        mat.use_object_color = True
                        bpy.context.object.color = (self.add_color)
                else:                                      
                    # regular material
                    pass
          
            else: 
                
                # toggle color target
                if self.add_objmat == False:   
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            mat.diffuse_color = RGB                       
                    else:
                        mat.use_object_color = True
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            bpy.context.object.color = RGB
               
                else:        
                    # regular material    
                    if bpy.context.scene.render.engine == 'CYCLES':
                        node=mat.node_tree.nodes['Diffuse BSDF']
                        for i in range(3):
                            node.inputs['Color'].default_value[i] *= random.random()             
                    else:
                        for i in range(3):
                            mat.diffuse_color[i] *= random.random()   














