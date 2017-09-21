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
#
# ***** END GPL LICENCE BLOCK *****

"""
bl_info = {
	"name": "Booltron",
	"author": "Mikhail Rachinskiy (jewelcourses.com)",
	"version": (2000,),
	"blender": (2,7,4),
	"location": "3D View → Tool Shelf (Shift Ctrl B)",
	"description": "Booltron—super add-on for super fast booleans.",
	"wiki_url": "https://github.com/mrachinskiy/blender-addon-booltron",
	"tracker_url": "https://github.com/mrachinskiy/blender-addon-booltron/issues",
	"category": "Mesh"}
"""

import bpy
from bpy.types import (Panel, Menu)
from bpy.types import Operator

"""
class BooltronPanel(Panel):

	bl_label = "Booltron"
	bl_idname = "Booltron Panel"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "Booltron"

	@classmethod
	def poll(cls, context):
		return (context.active_object and context.mode == 'OBJECT')

	def draw(self, context):
		layout = self.layout

		#if len(context.selected_objects) < 2:
			#layout.enabled = False

		col = layout.column(align=True)
		col.operator("booltron.union", text="Union")
		col.operator("booltron.difference", text="Difference")
		col.operator("booltron.intersect", text="Intersect")

		col.separator()
		col.operator("booltron.separate", text="Separate")


class BooltronPopup(Menu):

	bl_label = "Booltron"
	bl_idname = "Booltron Popup"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'

		if len(context.selected_objects) < 2:
			layout.enabled = False

		layout.operator("booltron.union", text="Union")
		layout.operator("booltron.difference", text="Difference")
		layout.operator("booltron.intersect", text="Intersect")

		layout.separator()
		layout.operator("booltron.separate", text="Separate")

"""
class BoolToolMenu(bpy.types.Menu):
    bl_label = "BoolTool"
    bl_idname = "tp_ops.booltool"
    
    def draw(self, context):
        layout = self.layout

        layout.operator("btool.boolean_union", text = "Union Brush",icon = "ROTATECOLLECTION")
        layout.operator("btool.boolean_inters", text ="Intersection Brush",icon = "ROTATECENTER")
        layout.operator("btool.boolean_diff", text ="Difference Brush",icon = "ROTACTIVE")
        
        layout.separator()

        layout.operator("btool.boolean_union_direct", text = "Union Brush",icon = "ROTATECOLLECTION")
        layout.operator("btool.boolean_inters_direct", text ="Intersection Brush",icon = "ROTATECENTER")
        layout.operator("btool.boolean_diff_direct", text ="Difference Brush",icon = "ROTACTIVE")
        
        layout.separator()  
              
        layout.operator("btool.draw_polybrush",icon = "LINE_DATA")
               
bpy.utils.register_class(BoolToolMenu)

### Helpers ###

def object_prepare():
	ops_ob = bpy.ops.object
	ops_ob.make_single_user(object=True, obdata=True)
	ops_ob.convert(target="MESH")


def mesh_selection(ob, select_action):
	context = bpy.context
	sce = context.scene
	obj = context.active_object
	ops = bpy.ops
	ops_me = bpy.ops.mesh
	ops_ob = ops.object


	def mesh_cleanup():
		ops_me.select_all(action="SELECT")
		ops_me.delete_loose()
		ops_me.select_all(action="SELECT")
		ops_me.remove_doubles(threshold=0.0001)
		ops_me.fill_holes(sides=0)
		ops_me.normals_make_consistent()


	sce.objects.active = ob
	ops_ob.mode_set(mode="EDIT")

	mesh_cleanup()
	ops_me.select_all(action=select_action)

	ops_ob.mode_set(mode="OBJECT")
	sce.objects.active = obj


def modifier_boolean(obj, ob, mode):
	md = obj.modifiers.new('Booltron', 'BOOLEAN')
	md.show_viewport = False
	md.show_render = False
	md.operation = mode
	md.object = ob

	bpy.ops.object.modifier_apply(modifier="Booltron")
	bpy.context.scene.objects.unlink(ob)
	bpy.data.objects.remove(ob)


def boolean_optimized(mode):
	context = bpy.context
	obj = context.active_object

	object_prepare()

	obj.select = False
	obs = context.selected_objects
	ob = obs[0]

	if len(obs) != 1:
		context.scene.objects.active = ob
		bpy.ops.object.join()
		context.scene.objects.active = obj

	mesh_selection(obj, 'DESELECT')
	mesh_selection(ob, 'SELECT')
	modifier_boolean(obj, ob, mode)
	obj.select = True


def boolean_each(mode):
	context = bpy.context
	obj = context.active_object

	object_prepare()

	obj.select = False
	obs = context.selected_objects

	mesh_selection(obj, 'DESELECT')
	for ob in obs:
		mesh_selection(ob, 'SELECT')
		modifier_boolean(obj, ob, mode)
	obj.select = True


def union():
	context = bpy.context
	mode = 'UNION'


	def separate():
		ops = bpy.ops
		ops_ob = ops.object
		ops_ob.mode_set(mode="EDIT")
		ops.mesh.separate(type="LOOSE")
		ops_ob.mode_set(mode="OBJECT")


	boolean_optimized(mode)
	separate()
	if len(context.selected_objects) != 1:
		boolean_each(mode)


def intersect():
	mode = 'INTERSECT'
	boolean_each(mode)


def difference():
	mode = 'DIFFERENCE'
	boolean_optimized(mode)


