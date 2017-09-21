"""
bl_info = {
    "name": "Nikitron tools",
    "version": (0, 1, 3),
    "blender": (2, 6, 9), 
    "category": "Object",
    "author": "Nikita Gorodetskiy",
    "location": "object",
    "description": "Nikitron tools - vertices and object names, curves to 3d, material to object mode, spread objects, bounding boxes",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Object/Nikitron_tools",          
    "tracker_url": "http://www.blenderartists.org/forum/showthread.php?272679-Addon-WIP-Sverchok-parametric-tool-for-architects",  
}
"""
# 2013-09-03 shift
# 2013-09-04 hooks

import bpy
from mathutils.geometry import intersect_line_plane
import mathutils
from mathutils import Vector
import math
from math import radians
import re

class CurvesTo3D (bpy.types.Operator):
    """Put curves to ground and turn to 3d mode (wiring them) for farthere spread to layout sheet"""
    bl_idname = "object.curv_to_3d"
    bl_label = "Curves to 3d"
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        obj = bpy.context.selected_objects
        if obj[0].type == 'CURVE':
            for o in obj:
                o.data.extrude = 0.0
                o.data.dimensions = '3D'
                #o.matrix_world.translation[2] = 0
        return {'FINISHED'}

class CurvesTo2D (bpy.types.Operator):
    """Curves turn to 2d mode (and thicken 0.03 mm)"""
    bl_idname = "object.curv_to_2d"
    bl_label = "Curves to 2d"
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        obj = bpy.context.selected_objects
        if obj[0].type == 'CURVE':
            for o in obj:
                o.data.extrude = 0.0016
                o.data.dimensions = '2D'
                nam = o.data.name
                # Я фанат группы "Сплин", ребята.
                for splin in bpy.data.curves[nam].splines:
                    splin.use_smooth = False
                    for point in splin.bezier_points:
                        point.radius = 1.0
        return {'FINISHED'}

class ObjectNames (bpy.types.Operator):
    """Make all objects show names in 3d"""      
    bl_idname = "object.name_objects" 
    bl_label = "Name objects"        
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        obj = bpy.context.selected_objects
        for ob in obj:
            mw = ob.matrix_world.translation
            name_all = re.match(r'(\w+)', ob.name)
            name = name_all.group(1)
            box = ob.bound_box
            v1 = Vector((box[0][0:]))
            v2 = Vector((box[6][0:]))
            len = Vector((v2-v1)).length
            self.run(mw,name,len)
        return {'FINISHED'}

    def run(self, origin,text,length):
       # Create and name TextCurve object
        bpy.ops.object.text_add(
        location=origin,
        rotation=(radians(0),radians(0),radians(0)))
        ob = bpy.context.object
        ob.name = 'lable_'+str(text)
        tcu = ob.data
        tcu.name = 'lable_'+str(text)
        # TextCurve attributes
        tcu.body = str(text)
        tcu.font = bpy.data.fonts[0]
        tcu.offset_x = 0
        tcu.offset_y = -0.25
        tcu.resolution_u = 2
        tcu.shear = 0
        if length < 0.0625:
            Tsize = 0.01*(5*length)
        else:
            Tsize = 0.0625
        tcu.size = Tsize
        tcu.space_character = 1
        tcu.space_word = 1
        #tcu.align = 'CENTER'
        # Inherited Curve attributes
        tcu.extrude = 0.0
        tcu.fill_mode = 'NONE'
        
        
class VerticesNumbers3D (bpy.types.Operator):
    """make all vertices show numbers in 3D"""      
    bl_idname = "object.vertices_numbers3d"
    bl_label = "Vertices num."
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        obj1 = bpy.context.selected_objects[0]
        if obj1.type != 'MESH':
            print ("Select meshes, plase")
            return {'CANCELLED'}
        mw1 = obj1.matrix_world
        mesh1 = obj1.data
        mesh1.update()
        ver1 = mesh1.vertices
        for id in ver1:
            i = id.index
            coor = mw1 * ver1[i].co
            self.run(coor,i)
        return {'FINISHED'}
    
    def run(self, origin,text):
        # Create and name TextCurve object
        bpy.ops.object.text_add(
        location=origin,
        rotation=(radians(90),radians(0),radians(0)))
        ob = bpy.context.object
        ob.name = 'vert '+str(text)
        tcu = ob.data
        tcu.name = 'vert '+str(text)
        # TextCurve attributes
        tcu.body = str(text)
        tcu.font = bpy.data.fonts[0]
        tcu.offset_x = 0
        tcu.offset_y = 0
        tcu.shear = 0
        tcu.size = 0.3
        tcu.space_character = 1
        tcu.space_word = 1
        # Inherited Curve attributes
        tcu.extrude = 0
        tcu.fill_mode = 'BOTH'

