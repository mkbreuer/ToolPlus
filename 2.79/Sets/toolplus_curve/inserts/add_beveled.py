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



class VIEW3D_TP_Beveled_Curve(bpy.types.Operator):
    """create curve with bevel extrusion"""
    bl_idname = "tp_ops.beveled_curve"
    bl_label = "Add beveled Curve"
    bl_options = {'REGISTER', 'UNDO'}


    radius = bpy.props.FloatProperty(name="Radius",  description=" ", default=10, min=0.01, max=1000)
    depth = bpy.props.FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)

    ring = bpy.props.IntProperty(name="Ring",  description=" ", min=0, max=100, default=12) 
    nring = bpy.props.IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop = bpy.props.IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 

    offset = bpy.props.FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height = bpy.props.FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

    wire = bpy.props.BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})    

    curve_type = bpy.props.EnumProperty(
        items=[("tp_bezier"     ,"Bezier"     ,"Bezier Curve"),
               ("tp_circle"     ,"Circle"     ,"Circle Curve"),
               ("tp_nurbs"      ,"Nurbs Curve"      ,"Nurbs Curve"),
               ("tp_ncircle"    ,"Nurbs Circle"     ,"Nurbs Circle")],
               name = "Type",
               default = "tp_bezier",    
               description = "add geometry")

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

        row = box.column(1)  
        row.prop(self, 'curve_type')  

        row.separator()
        
        row.prop(self, 'radius')

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
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(1)
            row.prop(self, 'nring')        
     

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


    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    def execute(self, context):

        settings_write(self) 

        scene = bpy.context.scene
        
        if self.curve_type == "tp_bezier":   
            bpy.ops.curve.primitive_bezier_curve_add(radius=self.radius)

        if self.curve_type == "tp_circle":   
            bpy.ops.curve.primitive_bezier_circle_add(radius=self.radius)        
       
        if self.curve_type == "tp_nurbs":   
            bpy.ops.curve.primitive_nurbs_curve_add(radius=self.radius)

            bpy.context.object.data.splines[0].order_u = self.nring

        if self.curve_type == "tp_ncircle":   
            bpy.ops.curve.primitive_nurbs_circle_add(radius=self.radius)     

            bpy.context.object.data.splines[0].order_u = self.nring

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)        

        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = self.loop
        bpy.context.object.data.resolution_u = self.ring
        bpy.context.object.data.bevel_depth = self.depth
        bpy.context.object.data.offset = self.offset
        bpy.context.object.data.extrude = self.height
            

        # add material with enabled object color
        for i in range(self.add_mat):

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




        if self.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False  
     
        return {'FINISHED'}
    
    

class VIEW3D_TP_Wire_Curve(bpy.types.Operator):
    """Add wired Curve"""
    bl_idname = "tp_ops.wired_curve"
    bl_label = "Add wired Curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        active_wire = bpy.context.object.show_wire 

        if active_wire == True:
            bpy.context.object.show_wire = False             
        else:                       
            bpy.context.object.show_wire = True

        return {'FINISHED'}



class VIEW3D_TP_Bevel(bpy.types.Operator):
    """add bevel curve """
    bl_idname = "tp_ops.bevel_set"
    bl_label = "Beveled"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}    
    
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=350)


    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'     
        layout.operator_context = 'INVOKE_REGION_WIN'

        box = layout.box().column(1)         
        
        if context.mode == 'OBJECT': 
            row = box.row(1)
            row.label("", icon='MOD_CURVE') 
            row.prop(context.scene, "curve_type", text="") 
            row.operator("tp_ops.beveled_curve", text="Add Curve")                          
                           
            box.separator()
        
        row = box.row(1)                                                                                                                                                                                                            
        
        active_wire = bpy.context.object.show_wire 
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
        
        if active_wire == True:
            row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
        else:                       
            row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 
                    
        row = box.row(1)
        row.prop(context.object.data, "resolution_u", text="Rings")          
        row.prop(context.object.data, "bevel_resolution", text="Loops")

        row = box.row(1)
        row.prop(context.object.data, "offset")
        row.prop(context.object.data, "extrude","Height")
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(1)
            row.prop(context.object.data.splines.active, "order_u", text="U Order")

        box.separator() 

        row = box.row(1)
        row.prop(context.object.data, "fill_mode", text="")   
        active_bevel = bpy.context.object.data.bevel_depth            
        if active_bevel == 0.0:              
            row.operator("tp_ops.enable_bevel", text="Bevel on", icon='MOD_WARP')
        else:   
            row.operator("tp_ops.enable_bevel", text="Bevel off", icon='MOD_WARP')      
            
        box.separator() 


    def check(self, context):
        return True


