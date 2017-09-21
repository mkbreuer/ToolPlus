# BEGIN GPL LICENSE BLOCK #####
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
# END GPL LICENSE BLOCK #####


"""
bl_info = {
    "name": "Smart Join",
    "author": "Andrej Ivanis",
    "version": (1, 0, 3),
    "blender": (2, 73, 0),
    "location": "Relationships tab, Specials menu (w-key)",
    "warning": "",
    "description": "Enables non-destructive join of the objects",
    "wiki_url": "",
    "category": "Tools+"}
"""

import bpy, bmesh
from bpy.props import *
from bpy.app.handlers import persistent
import mathutils


######## JOINER #########################################################

# these make Function.view expected a SpaceView3D type, not SpaceTimeline
def add_to_all_visible_layers(obj, scn):
    sd = bpy.context.space_data
    if sd and type(sd) is bpy.types.SpaceView3D:
        scn.object_bases[obj.name].layers_from_view(bpy.context.space_data)

def add_to_loc_view(obj, scn):
    layers = obj.layers[:]

    add_to_all_visible_layers(obj,scn)
    obj.layers = layers

def duplicate_linked(objects, some_visible_obj = None, visible_only = True):
    context = bpy.context
    scn = bpy.context.scene
    # sel = context.selected_objects
    bpy.ops.object.select_all(action='DESELECT')
    # for o in scn.objects:
    #     o.select = False


    # link all object not in scene and select them
    to_unlink = []
    to_unhide = []
    for o in objects:
        # cpy = o.copy()
        # scn.objects.link(cpy)
        # cpy.select = True
        o.select = True

        # hidden object aren't duplicated properly
        if not visible_only:
            unhide_temp(o)

        if o.name not in scn.objects:
            scn.objects.link(o)
            to_unlink.append(o)

        # TODO: this needs to be reverted, but for now I always remove all object from scene somewhere later
        if some_visible_obj:
            o.layers = some_visible_obj.layers

        add_to_all_visible_layers(o, scn)
    scn.update()


    bpy.ops.object.duplicate(linked=True)
    for o in objects:
        rehide(o)


    for o in to_unlink:
        scn.objects.unlink(o)
    sel = context.selected_objects[:]
    for o in sel:
        rehide(o)

    scn.update()
    return sel




def unhide_temp(o):
    if o.hide:
        o.hide = False
        o['hide_temp'] = True

def rehide(o):
    ht = o.get('hide_temp')
    if ht:
        del o["hide_temp"]
        o.hide = True