vert_max = 0

class Connect2Meshes (bpy.types.Operator):
    """connect two objects by mesh edges with vertices shift and hooks to initial objects"""      
    bl_idname = "object.connect2objects"
    bl_label = "connect2objects"
    bl_options = {'REGISTER', 'UNDO'}
    
    def dis(self, x,y):
        vec = mathutils.Vector((x[0]-y[0], x[1]-y[1], x[2]-y[2]))
        return vec.length
    
    def maxObj(self, ver1, ver2, mw1, mw2):
        if len(ver1) > len(ver2):
            inverc = 0
            vert1 = ver1
            mworld1 = mw1
            vert2 = ver2
            mworld2 = mw2
        else:
            inverc = 1
            vert1 = ver2
            mworld1 = mw2
            vert2 = ver1
            mworld2 = mw1
        cache_max = [vert1, mworld1]
        cache_min = [vert2, mworld2]
        return cache_max, cache_min, inverc
    
    def points(self, ver1, ver2, mw1, mw2, shift):
        vert_new = []
        # choosing maximum vertex count in ver1/2, esteblish vert2 - mincount of vertex
        cache = self.maxObj(ver1, ver2, mw1, mw2)
        vert1 = cache[0][0]
        vert2 = cache[1][0]
        mworld1 = cache[0][1]
        mworld2 = cache[1][1]
        inverc = cache[2]
        # append new verts in new obj
        for v in vert2:
            v2 = mworld2 * v.co
            if len(vert2) > v.index + shift:
                v1 = mworld1 * vert1[v.index + shift].co
            else:
                v1 = mworld1 * vert1[v.index + shift - len(vert2)].co
            if inverc == True:
                m1 = mworld2.translation
                m2 = mworld2.translation
            else:
                m1 = mworld1.translation
                m2 = mworld1.translation
            vert_new.append(v2 - m2)
            vert_new.append(v1 - m1)
        return vert_new
    
    def edges(self, vert_new):
        edges_new = []
        i = -2
        for v in vert_new:
            # dis(vert_new[i],vert_new[i+1]) < 10 and 
            if i > -1 and i < (len(vert_new)):
                edges_new.append((i,i + 1))
            i += 2
        return edges_new
    
    def mk_me(self, name):
        me = bpy.data.meshes.new(name+'Mesh')
        return me
    
    def mk_ob(self, mesh, name, mw):
        loc = mw.translation.to_tuple()
        ob = bpy.data.objects.new(name, mesh)
        ob.location = loc
        ob.show_name = True
        bpy.context.scene.objects.link(ob)
        return ob
    
    def def_me(self, mesh, ver1, ver2, mw1, mw2, obj1, obj2, nam):
        ver = self.points(ver1, ver2, mw1, mw2, bpy.context.scene.shift_verts)
        edg = self.edges(ver)
        mesh.from_pydata(ver, edg, [])
        mesh.update(calc_edges=True)
        if bpy.context.scene.hook_or_not:
            self.hook_verts(ver, obj1, obj2, nam, ver1, ver2, mw1, mw2)
        return
    
    # preparations for hooking
    def hook_verts(self, ver, obj1, obj2, nam, ver1, ver2, mw1, mw2):
        # pull cache from maxObj
        cache = self.maxObj(ver1, ver2, mw1, mw2)
        vert1 = cache[0][0]
        vert2 = cache[1][0]
        mworld1 = cache[0][1]
        mworld2 = cache[1][1]
        inverc = cache[2]
        points_ev = []
        points_od = []
        # devide even/odd verts
        for v in ver:
            if (ver.index(v) % 2) == 0:
                points_ev.append(ver.index(v))
                # print ('чёт ' + str(ver.index(v)))
            else:
                points_od.append(ver.index(v))
                # print ('нечет ' + str(ver.index(v)))
        if bpy.context.selected_objects:
            bpy.ops.object.select_all(action='TOGGLE')
        # depend on bigger (more verts) object it hooks even or odd verts
        if inverc == False:
            # ob1 = obj1 ob2 = obj2, 1 - bigger
            self.hooking_action(obj2, nam, points_ev, ver)
            self.hooking_action(obj1, nam, points_od, ver)
        else:
            # ob1 = obj2 ob2 = obj1, 2 - bigger
            self.hooking_action(obj2, nam, points_od, ver)
            self.hooking_action(obj1, nam, points_ev, ver)
        
    # free hooks :-)
    def hooking_action(self, ob, nam, points, verts_of_object):
        # select 1st obj, second connection
        bpy.data.scenes[bpy.context.scene.name].objects[ob.name].select = True
        bpy.data.scenes[bpy.context.scene.name].objects[nam].select = True
        bpy.data.scenes[bpy.context.scene.name].objects.active = bpy.data.objects[nam]
        # deselect vertices
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.object.editmode_toggle()
        # select nearby vertices
        for vert in points:
            bpy.context.object.data.vertices[vert].select = True
        # hook itself
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.hook_add_selob(use_bone=False)
        #bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.object.editmode_toggle()
        # deselect all
        bpy.ops.object.select_all(action='TOGGLE')

    
    def execute(self, context):
        context.scene.update()
        obj1 = context.selected_objects[0]
        obj2 = context.selected_objects[1]
        mw1 = obj1.matrix_world
        mw2 = obj2.matrix_world
        mesh1 = obj1.data
        mesh1.update()
        mesh2 = obj2.data
        mesh2.update()
        ver1 = mesh1.vertices
        ver2 = mesh2.vertices
        nam = 'linked_' + str(obj1.name) + str(obj2.name)
        me = self.mk_me(nam)
        ob = self.mk_ob(me, nam, mw1)
        self.def_me(me, ver1, ver2, mw1, mw2, obj1, obj2, nam)
        print ('---- NIKITRON_connect2objects MADE CONNECTION BETWEEN: ' + str(obj1.name) + ' AND ' + str(obj2.name) + ' AND GOT ' + str(ob.name) + ' ----')
        return {'FINISHED'}


