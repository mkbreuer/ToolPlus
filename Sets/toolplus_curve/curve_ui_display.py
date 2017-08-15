43# ##### BEGIN GPL LICENSE BLOCK #####
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
__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons




def draw_curve_display_panel_layout(self, context, layout):
    
        icons = load_icons()     
        my_button_one = icons.get("icon_image1")
        
        obj = context.active_object  
        
        box = layout.box().column(1) 
                                                              
        if context.mode == 'OBJECT': 
    
            box.separator()
            
            row = box.row(1)
            row.prop(context.object, "show_name", text="Name", icon ="OUTLINER_DATA_FONT")
            row.prop(context.object, "show_axis", text="Axis", icon ="OUTLINER_DATA_EMPTY") 
  
            box.separator()

        box.separator()
        
        row = box.row(1)                                                          
        row.operator("tp_ops.wire_all", text="Wire all", icon='WIRE')
        
        obj = context.active_object
        if obj:
            active_wire = obj.show_wire 
            if active_wire == True:
                row.operator("tp_ops.wire_off", "Wire Select", icon = 'MESH_PLANE')              
            else:                       
                row.operator("tp_ops.wire_on", "Wire Select", icon = 'MESH_GRID')
        else:
            row.label("", icon="BLANK1")            
       
        row = box.row(1)
        
        obj = context.active_object
        if obj:               
            if obj.draw_type == 'WIRE':
                row.operator("tp_ops.draw_solid", text="Solid on", icon='GHOST_DISABLED')     
            else:
                row.operator("tp_ops.draw_wire", text="Solid off", icon='GHOST_ENABLED')        
        else:
            row.label("", icon="BLANK1")  
 
        ob = context.object
        if ob: 
            row.prop(ob, "draw_type", text="")
            
            row = box.row(1)
            row.prop(ob, "show_bounds", text="Bounds", icon='SNAP_PEEL_OBJECT') 
            row.prop(ob, "draw_bounds_type", text="")    
       
        else:
            row.label("", icon="BLANK1")         
            
                             
        if context.mode == 'EDIT_MESH':          

            box = layout.box().column(1) 

            row = box.row(1) 
            row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
            row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 
            
            row = box.row(1)
            row.prop(context.active_object.data, "show_double_sided",icon="GHOST")    
            row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
        
            row = box.row(1)
            row.active = context.active_object.data.use_auto_smooth
            row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")  

            box.separator()   
            box.separator()   

            row = box.row(1) 
            row.operator("mesh.mark_sharp", text="VertSharp", icon='SNAP_VERTEX').use_verts = True          
            props = row.operator("mesh.mark_sharp", text="Clear", icon='X')
            props.use_verts = True
            props.clear = True
            
            row = box.row(1)  
            row.operator("mesh.mark_sharp", text="EdgeSharp", icon='SNAP_EDGE')
            row.operator("mesh.mark_sharp", text="Clear", icon='X').clear = True

            box.separator()   
            box.separator() 
      
            row = box.row(1)
            row.operator("mesh.normals_make_consistent",text="Rec. Normals", icon='SNAP_NORMAL')
            row.operator("mesh.flip_normals", text="Flip", icon = "FILE_REFRESH")            

            row = box.row(1)
            row.operator("mesh.normals_make_consistent", text="Rec-Inside").inside = True        
            row.operator("mesh.normals_make_consistent", text="Rec-Outside").inside = False             
                   
            row = box.row(1)
            row.prop(context.active_object.data, "show_normal_vertex", text="", icon='VERTEXSEL')
            row.prop(context.active_object.data, "show_normal_loop", text="", icon='LOOPSEL')
            row.prop(context.active_object.data, "show_normal_face", text="", icon='FACESEL')
             
            row.active = context.active_object.data.show_normal_vertex or context.active_object.data.show_normal_face
            row.prop(context.scene.tool_settings, "normal_size", text="Size")  
            
            box.separator()  
        
        else:            

            box = layout.box().column(1) 
            
            if context.mode == 'OBJECT': 
                
                row = box.row(1)  
                row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
           
                obj = context.active_object     
                if obj:
                   obj_type = obj.type
                                  
                   if obj_type in {'MESH'}:

                       row = box.row(1)
                       row.prop(context.active_object.data, "show_double_sided",icon="GHOST")    
                       row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
                    
                       row = box.row(1)
                       row.active = context.active_object.data.use_auto_smooth
                       row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")  
                       
                row = box.row(1)
                row.operator("tp_ops.rec_normals", text="Consistent Normals", icon="SNAP_NORMAL")  

            else:                         
               
                if context.mode == 'EDIT_CURVE': 

                    row = box.column(1)
                    obj = context.active_object
                    if obj:
                        active_smooth = obj.data.splines.active.use_smooth
                        if active_smooth == True:                                      
                            row.prop(context.active_object.data.splines.active, "use_smooth", text="Smooth on", icon="SMOOTH")
                        else:
                            row.prop(context.active_object.data.splines.active, "use_smooth", text="Smooth off", icon="MESH_CIRCLE")                                                
                    row.operator("curve.normals_make_consistent", text="Consistent Normals", icon="SNAP_NORMAL")  


        box.separator() 



        if context.mode == 'EDIT_MESH':          
  
            box = layout.box().column(1) 

            row = box.row(1) 
            row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")            
            row.prop(context.space_data, "use_occlude_geometry", text="Occlude", icon='ORTHO')                       

            row = box.row(1)         
            row.prop(context.space_data, "show_backface_culling", text="Backface", icon ="MOD_LATTICE")   
            row.prop(context.space_data, "show_occlude_wire", text="Hidden", icon ="OUTLINER_DATA_LATTICE")      
    
            box.separator()   

        
        else:            
             
            box = layout.box().column(1) 

            row = box.row(1)          
            row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")

            if obj:
                obj_type = obj.type                    
                if obj_type in {'MESH'}:   
                    row.prop(context.space_data, "show_backface_culling", text="Backface", icon ="MOD_LATTICE")  

            box.separator() 


        row = box.row(1)                     
        obj = context.active_object
        if obj:
            obj_type = obj.type                    
            if obj_type in {'MESH'}: 
                row.prop(context.object, "show_transparent", text="Transparency", icon ="IMAGE_ALPHA") 
                                    
        if obj:
            obj_type = obj.type                    
            if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:                          
                row.prop(context.object, "show_texture_space", text="Texture Space", icon ="STICKY_UVS_LOC")


        box.separator()
         
        box = layout.box().column(1)  

        row = box.row(1)
        row.operator("tp_ops.material_color", text="Add Material", icon='ZOOMIN')
        row.operator("tp_ops.remove_all_material", text="Remove", icon="ZOOMOUT")     
              
        row = box.row(1)    

        if context.object.active_material and bpy.context.object.active_material.type in {'SURFACE','WIRE'}:
            row.prop(context.object.active_material, "use_object_color", text="Object Color", icon ="COLOR")                  
        else:
            row.label("Object Color")                           
  
        if bpy.context.scene.render.engine == 'CYCLES':
            row.prop(context.object.active_material, "diffuse_color", text="")  
        else:
            row.prop(context.object, "color", text="")                     
      
        row = box.row(1)                  
        row.menu("tp_ops.material_list", text="MatList", icon='COLLAPSEMENU')           
        row.operator("tp_purge.unused_material_data", text="Purge Unused", icon="PANEL_CLOSE")     

        box.separator()
                        
        obj = context.active_object
        if obj:
            obj_type = obj.type                
            if obj.type in {'CURVE'}: 

                box = layout.box().column(1)  

                row = box.row(1)  
                row.operator("dynamic.normalize", text="Draw Spline Points", icon='KEYTYPE_JITTER_VEC')        
                
                box.separator()   
                

        if context.mode == 'EDIT_CURVE': 

            row = box.row(1)  
            row.prop(context.active_object.data, "show_handles", text="Handles")
            row.prop(context.active_object.data, "show_normal_face", text="Normals")

            row = box.row(1) 
            row.prop(context.scene.tool_settings, "normal_size", text="Normal Size")

            box.separator() 



class VIEW3D_TP_Curve_Display_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Display_Panel_TOOLS"
    bl_label = "Display"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_curve_display_panel_layout(self, context, layout)


class VIEW3D_TP_Curve_Display_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Display_Panel_UI"
    bl_label = "Display"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'         

         draw_curve_display_panel_layout(self, context, layout)



# Registry               

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


