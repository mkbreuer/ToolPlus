bl_info = {
    "name": "Follow Path Array",
    "author": "pink vertex",
    "version": (1, 1),
    "blender": (2, 69, 0),
    "location": "Search Menu > Follow Path Array",
    "description": "Creates duplicates of an object with a follow-path-constraint",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "t+"}

import bpy
from bpy.props import *

def get_constraint(obj):
    for ctr in obj.constraints:
        if(ctr.type == "FOLLOW_PATH" and ctr.target is not None):
            return ctr
    #nothing found
    return None

class OBJECT_OT_fpath_array(bpy.types.Operator):
    """add follow path array as group"""
    bl_idname = "object.fpath_array"
    bl_label = "Follow Path Array"
    bl_options = {'REGISTER', 'UNDO'}
    
    type   = bpy.props.EnumProperty(
                 name  = "Type",
                 items = [
                 ("OFFSET"        , "Offset",         "", 0),
                 ("FIXED_POSITION", "Fixed Position", "", 1),
                 ("EVENLY_SPACED" , "Evenly Spaced",  "", 2)
                 ],
                 default = "OFFSET"
                 )

    offset = bpy.props.FloatProperty(name = "Offset", description = "Offset", default = 0.0)   
    factor = bpy.props.FloatProperty(name = "Offset factor", description = "offset factor", subtype = "FACTOR", default = 0.0, min = 0.0,max = 1.0)      
    count = bpy.props.IntProperty(name = "Count", description = "number of duplicates", default = 0, min = 0,soft_max = 100)
             
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj and obj.constraints and get_constraint(obj)

    def execute(self, context):
        if self.count == 0:
            return {'FINISHED'}
        #initialize
        dupli = bpy.context.active_object
        ctr = get_constraint(dupli)
        curve = ctr.target
        curve.data.use_path = True
        
        cyclic = 0 if curve.data.splines[0].use_cyclic_u else 1
        
        group = bpy.data.groups.get("fpath." + dupli.name)
        if not group:
            group = bpy.data.groups.new("fpath." + dupli.name)
        
        ctr.use_fixed_location = (self.type == "FIXED_POSITION")
        if   self.type == "OFFSET":
            offset = self.offset
        elif self.type == "EVENLY_SPACED":
            offset = -(curve.data.path_duration / (self.count + 1 - cyclic))
            if cyclic == 1:
                ctr.offset = 0.0
        
        for i in range(self.count):
            dupli = dupli.copy() #also copies constraints!
            ctr = dupli.constraints[ctr.name]
            group.objects.link(dupli)
            
            if not self.type == "FIXED_POSITION":
                ctr.offset += offset
            else:
                ctr.offset_factor += self.factor
        
        bpy.ops.object.fpath_link(group_name=group.name)
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)
         
        row = box.column(1)
        row.prop(self, "type","")
        row.prop(self, "count")
        if   self.type == "OFFSET":
            row.prop(self,"offset")
        elif self.type == "FIXED_POSITION":
            row.prop(self,"factor", "Offset")        


class OBJECT_OT_fpath_array_Panel(bpy.types.Operator):
    """add follow path array as group"""
    bl_idname = "object.fpath_array_panel"
    bl_label = "Follow Path Array"
    bl_options = {'REGISTER', 'UNDO'}
    
    bpy.types.Scene.type  = bpy.props.EnumProperty(
                 name  = "Type",
                 items = [
                 ("OFFSET"        , "Offset",         "", 0),
                 ("FIXED_POSITION", "Fixed Position", "", 1),
                 ("EVENLY_SPACED" , "Evenly Spaced",  "", 2)
                 ],
                 default = "OFFSET"
                 )

    bpy.types.Scene.offset = bpy.props.FloatProperty(name = "Offset", description = "Offset", default = 0.0)   
    bpy.types.Scene.factor = bpy.props.FloatProperty(name = "Offset factor", description = "offset factor", subtype = "FACTOR", default = 0.0, min = 0.0,max = 1.0)      
    bpy.types.Scene.count = bpy.props.IntProperty(name = "Count", description = "number of duplicates", default = 0, min = 0,soft_max = 100)
             
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj and obj.constraints and get_constraint(obj)

    def execute(self, context):
        scene = context.scene 
        
        if scene.count == 0:
            return {'FINISHED'}
       
        #initialize
        dupli = bpy.context.active_object
        ctr = get_constraint(dupli)
        curve = ctr.target
        curve.data.use_path = True
        
        cyclic = 0 if curve.data.splines[0].use_cyclic_u else 1        
        group = bpy.data.groups.get("fpath." + dupli.name)

        if not group:
            group = bpy.data.groups.new("fpath." + dupli.name)
        
        ctr.use_fixed_location = (scene.type == "FIXED_POSITION")

        if scene.type == "OFFSET":
            offset = scene.offset

        elif scene.type == "EVENLY_SPACED":
            offset = -(curve.data.path_duration / (scene.count + 1 - cyclic))

            if cyclic == 1:
                ctr.offset = 0.0
        
        for i in range(scene.count):
            dupli = dupli.copy() #also copies constraints!
            ctr = dupli.constraints[ctr.name]
            group.objects.link(dupli)
            
            if not scene.type == "FIXED_POSITION":
                ctr.offset += offset
            else:
                ctr.offset_factor += self.factor
        
        bpy.ops.object.fpath_link(group_name=group.name)
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene 
        
        box = layout.box().column(1)
         
        row = box.column(1)
        row.prop(scene, "type","")
        row.prop(scene, "count")
        if   scene.type == "OFFSET":
            row.prop(self,"offset")
        elif scene.type == "FIXED_POSITION":
            row.prop(scene,"factor", "Offset")        


class OBJECT_OT_fpath_link(bpy.types.Operator):
    bl_idname  = "object.fpath_link"
    bl_label   = "Link To Scene"
    bl_options = {"INTERNAL"}
    
    group_name = bpy.props.StringProperty()
    
    def execute(self,context):
        group = bpy.data.groups[self.group_name]
        for obj in group.objects:
            if not obj.users_scene:
                context.scene.objects.link(obj)
        return {"FINISHED"}            



def register():
    bpy.utils.register_class(OBJECT_OT_fpath_array)
    bpy.utils.register_class(OBJECT_OT_fpath_link)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_fpath_array)
    bpy.utils.unregister_class(OBJECT_OT_fpath_link)

if __name__ == "__main__":
    register()

