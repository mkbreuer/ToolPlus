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
import mathutils, bmesh




class VIEW3D_TP_Add_Displace_Noise(bpy.types.Operator):
    """add displace noise"""
    bl_idname = "tp_ops.add_displace_noise"
    bl_label = "Add Noise"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        obj = context.active_object

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # get or add texture
        gettex = bpy.data.textures.get("Sculpt_Noise")   
        if not gettex:          
            noisetex = bpy.data.textures.new('Sculpt_Noise', type = 'MUSGRAVE')

        # get or add displace
        getmod = bpy.context.object.modifiers.get("Displace")   
        if not getmod:           
            noisetex = bpy.data.textures['Sculpt_Noise']
            
            dispMod = obj.modifiers.new("Displace", type='DISPLACE')
            dispMod.texture = noisetex
            dispMod.strength = 0.5

        bpy.ops.object.mode_set(mode=oldmode)        
        return {"FINISHED"}
        


class VIEW3D_TP_Paint_Displace_Mask(bpy.types.Operator):
    """paint displace mask"""
    bl_idname = "tp_ops.displace_mask_paint"
    bl_label = "Paint Displace Mask"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        
        obj = context.active_object
        paint = context.tool_settings.image_paint
        bpy.context.object.modifiers["Displace"].show_viewport = False
        bpy.ops.paint.brush_select(sculpt_tool='MASK')    
       
        return {"FINISHED"}   

        
class VIEW3D_TP_Displace_Mask(bpy.types.Operator):
    """displace the masking areas"""
    bl_idname = "tp_ops.displace_mask_areas"
    bl_label = "Displace Mask"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.context.object.modifiers["Displace"].show_viewport = False          
       
        bpy.ops.object.mode_set(mode='OBJECT')             
       
        obj_list = [obj for obj in bpy.context.selected_objects]
        
        obj = context.active_object
        for obj in obj_list:  
            bpy.context.scene.objects.active = obj
            obj.select = True
            
            # remove groups
            for vgroup in obj.vertex_groups:
                if vgroup.name.startswith("D"):
                    obj.vertex_groups.remove(vgroup)
            
            bpy.ops.object.mode_set(mode='SCULPT')
            bpy.ops.paint.hide_show(action='HIDE', area='MASKED')

            bpy.ops.object.mode_set(mode='EDIT')
            
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.reveal()                           
            
            # add group
            obj.vertex_groups.new("Displace_Mask")
            for vgroup in obj.vertex_groups:
                if vgroup.name.startswith("D"):
                    bpy.ops.object.vertex_group_assign()
                    
            bpy.ops.object.mode_set(mode='OBJECT')        
          
            noisetex = bpy.data.textures['Sculpt_Noise']                
            bpy.context.object.modifiers["Displace"].vertex_group = "Displace_Mask"
            bpy.context.object.modifiers["Displace"].texture = noisetex

        bpy.context.object.modifiers["Displace"].show_viewport = True  

        bpy.ops.sculpt.sculptmode_toggle()
        return {"FINISHED"}   
      


class VIEW3D_TP_Remove_Displace_Mask(bpy.types.Operator):
    """remove displace mask"""
    bl_idname = "tp_ops.displace_mask_remove"
    bl_label = "Remove Displace Mask"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        obj = context.active_object
        
        # remove groups with m as first letter
        for vgroup in obj.vertex_groups:
            if vgroup.name.startswith("D"):
                obj.vertex_groups.remove(vgroup)
        bpy.context.object.modifiers["Displace"].vertex_group = ""
        
        return {"FINISHED"}
 
    



# PROPERTY GROUP: REMESH #
class Sculpt_Displace_Properties(bpy.types.PropertyGroup):

    bpy.types.Object.frozen = BoolProperty(name="frozen", default = False)

        
    remeshDepthInt = IntProperty(min = 2, max = 10, default = 4)
    remeshSubdivisions = IntProperty(min = 0, max = 6, default = 0)
    remeshPreserveShape = BoolProperty(default = True)

    extractDepthFloat = FloatProperty(min = -10.0, max = 10.0, default = 0.1)
    extractOffsetFloat = FloatProperty(min = -10.0, max = 10.0, default = 0.0)
    extractSmoothIterationsInt = IntProperty(min = 0, max = 50, default = 5)    
    extractStyleEnum = EnumProperty(name="Extract style", items = (("SOLID","Solid",""), ("SINGLE","Single Sided",""), ("FLAT","Flat","")), default = "SOLID")



# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    tp = bpy.context.window_manager.tp_props_remesh
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, key))


# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp = bpy.context.window_manager.tp_props_remesh
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, key, getattr(self, key))



# REGISTRY #        

def register():
    bpy.utils.register_module(__name__)

    bpy.types.WindowManager.tp_props_displace = PointerProperty(type = Sculpt_Displace_Properties)   

def unregister():
    bpy.utils.unregister_module(__name__)
    
    try:
        del bpy.types.WindowManager.tp_props_displace        
    except:
        pass

if __name__ == "__main__":
    register()