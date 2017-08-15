bl_info = {
    "name": "Itérative tree",
    "author": "Herpin Maxime",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > Toolshelf > Create > Tree",
    "description": "Adds a Tree",
    "warning": "",
    "wiki_url": "",
    "category": "Add Curve"}


import bpy
import mathutils
from random import *
from math import *
from bpy.props import *


# create_tree: int*Float*Float*Float*Float*Float*int*int*Float*Int*Float*Float*Bool*Float*Float*Float*Bool*Float*Vector3 -> None
#			create a tree as a curve

def create_tree(iterations, radius, radius_dec, trunk_radius_dec, split_proba, dist, split_angle, first_split_angle, bevel, trunk_min_length, trunk_variation, gravity_fact, preserve_trunk, dist_decr, branch_variation, split_proba_rise, is_force, force, emitter):

    # The first point of the tree:
    root = [(0, 0, 0, 1), (0, 0, 1), 1]
    # Setting up the curve
    cu = bpy.data.curves.new("Tree", "CURVE")
    ob = bpy.data.objects.new("Tree", cu)
    ob.location = bpy.context.scene.cursor_location
    scn = bpy.context.scene
    scn.objects.link(ob)
    scn.objects.active = ob
    cu.dimensions = "3D"
    cu.fill_mode = "FULL"
    cu.bevel_resolution = 1
    # overall radius of the tree
    cu.bevel_depth = .3 * radius if bevel else 0
    cu.use_uv_as_generated = True

    ob.select = True
    spline = cu.splines.new("POLY")
    spline.points[0].co = root[0]
    spline.points[0].radius = 1
    # fpoint : list of the splines with their last point
    # points : list of fpoint
    fpoint = [spline, root]
    points = [fpoint]

    # function apply_force: vector3*Float -> vector3
    #						modify the coordinates to push them from or towards the emitter
    emitter = ob.matrix_world * mathutils.Vector(emitter)

    def apply_force(coord, f):
        return force / 100 * (f - coord)

    # shows an empty object at the location of the emitter, for better visualization
    if is_force:
        empt = bpy.ops.object.add(type='EMPTY', location=emitter)
        bpy.context.active_object.name = 'forceEmpty'
    elif bpy.data.objects.get("forceEmpty") is not None:
        empt.delete()

    # function create_points: point -> None
    #						  given a spline and its last point, creates new points and update the list of points
    def create_points(point):

        # currently stupid, but I keep it because I may use it to add badass new things.
        longevity = point[1][2]

        # Separate the last point coordinates for better readability
        xyz = point[1][0]
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]

        # Same here
        # The direction is a vector showing where the next point should be
        direction = point[1][1]
        a = direction[0]
        b = direction[1]
        c = direction[2]

        # The spline we are using to create new points
        curr_spline = point[0]
        curr_spline_length = len(point[0].points)

        # if the iteration number is lower than wanted, keep making trunk points
        if longevity <= trunk_min_length:
            splits = 1 if longevity < trunk_min_length else 2
            real_split_angle = split_angle * trunk_variation
            real_rad_dec = trunk_radius_dec

        else:
            splits = int(2 + split_proba - random())
            real_split_angle = split_angle
            real_rad_dec = radius_dec

        # Random angle to randomise the split direction
        rand_theta = random() * 2 * pi

        # Will be used to know if the current spline is the trunk
        pind = points.index(point)

        # If there is no split, change the split angle to just add variation is the branch
        if (splits == 1) and (pind > 0):
            real_split_angle = split_angle * branch_variation

        # This is overkill since there is a maximum of two splits, but in case I want to add an option with more splits...
        for i in range(0, splits):
            # if the trunkk has to be preserved, keep the branch variation as it should be
            if (preserve_trunk) and (pind == 0) and (longevity > trunk_min_length):
                if i == 0:
                    real_split_angle = split_angle * trunk_variation
                    real_rad_dec = trunk_radius_dec * 2
                else:
                    real_split_angle = first_split_angle
                    real_rad_dec = radius_dec
            # rotate the angle so the points will be distributed at uniform angles
            theta = rand_theta + i * 2 * pi / splits
            # the split angle
            phi = real_split_angle * pi / 180
            # distances between the direction coordinates
            n_ab = 1.0 if b * c == 0 else sqrt(a * a + b * b)
            n_cb = 1.0 if a * b == 0 else sqrt(c * c + b * b)
            n_abc = 1.0 if a * b * c == 0 else sqrt(a * a + b * b + c * c)

            sin_the = sin(theta)
            cos_the = cos(theta)
            sin_phi = sin(phi)
            cos_phi = cos(phi)

            # convert spherical coordinates aligned with the direction vector, to global carthesian ones
            new_x = x + dist * cos_phi * a / n_abc + dist * sin_phi * sin_the * b / n_ab
            new_y = y + dist * cos_phi * b / n_abc - dist * sin_phi * sin_the * a / n_ab + dist * sin_phi * cos_the * c / n_cb
            new_z = z + dist * cos_phi * c / n_abc - dist * sin_phi * cos_the * b / n_cb - gravity_fact * longevity / 500

            # apply force to new coordinates
            if is_force:
                new_x += apply_force(new_x, emitter[0])
                new_y += apply_force(new_y, emitter[1])
                new_z += apply_force(new_z, emitter[2])
            # generate a tuple with those coordinates
            new_xyz = (new_x, new_y, new_z)
            # generate a new direction vector
            new_d = mathutils.Vector((new_x - x, new_y - y, new_z - z))
            new_d.normalize()

            # if the split branch is the first one, just add the new point to current spline, else create a new spline
            if i == 0:
                point[0].points.add(1)
                point[0].points[curr_spline_length].co = (new_x, new_y, new_z, 1)
                point[0].points[curr_spline_length].radius = ((1 - real_rad_dec / 5)**(longevity - trunk_min_length)) * (1 - trunk_radius_dec / 5)**trunk_min_length
                point[1][0] = new_xyz
                point[1][1] = new_d
                point[1][2] += 1
            else:
                new_spline = cu.splines.new("POLY")
                new_spline.points[0].co = (x, y, z, 1)
                new_spline.points[0].radius = ((1 - real_rad_dec / 5)**(longevity - trunk_min_length)) * (1 - trunk_radius_dec / 5)**trunk_min_length
                new_spline.points.add(1)
                new_spline.points[1].co = (new_x, new_y, new_z, 1)
                new_spline.points[1].radius = ((1 - real_rad_dec / 5)**(longevity + 1 - trunk_min_length)) * (1 - trunk_radius_dec / 5)**trunk_min_length
                new_point = [new_xyz, new_d, longevity + 1]
                points.append([new_spline, new_point])
        # end of the function

    # execute the previous function
    for i in range(iterations + 1):
        dist *= (1 - dist_decr / 10)

        split_proba += split_proba_rise / 100
        for pt in points:
            create_points(pt)

    # not used for now, it will be usefull to keep the tree inside a other object
    def inside(point, obj):
        point = obj.matrix_world.inverted() * point
        cpom = obj.closest_point_on_mesh(point)
        vec = point - cpom[0]
        ang = cpom[1].angle(vec)
        return (ang > 1.57079633, cpom[0])

    def check_inside(ob, obj):
        ob_m = ob.matrix_world
        ob_m_i = ob.matrix_world.inverted()
        obj_m = obj.matrix_world
        for spline in cu.splines:

            for point in spline.points:
                a = ob_m * point.co
                b = mathutils.Vector((a[0], a[1], a[2]))
                (test, coord) = inside(b, obj)
                if test:
                    point.co = ob_m_i * obj_m * coord


