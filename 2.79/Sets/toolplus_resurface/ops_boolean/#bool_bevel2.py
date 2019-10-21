bl_info = {
    "name": "Boolean Bevel",
    "author": "Rodinkov Ilya",
    "version": (0, 1, 2),
    "blender": (2, 75, 0),
    "location": "View3D > Tools > Boolean Bevel > Bevel",
    "description": "Create bevel after boolean",
    "warning": "This add-on is still in development.",
    "wiki_url": "",
    "category": "Object",
}

import bpy
import time
import addon_utils
import bmesh
from bpy.types import AddonPreferences


class BooleanBevelPreferences(AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        layout.label(text="Links:")
        layout.operator("wm.url_open",
                        text="Bevel After Boolean on BlenderArtist Forum ").url = "https://blenderartists.org/forum/showthread.php?434699-Add-on-WIP-Bevel-after-Boolean"
        layout.operator("wm.url_open",
                        text="Bevel After Boolean on 3DMir Forum ").url = "http://www.3dmir.ru/forum/read/5483/1.html"


class ObjectBooleanBevelRemovePipes(bpy.types.Operator):
    """Remove Pipes"""
    bl_idname = "object.boolean_bevel_remove_pipes"
    bl_label = "Remove Pipes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        for i in bpy.data.objects:
            if i.name.find("_BB_PIPE") != -1:
                i.select = True
        bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}


class ObjectBooleanBevelSymmetrize(bpy.types.Operator):
    """Symmetrize Object"""
    bl_idname = "object.boolean_bevel_symmetrize"
    bl_label = "Boolean Bevel Symmetrize"
    bl_options = {'REGISTER', 'UNDO'}

    direction = bpy.props.EnumProperty(name="Direction",
                                       items=(("NEGATIVE_X", "-x to +x", "-x to +x"),
                                              ("POSITIVE_X", "+x to -x", "+x to -x"),
                                              ("NEGATIVE_Y", "-y to +y", "-y to +y"),
                                              ("POSITIVE_Y", "+y to -y", "+y to -y"),
                                              ("NEGATIVE_Z", "-z to +z", "-z to +z"),
                                              ("POSITIVE_Z", "+z to -z", "+z to -z")),
                                       description="",
                                       default="NEGATIVE_X")

    threshold = bpy.props.FloatProperty(name="Threshold", default=0.0001, min=0, max=1000, step=0.01)

    def execute(self, context):
        src_obj = bpy.context.active_object
        # bpy.ops.object.vertex_group_remove(all=True)
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False, "mode": 'TRANSLATION'})
        normals_object = bpy.context.active_object
        normals_object.name = src_obj.name + "_Normals"

        if self.direction[-1] == "X":
            transform_value = (-1.0, 1.0, 1.0)
            axys = 0
        elif self.direction[-1] == "Y":
            axys = 1
            transform_value = (1.0, -1.0, 1.0)
        elif self.direction[-1] == "Z":
            axys = 2
            transform_value = (1.0, 1.0, -1.0)

        print(axys)
        bpy.context.scene.objects.active = src_obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.symmetrize(direction=self.direction, threshold=self.threshold)
        bpy.ops.mesh.select_all(action='DESELECT')
        bm = bmesh.from_edit_mesh(src_obj.data)

        if self.direction.find("NEGATIVE") != -1:
            for vert in bm.verts:
                if vert.co[axys] >= -0.0 or vert.co[axys] >= 0.0:
                    vert.select = True
                    # print(vert.co[0])
        else:
            for vert in bm.verts:
                if vert.co[axys] <= 0.0 or vert.co[axys] <= -0.0:
                    vert.select = True
                    # print(vert.co[0])
        bpy.ops.mesh.select_more(use_face_step=True)
        bpy.ops.mesh.select_less(use_face_step=True)
        # bpy.ops.mesh.split()
        src_obj.vertex_groups.new(name="symmetrize")
        bpy.ops.object.vertex_group_assign()
        symmetrize_group = src_obj.vertex_groups.active.name
        bpy.ops.object.mode_set(mode='OBJECT')

        data_transfer_modifier = src_obj.modifiers.new(name="Boolean Bevel Custom Normals", type="DATA_TRANSFER")
        data_transfer_modifier.object = normals_object
        data_transfer_modifier.use_vert_data = True
        data_transfer_modifier.vert_mapping = "NEAREST"
        data_transfer_modifier.use_loop_data = True
        data_transfer_modifier.loop_mapping = "POLYINTERP_NEAREST"
        # data_transfer_modifier.vertex_group = symmetrize_group
        data_transfer_modifier.data_types_verts = {'VGROUP_WEIGHTS'}
        data_transfer_modifier.data_types_loops = {"CUSTOM_NORMAL"}
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=data_transfer_modifier.name)

        bpy.context.scene.objects.active = normals_object
        bpy.ops.transform.resize(value=transform_value)

        bpy.context.scene.objects.active = src_obj
        data_transfer_modifier = src_obj.modifiers.new(name="Boolean Bevel Custom Normals", type="DATA_TRANSFER")
        data_transfer_modifier.object = normals_object
        data_transfer_modifier.use_vert_data = True
        data_transfer_modifier.vert_mapping = "NEAREST"
        data_transfer_modifier.use_loop_data = True
        data_transfer_modifier.loop_mapping = "POLYINTERP_NEAREST"
        data_transfer_modifier.vertex_group = symmetrize_group
        data_transfer_modifier.data_types_verts = {'VGROUP_WEIGHTS'}
        data_transfer_modifier.data_types_loops = {"CUSTOM_NORMAL"}
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=data_transfer_modifier.name)

        normals_object.select = True
        bpy.ops.object.delete(use_global=False)
        src_obj.select = True
        bpy.context.scene.objects.active = src_obj
        bpy.ops.object.vertex_group_remove(all=True)
        return {'FINISHED'}


