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



# MAIN OPERATOR #
class VIEW3D_TP_Draw_Curve(bpy.types.Operator):
    bl_description = "create empty bezier object for curve draw on surface or to view"
    bl_idname = "tp_ops.curve_draw"
    bl_label = "C-Draw"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return hasattr(bpy.types, "CURVE_OT_draw")

    bpy.types.Scene.add_bevel = bpy.props.BoolProperty(name="Bevel Toggle", description="add bevel to for surface and view draw", default=False)     

    mode = bpy.props.StringProperty(default="")   

    bpy.types.Scene.spline_name = bpy.props.StringProperty(name="Name", default="Curve Draw")

    def execute(self, context):
        
        scene = bpy.context.scene
    
        obj = context.active_object     
        if obj:
            
            add_mat = bpy.context.scene.tp_props_insert.add_mat
            add_objmat = bpy.context.scene.tp_props_insert.add_objmat  
            add_random = bpy.context.scene.tp_props_insert.add_random
            add_color = bpy.context.scene.tp_props_insert.add_color
            add_cyclcolor = bpy.context.scene.tp_props_insert.add_cyclcolor

            obj = context.active_object     
            if obj:
               obj_type = obj.type
               if obj_type in {'CURVE'}:
                   pass                 
               else:
                    bpy.ops.view3d.snap_cursor_to_selected()
                                                  
                    bpy.ops.curve.primitive_bezier_curve_add(view_align=True, enter_editmode=True)
     
            if bpy.context.object.data.bevel_depth == 0 and scene.add_bevel == True: 
                bpy.context.object.data.fill_mode = 'FULL'
                bpy.context.object.data.bevel_depth = 3
                bpy.context.object.data.bevel_resolution = 3


            bpy.ops.object.mode_set(mode = 'OBJECT')            

            # add material with enabled object color
            for i in range(add_mat):

                active = bpy.context.active_object
                # Get material
                mat = bpy.data.materials.get("Mat_Curve")
                if mat is None:
                    # create material
                    mat = bpy.data.materials.new(name="Mat_Curve")
                else:
                    bpy.ops.object.material_slot_remove()
                    mat = bpy.data.materials.new(name="Mat_Curve")
                         
                # Assign it to object
                if len(active.data.materials):
                    # assign to 1st material slot
                    active.data.materials[0] = mat
                else:
                    # no slots
                    active.data.materials.append(mat)
                            
                if add_random == False:                            
                    if add_objmat == False: 
                        if bpy.context.scene.render.engine == 'CYCLES':
                            mat.diffuse_color = (add_cyclcolor)                        
                        else:
                            mat.use_object_color = True
                            bpy.context.object.color = (add_color)
                    else:
                         pass                    
                else: 
                    if bpy.context.scene.render.engine == 'CYCLES':
                        node=mat.node_tree.nodes['Diffuse BSDF']
                        for i in range(3):
                            node.inputs['Color'].default_value[i] *= random.random()             
                    else:
                        for i in range(3):
                            mat.diffuse_color[i] *= random.random()   


            # go to edit and draw curve
            bpy.ops.object.mode_set(mode = 'EDIT')        
            bpy.ops.curve.select_all(action='SELECT')
            bpy.ops.curve.delete(type='VERT')
            bpy.context.object.data.show_normal_face = False
            bpy.context.scene.tool_settings.curve_paint_settings.use_corners_detect = True        

            if "surface" in self.mode:  
                bpy.context.scene.tool_settings.curve_paint_settings.depth_mode = 'SURFACE'

            if "cursor" in self.mode:          
                bpy.context.scene.tool_settings.curve_paint_settings.depth_mode = 'CURSOR'

            spline_name="draw curve to"   
            bpy.context.object.name = scene.spline_name
                           
            bpy.ops.curve.draw('INVOKE_DEFAULT')

        else:
            print(self)
            self.report({'INFO'}, "Need Active Object!") 

        return {'FINISHED'}




        