# The class who adds a tree
class Add_iterative_Tree(bpy.types.Operator):
    """Create an interative tree"""
    bl_idname = "mesh.add_iterative_tree"
    bl_label = "Add iterative tree"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
    # Geometry panel.........................................................
        box = layout.box()
        box.label("basic")
        box.prop(self, "SeedProp")
        box.prop(self, "iterations")

        box.prop(self, "bevel")
        col = box.column(True)
        col.prop(self, "radius")
        col.prop(self, "rad_dec")
        # trunk panel............................................................
        box = layout.box()
        box.label("trunk")
        split = box.split()
        col = split.column(True)
        col.prop(self, "trunk_min_length")
        col.prop(self, "trunk_variation")
        col.prop(self, "trunk_radius_dec")
        col.prop(self, "preserve_trunk")
        # branch panel...................................................
        box = layout.box()
        box.label("branches")
        box.prop(self, "branch_variation")
        col = box.column(True)
        col.prop(self, "split_proba")
        col.prop(self, "split_proba_rise")
        column = box.column(True)
        split = box.split()
        col = split.column(True)
        col.prop(self, "dist")
        col.prop(self, "dist_dec")
        col = split.column()
        col.prop(self, "split_angle")
        col.prop(self, "first_split_angle")
        # advanced...............................................................
        box = layout.box()
        box.label("advanced")
        box.prop(self, "force")
        box.prop(self, "emitter")
        box.prop(self, "force_factor")
        box.prop(self, "gravity_fact")
    # the properties
    first_split_angle = FloatProperty(
        name="first split angle",
        min=0.0,
        default=35,
        description="how wide is the angle in a split if this split comes from the trunk",
    )
    split_proba_rise = FloatProperty(
        name="Split probabibity rise amount",
        default=.1,
    )
    branch_variation = FloatProperty(
        name="Branches variations",
        default=.5,
    )
    force = BoolProperty(
        name="force",
        default=False
    )
    emitter = FloatVectorProperty(
        name="force emitter",
        default=(5.0, 5.0, 5.0),
    )
    force_factor = FloatProperty(
        name="force factor",
        default=-.1,
    )
    trunk_radius_dec = FloatProperty(
        name="trunk radius decrease",
        default=.3,
    )
    preserve_trunk = BoolProperty(
        name="preserve trunk",
        default=True,
    )
    trunk_variation = FloatProperty(
        name="trunk variation",
        default=.1,
    )

    bevel = BoolProperty(
        name="bevel",
        default=False,
    )
    radius = FloatProperty(
        name="Radius",
        min=0.0,
        default=1,
    )
    rad_dec = FloatProperty(
        name="radius decrease",
        min=0.0,
        max=1.0,
        default=0.55,
    )
    Is_curve = BoolProperty(
        name="is curve",
        default=False,
    )
    iterations = IntProperty(
        name="branch iterations",
        min=1,
        default=25,
        description="number of recursive call. WARNING : rise fast",
    )
    trunk_min_length = IntProperty(
        name="trunk min length",
        min=0,
        default=9,
        description="iteration from from which first split is alload",
    )
    Preserve_trunk = BoolProperty(
        name="preserve trunk",
        default=False,
    )
    split_proba = FloatProperty(
        name="split probability",
        min=0.0,
        max=1.0,
        default=0.25,
        description="probability for a branch to split. WARNING : sensitive",
    )
    dist = FloatProperty(
        name="points distance",
        min=0.0,
        default=.5,
        description="distance beetwen two consecutive points",
    )
    dist_dec = FloatProperty(
        name="distance decrease",
        default=0.2,
        description="how do the branches sizes decrease",
    )
    split_angle = FloatProperty(
        name="split angle",
        min=0.0,
        default=35,
        description="how wide is the angle in a split",
    )

    gravity_fact = FloatProperty(
        name="gravity factor",
        default=0.0,
    )
    SeedProp = IntProperty(
        name="Seed",
        default=1,
    )

    def execute(self, context):
        seed(self.SeedProp)

        create_tree(self.iterations, self.radius, self.rad_dec, self.trunk_radius_dec, self.split_proba, self.dist, self.split_angle, self.first_split_angle, self.bevel, self.trunk_min_length, self.trunk_variation, self.gravity_fact, self.preserve_trunk, self.dist_dec, self.branch_variation, self.split_proba_rise, self.force, self.force_factor, self.emitter)
        return {'FINISHED'}

