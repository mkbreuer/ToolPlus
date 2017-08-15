# orphan_cleanup.py (c) 2011 Phil Cote (cotejrp1)
#
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****
"""
bl_info = {
    'name': 'Orphan Cleanup',
    'author': 'Phil Cote, cotejrp1, (http://www.blenderaddons.com)',
    'version': (0,2),
    "blender": (2, 6, 0),
    "api": 41098,
    'location': 'VIEW 3D -> TOOLS',
    'description': 'Deletes unused objects from the bpy.data modules',
    'warning': 'Know what it is you are deleting. Check datablocks view within outliner if there are any doubts!', # used for warning icon and text in addons panel
    'category': 'System'}
"""
import bpy, random, time
from pdb import set_trace

mod_data = [tuple(["meshes"]*3), tuple(["armatures"]*3), 
                 tuple(["cameras"]*3), tuple(["curves"]*3),
                 tuple(["fonts"]*3), tuple(["grease_pencil"]*3),
                 tuple(["groups"]*3), tuple(["images"]*3),
                 tuple(["lamps"]*3), tuple(["lattices"]*3),
                 tuple(["libraries"]*3), tuple(["materials"]*3),
                 tuple(["actions"]*3), tuple(["metaballs"]*3),
                 tuple(["node_groups"]*3), tuple(["objects"]*3),
                 tuple(["sounds"]*3), tuple(["texts"]*3), 
                 tuple(["textures"]*3),]

if bpy.app.version[1] >= 60:
    mod_data.append( tuple(["speakers"]*3), )



class DeleteSceneObsOp(bpy.types.Operator):
    '''Delete Objects from all Scene'''
    bl_idname = "ba.delete_scene_obs"
    bl_label = "Delete from all Scene"
 
    def execute(self, context):
        for ob in context.scene.objects:
            context.scene.objects.unlink(ob)
        return {'FINISHED'}


class DeleteOrphansOp(bpy.types.Operator):
    '''Remove all orphaned objects of a selected type from the project.'''
    bl_idname="ba.delete_data_obs"
    bl_label="Clear Orphans"
    
    def execute(self, context):
        target = context.scene.mod_list
        target_coll = eval("bpy.data." + target)
        
        num_deleted = len([x for x in target_coll if x.users==0])
        num_kept = len([x for x in target_coll if x.users==1])
        
        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)
        
        msg = "Removed %d orphaned %s objects. Kept %d non-orphans" % (num_deleted, target,
                                                            num_kept)
        self.report( { 'INFO' }, msg  )
        return {'FINISHED'}




def register():
    
    
    bpy.types.Scene.mod_list = bpy.props.EnumProperty(name="Target", 
                           items=mod_data, 
                           description="Module choice made for orphan deletion")

    bpy.utils.register_class(DeleteOrphansOp)
    #bpy.utils.register_class(OrphanCleanupPanel)
    bpy.utils.register_class(DeleteSceneObsOp)    

def unregister():
    #bpy.utils.unregister_class(OrphanCleanupPanel)
    bpy.utils.unregister_class(DeleteOrphansOp)
    bpy.utils.unregister_class(DeleteSceneObsOp)

if __name__ == "__main__":
    register()