def join_to_mesh(context, mesh, objects, some_visible_obj):

    sel = context.selected_objects
    act = context.active_object

    scn = context.scene

    duplicate_linked(objects, some_visible_obj)

    ## make real recursively in case of dupli groups inside dupli groups
    def doop(o):
        return o.dupli_type != 'NONE'
    while any([doop(o) for o in context.selected_objects]):
        bpy.ops.object.duplicates_make_real()

    # and once for particles
    bpy.ops.object.duplicates_make_real()

    # make new meshes and apply modifiers, can't use object.make_single_user because it can mess up curves used by modifiers I need copy all objects
    newObjs = []
    applied_meshes = []
    old_objs = []
    for obj in context.selected_objects[:]:
        if not obj.data:
            continue
        # to_mesh will fail if no geometry data is found
        try:
            m = obj.to_mesh(bpy.context.scene, True, 'PREVIEW')
            # looks like obj.to_mesh can return None (empty curve?)
            if not m:
                continue
        except:
            continue

        # if there are no material create empty slot so you don't get other materials in join
        if len(m.materials) == 0:
            m.materials.append(None)

        objcpy = bpy.data.objects.new('copy', object_data = m)
        scn.objects.link(objcpy)
        objcpy.layers = some_visible_obj.layers
        add_to_loc_view(objcpy, scn)
        objcpy.matrix_world = obj.matrix_world
        applied_meshes.append(m)
        newObjs.append(objcpy)
        old_objs.append(obj)



    # set all the sharp angles from autosmooth
    for i, new_mesh in enumerate(applied_meshes):
        o = old_objs[i]
        if o.type != 'MESH':
            continue


        # make unique UVMap
        # TODO: I won't ever need this probably, but I should keep other maps
        '''
        if 'sjoin_uvs' not in new_mesh.uv_textures:
            new_mesh.uv_textures.new('sjoin_uvs')
        '''

        for t in new_mesh.uv_textures[:]:
            # texture layer 'NGon Face' not found??? fixed by: and t.name in new_mesh.uv_textures
            if not t.active and t.name in new_mesh.uv_textures:
                new_mesh.uv_textures.remove(t)

        if new_mesh.uv_textures.active:
            new_mesh.uv_textures.active.name = 'UVMap'

        correct_normals(new_mesh, o.scale)




        if not o.data.use_auto_smooth or (o.data.use_auto_smooth and o.data.auto_smooth_angle == 180) or o.data.is_sjoin:
            pass
        else:
            #looks like o.data.auto_smooth_angle is in radians although displayed in degrees in GUI
            correct_somoothing(new_mesh, o.data.auto_smooth_angle)



    # delete copied objects and select duplicate ones
    bpy.ops.object.delete(use_global=False)

    for o in newObjs:
        o.select = True


    ### clear the mesh geometry
    # clear_mesh(mesh)

    ## autosmooth on (might not always help)
    mesh.use_auto_smooth = True
    mesh.auto_smooth_angle = 180

    #create new join object with given mesh
    j_obj = bpy.data.objects.new(name = 'temp_obj', object_data= mesh)

    j_obj.select = True
    j_obj.location = (0,0,0)
    j_obj.layers = [True] * 20
    scn.objects.link(j_obj)
    # without this local view won't work
    j_obj.layers = some_visible_obj.layers
    add_to_loc_view(j_obj, scn)

    scn.objects.active = j_obj

    ### join to mesh and delete objects if any left
    bpy.ops.object.join()

    # for o in newObjs:
    #     if o:
    #         if o.name in scn.objects:
    #             scn.objects.unlink(o)
    #         bpy.data.objects.remove(o)

    for m in applied_meshes:
        if m.users == 0:
            bpy.data.meshes.remove(m)


    # delete the joined object
    #  it looks like removing the object deletes materials of j_obj.data??? so I make a dummy mesh as a workaround
    bug_fix = bpy.data.meshes.new(name = 'bug_fix')
    j_obj.data = bug_fix
    for o in bpy.context.selected_objects[:]:
        scn.objects.unlink(o)
        #  this will mess up materials of o.data if i remove o afterwards?
        bpy.data.objects.remove(o)

    bpy.data.meshes.remove(bug_fix)

    ## get old selection
    for o in sel:
        o.select = True
    scn.objects.active = act
    # scn.update()


def clear_mesh(mesh):
    bm = bmesh.new()
    bm.to_mesh(mesh)
    bm.free()
    mesh.materials.clear()
    mesh.update()


def correct_normals(mesh, scale):
    tot_scale = 1
    # this is not real scale? but works anyways
    for s in scale:
        tot_scale *= 1 if s >= 0 else -1

    if tot_scale < 0:
        bm = bmesh.new()   # create an empty BMesh
        bm.from_mesh(mesh)   # fill it in from a Mesh

        bmesh.ops.reverse_faces(bm, faces=bm.faces[:])

        # Finish up, write the bmesh back to the mesh
        bm.to_mesh(mesh)
        bm.free()




def correct_somoothing(mesh, angle):
    bm = bmesh.new()   # create an empty BMesh
    bm.from_mesh(mesh)   # fill it in from a Mesh

    bmesh_correct_somoothing(bm, angle)

    # Finish up, write the bmesh back to the mesh
    bm.to_mesh(mesh)
    bm.free()

def bmesh_correct_somoothing(bm, angle):

    for e in bm.edges:
        ang = e.calc_face_angle(None)

        if ang:
            if ang > angle:
                e.smooth = False







######## CORE ######################

def get_sjmesh(name):
    mesh = bpy.data.meshes.get(name)
    if mesh and mesh.is_sjoin:
        return mesh
    return None

def get_stored_sjobjects_unsafe(sj_mesh_name):
    return [o for o in bpy.data.objects if o.sjoin_mesh == sj_mesh_name]

