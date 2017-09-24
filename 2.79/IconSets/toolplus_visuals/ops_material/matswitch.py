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

import bpy, random
from bpy.props import *


class VIEW3D_TP_Visual_SetColors(bpy.types.Operator):
    """switch material color by choosen material id"""  
    bl_idname = "tp_mat.set_colors"
    bl_label = "Set Color"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(self, context):
        if context.object and context.object.type == 'MESH':
            return len(context.object.data.materials)


    matrandom = bpy.props.BoolProperty(name="ID-Switch / ID-Random", description="enable random material", default=False)  

    new_swatch = FloatVectorProperty(name = "Color", default=[0.0,1.0,1.0], min = 0, max = 1,  subtype='COLOR')
    index_count = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0) 

    mat_mode = bpy.props.StringProperty(default="")
    index_count_sw = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)         
    mat_switch = bpy.props.EnumProperty(
                              items = [("tp_mat_00", "Light", "", 1),
                                       ("tp_mat_01", "Darken",  "", 2)],
                                       name = "",
                                       default = "tp_mat_00",  
                                       description="material index switch") 


    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
   
        box = col.box().column(1) 
        
        row = box.row(1)
        row.prop(self, "matrandom", text="ColorSwitch / ColorRandom")                   

        box.separator()

        if self.matrandom == False:

            row = box.row()
            row.prop(self,"index_count_sw")
            row.prop(self,"new_swatch", text="")

            box.separator()   

        else:
            
            row = box.row(1)
            row.prop(self, "index_count")       
            row.prop(self, "mat_switch")       

            row = box.row(1)
            row.operator('tp_mat.set_colors', text='Invert').mat_mode = 'INVERT'
            row.operator('tp_mat.set_colors', text='Repeat')

            box.separator()    
        

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)


    def execute(self, context):

         settings_write(self) # custom props

        # material check with mat-id and color picker type
        #if len(context.object.material_slots) > 0:

         if self.matrandom == False:
             
            ob = bpy.context.object
            try:
               mat = ob.data.materials[self.index_count_sw]
            except IndexError:
                print(self)
                self.report({'INFO'}, "No further Material!")  
                pass
            else:        
                if bpy.context.scene.render.engine == 'BLENDER_RENDER':                   
                    words = self.new_swatch
                    color = (float(words[0]), float(words[1]), float(words[2]))            
                    mat.diffuse_color = color

                else:
                    node=mat.node_tree.nodes['Diffuse BSDF']         
                    words = self.new_swatch
                    RGB = (float(words[0]), float(words[1]), float(words[2]),1) 
                    node.inputs['Color'].default_value = RGB

            
         else:

            ob = context.object
            if self.mat_switch == "tp_mat_00":
                try:
                
                   mat = ob.data.materials[self.index_count]
                except IndexError:
                    print(self)
                    self.report({'INFO'}, "No further Material!")  
                    pass
                else:
                    if bpy.context.scene.render.engine == 'BLENDER_RENDER':                   
                       for i in range(3):
                            mat.diffuse_color[i] = random.random()
                    else:
                        node=mat.node_tree.nodes['Diffuse BSDF']
                        #r = random.randint(0, 20)
                        #g = random.randint(0, 20)
                        #b = random.randint(0, 20)
                        #RGB = (r/255, g/255, b/255, 1)                  
                        RGB = (random.random(),random.random(),random.random(),1)
                        node.inputs['Color'].default_value = RGB


            if self.mat_switch == "tp_mat_01":
                try:
                   mat = ob.data.materials[self.index_count]
                except IndexError:
                    print(self)
                    self.report({'INFO'}, "No further Material!")  
                    pass
                else:
                    if bpy.context.scene.render.engine == 'BLENDER_RENDER':
                        for i in range(3):
                            mat.diffuse_color[i] *= random.random()  
                    else:
                        node=mat.node_tree.nodes['Diffuse BSDF']
                        for i in range(3):
                            node.inputs['Color'].default_value[i] *= random.random()  

                    
            if "INVERT" in self.mat_mode:           
                try:
                   mat = ob.data.materials[self.index_count]
                except IndexError:
                    print(self)
                    self.report({'INFO'}, "No further Material!")  
                    pass
                else:
                    for i in range(3):
                        mat.diffuse_color[i] = 1 - mat.diffuse_color[i]
                    
        #else:
            #pass
            
         return{'FINISHED'}   




# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    tp = bpy.context.window_manager.tp_props_visual
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, key))



# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp = bpy.context.window_manager.tp_props_visual
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, key, getattr(self, key))
 


# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
