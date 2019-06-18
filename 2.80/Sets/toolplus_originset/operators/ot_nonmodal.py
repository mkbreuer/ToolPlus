# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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
from bpy.props import StringProperty


# OPERATOR WITH STRING MODE ID #
class VIEW3D_OT_set_origin_to(bpy.types.Operator):
    '''set origin to selected...'''# Tool-Tip  
    bl_idname = "tpc_ops.set_origin_to"
    bl_label = "Selected Edit"
    bl_options = {"REGISTER", 'UNDO'}   

    # property to define mode id  
    mode : bpy.props.StringProperty(default="")    

    def execute(self, context):
            
        oldmode = bpy.context.object.mode

        if context.mode =='EDIT_MESH':
                        
            if "LINKED_MESH" in self.mode:          
                bpy.ops.mesh.select_linked(delimit=set())
                bpy.ops.view3d.snap_cursor_to_selected() 
       
            if "SELECTED_MESH" in self.mode:     
                bpy.ops.view3d.snap_cursor_to_selected() 

            if "ORIGIN_CURSOR" in self.mode:
                pass
            else:        
                bpy.ops.view3d.snap_cursor_to_selected() 

        bpy.ops.object.mode_set(mode='OBJECT')  

        if "COPY_ORIGIN" in self.mode:
            current_pivot = bpy.context.space_data.pivot_point     
            bpy.ops.view3d.snap_cursor_to_active() 
 
        if "ORIGIN_CENTER" in self.mode:
            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
     
        if "ORIGIN_GEOMETRY" in self.mode:
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        
        if "GEOMETRY_ORIGIN" in self.mode:
            bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
       
        if "ORIGIN_CURSOR" in self.mode:
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

        if "ORIGIN_CENTER_OF_MASS" in self.mode:       
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN') 
        
        if "ORIGIN_CENTER_OF_VOLUME" in self.mode:              
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
    
        if "COPY_ORIGIN" in self.mode:                    
            bpy.context.space_data.pivot_point = current_pivot   

        bpy.ops.object.mode_set(mode=oldmode)
        return{'FINISHED'}  




# OPERATOR FOR EDIT MODE #
class VIEW3D_OT_set_origin_to_edit(bpy.types.Operator):
    """set origin to selected or active / [SHIFT] = go to objectmode""" # Tool-Tip                  
    bl_idname = "tpc_ops.set_origin_to_edit"          
    bl_label = "Origin to Edit"                 
    bl_options = {'REGISTER', 'UNDO'}   
    
    # property to define mode id
    mode : StringProperty( name="", description="", default="selected")

    def store(self):            

        #store 3d view mode
        store_mode : bpy.context.object.mode
 
        #store cursor to
        self.toggle_cursor_to : "selected"  

 
    # do before execute
    def invoke(self, context, event):  
        
        # when event than...
        if event.shift:   
            self.store_mode = 'OBJECT'         
        else:
            #store 3d view mode
            self.store_mode = bpy.context.object.mode       
      
        # when event than...
        if event.ctrl:   
            self.toggle_cursor_to =  "active"  
        else:
            self.toggle_cursor_to =  "selected"  

        # execute operator
        self.execute(context)

        # create 3d view header message
        self.report({'INFO'}, "Done!")  
        
        return {'FINISHED'}
  

    # perform operator     
    def execute(self, context):
           
        # switch cursor to
        if self.toggle_cursor_to in self.mode:
            bpy.ops.view3d.snap_cursor_to_selected()              
        else:
            bpy.ops.view3d.snap_cursor_to_active()     
  
        # switch to object mode
        bpy.ops.object.mode_set(mode='OBJECT')  
      
        # set origin           
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

        # reload 3d view mode
        bpy.ops.object.mode_set(mode=self.store_mode)   
 
        return {'FINISHED'}




# OPERATOR ONLY FOR MESH EDIT MODE #
import bmesh
class VIEW3D_OT_set_origin_to_edit_mesh(bpy.types.Operator):
    """set origin to selected or active / [SHIFT] = go to objectmode""" # Tool-Tip                
    bl_idname = "tpc_ops.set_origin_to_edit_mesh"          
    bl_label = "Origin to Edit"                 
    bl_options = {'REGISTER', 'UNDO'}   

    # property to define mode id
    mode : StringProperty( name="", description="", default="selected")

    def store(self):            
        #store selection mode
        self.store_select_x_mode : bpy.context.tool_settings.mesh_select_mode[0]  
        self.store_select_y_mode : bpy.context.tool_settings.mesh_select_mode[1] 
        self.store_select_z_mode : bpy.context.tool_settings.mesh_select_mode[2] 
        
        #store 3d view mode
        store_mode : bpy.context.object.mode
     
        #store cursor to
        self.toggle_cursor_to : "selected"  


    # do before execute
    def invoke(self, context, event):  
      
        # when event than...
        if event.shift:   
            self.store_mode = 'OBJECT'         
        else:
            #store 3d view mode
            self.store_mode = bpy.context.object.mode       
 
        # when event than...
        if event.ctrl:   
            self.toggle_cursor_to =  "active"  
        else:
            self.toggle_cursor_to =  "selected"  
                 
        #store selection mode
        self.store_select_x_mode = bpy.context.tool_settings.mesh_select_mode[0]  
        self.store_select_y_mode = bpy.context.tool_settings.mesh_select_mode[1] 
        self.store_select_z_mode = bpy.context.tool_settings.mesh_select_mode[2]  
        
        # execute operator
        self.execute(context)

        # create 3d view header message
        self.report({'INFO'}, "Done!")  
        
        return {'FINISHED'}

  
    # perform operator 
    def execute(self, context):

        # check for mesh selections
        object = context.object
        
        # get the editmode changes
        object.update_from_editmode()

        # get mesh data
        mesh_bm = bmesh.from_edit_mesh(object.data)

        # check for mesh mode selections
        selected_faces = [f for f in mesh_bm.faces if f.select]
        selected_edges = [e for e in mesh_bm.edges if e.select]
        selected_verts = [v for v in mesh_bm.verts if v.select]
                             
       # check selection value
        if len(selected_verts) < 0:
            self.report({'WARNING'}, "nothing selected")
            return {'CANCELLED'}
       
        elif len(selected_edges) < 0:
            self.report({'WARNING'}, "nothing selected")
            return {'CANCELLED'}        
       
        elif len(selected_faces) < 0:
            self.report({'WARNING'}, "nothing selected")
            return {'CANCELLED'}
      
        else:
                       
            # switch cursor to
            if self.toggle_cursor_to in self.mode:
                bpy.ops.view3d.snap_cursor_to_selected()              
            else:
                bpy.ops.view3d.snap_cursor_to_active()                        
            
            # reload selection mode
            bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
            bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
            bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode

            # switch to object mode
            bpy.ops.object.mode_set(mode='OBJECT')  
          
            # set origin           
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

            # reload 3d view mode
            bpy.ops.object.mode_set(mode=self.store_mode)   

        return {'FINISHED'}


def register():
    bpy.utils.register_class(VIEW3D_OT_set_origin_to)
    bpy.utils.register_class(VIEW3D_OT_set_origin_to_edit)
    bpy.utils.register_class(VIEW3D_OT_set_origin_to_edit_mesh)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_set_origin_to)
    bpy.utils.unregister_class(VIEW3D_OT_set_origin_to_edit)
    bpy.utils.unregister_class(VIEW3D_OT_set_origin_to_edit_mesh)

if __name__ == "__main__":
    register()
