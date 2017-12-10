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


# LOAD MODUL #    
import bpy, random
from bpy import *
from bpy.props import *


class VIEW3D_TP_Visual_Set_Color(bpy.types.Operator):
    """switch material color by choosen material id"""  
    bl_idname = "tp_mat.set_colors"
    bl_label = "Set Color"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(self, context):
        if context.object and context.object.type == 'MESH':
            return len(context.object.data.materials)

    new_swatch = FloatVectorProperty(name = "Color", default=[0.0,1.0,1.0], min = 0, max = 1,  subtype='COLOR')
    index_count_sw = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)    

    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
   
        box = col.box().column(1) 

        row = box.row()
        row.prop(self,"index_count_sw")
        row.prop(self,"new_swatch", text="")

        box.separator()   

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    def execute(self, context):

        settings_write(self)

        mat_activ = context.object.active_material
        if mat_activ:
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
            print(self)
            self.report({'INFO'}, "Not possible!")              
                       
        return{'FINISHED'}   





class VIEW3D_TP_Visual_Set_Color_Contrast(bpy.types.Operator):
    """switch material color by choosen material id"""  
    bl_idname = "tp_mat.set_color_constrast"
    bl_label = "Set Color Constrast"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(self, context):
        if context.object and context.object.type == 'MESH':
            return len(context.object.data.materials)

    mat_mode = bpy.props.StringProperty(default="")
    index_count = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)      
    mat_switch = bpy.props.EnumProperty(
                              items = [("tp_mat_00", "Light", "", 1),
                                       ("tp_mat_01", "Darken",  "", 2)],
                                       name = "Contrast",
                                       default = "tp_mat_00",  
                                       description="material index switch") 

    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
   
        box = col.box().column(1) 
        
        row = box.row(1)
        row.prop(self, "index_count")       
        row.prop(self, "mat_switch", text="")       

        row = box.row(1)
        row.operator('tp_mat.set_color_constrast', text='Invert', icon ="FILE_REFRESH").mat_mode = 'INVERT'
        row.operator('tp_mat.set_color_constrast', text='Repeat', icon ="COLOR")

        box.separator()    
    

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)


    def execute(self, context):

        settings_write(self) 

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

        return{'FINISHED'}   




# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    tp_props = bpy.context.window_manager.tp_props_display
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp_props, key))



# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp_props = bpy.context.window_manager.tp_props_display
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp_props, key, getattr(self, key))
 


# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
