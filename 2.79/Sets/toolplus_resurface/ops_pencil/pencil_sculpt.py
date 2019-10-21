# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****


#bl_info = {
#    "name": "Sculpt Tools",
#    "author": "Ian Lloyd Dela Cruz, Nicholas Bishop, Roberto Roch, Bartosz Styperek, Piotr Adamowicz",
#    "version": (1, 0),
#    "blender": (2, 7, 0),
#    "location": "3d View > Tool shelf, Shift-Ctrl-B",
#    "description": "Simple UI for Boolean and Remesh operators",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "Sculpting"}

    
# LOAD MODULE #
import bpy
import mathutils, bmesh
from bpy import*
from bpy.props import *


# helper function for face selection
def objSelectFaces(obj, mode):
    
    #store active object
    activeObj = bpy.context.active_object
    
    #store the mode of the active object
    oldMode = activeObj.mode
    
    #perform selection
    bpy.context.scene.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action=mode)
    
    #restore old active object and mode
    bpy.ops.object.mode_set(mode=oldMode)
    bpy.context.scene.objects.active = activeObj

#helper function to duplicate an object    
def objDuplicate(obj):

    activeObj = bpy.context.active_object
    oldMode = activeObj.mode    

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action = 'DESELECT')
    bpy.ops.object.select_pattern(pattern = obj.name)
    bpy.ops.object.duplicate()
    objCopy = bpy.context.selected_objects[0]

    bpy.context.scene.objects.active = activeObj
    bpy.ops.object.mode_set(mode=oldMode)
    return objCopy
    
def objDiagonal(obj):
    return ((obj.dimensions[0]**2)+(obj.dimensions[1]**2)+(obj.dimensions[2]**2))**0.5
    
def objDelete(obj):
    rem = obj
    remname = rem.data.name
    bpy.data.scenes[bpy.context.scene.name].objects.unlink(rem)
    bpy.data.objects.remove(rem)
    # remove mesh to prevent memory being cluttered up with hundreds of high-poly objects
    bpy.data.meshes.remove(bpy.data.meshes[remname])


  


class GreaseTrim(bpy.types.Operator):
    """Cuts the selected object along the grease pencil stroke"""
    bl_idname = "boolean.grease_trim"
    bl_label = "Grease Cut"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod 
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'OBJECT' and context.active_object.type == 'MESH'  and 0<len(bpy.context.selected_objects)<=2

    def execute(self, context):
        objBBDiagonal = objDiagonal(context.active_object)*2
        # objBBDiagonal = objBBDiagonal*2
        subdivisions = 32

        if len(bpy.context.selected_objects)==1:
            try:
                mesh = bpy.context.active_object
                bpy.ops.gpencil.convert(type='POLY', timing_mode='LINEAR', use_timing_data=False)
                context.active_object.grease_pencil.clear()
                mesh = bpy.context.active_object
                if mesh == bpy.context.selected_objects[0]:
                    ruler = bpy.context.selected_objects[1]
                else: 
                    ruler = bpy.context.selected_objects[0]
                bpy.context.scene.objects.active = ruler
                bpy.ops.object.convert(target='MESH')
                
                rulerDiagonal = objDiagonal(ruler)
                verts = []
                
                bm = bmesh.new()
                bm.from_mesh(ruler.data)
                
                for v in bm.verts:
                    if len(v.link_edges) == 1:
                        v.select = True
                        verts.append(v)
                dist = verts[0].co - verts[1].co
                if dist.length < rulerDiagonal/10:
                    bm.edges.new(verts)
                
                bm.to_mesh(ruler.data)
                
            except:
                self.report({'WARNING'}, "Draw a line with grease pencil first")
                return {'FINISHED'}
        elif len(bpy.context.selected_objects)==2:
            mesh = bpy.context.active_object
            
            if mesh == bpy.context.selected_objects[0]:
                ruler = bpy.context.selected_objects[1]
            else: 
                ruler = bpy.context.selected_objects[0]
            
            if ruler.type == 'MESH' and len(ruler.data.polygons)>0:
                bpy.context.scene.objects.active = ruler
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_mode(type="EDGE")
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.region_to_loop()
                bpy.ops.mesh.select_all(action='INVERT')
                bpy.ops.mesh.delete(type='EDGE')
                bpy.ops.object.mode_set(mode='OBJECT')
            elif ruler.type == 'CURVE':
                bpy.context.scene.objects.active = ruler
                bpy.ops.object.convert(target='MESH')
            


        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                viewZAxis = tuple([z * objBBDiagonal for z in area.spaces[0].region_3d.view_matrix[2][0:3]])
                negViewZAxis = tuple([z * (-2*objBBDiagonal*(1/subdivisions)) for z in area.spaces[0].region_3d.view_matrix[2][0:3]])
                break
        
        bpy.context.scene.objects.active = ruler

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.select_mode(type="EDGE")
        bpy.ops.transform.translate(value = viewZAxis)
        for i in range(0, subdivisions):
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":negViewZAxis})
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent()
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.scene.objects.active = mesh
        bpy.ops.boolean.separate()
    
        return {'FINISHED'}