def check_fix_rename(sj_mesh, sj_obj = None, scn = None):

    # sjoin check performed by update object

    # first, check if mesh is renamed or duplicated
    if sj_mesh.sjoin_link_name != sj_mesh.name and sj_mesh.sjoin_link_name != '':
        # make sure some delete mesh didn't leave objects
        objs = get_stored_sjobjects_unsafe(sj_mesh.name)
        for o in objs:
            o.sjoin_mesh = ''
            o.fake_user = False


        # mesh is renamed or duplicated, see if there is old mesh with this name to determine
        old_mesh = get_sjmesh(sj_mesh.sjoin_link_name)
        if old_mesh:
            # duplicated, duplicate all the object and link them to this mesh
            if scn:
                sel = [o for o in scn.objects if o.select]
            collapse_expanded(old_mesh)
            if sj_obj:
                set_object_collapsed(sj_obj)

                '''
                if len(sj_obj.children) == 0:
                    set_object_collapsed(sj_obj)
                else:
                    set_object_expended(sj_obj)
                '''
            sj_objs = get_stored_sjobjects_unsafe(sj_mesh.sjoin_link_name)
            duplicates = duplicate_linked(sj_objs, sj_obj, False)
            for new_o in duplicates:
                unlink_store(new_o, sj_mesh)

            if scn:
                for o in sel:
                    o.select = True

            # introduces crash bug
            # update_stored(sj_mesh)
        else:
            # renamed
            sj_objs = get_stored_sjobjects_unsafe(sj_mesh.sjoin_link_name)
            for o in sj_objs:
                o.sjoin_mesh = sj_mesh.name

    # no matter what keep sjoin_link_name same as sj_mesh.name
    sj_mesh.sjoin_link_name = sj_mesh.name

    # make sure there are no two expended objects, actually ones that look expended, this can happen if expended sj is duplicated
    if not check_is_expended(sj_obj):
        set_object_collapsed(sj_obj)


def check_is_sjoin_obj(obj):
    return obj and obj.type == 'MESH' and obj.data.is_sjoin


def check_is_expended(obj):
    return check_is_sjoin_obj(obj) and obj.data.expanded_obj == obj.name

def check_is_there_expended_obj(mesh):
    return mesh.expanded_obj != ''

def get_stored_sjobjects(sj_mesh):
    # check_fix_rename(sj_mesh)
    return get_stored_sjobjects_unsafe(sj_mesh.name)

import mathutils

# def collect_children_no_clear

def get_dependent_meshes(data):
    dep = []
    for o in bpy.data.objects:
        if o.data == data:
            # if object is part of sjoin add it
            sj = get_sjmesh(o.sjoin_mesh)
            if sj and sj != data and not check_is_there_expended_obj(sj):
                dep.append(sj)
    return dep


def update_stored(mesh):
    clear_mesh(mesh)
    # I need to redesign this passing bpy.context.active_object is bad, pass context everywhere or something
    if bpy.context.active_object:
        join_to_mesh(bpy.context, mesh, get_stored_sjobjects(mesh), bpy.context.active_object)


def update_meshes_rec_co(meshes, c):
    if c == 10:
        return

    next_dep = []
    for mesh in meshes:
        update_stored(mesh)
        next_dep += get_dependent_meshes(mesh)

    update_meshes_rec_co(next_dep, c+1)

def update_meshes_rec(meshes):
    update_meshes_rec_co(meshes, 0)

def update_data_rec(data):
    mashes = get_dependent_meshes(data)
    update_meshes_rec(mashes)

def collect_children_unsafe(obj, scn):
    if not obj:
        return
    set_object_collapsed(obj)
    clear_mesh(obj.data)
    all_ch = get_all_children(obj)


    obj.data.sjoin_link_name = obj.data.name


    for ch in all_ch:
        # unlink_store(ch, obj.data)
        if ch.parent == obj:
            basis = ch.matrix_parent_inverse * ch.matrix_basis
            ch.parent = None
            ch.matrix_basis = basis

    scn.update()
    join_to_mesh(bpy.context, obj.data, all_ch + get_stored_sjobjects(obj.data), obj)
    update_meshes_rec(get_dependent_meshes(obj.data))

    for ch in all_ch:
        unlink_store(ch, obj.data)


# careful this return parent too
def get_leaf_children(obj):
    if len(obj.children) == 0:
        return [obj]
    else:
        return [x for o in obj.children for x in get_leaf_children(o)]