class ObjectBooleanBevelApplyModifiers(bpy.types.Operator):
    """Apply all modifiers on selected Objects"""
    bl_idname = "object.boolean_bevel_apply_modifiers"
    bl_label = "Boolean Bevel Apply Modifiers"
    bl_options = {'REGISTER', 'UNDO'}

    all = bpy.props.BoolProperty(name="Apply All Modifiers", default=True)

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            for modifier in obj.modifiers:
                modifier.show_viewport = False

            context.scene.objects.active = obj
            for modifier in obj.modifiers:
                if self.all:
                    try:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)
                    except:
                        bpy.ops.object.modifier_remove(modifier=modifier.name)
                elif modifier.name.find("Boolean Bevel") != -1:
                    try:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)
                    except:
                        bpy.ops.object.modifier_remove(modifier=modifier.name)

            for modifier in obj.modifiers:
                modifier.show_viewport = True
        return {'FINISHED'}


class ObjectBooleanBevelRemoveObjects(bpy.types.Operator):
    """Remove all created Guides and Curves"""
    bl_idname = "object.boolean_bevel_remove_objects"
    bl_label = "Boolean Bevel Remove Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        for i in ['BOOLEAN_BEVEL_CURVE', 'BOOLEAN_BEVEL_GUIDE', 'BOOLEAN_BEVEL_CURVE_PROFILE',
                  'BOOLEAN_BEVEL_GUIDE_CUSTOM']:
            index = bpy.data.objects.find(i)
            if index != -1:
                bpy.data.objects[i].select = True
                bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}


class ObjectBooleanBevelRemoveModifiers(bpy.types.Operator):
    """Remove all modifiers on selected Objects"""
    bl_idname = "object.boolean_bevel_remove_modifiers"
    bl_label = "Boolean Bevel Remove Modifiers"
    bl_options = {'REGISTER', 'UNDO'}

    all = bpy.props.BoolProperty(name="Remove  All Modifiers", default=True)

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            for modifier in obj.modifiers:
                modifier.show_viewport = False

            context.scene.objects.active = obj

            for modifier in obj.modifiers:
                if self.all:
                    bpy.ops.object.modifier_remove(modifier=modifier.name)
                elif modifier.name.find("Boolean Bevel") != -1:
                    bpy.ops.object.modifier_remove(modifier=modifier.name)

            for modifier in obj.modifiers:
                modifier.show_viewport = True
        return {'FINISHED'}


