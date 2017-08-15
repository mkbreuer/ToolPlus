####################################
# Look at it
#       v.1.0
#  (c)ishidourou 2013
####################################

#!BPY
import bpy

#bl_info = {
#    "name": "Look at it",
#    "author": "ishidourou",
#    "version": (1, 0),
#    "blender": (2, 65, 0),
#    "location": "View3D > Toolbar",
#    "description": "LookatIt",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": 'User Changed'}
"""    
#    Menu in tools region
class LookatItPanel(bpy.types.Panel):
    bl_label = "Look at it"
    #bl_space_type = "VIEW_3D"
    #bl_region_type = "TOOLS"
 
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("lookat.it", text="Object")
        row.operator("lookat.cursor", text="Cursor")

        col.label(text="Add Constraint:")
        row = col.row(align=True)
        row.operator("track.to", text="Track To")
        row.operator("damped.track", text="Damped Track")
        row.operator("lock.track", text="Lock Track")

        col.label(text="Add Const & Empty at CursorPos:")
        row = col.row(align=True)
        row.operator("track.toempty", text="Track To")
        row.operator("damped.trackempty", text="Damped Track")
        row.operator("lock.trackempty", text="Lock Track")
"""
#---- main ------

def objselect(objct,selection):
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True

class LookatIt(bpy.types.Operator):
    bl_idname = "lookat.it"
    bl_label = "Look at it"
    def execute(self, context):
        cobj = bpy.context.object
        if bpy.context.mode != 'OBJECT':
            return{'FINISHED'}
        if cobj == None:
            return{'FINISHED'}
        slist = bpy.context.selected_objects
        ct = 0
        for i in slist:
            ct += 1
        if ct == 1:
            return{'FINISHED'}
        bpy.ops.object.track_set(type='TRACKTO')
        bpy.ops.object.track_clear(type='CLEAR_KEEP_TRANSFORM')
        return{'FINISHED'}


def lookatempty(mode):
    if bpy.context.mode != 'OBJECT':
        return
    cobj = bpy.context.object
    slist = bpy.context.selected_objects
    ct = 0
    for i in slist:
        ct += 1
    if ct == 0:
        return            
    bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False)
    bpy.context.object.empty_draw_size = 3.00
    target = bpy.context.object
    for i in slist:
        i.select = True
    if mode == 'cursor' or 'damptrackempty':
        bpy.ops.object.track_set(type='DAMPTRACK')
    if mode == 'tracktoempty':
        bpy.ops.object.track_set(type='TRACKTO')
    if mode == 'locktrackempty':
        bpy.ops.object.track_set(type='LOCKTRACK')
    if mode == 'cursor':
        bpy.ops.object.track_clear(type='CLEAR_KEEP_TRANSFORM')
        objselect(target,'ONLY')
        bpy.ops.object.delete(use_global=False)
        objselect(cobj,'ADD')
        for i in slist:
            i.select = True

class LookatCursor(bpy.types.Operator):
    bl_idname = "lookat.cursor"
    bl_label = "Look at Cursor"
    def execute(self, context):
        lookatempty('cursor')
        return{'FINISHED'}
    
class TrackTo(bpy.types.Operator):
    bl_idname = "track.to"
    bl_label = "TrackTo"
    def execute(self, context):
        if bpy.context.mode != 'OBJECT':
            return{'FINISHED'}
        bpy.ops.object.track_set(type='TRACKTO')
        return{'FINISHED'}

class DampedTrack(bpy.types.Operator):
    bl_idname = "damped.track"
    bl_label = "DampedTrack"
    def execute(self, context):
        if bpy.context.mode != 'OBJECT':
            return{'FINISHED'}
        bpy.ops.object.track_set(type='DAMPTRACK')
        return{'FINISHED'}

class LockTrack(bpy.types.Operator):
    bl_idname = "lock.track"
    bl_label = "LockTrack"
    def execute(self, context):
        if bpy.context.mode != 'OBJECT':
            return{'FINISHED'}
        bpy.ops.object.track_set(type='LOCKTRACK')
        return{'FINISHED'}

class TrackToEmpty(bpy.types.Operator):
    bl_idname = "track.toempty"
    bl_label = "TrackTo"
    def execute(self, context):
        lookatempty('tracktoempty')
        return{'FINISHED'}

class DampedTrackEmpty(bpy.types.Operator):
    bl_idname = "damped.trackempty"
    bl_label = "DampedTrack"
    def execute(self, context):
        lookatempty('damptrackempty')
        return{'FINISHED'}

class LockTrackEmpty(bpy.types.Operator):
    bl_idname = "lock.trackempty"
    bl_label = "LockTrack"
    def execute(self, context):
        lookatempty('locktrackempty')
        return{'FINISHED'}

#	Registration
"""
def register():
    #bpy.utils.register_class(LookatItPanel)
    bpy.utils.register_class(LookatIt)
    bpy.utils.register_class(LookatCursor)
    bpy.utils.register_class(TrackTo)
    bpy.utils.register_class(DampedTrack)
    bpy.utils.register_class(LockTrack)
    bpy.utils.register_class(TrackToEmpty)
    bpy.utils.register_class(DampedTrackEmpty)
    bpy.utils.register_class(LockTrackEmpty)

def unregister():
    #bpy.utils.unregister_class(LookatItPanel)
    bpy.utils.unregister_class(LookatIt)
    bpy.utils.unregister_class(LookatCursor)
    bpy.utils.unregister_class(TrackTo)
    bpy.utils.unregister_class(DampedTrack)
    bpy.utils.unregister_class(LockTrack)
    bpy.utils.unregister_class(TrackToEmpty)
    bpy.utils.unregister_class(DampedTrackEmpty)
    bpy.utils.unregister_class(LockTrackEmpty)
"""

