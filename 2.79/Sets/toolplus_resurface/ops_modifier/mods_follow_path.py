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
#


#bl_info = {
    #"name": "FollowPathArray",
    #"author": "pink vertex",
    #"version": (1, 0),
    #"blender": (2, 69, 0),
    #"location": "Search Menu > FollowPathArray",
    #"description": "creates duplicates of an object with a follow-path-constraint",
    #"warning": "",
    #"wiki_url": "",
    #"tracker_url": "",
    #"category": "Object"}

import bpy

def main(context,count,offset,type):
    obj=bpy.context.object
    ctr=get_constraint(obj)
    curve=ctr.target
    curve.data.use_path=True
    
    cyclic=0 if curve.data.splines[0].use_cyclic_u else 1
    
    group=bpy.data.groups.get("fpath.duplicates." + obj.name)
    if(group is None):
        group=bpy.data.groups.new("fpath.duplicates." + obj.name)
    
    for i in range(1,count+cyclic):
        dupli=obj.copy() #also copies constraints!
        group.objects.link(dupli)
        if  (type=="EVENLY_SPACED"):
            if cyclic==1:
                ctr.offset=0.0
            dupli.constraints[ctr.name].offset=-(curve.data.path_duration/count)*i+ctr.offset
        elif(type=="OFFSET"):
            dupli.constraints[ctr.name].offset=-(offset*i)+ctr.offset
        elif(type=="FIXED_POSITION"):
            dupli.constraints[ctr.name].offset_factor=offset*i+ctr.offset_factor
            dupli.constraints[ctr.name].use_fixed_location=True
    
    bpy.ops.object.fpath_link(group_name=group.name)
    
def check(context):
    obj=context.active_object
    if(obj is not None and len(obj.constraints)>=1):
        if(get_constraint(obj) is not None):
            return True;
    return False;

def get_constraint(obj):
    for ctr in obj.constraints:
        if(ctr.type=="FOLLOW_PATH" and ctr.target is not None):
            return ctr
    #nothing found
    return None

from bpy.props import FloatProperty, IntProperty, EnumProperty

class FollowPathArray(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.fpath_array"
    bl_label = "FollowPathArray"
    bl_options = {'REGISTER', 'UNDO'}
    
    type   = EnumProperty(
             name="type",
             items=[
             ("OFFSET"        , "offset",         "", 0),
             ("FIXED_POSITION", "fixed position", "", 1),
             ("EVENLY_SPACED" , "evenly spaced",  "", 2)
             ],
             default="OFFSET"
             )

    offset = FloatProperty(
             name="offset",
             description="offset",
             default=0.0
             )
   
    factor = FloatProperty(
             name="offset factor",
             description="offset factor",
             subtype="FACTOR",
             default=0.0,
             min=0.0,
             max=1.0
             )   
   
    count = IntProperty(
             name="count",
             description="number of duplicates",
             default=0,
             min=0,
             soft_max=100
             )
             
    @classmethod
    def poll(cls, context):
        return check(context)

    def execute(self, context):
        offset=self.offset if self.type=="OFFSET"         else\
               self.factor if self.type=="FIXED_POSITION" else\
               None
        main(context,self.count,offset,self.type)
        return {'FINISHED'}

    def draw(self, context):
        layout=self.layout
        col=layout.column()
        col.prop(self,"type","")
        col.prop(self,"count")
        if   self.type == "OFFSET":
            col.prop(self,"offset")
        elif self.type == "FIXED_POSITION":
            col.prop(self,"factor")        

class LinkToScene(bpy.types.Operator):
    bl_idname="object.fpath_link"
    bl_label="link to scene"
    bl_options={'INTERNAL'}
    
    from bpy.props import StringProperty
    
    group_name=StringProperty()
    
    def execute(self,context):
        group=bpy.data.groups[self.group_name]
        for obj in group.objects:
            if len(obj.users_scene)==0:
                context.scene.objects.link(obj)
        return {'FINISHED'}            
    
def register():
    bpy.utils.register_class(FollowPathArray)
    bpy.utils.register_class(LinkToScene)


def unregister():
    bpy.utils.unregister_class(FollowPathArray)
    bpy.utils.unregister_class(LinkToScene)

if __name__ == "__main__":
    register()