class BooleanBevelPanel(bpy.types.Panel):
    bl_label = "Boolean Bevel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        split = layout.split()
        col = split.column(align=True)
        if bpy.context.object:
            if 0 < len(bpy.context.selected_objects) < 2 and bpy.context.object.mode == "OBJECT":
                col.operator("object.boolean_bevel", text="Bevel", icon='MOD_BEVEL')
                col.operator("object.boolean_bevel_symmetrize", text="Symmetrize", icon='MOD_MIRROR')
                # col.operator("object.boolean_bevel_make_pipe", text="Make Pipe", icon="MOD_CURVE")

                #     if bpy.data.objects.find('BOOLEAN_BEVEL_CURVE') != -1 and bpy.data.objects.find(
                #             'BOOLEAN_BEVEL_GUIDE') != -1:
                #         col.operator("object.boolean_custom_bevel", text="Custom Bevel", icon='MOD_BEVEL')
                # if bpy.context.object.mode == "EDIT":
                #     col.operator("object.boolean_bevel_custom_edge", text="Custom Edge", icon='EDGESEL')
                # col.operator("object.boolean_bevel_bridge", text="Bridge Edge", icon='EDGESEL')
        col.separator()
        col.operator("object.boolean_bevel_remove_objects", text="Remove Objects", icon='X')
        if len(bpy.context.selected_objects) > 0 and bpy.context.object.mode == "OBJECT":
            col.operator("object.boolean_bevel_apply_modifiers", text="Apply Modifiers", icon='IMPORT')
            col.operator("object.boolean_bevel_remove_modifiers", text="Remove Modifiers", icon='X')
        col.operator("object.boolean_bevel_remove_pipes", text="Remove Pipes", icon='X')


