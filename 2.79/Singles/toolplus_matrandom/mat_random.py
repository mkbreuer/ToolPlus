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


bl_info = {
    "name": "MAT-Random",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 1),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] > MAT-Random Panel",
    "description": "simple material randomizer > random, darken or invert the color(based on cookbook) > added random for cycles materials",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "https://wiki.blender.org/index.php/Dev:Py/Scripts/Cookbook/Code_snippets/Interface",
    "category": "ToolPlus"}


# LOAD MODULE #
import bpy
import random
from bpy import*
from bpy.props import *
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #
panels = (VIEW3D_TP_MATRANDOM_Panel_UI, VIEW3D_TP_MATRANDOM_Panel_TOOLS)

def update_panel_location(self, context):
    message = "LoopTools: Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':            
            VIEW3D_TP_MATRANDOM_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category        
            bpy.utils.register_class(VIEW3D_TP_MATRANDOM_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
            bpy.utils.register_class(VIEW3D_TP_MATRANDOM_Panel_UI)
      
        if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
            return None

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass




# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    # TAB LOACATION #           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location)

    # UPADTE: PANEL #
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)

    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)
         
        row = box.row(1)  
        row.label("Location: Panel")
        
        row= box.row(1)
        row.prop(self, 'tab_location', expand=True)

        box.separator()
                                           
        if self.tab_location == 'tools':
            
            row = box.row(1)                                                
            row.prop(self, "tools_category")
     
        box.separator()




# PANEL LOCATION #
EDIT = ["OBJECT", "EDIT_MESH"]

class VIEW3D_TP_MATRANDOM_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_MATRANDOM_Panel_TOOLS"
    bl_label = "MAT-Random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode and context.mode in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        draw_madrandom_panel_layout(self, context, layout) 


class VIEW3D_TP_MATRANDOM_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_MATRANDOM_Panel_UI"
    bl_label = "MAT-Random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode and context.mode in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        draw_madrandom_panel_layout(self, context, layout) 


# PANEL LAYOUT #
def draw_madrandom_panel_layout(self, context, layout):
    tp_props = context.window_manager.tp_props_madrandom 

    col = layout.column(align = True)
   
    box = col.box().column(1) 
    row = box.row(1)
    row.prop(tp_props, "index_count")       
    row.prop(tp_props, "mat_switch")       

    row = box.row(1)
    row.operator('tp_mat.random_mat', text='Invert').mat_mode = 'INVERT'
    row.operator('tp_mat.random_mat', text='Repeat')




# OPERATOR #
class VIEW3D_TP_MAD_Random(bpy.types.Operator):
    """invert or random material by choosen material index""" 
    bl_idname = "tp_mat.random_mat"
    bl_label = "MAT-Random"
    bl_options = {'REGISTER', 'UNDO'} 

    index_count = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)    
 
    mat_switch = bpy.props.EnumProperty(
                              items = [("tp_mat_00", "Light", "", 1),
                                       ("tp_mat_01", "Darken",  "", 2)],
                                       name = "",
                                       default = "tp_mat_00",  
                                       description="material index switch") 
  
    mat_mode = bpy.props.StringProperty(default="")


    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)


    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        col = layout.column(align = True)
   
        box = col.box().column(1) 
        row = box.row(1)
        row.prop(self, "index_count")       
        row.prop(self, "mat_switch")       

        row = box.row(1)
        row.operator('tp_mat.random_mat', text='Invert').mat_mode = 'INVERT'
        row.operator('tp_mat.random_mat', text='Repeat')


    # PERFORMING #    
    def execute(self, context):

        # load custom panel props:
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
    tp = bpy.context.window_manager.tp_props_madrandom
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, key))



# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp = bpy.context.window_manager.tp_props_madrandom
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, key, getattr(self, key))
 
     

# PROPS #
class Dropdown_MadRandom_Props(bpy.types.PropertyGroup):

    index_count = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)    
 
    mat_switch = bpy.props.EnumProperty(
                              items = [("tp_mat_00", "Light", "", 1),
                                       ("tp_mat_01", "Darken",  "", 2)],
                                       name = "",
                                       default = "tp_mat_00",  
                                       description="material index switch") 
  
    mat_mode = bpy.props.StringProperty(default="")




# ADD TO DEFAULT SPECIAL MENU [W] #  
def draw_madrandom_item(self, context):
    icons = load_icons()

    layout = self.layout

    layout.separator() 
    layout.operator("tp_mat.random_mat") 



# REGISTRY #
import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
    
    # PANEL LOCATION
    update_panel_location(None, bpy.context)
    
    # TO MENU
    bpy.types.VIEW3D_MT_object_specials.append(draw_madrandom_item) 
   
    # PROPS
    bpy.types.WindowManager.tp_props_madrandom = bpy.props.PointerProperty(type = Dropdown_MadRandom_Props)    



def unregister():

    # PROPS    
    del bpy.types.WindowManager.tp_display_madrandom

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()


if __name__ == "__main__":
    register()
        
        

