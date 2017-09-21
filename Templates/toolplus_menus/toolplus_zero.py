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
    "name": "T+ ZeroAxis",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "Editor: 3D Viewport",
    "description": "zero object, origin or cursor to x/y/z axis",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


import bpy
from bpy import *
from bpy.props import *


class VIEW3D_TP_Zero_to_Axis(bpy.types.Operator):
    """Zero Axis"""                 
    bl_idname = "tp_ops.zero_axis"          
    bl_label = "ZeroAxis"                 
    bl_options = {'REGISTER', 'UNDO'}   

    tp_switch = bpy.props.EnumProperty(
        items=[("tp_obj"    ,"Object"    ,"01"),
               ("tp_org"    ,"Origin"    ,"02"),
               ("tp_crs"    ,"Cursor"    ,"03")],
               name = "ZeroFor",
               default = "tp_obj",    
               description = "zero object or cursor")

    tp_switch_axis = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"All"  ,"04")],
               name = "ZeroAxis",
               default = "tp_x",    
               description = "zero target to choosen axis")


    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)

        row = box.row()
        row.prop(self, 'tp_switch', expand=True)

        row = box.row()
        row.prop(self, 'tp_switch_axis', expand=True)
        
        box.separator()
        
    def execute(self, context):

           

        if self.tp_switch_axis == "tp_x":  
            
            if self.tp_switch == "tp_obj":        
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[0] = 0     

            if self.tp_switch == "tp_org":                
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 
                                            
                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[0] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[0] = 0 

        if self.tp_switch_axis == "tp_y":  

            if self.tp_switch == "tp_obj":        
                for ob in bpy.context.selected_objects:
                    bpy.context.object.location[1] = 0  

            if self.tp_switch == "tp_org":
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 

                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[1] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[1] = 0 

        if self.tp_switch_axis == "tp_z":  

            if self.tp_switch == "tp_obj":     
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[2] = 0  

            if self.tp_switch == "tp_org":        
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 

                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[2] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[2] = 0 


        if self.tp_switch_axis == "tp_a": 
            
            if self.tp_switch == "tp_obj":   
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob                   
                    bpy.context.object.location[0] = 0  
                    bpy.context.object.location[1] = 0  
                    bpy.context.object.location[2] = 0  

            if self.tp_switch == "tp_org":        
                
                if context.mode == 'OBJECT':
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[0] = 0 
                bpy.context.space_data.cursor_location[1] = 0 
                bpy.context.space_data.cursor_location[2] = 0 



        return {'FINISHED'} 


    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)





def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()