# the class who creates the buttons and call other classes


#class TreeMaker(bpy.types.Panel):
    #bl_space_type = "VIEW_3D"
    #bl_region_type = "TOOLS"
    #bl_context = "objectmode"
    #bl_category = "Create"
    #bl_label = "Add Tree"
    #bl_options = {'DEFAULT_CLOSED'}

    #def draw(self, context):
        #TheCol = self.layout.column()
        #TheCol.operator("mesh.add_iterative_tree", text="Add Tree")
        #TheCol.operator("mesh.addleaves", text="Add leaves")
        #TheCol.operator("mesh.adddetail", text="Add detail")


# the class who adds details to the created tree
class AddDetail(bpy.types.Operator):
    bl_idname = "mesh.adddetail"
    bl_label = "Add detail"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        box = layout.box()
        box.label("add detail")
        box.prop(self, "length")
        box.prop(self, "iteration")
        box.prop(self, "fractal")

    length = FloatProperty(
        name="length",
        default=.4,
    )
    iteration = IntProperty(
        name="subdivisions",
        default=2,
        description="add detail to large faces",
    )
    fractal = FloatProperty(
        name="fractal factor",
        default=.4,
    )

    def execute(self, context):
        ob = context.active_object
        if ob and ob.select and ob.type == 'CURVE':
            em = (ob.mode == 'EDIT')
            bpy.ops.object.mode_set()
            bpy.ops.object.convert(target='MESH', keep_original=False)
            if em:
                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        add_detail(ob, self.length, self.iteration, self.fractal)
        return{'FINISHED'}