class PurgeAllPencils(bpy.types.Operator):
    """Removes all Grease Pencil Layers"""
    bl_idname = "boolean.purge_pencils"
    bl_label = "Clears all grease pencil user data in the scene"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if not context.scene.grease_pencil == None:
            context.scene.grease_pencil.clear()
        for obj in context.scene.objects:
            if not context.scene.objects[obj.name].grease_pencil == None:
                context.scene.objects[obj.name].grease_pencil.clear() 
        return {'FINISHED'}   



class ExecuteGreaseCutOperator(bpy.types.Operator):
    '''execute grease cut to split the active object'''
    bl_idname = "grease.execution"
    bl_label = "Execute Grease Cut"
    bl_options = {'REGISTER', 'UNDO'}
  
    remove = bpy.props.BoolProperty(name="Remove Grease Pencil Stroke",  description="Profil", default=False)
    origin = bpy.props.BoolProperty(name="Origin to Active",  description="Profil", default=False)

    def execute(self, context):
        bpy.ops.boolean.grease_trim()
        bpy.ops.boolean.grease_trim()
                                                            
        for i in range(self.remove):             
            bpy.ops.boolean.purge_pencils()
                                                            
        for i in range(self.origin):             
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            
        return {'FINISHED'}    



#        layout.separator()
#        
#        row_gt = layout.row(align=True)
#        row_gt.operator("boolean.grease_trim", text='Grease Cut')
#        
#        box = layout.box().column(align=True)
#        if wm.expand_grease_settings == False: 
#            box.prop(wm, "expand_grease_settings", icon="TRIA_RIGHT", icon_only=True, text=" Grease Pencil Settings", emboss=False)
#        else:
#            box.prop(wm, "expand_grease_settings", icon="TRIA_DOWN", icon_only=True, text=" Grease Pencil Settings", emboss=False)
#            box.separator()
#            box.prop(edit, "grease_pencil_manhattan_distance", text="Manhattan Distance")
#            box.prop(edit, "grease_pencil_euclidean_distance", text="Euclidean Distance")
#            boxrow = box.row(align=True)
#            boxrow.prop(edit, "use_grease_pencil_smooth_stroke", text="Smooth")
#            boxrow.prop(edit, "use_grease_pencil_simplify_stroke", text="Simplify")
#            box.separator()                                         
#            box.operator("boolean.purge_pencils", text='Purge All Grease Pencils')



##------------------------------------------------------  
#
# GP Lines
#
##------------------------------------------------------ 
bpy.types.Scene.obj1 = bpy.props.StringProperty()