class ObjectBooleanBevel(bpy.types.Operator):
    """Create the bevel on Object"""
    bl_idname = "object.boolean_bevel"
    bl_label = "Boolean Bevel"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label("Show/Hide:")
        row = box.row(align=True)
        row.alignment = 'CENTER'
        row.prop(self, "wire")
        row.prop(self, "preview_curve")
        row = box.row(align=True)
        row.alignment = 'CENTER'
        row.prop(self, "all_settings")

        box = layout.box()
        box.label("Basic Parameters:")
        box.prop(self, "stop_calc")
        box.prop(self, "change_operation")
        box.prop(self, "change_subdivide")
        if self.change_subdivide:
            box.prop(self, "subdiv_a")
            box.prop(self, "subdiv_b")
        box.prop(self, "value_radius")
        box.prop(self, "fillet_profile")
        box.prop(self, "fillet_segments")
        box.separator()
        box.prop(self, "smooth_bevel")
        if self.smooth_bevel:
            box.prop(self, "smooth_bevel_value")
            box.prop(self, "smooth_bevel_step")
        box = layout.box()
        box.label("Curve Parameters:")
        box.prop(self, "relax")
        box.prop(self, "repeat")
        if self.all_settings:
            box.prop(self, "simplify")
            box.prop(self, "subdivide")
            row = box.row(align=True)
            row.alignment = 'EXPAND'
            box.prop(self, "sides")

        if self.all_settings:
            box = layout.box()
            box.label("Other Parameters:")
            box.prop(self, "fix_curve")
            box.prop(self, "curve_tilt")
            box.prop(self, "twist_mode")
            box.prop(self, "smooth")
            box.separator()
        box.prop(self, "triangulate")
        if self.triangulate:
            box.prop(self, "method")

    # сетка
    wire = bpy.props.BoolProperty(name="Wire", default=True)

    # Операции boolean
    change_operation = bpy.props.EnumProperty(name="Operation",
                                              items=(("False", "Not change", "Not change"),
                                                     ("UNION", "Union", "Use Union"),
                                                     ("DIFFERENCE", "Difference", "Use Difference"),
                                                     ("INTERSECT", "Intersect", "Use Intersect"),
                                                     ("SLICE", "Slice", "Use Slice")),
                                              description="Change Boolean Operation",
                                              default="False")

    # изменение подразделения
    change_subdivide = bpy.props.BoolProperty(name="Change subdivide", default=False)
    subdiv_a = bpy.props.IntProperty(name="Subdivision Object", default=1, min=0, max=6)
    subdiv_b = bpy.props.IntProperty(name="Subdivision Boolean", default=1, min=0, max=6)

    # место пересечения
    simplify = bpy.props.FloatProperty(name="Simplify", default=0.0, min=0.0, max=1.0, unit="ROTATION", step=100)
    subdivide = bpy.props.IntProperty(name="Subdivide Patch", default=0, min=0, max=500)
    relax = bpy.props.EnumProperty(name="Relax factor",
                                   items=(("0", "Not Use", "Not Use"),
                                          ("1", "1", "One"),
                                          ("3", "3", "Three"),
                                          ("5", "5", "Five"),
                                          ("10", "10", "Ten"),
                                          ("25", "25", "Twenty-five")),
                                   description="Number of times the loop is relaxed",
                                   default="5")
    repeat = bpy.props.IntProperty(name="Repeat relax", default=1, min=1, max=1000)

    # кривая
    value_radius = bpy.props.FloatProperty(name="Cut Radius", default=0.05, min=0.0001, max=30.0, step=1)
    sides = bpy.props.IntProperty(name="Sides of circle", default=8, min=3, max=10)
    fix_curve = bpy.props.BoolProperty(name="Fix Curve Twist", default=True)
    curve_tilt = bpy.props.FloatProperty(name="Mean Tilt", default=45.0, min=-45.0, max=45.0)
    twist_mode = bpy.props.EnumProperty(name="Twist Mode",
                                        items=(("MINIMUM", "Minimum", "Use the least twist over the entire curve"),
                                               ("TANGENT", "Tangent", "Use the tangent to calculate twist")),
                                        description="The type of tilt calculation for 3D Curves",
                                        default="MINIMUM")
    smooth = bpy.props.IntProperty(name="Smooth", default=60, min=0, max=500)
    preview_curve = bpy.props.BoolProperty(name="Curve", default=False)

    # bevel
    fillet_profile = bpy.props.FloatProperty(name="Fillet Profile", default=0.7, min=-0.15, max=1.0)
    fillet_segments = bpy.props.IntProperty(name="Fillet Segments", default=10, min=1, max=200)

    triangulate = bpy.props.BoolProperty(name="Split NGon", default=False)
    method = bpy.props.EnumProperty(name="Method",
                                    items=(("BEAUTY", "BEAUTY", "Use BEAUTY"),
                                           ("CLIP", "CLIP", "Use CLIP")),
                                    description="Method for splitting the polygons into triangles",
                                    default="BEAUTY")
    smooth_bevel = bpy.props.BoolProperty(name="Smooth Bevel", default=True)
    smooth_bevel_value = bpy.props.IntProperty(name="Smooth Value", default=5, min=0, max=30)
    smooth_bevel_step = bpy.props.IntProperty(name="Smooth Step", default=3, min=0, max=1000)

    stop_calc = bpy.props.BoolProperty(name="Stop calculations", default=False)
    preview_curve = bpy.props.BoolProperty(name="Curve", default=False)
    all_settings = bpy.props.BoolProperty(name="All settings", default=False)

    def execute(self, context):
        time_start = time.time()
        loop_tools_addon = "mesh_looptools"
        state = addon_utils.check(loop_tools_addon)
        if not state[0]:
            bpy.ops.wm.addon_enable(module=loop_tools_addon)

        if self.stop_calc:
            return {'FINISHED'}
        context.tool_settings.vertex_group_weight = 1.0
        custom = False
        scene = context.scene
        src_obj = scene.objects.active
        clear_objects(scene, src_obj)
        if src_obj.modifiers:
            if src_obj.modifiers[len(src_obj.modifiers) - 1].type != "BOOLEAN":
                self.report({'ERROR'}, "Object does not have a Boolean modifier")
                return {'CANCELLED'}
        boolean_solver = src_obj.modifiers[len(src_obj.modifiers) - 1].solver
        boolean_oper = src_obj.modifiers[len(src_obj.modifiers) - 1].operation
        src_obj.show_wire = self.wire
        src_obj.show_all_edges = self.wire
        name = prepare_object(scene, src_obj, self.change_subdivide, self.subdiv_a, self.subdiv_b,
                              self.change_operation)
        get_guide(scene, self.simplify, self.subdivide, self.relax, custom, self.repeat, src_obj, name)
        create_curve(self.value_radius, self.sides, self.fix_curve, self.curve_tilt, self.twist_mode, scene,
                     self.smooth)
        if self.preview_curve:
            return {'FINISHED'}
        do_boolean(scene, src_obj)
        create_bevel(scene, src_obj, self.fillet_profile, self.fillet_segments, self.triangulate, self.smooth_bevel,
                     self.method, self.smooth_bevel_value, self.smooth_bevel_step)
        if self.change_operation == "DIFFERENCE" or self.change_operation == "SLICE" or (
                        self.change_operation == "False" and boolean_oper == "DIFFERENCE"):
            # Возвращаем нормали boolean
            scene.objects.active = bpy.data.objects[name]
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.flip_normals()
            bpy.ops.object.mode_set(mode='OBJECT')

        if self.change_operation == "SLICE":
            bpy.ops.object.select_all(action='DESELECT')
            scene.objects.active = bpy.data.objects[name]
            bpy.data.objects[name].select = True
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False, "mode": 'TRANSLATION'})
            slice_obj = scene.objects.active
            slice_obj.name = src_obj.name + "_SLICE"
            boolean_modifier = slice_obj.modifiers.new(name="Boolean Bevel Boolean", type='BOOLEAN')
            for modifier in slice_obj.modifiers:
                modifier.show_viewport = False
            boolean_modifier.operation = "INTERSECT"
            boolean_modifier.solver = boolean_solver
            boolean_modifier.object = bpy.data.objects[src_obj.name + "_Normals"]
            for modifier in slice_obj.modifiers:
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_mode(type='FACE')
            bpy.ops.mesh.select_all(action='DESELECT')
            # создаем необходимые группы вершин
            bpy.ops.mesh.reveal()
            slice_obj.vertex_groups.new(name=src_obj.name + "_Normals")
            bpy.ops.object.vertex_group_assign()
            bpy.ops.mesh.select_all(action='INVERT')
            slice_obj.vertex_groups.new(name=name)
            bpy.ops.object.vertex_group_assign()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.hide(unselected=False)
            bpy.ops.object.mode_set(mode='OBJECT')
            do_boolean(scene, slice_obj)
            create_bevel(scene, slice_obj, self.fillet_profile, self.fillet_segments, self.triangulate,
                         self.smooth_bevel,
                         self.method, self.smooth_bevel_value, self.smooth_bevel_step)
            slice_obj.draw_type = "TEXTURED"
            slice_obj.hide_render = False
            slice_obj.show_wire = self.wire
            slice_obj.show_all_edges = self.wire

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[src_obj.name + "_Normals"].select = True
        bpy.ops.object.delete(use_global=False)
        # src_obj.select = True
        # scene.objects.active = src_obj
        clear_objects(scene, src_obj)
        print("Общее время: %.4f sec\n" % (time.time() - time_start))
        return {'FINISHED'}


