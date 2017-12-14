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
#


# LOAD MODUL #
import bpy
from bpy import*
from bpy.props import  *
from .icons.icons import load_icons

class VIEW3D_TP_Purge_Mesh(bpy.types.Operator):
    '''Purge orphaned mesh'''
    bl_idname="tp_ops.purge_unused_mesh_data"
    bl_label="Purge Mesh"
    bl_options = {"REGISTER", 'UNDO'}    

    def execute(self, context):

        target_coll = eval("bpy.data.meshes")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}
    


class View3D_TP_Axis_Planes_Menu(bpy.types.Menu):
    bl_label = "Axis Planes"
    bl_idname = "tp_menu.intersetion_planes"

    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        button_axis_x = icons.get("icon_axis_x")
        layout.operator("tp_ops.axis_plane",text="Plane", icon_value=button_axis_x.icon_id).pl_axis = "axis_x"      
      
        button_axis_y = icons.get("icon_axis_y")
        layout.operator("tp_ops.axis_plane",text="Plane", icon_value=button_axis_y.icon_id).pl_axis = "axis_y"       

        button_axis_z = icons.get("icon_axis_z")
        layout.operator("tp_ops.axis_plane",text="Plane", icon_value=button_axis_z.icon_id).pl_axis = "axis_z" 

        button_axis_n = icons.get("icon_axis_n")
        layout.operator("tp_ops.planefit",text="Plane", icon_value=button_axis_n.icon_id) 



class View3D_TP_CleanUP_BoolBevel(bpy.types.Operator):
    """CleanUp after bevel"""
    bl_idname = "tp_ops.cleanup_boolbevel"
    bl_label = "CleanUp"

    def execute(self, context):
                
        obj = context.active_object
        if obj:
     
            mo_types = []
            append = mo_types.append

            for mo in obj.modifiers:
                            
                if mo.type == 'BEVEL':
                    bpy.ops.object.modifier_apply(modifier="Boolean Bevel")

                if mo.type == 'SMOOTH' :        
                    bpy.ops.object.modifier_apply(modifier="Boolean Bevel Smooth")

        if obj:
            mod_list = obj.modifiers
            if not mod_list:

                for ob in bpy.context.selected_editable_objects:
                    for vgroup in ob.vertex_groups:
                        ob.vertex_groups.remove(vgroup)
               
        return {'FINISHED'}  




class View3D_TP_Boolean_Intersect_Edm_Menu(bpy.types.Operator):
    """Boolean Intersect"""
    bl_idname = "tp_ops.bool_intersect_edm_menu"
    bl_label = "Intersect"

    def execute(self, context):
      
        bpy.ops.tp_ops.bool_intersect()   
        
        return {'FINISHED'} 



class View3D_TP_Boolean_Union(bpy.types.Operator):
    """Boolean Union"""
    bl_idname = "tp_ops.bool_union"
    bl_label = "Union"
    bl_options = {"REGISTER", 'UNDO'}  

    def execute(self, context):
        
        bpy.ops.mesh.intersect_boolean(operation='UNION')     
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Difference(bpy.types.Operator):
    """Boolean Difference"""
    bl_idname = "tp_ops.bool_difference"
    bl_label = "Difference"
    bl_options = {"REGISTER", 'UNDO'}  

    swap = bpy.props.BoolProperty(name="Swap",  description="swap boolean direction", default=False, options={'SKIP_SAVE'})  

    def execute(self, context):
        
        bpy.ops.mesh.intersect_boolean(use_swap=self.swap, operation='DIFFERENCE')      
        
        return {'FINISHED'}  


class View3D_TP_Boolean_Intersect(bpy.types.Operator):
    """Boolean Intersect"""
    bl_idname = "tp_ops.bool_intersect"
    bl_label = "Intersect"
    bl_options = {"REGISTER", 'UNDO'}  

    def execute(self, context):
       
        bpy.ops.mesh.intersect_boolean(operation='INTERSECT')      
        
        return {'FINISHED'} 


