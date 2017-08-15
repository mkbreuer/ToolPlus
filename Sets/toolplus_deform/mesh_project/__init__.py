#  __init__.py (c) 2016 Mattias Fredriksson
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

#Addon info
bl_info = {
	'name': "Projection Operators",
    'author': "Mattias Fredriksson ",
    'version': (0, 9, 1),
    'blender': (2, 77, 0),
    'location': "3DView > Objectmode: Project Mesh onto UV Surface, Mirror Mesh over Defined Surface, Project Mesh(es) onto Active",
    'warning': "Bugs can exist, beware of using operators outside the usecase",
    'description': "3 Operators containing functionality for mirroring and projection mesh objects over/onto a mesh surface",
    'wiki_url': "",
    'tracker_url': "",
    'category': 'T+ Auxiliary'}
	
#Script reloading
if "bpy" in locals():
    import importlib
    if "funcs_blender" in locals():
        importlib.reload(funcs_blender)
    if "funcs_math" in locals():
        importlib.reload(funcs_math)
    if "funcs_tri" in locals():
        importlib.reload(funcs_tri)
    if "proj_data" in locals():
        importlib.reload(proj_data)
    if "bound" in locals():
        importlib.reload(bound)
    if "partition_grid" in locals():
        importlib.reload(partition_grid)
    if "uv_project" in locals():
        importlib.reload(uv_project)
    if "project" in locals():
        importlib.reload(project)
    if "mesh_mirror_script" in locals():
        importlib.reload(mesh_mirror_script)
#Script loading
else:
    from . import funcs_blender, funcs_math, funcs_tri, proj_data, bound, partition_grid, uv_project, project, mesh_mirror_script


import bpy

from .uv_project import UVProjectMesh
from .project import ProjectMesh
from .mesh_mirror_script import MirrorMesh

	

# Register the operator
def register():
	bpy.utils.register_class(UVProjectMesh)
	bpy.utils.register_class(ProjectMesh)
	bpy.utils.register_class(MirrorMesh)

def unregister():
	bpy.utils.unregister_class(UVProjectMesh)
	bpy.utils.unregister_class(ProjectMesh)
	bpy.utils.unregister_class(MirrorMesh)

if __name__ == "__main__":
		register()