def prepare_object(scene, src_obj, change_subdivide, subdiv_a, subdiv_b, change_operation):
    time_start = time.time()
    # Скрываем все модификаторы для ускорения процесса
    for modifier in src_obj.modifiers:
        modifier.show_viewport = False
    if len(src_obj.vertex_groups) != 0:
        src_obj.vertex_groups.clear()
    # выноси модификатор boolean в переменную
    boolean = src_obj.modifiers[len(src_obj.modifiers) - 1]
    boolean_obj = boolean.object

    if change_subdivide:
        # меняем подразделение у объекта

        for modifier in reversed(src_obj.modifiers):
            if modifier.type == "SUBSURF":
                modifier.levels = subdiv_a

                # если уровень подразделения 0, то удаляем его
                if subdiv_a == 0:
                    bpy.ops.object.modifier_remove(modifier=modifier.name)
                break
        # меняем подразделение у boolean
        for modifier in reversed(boolean_obj.modifiers):
            if modifier.type == "SUBSURF":
                modifier.levels = subdiv_b
                # если уровень подразделения 0, то удаляем его
                if subdiv_a == 0:
                    bpy.ops.object.modifier_remove(modifier=modifier.name)
                break

    # Меняем операцию Boolean
    if change_operation != "False":
        if change_operation == "SLICE":
            boolean.operation = "DIFFERENCE"
        else:
            boolean.operation = change_operation
    print("Операция:" + change_operation)

    # скрываем полигоны у объекта
    vert = src_obj.data
    for i in vert.polygons:
        i.hide = True

    # показываем полигоны у boolean
    vert = boolean_obj.data
    for i in vert.polygons:
        i.hide = False

    boolean_obj.draw_type = 'BOUNDS'

    # применяем все модификаторы
    for modifier in src_obj.modifiers:
        if modifier.type == "BOOLEAN":
            # делаем копию, для нормалей
            bpy.ops.object.select_all(action='DESELECT')
            src_obj.select = True
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False, "mode": 'TRANSLATION'})
            normals_object = scene.objects.active
            normals_object.name = src_obj.name + "_Normals"
            src_obj.select = False
            boolean_obj.select = True
            normals_object.select = True
            bpy.ops.object.shade_smooth()
            normals_object.hide_render = True
            normals_object.draw_type = 'BOUNDS'
            # удаляем модификатор boolean
            bpy.ops.object.modifier_remove(modifier=boolean.name)

            if boolean.operation == "DIFFERENCE":
                scene.objects.active = src_obj
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)
                scene.objects.active = boolean_obj
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.flip_normals()
                bpy.ops.object.mode_set(mode='OBJECT')
            else:
                scene.objects.active = src_obj
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)

        else:
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)

    scene.objects.active = src_obj
    bpy.ops.object.select_all(action='DESELECT')
    print("Время Prepare Object: %.4f sec\n" % (time.time() - time_start))
    return boolean_obj.name


