# ##### BEGIN GPL LICENSE BLOCK #####
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
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.props import (
        IntProperty,
        BoolProperty,
        )


class VIEW3D_OT_shrinkwrap_smooth(bpy.types.Operator):
        """Smooths the selected vertices while trying to keep the original shape with a shrinkwrap modifier. """
        bl_idname = "tpc_ot.shrinkwrap_smooth"
        bl_label = "Shrinkwrap Smooth"
        bl_options = {'REGISTER', 'UNDO'}

        pin : BoolProperty(name="Pin Selection Border", description="Pins the outer edge of the selection.", default = True)
        subsurf : IntProperty(name="Subsurf Levels", description="More reliable, but slower results", default = 0, min = 0, soft_max = 4)

        def execute(self, context):

                iterate = 6
                pin = self.pin
                data = bpy.context.object.data.name

                # Set up for vertex weight
                bpy.context.scene.tool_settings.vertex_group_weight = 1
                v_grps = len(bpy.context.object.vertex_groups.items())

                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                org_ob = bpy.context.object.name

                # Create intermediate object
                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                bpy.ops.mesh.primitive_plane_add(size=1, align='WORLD', enter_editmode=False)
                bpy.context.object.data = bpy.data.meshes[data]
                tmp_ob = bpy.context.object.name


                bpy.ops.object.duplicate(linked=False)
                shrink_ob = bpy.context.object.name

                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=tmp_ob)
                bpy.context.view_layer.objects.active = bpy.data.objects[tmp_ob]

                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')

                if v_grps >= 1:
                    for x in range(v_grps):
                        bpy.ops.object.vertex_group_add()


                if pin == True:
                        bpy.ops.object.vertex_group_assign_new()
                        org_id = bpy.context.object.vertex_groups.active_index

                        bpy.ops.object.vertex_group_assign_new()
                        sel = bpy.context.object.vertex_groups.active.name
                        sel_id = bpy.context.object.vertex_groups.active_index

                        bpy.ops.mesh.region_to_loop()
                        bpy.ops.object.vertex_group_remove_from(use_all_groups=False, use_all_verts=False)

                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.mesh.region_to_loop()
                        bpy.ops.object.vertex_group_remove_from(use_all_groups=False, use_all_verts=False)

                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.vertex_group_select(sel_id)


                else:
                        bpy.ops.object.vertex_group_assign_new()
                        sel = bpy.context.object.vertex_groups.active.name


                for x in range(iterate):
                        bpy.ops.object.modifier_add(type='SHRINKWRAP')
                        mod_id = (len(bpy.context.object.modifiers)-1)
                        shrink_name = bpy.context.object.modifiers[mod_id].name

                        bpy.context.object.modifiers[shrink_name].target = bpy.data.objects[shrink_ob]
                        bpy.context.object.modifiers[shrink_name].vertex_group = sel

                        bpy.context.object.modifiers[shrink_name].wrap_method = 'PROJECT'
                        bpy.context.object.modifiers[shrink_name].use_negative_direction = True
                        bpy.context.object.modifiers[shrink_name].subsurf_levels = self.subsurf


                        bpy.ops.mesh.vertices_smooth(factor=1, repeat=1)


                        bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                        bpy.ops.object.convert(target='MESH')
                        bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)


                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)



                bpy.ops.object.vertex_group_remove(all = False)
                bpy.ops.object.modifier_remove(modifier=shrink_name)

                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=shrink_ob)
                bpy.context.view_layer.objects.active = bpy.data.objects[shrink_ob]

                #Delete all geo inside Shrink_Object
                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.delete(type='VERT')
                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                bpy.ops.object.delete(use_global=True)

                bpy.ops.object.select_pattern(pattern=tmp_ob)
                bpy.context.view_layer.objects.active = bpy.data.objects[tmp_ob]


                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)

                if pin == True:
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.vertex_group_select(org_id)

                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                bpy.ops.object.delete(use_global=False)


                bpy.ops.object.select_pattern(pattern=org_ob)
                bpy.context.view_layer.objects.active = bpy.data.objects[org_ob]

                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)

                # Fix for Blender remembering the previous selection
                bpy.ops.object.vertex_group_assign_new()
                bpy.ops.object.vertex_group_remove(all = False)

                return {'FINISHED'}
            


# REGISTER #
classes = (
    VIEW3D_OT_shrinkwrap_smooth,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()            