# Create GP Line
class CreateGPLines(bpy.types.Operator):
    bl_idname = "object.creategpline"
    bl_label = "Create GP Lines"
    bl_description = "Create GP Lines !! Press D to create Grease Pencil Lines !!"
    bl_options = {"REGISTER", "UNDO"}


    def execute(self, context):
        selected = context.selected_objects
        actObj = context.active_object if context.object is not None else None
        if actObj :
            bpy.context.scene.obj1 = actObj.name
        
        wm = context.window_manager
        ref_obj = bpy.context.window_manager.ref_obj 
        
        #prepare GP
        if context.selected_objects:
            bpy.context.scene.tool_settings.grease_pencil_source = 'OBJECT'
            bpy.context.scene.tool_settings.gpencil_stroke_placement_view3d = 'SURFACE'
            
            
            #Add snap
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            
        else :
            bpy.context.scene.tool_settings.use_snap = False
            bpy.context.scene.tool_settings.grease_pencil_source = 'OBJECT'
            bpy.context.scene.tool_settings.gpencil_stroke_placement_view3d = 'VIEW'
        

        bpy.context.scene.tool_settings.use_gpencil_continuous_drawing = True
        
        

        #Create Empty mesh
        bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False)
        bpy.context.active_object.name= "GP_Surface"
#        bpy.ops.object.shade_smooth()
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.delete(type='VERT')    
        bpy.ops.object.mode_set(mode = 'OBJECT')  
        
        if wm.add_mirror :
            bpy.ops.object.modifier_add(type='MIRROR')
            bpy.context.object.modifiers["Mirror"].use_x = True
            bpy.context.object.modifiers["Mirror"].use_mirror_merge = False

            if wm.ref_obj :
                bpy.context.object.modifiers["Mirror"].mirror_object = bpy.data.objects[ref_obj]
                skin_origin = False
                
            elif actObj :
                bpy.context.object.modifiers["Mirror"].mirror_object = actObj
                skin_origin = False
                
            else :
                bpy.ops.object.modifier_remove(modifier="Mirror")

                  
        #Add Solidify    
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        
        bpy.context.object.modifiers["Solidify"].thickness = 0.4
        bpy.context.object.modifiers["Solidify"].offset = 0
        bpy.context.object.modifiers["Solidify"].use_quality_normals = True
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        
        #Add subsurf
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subsurf"].levels = 3
        
        #Add Shrinkwrap
        if selected :
            bpy.ops.object.modifier_add(type='SHRINKWRAP')
            bpy.context.object.modifiers["Shrinkwrap"].target = actObj
            bpy.ops.object.modifier_move_up(modifier="Shrinkwrap")
            bpy.ops.object.modifier_move_up(modifier="Shrinkwrap")
            bpy.ops.object.modifier_move_up(modifier="Shrinkwrap")
            bpy.ops.object.modifier_move_up(modifier="Shrinkwrap")

        bpy.ops.object.mode_set(mode = 'EDIT')
        
        bpy.ops.gpencil.draw('INVOKE_DEFAULT')
        
        return {"FINISHED"}

# Shrinkwrap Surface on mesh
class ShrinkwrapGPLines(bpy.types.Operator):
    bl_idname = "object.shrinkwrap_gplines"
    bl_label = "Shrinkwrap Gplines"
    bl_description = "Add a Shrinkwrap modifier to fit the object surface"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        obj_name = bpy.context.scene.obj1
        
        bpy.ops.object.mode_set(mode = 'OBJECT')  
        bpy.ops.object.shade_smooth() 
        bpy.ops.object.modifier_add(type='SHRINKWRAP')
        bpy.context.object.modifiers["Shrinkwrap"].target = bpy.data.objects[obj_name]
        bpy.ops.object.modifier_move_up(modifier="Shrinkwrap")
        bpy.ops.object.modifier_move_up(modifier="Shrinkwrap")
        bpy.ops.object.modifier_move_up(modifier="Shrinkwrap")
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")
        bpy.ops.object.mode_set(mode = 'EDIT')
        return {"FINISHED"}



# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():  
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 
    