def get_guide(scene, simplify, subdivide, relax, custom, repeat, src_obj, name):
    time_start = time.time()
    # заходим в режим редактирования
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.looptools_relax(iterations="1", interpolation="cubic")
    # создаем необходимые группы вершин
    bpy.ops.mesh.reveal()
    src_obj.vertex_groups.new(name=src_obj.name + "_Normals")
    bpy.ops.object.vertex_group_assign()
    bpy.ops.mesh.select_all(action='INVERT')
    src_obj.vertex_groups.new(name=name)
    bpy.ops.object.vertex_group_assign()

    # выделяем пересечение
    bpy.ops.mesh.region_to_loop()
    bpy.ops.mesh.duplicate_move()

    # обрабатываем пересечение
    if simplify > 0:
        bpy.ops.mesh.dissolve_limited(angle_limit=simplify)
    if subdivide > 0:
        bpy.ops.mesh.subdivide(number_cuts=subdivide)
    for i in range(repeat):
        if relax != '0':
            bpy.ops.mesh.looptools_relax(iterations=relax, interpolation="cubic")

    # создаем новый объект из пересечения
    bpy.ops.mesh.separate(type='SELECTED')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.hide(unselected=False)
    bpy.ops.object.mode_set(mode='OBJECT')
    guide = bpy.context.selected_objects[0]
    guide.name = "BOOLEAN_BEVEL_GUIDE"
    scene.objects.active = guide
    print("Время Get Guide: %.4f sec\n" % (time.time() - time_start))


def create_curve(value_radius, sides, fix_curve, curve_tilt, twist_mode, scene, smooth):
    time_start = time.time()
    bpy.ops.object.convert(target='CURVE', keep_original=True)
    curve_cut = bpy.context.object
    curve_cut.name = "BOOLEAN_BEVEL_CURVE"
    curve_cut.data.fill_mode = 'FULL'
    curve_cut.data.bevel_depth = value_radius
    curve_cut.data.bevel_resolution = sides
    if fix_curve:
        curve_cut.data.resolution_u = 1
        curve_cut.data.twist_mode = twist_mode
        curve_cut.data.twist_smooth = smooth
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.spline_type_set(type='BEZIER')
        bpy.ops.curve.handle_type_set(type='FREE_ALIGN')
        bpy.ops.curve.normals_make_consistent()
        bpy.ops.transform.tilt(value=curve_tilt)
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.transform.tilt(value=curve_tilt)
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.mesh.primitive_circle_add(vertices=sides, radius=value_radius, enter_editmode=False)
    bpy.ops.object.convert(target='CURVE', keep_original=False)
    circle = scene.objects.active
    circle.name = "BOOLEAN_BEVEL_CURVE_PROFILE"
    scene.objects.active = curve_cut
    curve_cut.data.bevel_object = circle
    print("Время Create Curve: %.4f sec\n" % (time.time() - time_start))


def do_boolean(scene, src_obj):
    time_start = time.time()
    curve_cut = bpy.data.objects['BOOLEAN_BEVEL_CURVE']
    scene.objects.active = curve_cut
    curve_cut.select = True
    if curve_cut.type != "MESH":
        bpy.ops.object.convert(target='MESH', keep_original=False)
    curve_cut.draw_type = 'BOUNDS'
    boolean_modifier = src_obj.modifiers.new(name="BooleanBevel", type='BOOLEAN')
    boolean_modifier.show_viewport = False
    boolean_modifier.object = curve_cut
    boolean_modifier.operation = "UNION"
    bpy.ops.object.select_all(action='DESELECT')
    scene.objects.active = src_obj
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=boolean_modifier.name)
    print("Время Do Boolean: %.4f sec\n" % (time.time() - time_start))