class VIEWD_TP_Curve_Lathe(bpy.types.Operator):
    """draw a screw curve to 3d cursor"""
    bl_idname = "tp_ops.curve_lathe"
    bl_label = "Curve Lathe"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return hasattr(bpy.types, "CURVE_OT_draw")
    
    bpy.types.Scene.spline_name = bpy.props.StringProperty(name="Name", default="Curve Draw")

    def execute(self, context):

        scene = bpy.context.scene

        add_mat = bpy.context.scene.tp_props_insert.add_mat
        add_objmat = bpy.context.scene.tp_props_insert.add_objmat  
        add_random = bpy.context.scene.tp_props_insert.add_random
        add_color = bpy.context.scene.tp_props_insert.add_color
        add_cyclcolor = bpy.context.scene.tp_props_insert.add_cyclcolor
     

        obj = context.object 
        if obj:

            active = context.active_object if context.object is not None else None
            if active :
                bpy.context.scene.name = active.name
                    
            bpy.ops.object.mode_set(mode = 'OBJECT')
                
            # add curve          
            bpy.ops.curve.primitive_bezier_curve_add(view_align=True) 
            
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.curve.select_all(action='SELECT')            
            bpy.ops.curve.delete(type='VERT')
            bpy.context.object.data.show_normal_face = False

            # add screw modifier to curve           
            bpy.ops.object.modifier_add(type='SCREW')
            bpy.context.object.modifiers["Screw"].steps = 40
            bpy.context.object.modifiers["Screw"].use_normal_flip = False            
            bpy.context.object.modifiers["Screw"].use_smooth_shade = True
        
            if active:
                bpy.context.object.modifiers["Screw"].object = active

        else:
            
            # add curve            
            bpy.ops.curve.primitive_bezier_curve_add(view_align=True) 
           
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.curve.select_all(action='SELECT')            
            bpy.ops.curve.delete(type='VERT')
            bpy.context.object.data.show_normal_face = False

            # add screw modifier to curve           
            bpy.ops.object.modifier_add(type='SCREW')
            bpy.context.object.modifiers["Screw"].steps = 40
            bpy.context.object.modifiers["Screw"].use_normal_flip = False          
            bpy.context.object.modifiers["Screw"].use_smooth_shade = True


        bpy.ops.object.mode_set(mode = 'OBJECT')            
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


        # add material with enabled object color
        for i in range(add_mat):

            active = bpy.context.active_object
            # Get material
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
                        
            if add_random == False:                            
                if add_objmat == False: 
                    if bpy.context.scene.render.engine == 'CYCLES':
                        mat.diffuse_color = (add_cyclcolor)                        
                    else:
                        mat.use_object_color = True
                        bpy.context.object.color = (add_color)
                else:
                     pass                    
            else: 
                if bpy.context.scene.render.engine == 'CYCLES':
                    node=mat.node_tree.nodes['Diffuse BSDF']
                    for i in range(3):
                        node.inputs['Color'].default_value[i] *= random.random()             
                else:
                    for i in range(3):
                        mat.diffuse_color[i] *= random.random()   

        # go to edit and draw curve
        bpy.ops.object.mode_set(mode = 'EDIT')        

        spline_name="draw curve lathe"   
        bpy.context.object.name = scene.spline_name  

        bpy.ops.curve.draw('INVOKE_DEFAULT')

        return {"FINISHED"}





# PROPERTY INSERTS # 
class Insert_Props(bpy.types.PropertyGroup):

    add_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    add_random = bpy.props.BoolProperty(name="Add Random",  description="add random materials", default=False, options={'SKIP_SAVE'})    
    add_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    add_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])



# ADD TO MENU # 
def menu_curve(self, context):
    layout = self.layout

    if context.mode =="OBJECT":
        
        self.layout.operator("tp_ops.draw_curve", text="Curve Draw", icon="LINE_DATA") 



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

    bpy.types.Scene.tp_props_insert = bpy.props.PointerProperty(type=Insert_Props)   
    bpy.types.WindowManager.tp_props_insert = bpy.props.PointerProperty(type=Insert_Props)   

def unregister():   
    bpy.utils.unregister_module(__name__)

    del bpy.types.Scene.tp_props_insert  
    del bpy.types.WindowManager.tp_props_insert  

if __name__ == "__main__":
    register()