def get_all_children(obj):
    if len(obj.children) == 0:
        return []
    else:
        return list(obj.children) + [x for o in obj.children for x in get_leaf_children(o)]

def get_children_hierarchically(obj_list):
    if not obj_list:
        return []

    next_level = []
    for obj in obj_list:
        next_level += list(obj.children)


    return get_children_hierarchically(next_level) + obj_list

def get_expanded_obj(sj_mesh):
    return bpy.data.objects.get(sj_mesh.expanded_obj)

def collapse_expanded(sj_mesh):
    obj = get_expanded_obj(sj_mesh)
    if obj:
        collect_children(obj, bpy.context.scene)


def collect_children(obj, scn):
    # collect_children_unsafe(obj, scn)
    # return
    if obj is None:
        return

    global update_lock
    update_lock = True

    children = get_children_hierarchically([obj])

    for ch in children:
        # check_is_expended fixed the crashing bug
        if check_is_expended(ch):
            collect_children_unsafe(ch, scn)


    update_lock = False



def set_object_expended(j_obj):
    j_obj.data.expanded_obj = j_obj.name
    j_obj.draw_type = 'BOUNDS'

def set_object_collapsed(j_obj):
    if j_obj.data.expanded_obj == j_obj.name:
        j_obj.data.expanded_obj = ''
    j_obj.draw_type = 'TEXTURED'

def expand_objects(j_obj, scn):
    if j_obj is None:
        return

    global update_lock
    update_lock = True

    # if there is expended collapse it
    collapse_expanded(j_obj.data)


    # set current to expended
    set_object_expended(j_obj)

    # for o in bpy.data.objects:
    #     if o.data.is_sjoin:
    #         collect_children(o, scn)
    j_obj.select = False

    sj_objects = get_stored_sjobjects(j_obj.data)

    for o in sj_objects:
        link_stored(o, j_obj, scn)

    update_lock = False



def unlink_store(obj, sjoin_mesh):
    obj.use_fake_user = True
    obj.sjoin_mesh = sjoin_mesh.name

    # remove parent, and make transform relative to ex-parent

    for s in obj.users_scene[:]:
        s.objects.unlink(obj)

def link_stored(obj, sjoin_object, scn):
    if obj.name not in scn.objects:
        scn.objects.link(obj)

    scn.update()

    if not obj.parent:
        obj.parent = sjoin_object

    # always call fake_ser and sjoin_mesh together

    # this adds objects to local view
    obj.layers = sjoin_object.layers
    add_to_loc_view(obj, scn)

    obj.use_fake_user = False
    obj.sjoin_mesh = ''

    obj.select = True
    scn.objects.active = obj


from bpy.app.handlers import persistent


# looks like scene_update will be called by every operator in join_to_mesh update so I need to lock it
update_lock = False
@persistent
def scene_update(scene):
    # disable edit mode for sjoin objects

    global update_lock
    if update_lock:
        return
    update_lock = True
    active = scene.objects.active
    if check_is_sjoin_obj(scene.objects.active) and active.data.is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT')
        # this below won't always work??
        '''
        scene.update()
        bpy.ops.sjoin.expand()
        scene.update()
        '''

    object_update(active, scene)

    # this won't detect modifier updates
    # according to the wiki it should http://wiki.blender.org/index.php/Dev:2.6/Source/Render/UpdateAPI
    '''
    if bpy.data.objects.is_updated:
        for ob in scene.objects[:]:
            if ob.is_updated or ob.is_updated_data:
                object_update(ob, scene)
            # if not check_is_sjoin_obj(ob) and ob.data and ob.is_updated_data:
            #     print('updating object data for ', ob.data)
                # update_data_rec(ob.data)
    '''

    update_lock = False


def object_update(obj, scn):
    if check_is_sjoin_obj(obj):
        # update_lock = True
        check_fix_rename(obj.data, obj, scn)
        # recursive update could be added here but it might be slow for large scenes
        # update_lock = False

@persistent
def before_save(dummy):
    # don't save any meshes that have fake user because of sjoin if sjoin is deleted or has 0 users
    for o in bpy.data.objects:
        if o.sjoin_mesh != '':
            sjoin = get_sjmesh(o.sjoin_mesh)
            if not sjoin or not sjoin.is_sjoin:
                o.use_fake_user = False
                o.sjoin_mesh = ''
            else:
                o.use_fake_user = sjoin.users != 0