def create_bevel(scene, src_obj, fillet_profile, fillet_segments, triangulate, smooth_bevel, method, smooth_bevel_value,
                 smooth_bevel_step):
    time_start = time.time()
    # создаем группу вершин для bevel
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.region_to_loop()
    bpy.ops.mesh.select_all(action='INVERT')
    src_obj.vertex_groups.new(name="Bevel")
    bpy.ops.object.vertex_group_assign()
    bevel_group = src_obj.vertex_groups.active.name
    bpy.ops.object.mode_set(mode='OBJECT')
    # прпитягиваем вершины к нужному месту.
    guide = bpy.data.objects['BOOLEAN_BEVEL_GUIDE']
    shrinkwrap_modifier = src_obj.modifiers.new(name="shrinkwrap", type='SHRINKWRAP')
    shrinkwrap_modifier.show_viewport = False
    shrinkwrap_modifier.wrap_method = 'NEAREST_VERTEX'
    shrinkwrap_modifier.vertex_group = bevel_group
    shrinkwrap_modifier.target = guide
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=shrinkwrap_modifier.name)
    # удаляем дубли вершин
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.vertex_group_select()
    bpy.ops.mesh.remove_doubles()
    # удаление мешающих ребер
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.vertex_group_select()
    bpy.ops.mesh.select_more(use_face_step=False)
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.mesh.edge_collapse()
    bpy.ops.mesh.dissolve_verts(use_face_split=True, use_boundary_tear=False)
    #
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.object.vertex_group_select()
    bpy.ops.mesh.select_more(use_face_step=True)
    bpy.ops.mesh.hide(unselected=True)
    bpy.ops.mesh.select_face_by_sides(number=3, type='EQUAL', extend=False)
    bpy.ops.object.vertex_group_deselect()
    bpy.ops.mesh.edge_collapse()
    bpy.ops.mesh.reveal()

    # триангуляция
    if triangulate:
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        bpy.ops.mesh.select_more(use_face_step=True)
        bpy.ops.mesh.select_more(use_face_step=True)
        bpy.ops.mesh.hide(unselected=True)
        bpy.ops.mesh.select_face_by_sides(number=4, type='GREATER', extend=False)
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method=method)
        bpy.ops.mesh.reveal()

    bpy.ops.mesh.select_all(action='DESELECT')
    if smooth_bevel:
        bpy.ops.object.vertex_group_select()
        src_obj.vertex_groups.new(name="Smooth")
        bpy.ops.object.vertex_group_assign()
        for i in range(smooth_bevel_step):
            bpy.context.tool_settings.vertex_group_weight = bpy.context.tool_settings.vertex_group_weight - 1 / smooth_bevel_step
            bpy.ops.mesh.select_more(use_face_step=True)
            bpy.ops.object.vertex_group_deselect()
            bpy.ops.object.vertex_group_assign()
        smooth_group = src_obj.vertex_groups.active.name

    bpy.context.tool_settings.vertex_group_weight = 1.0
    bpy.ops.mesh.reveal()
    bpy.ops.mesh.select_all(action='SELECT')
    # bpy.ops.mesh.normals_make_consistent(inside=False)
    # bpy.ops.object.mode_set(mode='OBJECT')
    # сглаживание
    if smooth_bevel:
        smooth_modifier = src_obj.modifiers.new(name="Boolean Bevel Smooth", type='SMOOTH')
        smooth_modifier.show_viewport = False
        smooth_modifier.iterations = smooth_bevel_value
        smooth_modifier.vertex_group = smooth_group

    # все модификаторы видны
    # for modifier in src_obj.modifiers:
    #     modifier.show_viewport = True
    # исправаление групп вершин
    bpy.ops.mesh.select_mode(type='VERT')
    #
    bpy.ops.mesh.select_all(action='DESELECT')
    src_obj.vertex_groups.active_index = 0
    bpy.ops.object.vertex_group_select()
    bpy.ops.mesh.select_more(use_face_step=True)
    bpy.ops.object.vertex_group_assign()
    #
    bpy.ops.mesh.select_all(action='DESELECT')
    src_obj.vertex_groups.active_index = len(src_obj.vertex_groups) - 2 - smooth_bevel
    bpy.ops.object.vertex_group_select()
    bpy.ops.mesh.select_more(use_face_step=True)
    bpy.ops.object.vertex_group_assign()
    bpy.ops.mesh.select_all(action='DESELECT')
    # bevel
    src_obj.vertex_groups.active_index = 2
    bpy.ops.object.vertex_group_select()
    bevel_width = 100 - (200 / (fillet_segments + 3))
    bpy.ops.mesh.bevel(vertex_only=False, offset_type='PERCENT', profile=fillet_profile, segments=fillet_segments,
                       clamp_overlap=False, offset=bevel_width)
    bpy.ops.object.mode_set(mode='OBJECT')

    # переносим нормали
    data_transfer_modifier = src_obj.modifiers.new(name="Boolean Bevel Custom Normals", type="DATA_TRANSFER")
    data_transfer_modifier.show_viewport = False
    data_transfer_modifier.object = bpy.data.objects[src_obj.vertex_groups[0].name]
    data_transfer_modifier.use_loop_data = True
    data_transfer_modifier.data_types_loops = {"CUSTOM_NORMAL"}
    data_transfer_modifier.loop_mapping = "POLYINTERP_NEAREST"
    data_transfer_modifier.vertex_group = src_obj.vertex_groups[0].name

    data_transfer_modifier = src_obj.modifiers.new(name="Boolean Bevel Custom Normals", type="DATA_TRANSFER")
    data_transfer_modifier.show_viewport = False
    data_transfer_modifier.object = bpy.data.objects[src_obj.vertex_groups[1].name]
    data_transfer_modifier.use_loop_data = True
    data_transfer_modifier.data_types_loops = {"CUSTOM_NORMAL"}
    data_transfer_modifier.loop_mapping = "POLYINTERP_NEAREST"
    data_transfer_modifier.vertex_group = src_obj.vertex_groups[1].name

    # включаем автосглаживание
    bpy.context.object.data.use_auto_smooth = True
    bpy.context.object.data.auto_smooth_angle = 3.14159

    src_obj.select = True
    bpy.ops.object.shade_smooth()
    # применяем все модификаторы
    for modifier in src_obj.modifiers:
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)
    src_obj.vertex_groups.clear()
    print("Время Create Bevel: %.4f sec\n" % (time.time() - time_start))


