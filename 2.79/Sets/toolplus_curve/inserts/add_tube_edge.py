# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

#author: Kjartan Tysdal, MKB
#

# LOAD MODUL #   
import bpy, bmesh, random 
from bpy import *
from bpy.props import *

   
class VIEW3D_TP_EdgeTubes(bpy.types.Operator):
        """Creates a spline tube to selected edges""" 
        bl_idname = "tp_ops.edgetubes"                
        bl_label = "Edge Tubes"             
        bl_options = {'REGISTER', 'UNDO', 'PRESET'} 

        bevel = FloatProperty(name="Radius", description="Change width of the tube.", default=0.1, min = 0)
        res = IntProperty(name="Loop", description="Change resolution of the tube.", default=4, min = 0, max = 100)
        ring = IntProperty(name="Ring", description="Change resolution of the tube.", default=0, min = 0, max = 100)
        offset = bpy.props.FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
        height = bpy.props.FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

        fill = EnumProperty(name = "Fill Type",
                items=(('FULL',  "Full",  ""),                                                    
                       ('BACK',  "Back",  ""),                   
                       ('FRONT', "Front", ""),                   
                       ('HALF',  "Half",  "")),                   
                       default='FULL',
                       description="change fill type of spline")      

        handle = EnumProperty(name = "Handle Type",
                items=(('FREE_ALIGN', "Free",    ""),                                                    
                       ('VECTOR',     "Vector",  ""),                   
                       ('ALIGNED',    "Align",   ""),                   
                       ('AUTOMATIC',  "Auto",    "")),                   
                       default='VECTOR',
                       description="change handle type of spline")

        switch_direction = bpy.props.BoolProperty(name="Direction",  description=" ", default=False, options={'SKIP_SAVE'})    
        shade_smooth = bpy.props.BoolProperty(name="Smooth",  description=" ", default=True, options={'SKIP_SAVE'})    
        wire = bpy.props.BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})    

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
            
            row = box.row(1)  
            active_wire = bpy.context.object.show_wire 
            if active_wire == True:
                row.prop(self, "wire", "", icon = 'MESH_PLANE')              
            else:                       
                row.prop(self, "wire", "", icon = 'MESH_GRID') 
            row.prop(self, "bevel", text="Bevel Radius")
            row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  
         
            box.separator()             
           
            row = box.row(1)  
            row.prop(self, "ring", text="Rings")          
            row.prop(self, "res", text="Loops")
        
            row = box.row(1)  
            row.prop(self, "offset", text="Offset")          
            row.prop(self, "height", text="Height")

            box.separator()
            
            row = box.row(1)                  
            row.prop(self, "shade_smooth", text="Smooth") 
            row.prop(self, "handle", text="") 
           
            row = box.row(1)                  
            row.prop(self, "switch_direction", text="Direction")            
            row.prop(self, "fill", text="") 
           
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
                if self.add_objmat == False:
                    if bpy.context.scene.render.engine == 'CYCLES':
                        row.prop(self, "add_cyclcolor", text ="")        
                    else:
                        row.prop(self, "add_color", text ="")          
                else:
                    row.prop(context.object.active_material, "diffuse_color", text="")              

            row.prop(self, "add_random", text ="", icon="FILE_REFRESH")
           
            box.separator()


        def execute(self, context):
                
            mode = bpy.context.active_object.mode
            type = bpy.context.active_object.type
            bevel = self.bevel  
            res = self.res           
            ring = self.ring                   
            offset = self.offset                   
            height = self.height                   
            fill = self.fill                   
            handle = self.handle                   
            shade_smooth = self.shade_smooth           
            switch_direction = self.switch_direction           

            if mode == 'EDIT' and type == 'MESH':
                    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                    bpy.ops.object.duplicate()
                    
                    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                    bpy.ops.mesh.select_all(action='INVERT')
                    bpy.ops.mesh.delete(type='EDGE')
                                      
                    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                    bpy.ops.object.subdivision_set(level=0)
                    bpy.ops.object.convert(target='CURVE')
                    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                    bpy.ops.curve.select_all(action='SELECT')
                    bpy.ops.curve.spline_type_set(type='BEZIER')
                    bpy.ops.curve.handle_type_set(type='AUTOMATIC')

                    # get default values
                    bpy.context.object.data.fill_mode = fill                    
                    bpy.context.object.data.bevel_depth = bevel
                    bpy.context.object.data.bevel_resolution = res
                    bpy.context.object.data.resolution_u = ring
                    bpy.context.object.data.offset = offset
                    bpy.context.object.data.extrude = height
                    bpy.ops.curve.handle_type_set(type=handle)                                        

            elif type == 'CURVE':
       
                    bpy.context.object.data.fill_mode = fill                    
                    bpy.context.object.data.bevel_depth = bevel
                    bpy.context.object.data.bevel_resolution = res
                    bpy.context.object.data.resolution_u = ring
                    bpy.context.object.data.offset = offset
                    bpy.context.object.data.extrude = height
                    bpy.ops.curve.handle_type_set(type=handle)
    
                    
            elif mode != 'EDIT' and type == 'MESH':
                    self.report({'ERROR'}, "This one only works in Edit mode")
                    return {'CANCELLED'}


            if shade_smooth == True: 
                bpy.context.object.data.splines[0].use_smooth = True
            else:
                bpy.context.object.data.splines[0].use_smooth = False
            
            if switch_direction == True: 
                bpy.ops.curve.switch_direction()
         
            # add material with enabled object color
            for i in range(self.add_mat):
                
                bpy.ops.object.mode_set(mode='OBJECT')
               
                active = bpy.context.active_object
                # Get material
                mat = bpy.data.materials.get("Mat_EdgeTube")
                if mat is None:
                    # create material
                    mat = bpy.data.materials.new(name="Mat_EdgeTube")
                else:
                    bpy.ops.object.material_slot_remove()
                    mat = bpy.data.materials.new(name="Mat_EdgeTube")
                         
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

            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            
            if self.wire == True:
                bpy.context.object.show_axis = True
                bpy.context.object.show_wire = True            
            else:
                bpy.context.object.show_axis = False
                bpy.context.object.show_wire = False  
            return {'FINISHED'} 


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()










 