class Purge_Curve(bpy.types.Operator):
    '''Purge orphaned curve'''
    bl_idname="purge.unused_curve_data"
    bl_label="Purge Mesh"
    
    def execute(self, context):

        target_coll = eval("bpy.data.curves")
        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}



class VIEW3D_TP_Enable_Bevel(bpy.types.Operator):
    """toggle curve bevel extrusion"""
    bl_idname = "tp_ops.enable_bevel"
    bl_label = "Add enable Bevel"
    bl_options = {'REGISTER', 'UNDO'}

    depth = bpy.props.FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)

    ring = bpy.props.IntProperty(name="Ring",  description=" ", min=0, max=100, default=12) 
    nring = bpy.props.IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop = bpy.props.IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 

    offset = bpy.props.FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height = bpy.props.FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

    wire = bpy.props.BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})   


    def draw(self, context):
        layout = self.layout
        
        col = layout.column(align=True)

        box = col.box().column(1)                     
       
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
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(1)
            row.prop(self, 'nring')
     
        box.separator()


    def execute(self, context):
         
        active_bevel = bpy.context.object.data.bevel_depth
      
        if active_bevel == 0.0:              
            bpy.context.object.data.fill_mode = 'FULL'
            bpy.context.object.data.bevel_resolution = self.loop

            bpy.context.object.data.bevel_depth = self.depth
            bpy.context.object.data.offset = self.offset
            bpy.context.object.data.extrude = self.height 

            if context.object.data.splines.active.type == 'NURBS':            
                bpy.context.object.data.splines[0].order_u = self.nring            
            else:
                bpy.context.object.data.resolution_u = self.ring

        else:                   
            bpy.context.object.data.fill_mode = 'HALF'
            #bpy.context.object.data.bevel_resolution = 0
            #bpy.context.object.data.resolution_u = 0
            bpy.context.object.data.bevel_depth = 0.0
            bpy.context.object.data.extrude = 0
            bpy.context.object.data.offset = 0
    
        if self.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False 

        return {'FINISHED'}



class VIEW3D_TP_Quader_Curve(bpy.types.Operator):
    """select 2 vertices  on circle and execute"""
    bl_idname = "tp_ops.quader_curve"
    bl_label = "A full Bevel Quader Curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.curve.delete(type='VERT')
        bpy.ops.curve.select_all(action='TOGGLE')
        bpy.ops.curve.handle_type_set(type='ALIGNED')
        bpy.ops.curve.cyclic_toggle()   

        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_depth = 1.5
        bpy.context.object.data.bevel_resolution = 6
        bpy.context.object.show_wire = True

        return {'FINISHED'} 
    


class VIEW3D_TP_Half_Circle_Curve(bpy.types.Operator):
    """select start-point on circle and execute"""
    bl_idname = "tp_ops.half_curve"
    bl_label = "A full Bevel Quader CircleCurve"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        bpy.ops.curve.surfsk_first_points()
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.handle_type_set(type='ALIGNED')
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.delete(type='VERT')
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.cyclic_toggle()
        
        bpy.context.object.data.fill_mode = 'FULL'            
        bpy.context.object.data.bevel_depth = 1.5
        bpy.context.object.data.bevel_resolution = 6
        bpy.context.object.show_wire = True

        return {'FINISHED'}