def clear_objects(scene, src_obj):
    bpy.ops.object.select_all(action='DESELECT')
    for i in ['BOOLEAN_BEVEL_CURVE', 'BOOLEAN_BEVEL_GUIDE', 'BOOLEAN_BEVEL_CURVE_PROFILE']:
        index = bpy.data.objects.find(i)
        if index != -1:
            bpy.data.objects[i].select = True
            bpy.ops.object.delete(use_global=False)
    src_obj.select = True
    scene.objects.active = src_obj


def register():
    bpy.utils.register_class(ObjectBooleanBevel)
    bpy.utils.register_class(BooleanBevelPanel)
    bpy.utils.register_class(ObjectBooleanBevelApplyModifiers)
    bpy.utils.register_class(ObjectBooleanBevelRemoveModifiers)
    bpy.utils.register_class(ObjectBooleanBevelRemoveObjects)
    bpy.utils.register_class(ObjectBooleanBevelSymmetrize)
    bpy.utils.register_class(ObjectBooleanBevelRemovePipes)
    bpy.utils.register_class(BooleanBevelPreferences)


def unregister():
    bpy.utils.unregister_class(ObjectBooleanBevel)
    bpy.utils.unregister_class(BooleanBevelPanel)
    bpy.utils.unregister_class(ObjectBooleanBevelApplyModifiers)
    bpy.utils.unregister_class(ObjectBooleanBevelRemoveModifiers)
    bpy.utils.unregister_class(ObjectBooleanBevelRemoveObjects)
    bpy.utils.unregister_class(ObjectBooleanBevelSymmetrize)
    bpy.utils.unregister_class(ObjectBooleanBevelRemovePipes)
    bpy.utils.unregister_class(BooleanBevelPreferences)

if __name__ == "__main__":
    register()