######## GUI #########################

class ExpandSjoin(bpy.types.Operator):
    """Expand Smart Join"""
    bl_idname = "sjoin.expand"
    bl_label = "Expand Smart Join"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        ao = context.active_object
        if not ao:
            return False
        return check_is_sjoin_obj(ao) and not check_is_expended(ao)

    def execute(self, context):
        ao = context.active_object
        expand_objects(ao, context.scene)

        # somthing changes active object
        ao.select = True
        context.scene.objects.active = ao
        return {'FINISHED'}


def get_first_sjoin_parent(obj):
    robj = obj
    while True:
        if not robj:
            return None
        if check_is_expended(robj):
            return robj
        robj = robj.parent


def check_not_expanded_sjoin(context, obj):
    # can be done for multiple meshes with state
    return check_is_sjoin_obj(obj)


class CollapseSjoin(bpy.types.Operator):
    """Collapse Smart Join"""
    bl_idname = "sjoin.collapse"
    bl_label = "Collapse Smart Join"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        ao = context.active_object
        if not ao:
            return False
        return get_first_sjoin_parent(ao)

    def execute(self, context):

        # with expanded collapsed state i can use whole selection as ao
        ao = context.active_object
        scn = context.scene
        obj = get_first_sjoin_parent(ao)

        collect_children(obj, scn)
        obj.select = True
        scn.objects.active = obj
        return {'FINISHED'}


class SJoinObjects(bpy.types.Operator):
    """Add To Smart Join"""
    bl_idname = "sjoin.join_add"
    bl_label = "Add To Smart Join"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # TODO: if I don't respect len(context.selected_objects) > 1 everything disappears
        return check_is_sjoin_obj(context.active_object) and len(context.selected_objects) > 1

    def execute(self, context):
        scn = context.scene
        update_lock = True


        active = context.active_object




        # if active is sjoin add others to it
        # TODO: make it work, currently poll is limeted so this isn't called
        if not check_is_sjoin_obj(active):
            ac_cop_obj = active.copy()

            for c in active.children:
                if c in context.selected_objects:
                    parent_keep_tr(c, ac_cop_obj, scn)

            ac_cop_mesh = active.data.copy()

            scn.objects.link(ac_cop_obj)
            ac_cop_obj.data = ac_cop_mesh
            ac_cop_obj.select = True

        active.select = False

        selected = context.selected_objects[:]

        '''
        # find what to parent j_object to
        highest = active
        while highest.parent in selected:
            highest = highest.parent


        # create new s_join mesh at the position of active object
        active.data.is_sjoin = True
        active.parent = highest.parent
        '''

        #parerent the selection and merge it
        for o in selected:
            if o.parent not in selected:
                parent_keep_tr(o, active, scn)
                # o.matrix_parent_inverse = j_obj.matrix_world.inverted()

        if not check_is_expended(active):
            expand_objects(active, context.scene)
            collect_children(active, scn)


        update_lock = False
        active.select = True

        return {'FINISHED'}

bpy.utils.register_class(SJoinObjects)
#bpy.utils.unregister_class(SJoinObjects)

def parent_keep_tr(obj, parent, scn):
    w = obj.matrix_world.copy()
    obj.parent = parent
    scn.update()
    obj.matrix_world = w



class SJoinObjects(bpy.types.Operator):
    """Smart Join"""
    bl_idname = "sjoin.join"
    bl_label = "Smart Join"
    bl_options = {'REGISTER', 'UNDO'}


    origin_at_cursor = BoolProperty(default=False, name="Origin At Cursor")

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        update_lock = True


        active = context.active_object
        selected = context.selected_objects[:]
        scn = context.scene

        # find what to parent j_object to
        highest = active
        while highest.parent in selected:
            highest = highest.parent

        # create new s_join mesh at the position of active object
        name = active.name + '_sj'
        j_mesh = bpy.data.meshes.new(name = name)
        j_mesh.is_sjoin = True
        j_obj = bpy.data.objects.new(name = name, object_data= j_mesh)
        scn.objects.link(j_obj)
        j_obj.parent = highest.parent
        if self.origin_at_cursor:
            j_obj.location = context.scene.cursor_location
        else:
            j_obj.location = active.matrix_local.to_translation()
        j_obj.layers = active.layers

        j_obj.select = True
        add_to_loc_view(j_obj, scn)

        scn.objects.active = j_obj
        set_object_expended(j_obj)


        #parerent the selection and merge it
        for o in selected:
            if o.parent not in selected:
                parent_keep_tr(o, j_obj, scn)

                # o.matrix_parent_inverse = j_obj.matrix_world.inverted()

        collect_children(j_obj, scn)
        update_lock = False


        return {'FINISHED'}