class MaterialToObjectAll (bpy.types.Operator):
    """all materials turned to object mode"""      
    bl_idname = "object.materials_to_object"
    bl_label = "Materials to object"
    bl_options = {'REGISTER', 'UNDO'} 
    def execute(self, context):
        obj = bpy.context.selected_objects
        mode = 'OBJECT'
        for o in obj:
            materials = bpy.data.objects[o.name].material_slots
            for m in materials:
                m.link = mode
        return {'FINISHED'}
    
class MaterialToDataAll (bpy.types.Operator):
    """all materials turned to data mode"""      
    bl_idname = "object.materials_to_data"
    bl_label = "Materials to data"
    bl_options = {'REGISTER', 'UNDO'} 
    def execute(self, context):
        obj = bpy.context.selected_objects
        mode = 'DATA'
        for o in obj:
            materials = bpy.data.objects[o.name].material_slots
            for m in materials:
                m.link = mode
        return {'FINISHED'}


class BoundingBox (bpy.types.Operator):
    """Make bound boxes for selected objects in mesh"""      
    bl_idname = "object.bounding_boxers"
    bl_label = "Bounding boxes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        objects = bpy.context.selected_objects
        i = 0
        for a in objects:
            self.make_it(i, a)
            i += 1
        return {'FINISHED'}
    
    def make_it(self, i, obj):
        box = bpy.context.selected_objects[i].bound_box
        mw = bpy.context.selected_objects[i].matrix_world
        name = (bpy.context.selected_objects[i].name + '_bounding_box')
        me = bpy.data.meshes.new(name+'Mesh')
        ob = bpy.data.objects.new(name, me)
        ob.location = mw.translation
        ob.scale = mw.to_scale()
        ob.rotation_euler = mw.to_euler()
        ob.show_name = True
        bpy.context.scene.objects.link(ob)
        loc = []
        for ver in box:
            loc.append(mathutils.Vector((ver[0],ver[1],ver[2])))
        me.from_pydata((loc), [], ((0,1,2,3),(0,1,5,4),(4,5,6,7), (6,7,3,2),(0,3,7,4),(1,2,6,5)))
        me.update(calc_edges=True)
        return

class SpreadObjects (bpy.types.Operator):
    """spread all objects on sheet for farthere use in dxf layout export"""
    bl_idname = "object.spread_objects"
    bl_label = "Spread objects"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = bpy.context.selected_objects
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        count = len(obj) - 1                # items number
        row = math.modf(math.sqrt(count))[1] or 1 #optimal number of rows and columns !!! temporery solution
        locata = mathutils.Vector()    # while veriable 
        dx, dy, ddy = 0, 0, 0                       # distance
        while count > -1:   # iterations X
            locata[2] = 0               # Z = 0
            row1 = row
            x_curr = []                     # X bounds collection
            locata[1] = 0              # Y = 0
            while row1:         # iteratiorns Y
                # counting bounds
                bb = obj[count].bound_box
                mwscale = obj[count].matrix_world.to_scale()
                mwscalex = mwscale[0]
                mwscaley = mwscale[1]
                x0 = bb[0][0]
                x1 = bb[4][0]
                y0 = bb[0][1]
                y1 = bb[2][1]
                ddy = dy            # secondary distance to calculate avverage
                dx = mwscalex*(max(x0,x1)-min(x0,x1)) + 0.03        # seek for distance !!! temporery solution
                dy = mwscaley*(max(y0,y1)-min(y0,y1)) + 0.03        # seek for distance !!! temporery solution
                # shift y
                locata[1] += ((dy + ddy) / 2)
                # append x bounds
                x_curr.append(dx)
                bpy.ops.object.rotation_clear()
                bpy.context.selected_objects[count].location = locata
                row1 -= 1
                count -= 1
            locata[0] += max(x_curr)        # X += 1
            dx, dy, ddy = 0, 0, 0
            del(x_curr)
        return {'FINISHED'}
    