class View3D_TP_Boolean_2d_Union_Edm_Menu(bpy.types.Operator):
    """Boolean 2c Union"""
    bl_idname = "tp_ops.boolean_2d_union_edm_menu"
    bl_label = "2d Union"

    def execute(self, context):
                
        bpy.ops.bpt.boolean_2d_union()
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Union_Edm_Menu(bpy.types.Operator):
    """Boolean Union"""
    bl_idname = "tp_ops.bool_union_edm_menu"
    bl_label = "Union"

    def execute(self, context):
                
        bpy.ops.tp_ops.bool_union()  
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Difference_Edm_Menu(bpy.types.Operator):
    """Boolean Difference"""
    bl_idname = "tp_ops.bool_difference_edm_menu"
    bl_label = "Difference"

    def execute(self, context):
        
        bpy.ops.tp_ops.bool_difference()     
        
        return {'FINISHED'}  



class View3D_TP_BoolTools_Union(bpy.types.Operator):
    """Boolean Union"""
    bl_idname = "tp_ops.tboolean_union"
    bl_label = "Union"

    def execute(self, context):
          
        bpy.ops.btool.boolean_union()       
    
        return {'FINISHED'}  


class View3D_TP_BoolTools_Difference(bpy.types.Operator):
    """Boolean Difference"""
    bl_idname = "tp_ops.tboolean_diff"
    bl_label = "Difference"

    def execute(self, context):
        
        bpy.ops.btool.boolean_diff()     
        
        return {'FINISHED'}  


class View3D_TP_BoolTools_Intersect(bpy.types.Operator):
    """Boolean Intersect"""
    bl_idname = "tp_ops.tboolean_inters"
    bl_label = "Intersect"

    def execute(self, context):
       
        bpy.ops.btool.boolean_inters()   
        
        return {'FINISHED'} 


class View3D_TP_BoolTools_Slice(bpy.types.Operator):
    """Boolean Slice"""
    bl_idname = "tp_ops.tboolean_slice"
    bl_label = "Slice"

    def execute(self, context):
       
        bpy.ops.btool.boolean_slice() 
        
        return {'FINISHED'}


class View3D_TP_BoolTools_Draw(bpy.types.Operator):
    """Boolean Draw"""
    bl_idname = "tp_ops.draw_polybrush"
    bl_label = "Draw"

    def execute(self, context):
       
        bpy.ops.btool.draw_polybrush()   
        
        return {'FINISHED'}