# I'm sure you can guess for this one
class AddLeaves(bpy.types.Operator):
    """need smaller edges than the length / eg: unregular subdivided bezier curve"""
    bl_idname = "mesh.addleaves"
    bl_label = "Add leaves"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        box = layout.box()
        box.label("basic")
        box.prop(self, "visualize")
        box.prop(self, "length")
        box.prop(self, "create_new_leaf")
        col = box.column(True)
        col.prop(self, "number")
        col.prop(self, "display")
    visualize = BoolProperty(
        name="visualize",
        default=False,
    )
    length = FloatProperty(
        name="length",
        default=.02,
    )
    create_new_leaf = BoolProperty(
        name="create new leaf",
        default=False,
    )
    number = IntProperty(
        name="number of leaves",
        default=100000,
    )
    display = IntProperty(
        name="display",
        default=2000,
    )

    def execute(self, context):
        ob = context.active_object
        if ob and ob.select and ob.type == 'CURVE':
            em = (ob.mode == 'EDIT')
            bpy.ops.object.mode_set()
            bpy.ops.object.convert(target='MESH', keep_original=False)
            if em:
                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        else:
            le = 'not a curve object'
        Create_system(ob, self.length, self.create_new_leaf, self.number, self.display)
        if self.visualize:
            bpy.ops.paint.weight_paint_toggle()

        return{'FINISHED'}


# function create_group: object*Float -> None
#						 creates a vertex group based on edge length
def create_group(ob, length):
    data = ob.data
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    g = ob.vertex_groups.new("leaf")

    # search for a edge smaller than the length
    for edges in data.edges:
        verts = [data.vertices[edges.vertices[i]] for i in range(0, len(edges.vertices))]
        curr_length = (verts[0].co - verts[1].co).length
        # if found, select similar
        if curr_length < length:
            edges.select = True
            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_mode(type="EDGE")
            bpy.ops.mesh.select_similar(type='LENGTH', compare='LESS', threshold=0.01)
            bpy.ops.object.mode_set(mode='OBJECT')
            indexes = [i.index for i in data.vertices if i.select]
            # add the selection to the vertex group
            g.add(indexes, 1.0, "ADD")
            return g


# function Create_system: Object*Float*Bool*Int*Int
#						  create a particle system with some presets
def Create_system(ob, length, create_new_leaf, number, display):

    # Choose it a new leaf object has to be created
    if not(create_new_leaf) and bpy.data.objects.get("leaf") is None:
        create_new_leaf = True

    if create_new_leaf:
        leaf_object = create_leaf()
    else:
        leaf_object = bpy.data.objects['leaf']

    # get the vertex group
    g = create_group(ob, length)
    # customize the particle system
    leaf = ob.modifiers.new("psys name", 'PARTICLE_SYSTEM')
    part = ob.particle_systems[0]
    part.vertex_group_density = g.name
    set = leaf.particle_system.settings
    set.name = "leaf"
    set.type = "HAIR"
    set.use_advanced_hair = True
    set.draw_percentage = 100 * display / number
    set.count = number
    set.distribution = "RAND"
    set.normal_factor = .250
    set.factor_random = .7
    set.use_rotations = True
    set.phase_factor = 1
    set.phase_factor_random = 1
    set.particle_size = .015
    set.size_random = .25
    set.brownian_factor = 1
    set.render_type = "OBJECT"
    set.dupli_object = leaf_object