class SeparateObjects(bpy.types.Operator):
    """Separate S.Join"""
    bl_idname = "sjoin.separate"
    bl_label = "Separate S.Join"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.ops.sjoin.expand.poll()

    def execute(self, context):
        #TODO this needs to duplicate objects!!!
        active = context.active_object
        data = active.data
        # bpy.ops.sjoin.collapse()
        bpy.ops.sjoin.expand()
        clear_mesh(data)
        for o in active.children[:]:
            parent_keep_tr(o, active.parent, context.scene)
        active.select = False

        for sc in active.users_scene:
            sc.objects.unlink(active)

        bpy.data.objects.remove(active)
        return {'FINISHED'}


class UpdateRec(bpy.types.Operator):
    """Update S.Join Dependencies"""
    bl_idname = "sjoin.update_rec"
    bl_label = "Update S.Join Dependencies"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        #TODO this needs to duplicate objects!!!
        for o in context.selected_objects:
            if o.data:
                update_data_rec(o.data)
        return {'FINISHED'}


class ApplySJ(bpy.types.Operator):
    """Apply Smart Join"""
    bl_idname = "sjoin.apply"
    bl_label = "Apply Smart Join"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object and check_is_sjoin_obj(context.active_object) and not check_is_expended(context.active_object)

    def execute(self, context):
        context.active_object.data.is_sjoin = False
        return {'FINISHED'}

"""
class SJ_BasePanel(bpy.types.Panel):   
    bl_label = "Smart Join"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"
    bl_category = 'Relations'

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator('sjoin.join')
        row.operator('sjoin.separate')
        layout.operator('sjoin.join_add')
        layout.separator()
        row = layout.row(align=True)
        row.operator('sjoin.expand')
        row.operator('sjoin.collapse')
        layout.operator('sjoin.update_rec')
        layout.operator('sjoin.apply')
"""        

class SCULPTOpsMenu(bpy.types.Menu):
    """Smart Join Menu"""
    bl_label = "Smart Join Menu"
    bl_idname = "group.smartjoin_menu"
    
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'          

        layout.operator('sjoin.join', "SmartJoin", icon="LOCKVIEW_ON")
        layout.operator('sjoin.separate', "Separate All", icon="LOCKVIEW_OFF")

        layout.separator()  

        layout.operator('sjoin.join_add', "Add to Smart", icon="PASTEFLIPUP")

        layout.separator()  

        layout.operator('sjoin.expand', "Expand Join", icon="PASTEDOWN")
        layout.operator('sjoin.collapse', "Collapse Join", icon="COPYDOWN")    

        layout.separator()  

        layout.operator('sjoin.update_rec', "Update", icon="LOAD_FACTORY")
        
########################################################################################################
# define classes for registration
classes = [SJoinObjects, ExpandSjoin, SeparateObjects, UpdateRec, ApplySJ]    


def register():
    for c in classes:
        bpy.utils.register_class(c)


    bpy.utils.register_module(__name__)
    bpy.types.Mesh.is_sjoin = BoolProperty(default=False)

    bpy.types.Mesh.sjoin_link_name = StringProperty()
    bpy.types.Mesh.expanded_obj = StringProperty()
    bpy.types.Object.sjoin_mesh = StringProperty(default = '')
    bpy.app.handlers.scene_update_post.append(scene_update)
    bpy.app.handlers.save_pre.append(before_save)

    


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    del bpy.types.Mesh.is_sjoin
    del bpy.types.Object.sjoin_mesh
    bpy.app.handlers.scene_update_post.remove(scene_update)
    bpy.app.handlers.save_pre.remove(before_save)

    bpy.utils.unregister_module(__name__)



if __name__ == "__main__":
    register()