class View3D_TP_Plane_X(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "tp_ops.axis_plane"
    bl_label = "Axis Planes"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    # TRANSFORM #
    xpl_verts = bpy.props.IntProperty(name="Vertices", description="set x rotation value", default=4, min=1, max=80)
    xpl_scale = bpy.props.FloatProperty(name="Scale", description="set x rotation value", default=10, min=-100, max=100)
    plf_scale = bpy.props.FloatProperty(name="Scale", description="set x rotation value", default=10, min=-100, max=100)
    xpl_transform_use = bpy.props.BoolProperty(name="Use Transform",  description="enable transform tools", default=False)  

    pl_axis = bpy.props.EnumProperty(
        items=[("axis_x"     ,"X"     ,"X"),
               ("axis_y"     ,"Y"     ,"Y"),
               ("axis_z"     ,"Z"     ,"Z"),
               ("axis_n"     ,"N"     ,"N")],
               name = " ",
               default = "axis_x")

    xpl_depth = bpy.props.FloatProperty(name="Depth", description="extrusion depth value", default=0.0, min=-100, max=100)

  
    # TRANSFORM LOCATION #
    xpl_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100)
    xpl_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100)
    xpl_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100)

    # TRANSFORM ROTATE #
    xpl_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    xpl_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    xpl_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60)

    # TRANSFORM SCALE #
    xpl_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100)
    xpl_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100)
    xpl_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100)

    orient = bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View")],
               name = "",
               default = "GLOBAL",    
               description = "change plane orientation")

    loca_orient = bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View")],
               name = "",
               default = "GLOBAL",    
               description = "change rotation orientation")
  
    rota_orient = bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View")],
               name = "",
               default = "GLOBAL",    
               description = "change rotation orientation")

    scal_orient = bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View")],
               name = "",
               default = "GLOBAL",    
               description = "change rotation orientation")


    swap = bpy.props.BoolProperty(name="Swap",  description="swap boolean direction", default=False, options={'SKIP_SAVE'})  

    pl_bool = bpy.props.EnumProperty(
      items = [("pl_none"       ,"None"        ,"0"),      
               ("pl_union"      ,"Union"       ,"+"),
               ("pl_intersect"  ,"Intersect"   ,"/"),
               ("pl_difference" ,"Difference"  ,"-")],
               name = " ",
               default = "pl_none")


    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
      
        icons = load_icons()

        col = layout.column(align=True)

        box = col.box().column(1)              
            
        row = box.row(1) 
        row.prop(self, 'pl_axis', expand =True)

        if self.pl_axis == 'axis_n':    
           
            box.separator()             
           
            row = box.row(1)           
            row.prop(self, "plf_scale")  
           
            box.separator()   
      
        else:

            box.separator()  
           
            row = box.row(1)
            row.prop(self, "xpl_verts") 
            row.prop(self, "xpl_scale")  


            row = box.row(1)
            row.prop(self, "orient")  
            row.prop(self, "xpl_depth")  
            
            box.separator()       
            
            row = box.row(1)       
            row.prop(self, "xpl_transform_use")  
            
            box.separator()      
            
            if self.xpl_transform_use == True:    
                     
                box = col.box().column(1)   
                
                row = box.row(1)
                row.label("Location") 
                row.label(" ") 
                row.prop(self, "loca_orient")  
                
                row = box.row(1)        
                row.prop(self, "xpl_location_x") 
                row.prop(self, "xpl_location_y")               
                row.prop(self, "xpl_location_z") 
         
                box.separator()
                box.separator()

                row = box.row(1)
                row.label("Rotation") 
                row.label(" ") 
                row.prop(self, "rota_orient")  
                
                row = box.row(1)
                row.prop(self, "xpl_rotate_x") 
                row.prop(self, "xpl_rotate_y")               
                row.prop(self, "xpl_rotate_z") 
         
                box.separator()
                box.separator()

                row = box.row(1)
                row.label("Scale") 
                row.label(" ") 
                row.prop(self, "scal_orient")  
                
                row = box.row(1)
                row.prop(self, "xpl_scale_x") 
                row.prop(self, "xpl_scale_y")               
                row.prop(self, "xpl_scale_z") 
                
                box.separator()


            if  self.xpl_depth > 0: 

                box.separator()

                box = col.box().column(1)              
               
                row = box.column(1)                        

                row = box.row(1) 
                row.prop(self, 'pl_bool', expand =True)
              
                row = box.row(1) 
                row.prop(self, "swap", text="Swap Direction")    

                box.separator()


    # PERFORMING # 
    def execute(self, context):
               
        bpy.ops.view3d.snap_cursor_to_selected()        
           
        # use planfit
        if self.pl_axis == "axis_n":
            bpy.ops.tp_ops.planefit(size=self.plf_scale)
             
        else:            
                            
            # add circle as plane
            if self.pl_axis == "axis_x":
                bpy.ops.mesh.primitive_circle_add(vertices=self.xpl_verts, radius=self.xpl_scale, fill_type='NGON', rotation=(0, 0, 0.785398))  
                bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation= self.orient)

            if self.pl_axis == "axis_y":
                bpy.ops.mesh.primitive_circle_add(vertices=self.xpl_verts, radius=self.xpl_scale, fill_type='NGON', rotation=(0, 0, 0.785398))         
                bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL')        
                  
            if self.pl_axis == "axis_z":
                bpy.ops.mesh.primitive_circle_add(vertices=self.xpl_verts, radius=self.xpl_scale, fill_type='NGON', rotation=(0, 0, 0))       
                bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL')        

            
            # transform
            if self.xpl_transform_use == True:   
               
                # location 
                bpy.ops.transform.translate(value=(self.xpl_location_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation = self.loca_orient)
                bpy.ops.transform.translate(value=(0, self.xpl_location_y, 0), constraint_axis=(False, True, False), constraint_orientation = self.loca_orient)
                bpy.ops.transform.translate(value=(0, 0, self.xpl_location_z), constraint_axis=(False, False, True), constraint_orientation = self.loca_orient)

                # rotate 
                bpy.ops.transform.rotate(value=self.xpl_rotate_x, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation = self.rota_orient)
                bpy.ops.transform.rotate(value=self.xpl_rotate_y, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation = self.rota_orient)
                bpy.ops.transform.rotate(value=self.xpl_rotate_z, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation = self.rota_orient)
          
                # scale 
                bpy.ops.transform.resize(value=(self.xpl_scale_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation = self.scal_orient)
                bpy.ops.transform.resize(value=(0, self.xpl_scale_y, 0), constraint_axis=(False, True, False), constraint_orientation = self.scal_orient)
                bpy.ops.transform.resize(value=(0, 0, self.xpl_scale_z), constraint_axis=(False, False, True), constraint_orientation = self.scal_orient)


            # extrusion and cleanup for boolean
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, self.xpl_depth), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL'})
            bpy.ops.mesh.select_linked(delimit=set()) 
            bpy.ops.mesh.normals_make_consistent()

            
            # booleans
            if  self.xpl_depth > 0: 

                if self.pl_bool == "pl_none":
                    pass

                if self.pl_bool == "pl_union":
                    bpy.ops.mesh.intersect_boolean(operation='UNION')  
              
                if self.pl_bool == "pl_intersect":
                    bpy.ops.mesh.intersect_boolean(operation='INTERSECT')  
              
                if self.pl_bool == "pl_difference":
                    bpy.ops.mesh.intersect_boolean(use_swap=self.swap, operation='DIFFERENCE')  

        return {'FINISHED'}   


   

class View3D_TP_Boolean_Union_Obm_Menu(bpy.types.Operator):
    """Boolean Union"""
    bl_idname = "tp_ops.bool_union_obm_menu"
    bl_label = "Union"

    def execute(self, context):
        
        bpy.ops.btool.direct_union()   
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Intersect_Obm_Menu(bpy.types.Operator):
    """Boolean Intersect"""
    bl_idname = "tp_ops.bool_intersect_obm_menu"
    bl_label = "Intersect"

    def execute(self, context):
       
        bpy.ops.btool.direct_intersect()     
        
        return {'FINISHED'} 


class View3D_TP_Boolean_Difference_Obm_Menu(bpy.types.Operator):
    """Boolean Difference"""
    bl_idname = "tp_ops.bool_difference_obm_menu"
    bl_label = "Difference"

    def execute(self, context):
        
        bpy.ops.btool.direct_difference()     
        
        return {'FINISHED'}  


class View3D_TP_Boolean_Rebool_Obm_Menu(bpy.types.Operator):
    """Boolean Rebool"""
    bl_idname = "tp_ops.bool_rebool_obm_menu"
    bl_label = "Rebool"

    def execute(self, context):
        
        bpy.ops.btool.direct_slice()     
        
        return {'FINISHED'} 



class View3D_TP_Origin_Edm(bpy.types.Operator):
    """set origin to selected / editmode"""                 
    bl_idname = "tp_ops.origin_edm"          
    bl_label = "origin to selected"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class View3D_TP_Select_Linked(bpy.types.Operator):
    """select linked / editmode"""                 
    bl_idname = "tp_ops.select_linked_edm"          
    bl_label = "selecte linked"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        bpy.ops.mesh.select_linked(delimit=set())

        return {'FINISHED'}


    
# REGISTERY # 
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()