# function create_leaf: None -> Object
#						create a leaf
def create_leaf():
    # setting up the vertices and faces
    verts = [((-2.8946144580841064, -0.04747571051120758, 0.06105047091841698)), ((-0.003778815269470215, -0.18329660594463348, 0.06461216509342194)), ((-2.8945164680480957, 0.04747571051120758, 0.05965699255466461)), ((-0.0037790536880493164, -0.019920431077480316, 0.06660028547048569)), ((-0.5320309400558472, -0.5793617367744446, 0.19172759354114532)), ((-0.5320843458175659, 0.45810192823410034, 0.20311059057712555)), ((-1.0539054870605469, 0.6693136096000671, 0.31496328115463257)), ((-1.0538315773010254, -0.7448607087135315, 0.3081340789794922)), ((-1.4385014772415161, 0.7803475260734558, 0.336755633354187)), ((-1.4386969804763794, -0.7956905961036682, 0.3466308116912842)), ((-1.8466333150863647, 0.7721884250640869, 0.31564652919769287)), ((-1.9127564430236816, -0.7329368591308594, 0.33204150199890137)), ((-2.356304883956909, 0.548954963684082, 0.2288721650838852)), ((-2.3572182655334473, -0.4901292622089386, 0.24997609853744507)), ((-2.8945655822753906, 0.0, 0.04582677781581879)), ((-0.0037789344787597656, -0.1016085147857666, 0.051359549164772034)), ((-0.5320576429367065, -0.06062988191843033, 0.16666361689567566)), ((-1.0538685321807861, -0.03777353838086128, 0.32630106806755066)), ((-1.4385992288589478, -0.007671522442251444, 0.38123637437820435)), ((-1.846874713897705, -0.017651351168751717, 0.3504077196121216)), ((-2.3567614555358887, 0.02941284514963627, 0.20915958285331726))]

    faces = [(16, 15, 3, 5), (17, 16, 5, 6), (18, 17, 6, 8), (19, 18, 8, 10), (20, 19, 10, 12), (14, 20, 12, 2), (0, 13, 20, 14), (13, 11, 19, 20), (11, 9, 18, 19), (9, 7, 17, 18), (7, 4, 16, 17), (4, 1, 15, 16)]
    # setting up the object
    mesh = bpy.data.meshes.new("leaf")
    mesh.from_pydata(verts, [], faces)
    object = bpy.data.objects.new("leaf", mesh)
    object.location = (0, 0, 0)
    bpy.context.scene.objects.link(object)
    return object

# function add_detail: Object*Float*Int*Float -> None
#					   subdivide some parts of the object, to add detail


def add_detail(ob, length, iterations, fractal):

    obj = bpy.context.active_object
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    # select the first face, which should be the bigger one because it's on the base of the tree and wise people don't makes trees with a growing radius
    obj.data.polygons[0].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="FACE")
    # select similar faces
    bpy.ops.mesh.select_similar(type='PERIMETER', compare='EQUAL', threshold=length)
    # subdivide these faces
    bpy.ops.mesh.subdivide(number_cuts=iterations, smoothness=.645, fractal=fractal)
    bpy.ops.object.mode_set(mode='OBJECT')
    return None

# registration


def register():
    bpy.utils.register_class(Add_iterative_Tree)
    #py.utils.register_class(TreeMaker)
    bpy.utils.register_class(AddLeaves)
    bpy.utils.register_class(AddDetail)


def unregister():
    bpy.utils.unregister_class(Add_iterative_Tree)
    #bpy.utils.unregister_class(TreeMaker)
    bpy.utils.unregister_class(AddLeaves)
    bpy.utils.unregister_class(AddDetail)

if __name__ == "__main__":
    register()