def separate():
	context = bpy.context
	sce = context.scene
	obj = context.active_object


	def object_duplicate(ob):
		ops_ob = bpy.ops.object
		ops_ob.select_all(action="DESELECT")
		ops_ob.select_pattern(pattern=ob.name)
		ops_ob.duplicate()
		return context.selected_objects[0]


	object_prepare()

	obj.select = False
	ob = context.selected_objects[0]

	obj_copy = object_duplicate(obj)
	ob_copy = object_duplicate(ob)

	mode = 'INTERSECT'
	mesh_selection(obj_copy, 'SELECT')
	mesh_selection(ob, 'DESELECT')
	sce.objects.active = ob
	modifier_boolean(ob, obj_copy, mode)

	mode = 'DIFFERENCE'
	mesh_selection(ob_copy, 'SELECT')
	mesh_selection(obj, 'DESELECT')
	sce.objects.active = obj
	modifier_boolean(obj, ob_copy, mode)
	obj.select = True



### Operator ###

class UNION(bpy.types.Operator):
    """Performes a boolean union operation"""
    bl_idname = "booltron.union"
    bl_label = "Booltron Union"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(self, context):
        return context.mode == 'OBJECT'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("help.operator","Help", icon ="ROTATECOLLECTION")
    
    def execute(self, context):
        if len(context.selected_objects) >= 2:
             union()
        else:
             print(self)
             self.report({'INFO'}, "need 2 Objects selected")         
        return {'FINISHED'}




class DIFFERENCE(Operator):
    """Performes a boolean difference operation"""
    bl_idname = "booltron.difference"
    bl_label = "Booltron Difference"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return context.mode == 'OBJECT'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("help.operator","Help", icon ="ROTACTIVE")

    def execute(self, context):
        if len(context.selected_objects) >= 2:
             difference()
        else:
             print(self)
             self.report({'INFO'}, "need 2 Objects selected")         
        return {'FINISHED'}


class INTERSECT(Operator):
    """Performes a boolean intersect operation"""
    bl_idname = "booltron.intersect"
    bl_label = "Booltron Intersect"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("help.operator","Help", icon ="ROTATECENTER")        

    def execute(self, context):
        if len(context.selected_objects) >= 2:
             intersect()
        else:
            print(self)
            self.report({'INFO'}, "need 2 Objects selected")
        return {'FINISHED'}


class SEPARATE(Operator):
    """Separates the active object along the intersection of the selected object (can handle only two objects at the time)"""
    bl_idname = "booltron.separate"
    bl_label = "Booltron Separate"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("help.operator","Help", icon ="ROTATECENTER")    

    def execute(self, context):
        if len(context.selected_objects) >= 2:
             separate()
        else:
             print(self)
             self.report({'INFO'}, "need 2 Objects selected")         
        return {'FINISHED'}











"""bl_info = {
    "name": "Boolean Operators",
    "location": "View3D > Toolshelf > Addons",
    "description": "Add Boolean Tools for running boolean operations on two selected objects.",
    "author": "Jonathan Williamson",
    "version": (0, 4),
    "blender": (2, 71, 0),
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/booleanoperators",
    "tracker_url": "https://developer.blender.org/T34502",
    "category": "Object"}

"""

###------ Create Boolean Operators -------###

class Boolean(bpy.types.Operator):
    """Boolean the currently selected objects with Union / Intsect / Difference"""
    bl_idname = "mesh.boolean"
    bl_label = "Boolean Operator"
    bl_options = {'REGISTER', 'UNDO'}

    modOp = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):

        scene = bpy.context.scene

        modName = "Bool"

        activeObj = context.active_object
        selected = context.selected_objects

        if selected:    
            if len(selected) > 1:
                if len(selected) == 2:
                    for ob in selected:
                        if ob != activeObj:
                            nonActive = ob

                    bpy.ops.object.modifier_add(type="BOOLEAN")

                    for mod in activeObj.modifiers:
                        if mod.type == 'BOOLEAN':
                            mod.operation = self.modOp
                            mod.object = nonActive
                            mod.name = modName

                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modName)
                    scene.objects.active = nonActive
                    activeObj.select = False
                    bpy.ops.object.delete(use_global=False)
                    activeObj.select = True
                    scene.objects.active = activeObj
                else:
                    self.report({'INFO'}, "Select only 2 objects at a time")
            else:
                self.report({'INFO'}, "Only 1 object selected")
        else:
            self.report({'INFO'}, "No objects selected")

        return {"FINISHED"}





###------- Create the Boolean Menu --------###
"""
class booleanMenu(bpy.types.Menu):
    bl_label = "Boolean Tools"
    bl_idname = "object.boolean_menu"

    def draw(self, context):
        layout = self.layout

        union = layout.operator("mesh.boolean", "Union")
        union.modOp = 'UNION'

        intersect = layout.operator("mesh.boolean", "Intersect")
        intersect.modOp = 'INTERSECT'

        difference = layout.operator("mesh.boolean", "Difference")
        difference.modOp = 'DIFFERENCE'


###------- Create the Boolean Toolbar --------###

class booleanToolbar(bpy.types.Panel):
    bl_label = "Boolean Tools"
    bl_idname = "object.boolean_toolbar"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = 'objectmode'
    bl_category = 'Tools'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)

        col.label(text="Operation:", icon="MOD_BOOLEAN")

        row = col.row()
        union = row.operator("mesh.boolean", "Union")
        union.modOp = 'UNION'

        intersect = row.operator("mesh.boolean", "Intersect")
        intersect.modOp = 'INTERSECT'

        difference = row.operator("mesh.boolean", "Difference")
        difference.modOp = 'DIFFERENCE'



### Register ###

classes = (
	#BooltronPanel,
	#BooltronPopup,
    
    Boolean,
    
	UNION,
	DIFFERENCE,
	INTERSECT,
	SEPARATE,
)


def register():
	for cls in classes:
		bpy.utils.register_class(cls)


def unregister():
	for cls in classes:
		bpy.utils.unregister_class(cls)



"""


