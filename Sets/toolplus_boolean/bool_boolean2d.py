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
# ***** END GPL LICENCE BLOCK ***** 

# <pep8 compliant>

#bl_info = {
 #   'name': "Boolean 2D Union",
  #  'author': "luxuy blendercn",
    #'version': (1, 0, 0),
    #'blender': (2, 70, 0),
    #'location': 'View3D > EditMode > (w) Specials', 
    #'warning': "",
    #'category': 'User Changed'}

import bpy,bmesh
from bpy.props import FloatProperty, IntProperty, BoolProperty,EnumProperty,StringProperty



class Boolean2DUnion(bpy.types.Operator):
    """union coplanar 2D Faces """    
    bl_idname = "bpt.boolean_2d_union"
    bl_label = "Boolean 2D Union"
    bl_options = {'REGISTER', 'UNDO'}
    
    flag=BoolProperty( name="Dissolve edges", default=0)
    
    @classmethod
    def poll(cls, context):
        if context.mode=='EDIT_MESH':
            return True

    def invoke( self, context, event ):
        ob=context.object
        bpy.ops.object.mode_set(mode = 'OBJECT')
        faces=[f for f in ob.data.polygons if f.select]
        print(faces)
        bpy.ops.object.mode_set(mode = 'EDIT')
        if len(faces)>1:
            
            self.execute(context)
        else:
            msg ="Please select at least 2 faces !"
            self.report( {"INFO"}, msg  )
        
        
        
        return {"FINISHED"}
    def execute(self, context):
        
        ob_old=context.object
        bpy.ops.mesh.separate(type='SELECTED')
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        ob=list(set(context.selected_objects)-set([ob_old]))[0]
        
        old=bpy.data.objects[:]
        bpy.ops.object.select_all(action='DESELECT')
        ob.select=True
        bpy.context.scene.objects.active=ob
        print(ob)
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        new=bpy.data.objects[:]
        new_obs=list(set(new)-set(old))
        new_obs.append(ob)

        bpy.ops.object.mode_set(mode = 'OBJECT')

        for i in range(len(new_obs)):
            for j in range(len(new_obs)):
                if i!=j:
                    bpy.ops.object.select_all(action='DESELECT')
                    new_obs[j].select=True
                    bpy.context.scene.objects.active=new_obs[i]
                    bpy.ops.object.mode_set(mode = 'EDIT')
                    bpy.ops.mesh.knife_project(cut_through=True)
                    bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        for obj in new_obs:
            obj.select=True
        bpy.context.scene.objects.active=ob
        bpy.ops.object.join()
        
        bm=bmesh.new()
        bm.from_mesh(ob.data)

        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0003)
        if self.flag:
            bmesh.ops.dissolve_limit(bm, angle_limit=0.087, use_dissolve_boundaries=0, verts=bm.verts, edges=bm.edges)
        bm.to_mesh(ob.data)
        bm.free()
        bpy.ops.object.select_all(action='DESELECT')
        ob.select=True
        ob_old.select=True
        bpy.context.scene.objects.active=ob_old
        bpy.ops.object.join()
        
        bpy.ops.object.mode_set(mode = 'EDIT')
        
        return {'FINISHED'}
    
#---------------------------------------------
def menu_func(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator('bpt.boolean_2d_union')


"""
def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_edit_mesh_specials.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)
"""