class VIEW3D_TP_Convert_to_Mesh(bpy.types.Operator):
    """convert, get origin, remove doubles, recalculate, remesh"""
    bl_idname = "tp_ops.convert_mesh"
    bl_label = "Convert to Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    remesh = bpy.props.BoolProperty(name="Remesh",  description="remesh for curve extrude", default=True, options={'SKIP_SAVE'})    

    def execute(self, context):
   
        bpy.ops.object.mode_set(mode = 'OBJECT')
            
        bpy.ops.object.convert(target='MESH')                  
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        bpy.ops.object.mode_set(mode='EDIT')  

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.normals_make_consistent()

        bpy.ops.object.mode_set(mode = 'OBJECT')

        # from sculpt remesh 
        for i in range(self.remesh):                         
            bpy.ops.tp_ops.remesh(remeshDepthInt=4, remeshSubdivisions=1, remeshPreserveShape=True)

        return {'FINISHED'}
                
  
        
class VIEWD_TP_Curve_Lathe(bpy.types.Operator):
    """draw a screw curve to 3d cursor"""
    bl_idname = "tp_ops.curve_lathe"
    bl_label = "Curve Lathe"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return hasattr(bpy.types, "CURVE_OT_draw")
    

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
                bpy.context.scene.obj1 = active.name
                    
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
        bpy.ops.curve.draw('INVOKE_DEFAULT')

        return {"FINISHED"}




class VIEW3D_TP_Curve_Origin_Start(bpy.types.Operator):
    """Origin to curve start point / objectmode"""
    bl_idname = "tp_ops.origin_start_point"
    bl_label = "Origin to Start Point"
            
    def execute(self, context):
        blCurve = context.active_object
        blSpline = blCurve.data.splines[0]
      
        newOrigin = blCurve.matrix_world * blSpline.bezier_points[0].co
    
        origOrigin = bpy.context.scene.cursor_location.copy()

        bpy.context.scene.cursor_location = newOrigin
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor_location = origOrigin

        return {'FINISHED'}




class VIEW3D_TP_Curve_Extrude(bpy.types.Operator):
    """create 2d bevel extrude on curve"""
    bl_idname = "tp_ops.curve_extrude"
    bl_label = "Curve Extrude"
    bl_options = {"REGISTER", "UNDO"}

    depth = bpy.props.FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)
    ring = bpy.props.IntProperty(name="Ring",  description=" ", min=0, max=100, default=1) 
    nring = bpy.props.IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop = bpy.props.IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 
    offset = bpy.props.FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height = bpy.props.FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)
    wire = bpy.props.BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})    
    convert = bpy.props.BoolProperty(name="Convert to Mesh",  description=" ", default=False, options={'SKIP_SAVE'})   

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


    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)


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


        # curve extrude    
        if bpy.context.object.mode == "OBJECT":               
            bpy.ops.object.mode_set(mode = 'EDIT')
        
        if bpy.context.object.data.splines.active.use_cyclic_u == True:         
            pass
        else:
            bpy.ops.curve.cyclic_toggle()

        bpy.context.object.data.dimensions = '2D'
        bpy.context.object.data.fill_mode = 'BOTH'
        bpy.context.object.data.bevel_depth = self.depth
        bpy.context.object.data.bevel_resolution = self.ring         
        bpy.context.object.data.resolution_u = self.loop
        bpy.context.object.data.offset = self.offset            
        bpy.context.object.data.extrude = self.height           
        

        # wire visibility
        if self.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False 
                  
        return {"FINISHED"}




# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    tp = bpy.context.window_manager.tp_props_insert
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, key))


# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp = bpy.context.window_manager.tp_props_insert
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, key, getattr(self, key))
 


# PROPERTY INSERTS # 
class Insert_Props(bpy.types.PropertyGroup):

    add_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    add_random = bpy.props.BoolProperty(name="Add Random",  description="add random materials", default=False, options={'SKIP_SAVE'})    
    add_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    add_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])



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
