from bpy.props import IntProperty, BoolProperty

# this def for connect2objects maximum shift (it cannot update scene's veriable somehow)
def maxim():
    if bpy.context.selected_objects[0].type == 'MESH':
        if len(bpy.context.selected_objects) >= 2:     
            len1 = len(bpy.context.selected_objects[0].data.vertices)
            len2 = len(bpy.context.selected_objects[1].data.vertices)
            maxim = min(len1, len2)
            #print (maxim)
    return maxim

def shift():
    bpy.types.Scene.shift_verts = IntProperty(
        name="shift_verts",
        description="shift vertices of smaller object, it can reach maximum (look right), to make patterns",
        min=0, max=1000,  #maxim(), - this cannot be updated
        default = 0, options={'ANIMATABLE', 'LIBRARY_EDITABLE'})
    return
shift()

# this flag for connetc2objects, hook or not?
def hook_or_not():
    bpy.types.Scene.hook_or_not = BoolProperty(
        name="hook_or_not",
        description="hook or not new connected vertices to parents objects? it will get spider's web's linkage effect",
        default = True)
    return
hook_or_not()

# this cache for define vertex count of currently selected materials.
#cache_obj = []
#def cache_add():
#    for i in bpy.context.selected_objects:
#        cache_obj.append(i)
#    print (cache_obj)
#cache_add()
"""
class NikitronPanel(bpy.types.Panel):
    bl_idname = "panel.nikitron"
    bl_label = "Nikitron tools"
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'TOOLS'

    def draw(self, context):
        #global cache_obj
        #global cache_add
        #global shift
        global maxim
        layout = self.layout
        
        # it is all about maximum shift, it cannot update scene's veriable 'shift_verts' with 'maxim' veriable somehow
        #if context.selected_objects[0] != cache_obj[0]:
        #    bpy.data.scenes[0].update_tag()
        #    cache_obj = []
        #    cache_add()
        #    shift()

        row = layout.row()
        row.label(text="N.T._ver. 0.1.3")
        if context.selected_objects:
            if context.selected_objects[0].type == 'CURVE':
                row = layout.row()
                row.operator("object.curv_to_3d",icon="CURVE_DATA")
                
                row = layout.row()
                row.operator("object.curv_to_2d",icon="CURVE_DATA")
        
        row = layout.row()
        row.operator("object.spread_objects",icon="OBJECT_DATA")
        
        row = layout.row()
        row.operator("object.materials_to_object",icon="MATERIAL_DATA")
        
        row = layout.row()
        row.operator("object.materials_to_data",icon="MATERIAL_DATA")
            
        row = layout.row()
        row.operator("object.name_objects",icon="OBJECT_DATA")
        
        row = layout.row()
        row.operator("object.vertices_numbers3d",icon="MESH_DATA")
        
        row = layout.row()
        row.operator("object.bounding_boxers",icon="OBJECT_DATA")
        
        if context.selected_objects:
            if context.selected_objects[0].type == 'MESH':
                row = layout.row()
                row.operator("object.connect2objects",icon="MESH_DATA")
                row = layout.row()
                row.prop(bpy.context.scene, "shift_verts", text="shift")
                row.label(text="max " + str(maxim()))
                row = layout.row()
                row.prop(bpy.context.scene, "hook_or_not", text="hook new vertices?")
"""
        
my_classes = [CurvesTo3D, CurvesTo2D, ObjectNames, VerticesNumbers3D, Connect2Meshes, MaterialToObjectAll, MaterialToDataAll, BoundingBox, SpreadObjects]
    
def register():
    for clas in my_classes:
        bpy.utils.register_class(clas)

def unregister():
    for clas in my_classes:
        bpy.utils.unregister_class(clas)
    
if __name__ == "__main__":
    register()
