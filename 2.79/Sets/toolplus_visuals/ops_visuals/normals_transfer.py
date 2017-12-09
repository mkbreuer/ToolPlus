#  ***** BEGIN GPL LICENSE BLOCK *****
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
#  ***** END GPL LICENSE BLOCK *****

# object_transfervertexnorms.py

# Goals: - pep8-80 compliance - how is it?
#        - store normal offset in custom data layer (C, bmesh?)
#        - option to choose between nearest vertex or projection
#        - more EditNormals operators, so as to
#           warrant object_editnormals.py instead

# Bugs:  - does not work if a mesh has shape keys

# Usage: - select multiple mesh objects
#        - call Transfer Vertex Normals operator
#        - defaults to zero influence; see F6 or 3dview tool pane and:
#           - adjust influence slider to transfer normals from active object
#           - distance affects the reach of the transfer
#        - currently this is a one-shot operation;
#           transferred normals are lost if mesh data is altered
#        - setting boundary edges to 'only' will cause every object's
#           boundary edges to be averaged with every other object's.

#bl_info = {
#    "name": "Transfer Vertex Normals",
#    "description": "Transfers nearest vertex normals from active object to "
#                   "other selected objects.",
#    "author": "Jean Ayer (vrav)", # legal / tracker name: Cody Burrow
#    "version": (0, 2, 2),
#    "blender": (2, 6, 3),
#    "location": "3D View > Spacebar > Transfer Vertex Normals",
#    "warning": "",
#    "category": "Object"}


# LOAD MODULE #
from sys import float_info as fi
import bmesh
import bpy

def nearestVertexNormal(sourceverts, vert, MAXDIST):
    '''
    Acquire Vector normal of nearest-location sourcevert to vert.
    sourceverts = BMVertSeq, source object verts 
    vert = Vector, comparison vert coordinate 
    MAXDIST = float, max distance to consider nearest 
    '''
    nearest = None
    nearestdist = fi.max
    if MAXDIST == 0.0:
        MAXDIST = fi.max
    
    for svert in sourceverts:
        dist = (vert.co - svert.co).magnitude
        if dist < nearestdist and dist < MAXDIST:
            nearest = svert
            nearestdist = dist
    if nearest:
        return nearest.normal
    else:
        return

def gatherSourceVerts(bmsrc, src, scene, BOUNDS):
    '''
    Adjust source BMesh for providing desired source normals.
    bmsrc = BMesh, should be empty
    src = Object, source to acquire verts from
    scene = Scene, generally context.scene; required for src.to_mesh
    BOUNDS = str, whether to include, ignore, or only use boundary edges
    '''
    bmsrc.from_mesh(src.to_mesh(scene, True, 'PREVIEW'))
    bmsrc.transform(src.matrix_world)
    
    if BOUNDS != 'INCLUDE':
        invalidverts = []
        boundaryvert = False
        for edge in bmsrc.edges:
            if BOUNDS == 'IGNORE':
                # Boundary verts are invalid
                if len(edge.link_faces) < 2:
                    for vert in edge.verts:
                        invalidverts.append(vert)
            else:
                # Internal verts are invalid
                if len(edge.link_faces) > 1:
                    for vert in edge.verts:
                        for edge in vert.link_edges:
                            if len(edge.link_faces) < 2:
                                boundaryvert = True
                                break
                        if boundaryvert:
                            boundaryvert = False
                            continue
                        else:
                            invalidverts.append(vert)
        for vert in invalidverts:
            if vert.is_valid:
                bmsrc.verts.remove(vert)

def joinBoundaryVertexNormals(self, context, destobjs,
                              INFL=0.0, MAXDIST=0.01):
    '''
    Average smoothing over boundary verts, usually same-location.
    destobjs = list, generally context.selected_objects
    INFL = float, influence strength
    MAXDIST = float, distance to influence... probably not necessary
    '''
    bms = {}
    bmsrc = bmesh.new()
    scene = context.scene
    
    for obj in destobjs:
        # These type != 'MESH' checks could be alleviated by removing
        #  non-mesh objects in execute(), but, may wish to
        #  support non-mesh objects one day
        if obj.type != 'MESH':
            continue
        bms[obj.name] = bmesh.new()
        bm = bms[obj.name]
        bm.from_mesh(obj.to_mesh(scene, False, 'PREVIEW'))
        bm.transform(obj.matrix_world)
        destverts = bm.verts
        
        for otherobj in destobjs:
            if otherobj.type != 'MESH' or obj == otherobj:
                continue
            gatherSourceVerts(bmsrc, otherobj, scene, 'ONLY')
            sourceverts = bmsrc.verts
            
            for vert in destverts:
                near = nearestVertexNormal(sourceverts, vert, MAXDIST)
                if near:
                    offset = near * INFL
                    vert.normal = (vert.normal + offset) * 0.5
                    vert.normal.normalize()
            bmsrc.clear()
    
    for name in bms:
        # Everything's been modified by everything else's original state,
        #  time to apply the modified data to the original objects
        bm = bms[name]
        for obj in destobjs:
            if obj.name == name:
                bm.transform(obj.matrix_world.inverted())
                bm.to_mesh(obj.data)
                bm.free()
    bmsrc.free()

def transferVertexNormals(self, context, src, destobjs,
                          INFL=0.0, MAXDIST=0.01, BOUNDS='IGNORE'):
    '''
    Transfer smoothing from one object to other selected objects.
    src = source object to transfer from 
    destobjs = list of objects to influence 
    INFL = influence strength 
    MAXDIST = max distance to influence 
    BOUNDS = ignore/include/only use boundary edges
    '''
    bm = bmesh.new()
    bmsrc = bmesh.new()
    scene = context.scene
    gatherSourceVerts(bmsrc, src, scene, BOUNDS)
    sourceverts = bmsrc.verts
    
    for obj in destobjs:
        if obj.type != 'MESH' or obj == src:
            continue
        bm.from_mesh(obj.to_mesh(scene, False, 'PREVIEW'))
        bm.transform(obj.matrix_world)
        destverts = bm.verts
        
        for vert in destverts:
            near = nearestVertexNormal(sourceverts, vert, MAXDIST)
            if near:
                offset = near
                if INFL < 0.0:
                    offset = offset * -1
                vert.normal = vert.normal.lerp(offset,abs(INFL))
                vert.normal.normalize()
        
        bm.transform(obj.matrix_world.inverted())
        bm.to_mesh(obj.data)
        bm.clear()
    
    bm.free()

class EditNormals_Transfer(bpy.types.Operator):
    ''' 
    Transfers nearest worldspace vertex normals from active object to selected.
    When 'Boundary Edges' is set to Only, each object checks all other objects.
    Example uses: baking, mollifying lowpoly foliage, hiding sub-object seams.
    '''
    bl_idname = "tp_ops.editnormals_transfer"
    bl_label = "Transfer Vertex Normals"
    bl_description = "Transfer shading from active object to selected objects."
    bl_options = {'REGISTER', 'UNDO'}
    
    influence = bpy.props.FloatProperty(
            name='Influence',
            description='Transfer strength, negative inverts',
            subtype='FACTOR',
            min=-1.0,
            max=1.0,
            default=0.0
            )
    maxdist = bpy.props.FloatProperty(
            name='Distance',
            description='Transfer distance, 0 for infinite',
            subtype='DISTANCE',
            unit='LENGTH',
            min=0.0,
            max=fi.max,
            soft_max=20.0,
            default=0.01
            )
    bounds = bpy.props.EnumProperty(
            name='Boundary Edges',
            description="Management for single-face edges.",
            items=[('IGNORE', 'Ignore', 'Discard source boundary edges.'),
                   ('INCLUDE', 'Include', 'Include source boundary edges.'),
                   ('ONLY', 'Only', 'Operate only on boundary edges.')],
            default='IGNORE'
            )
    
    def execute(self,context):
        src = context.active_object
        destobjs = context.selected_objects
        
        if context.mode != 'OBJECT':
            self.report({'ERROR'},'Must be performed in object mode')
            return{'CANCELLED'}
        if not src or not isinstance(src.data, bpy.types.Mesh):
            self.report({'ERROR'},'No active object with mesh data')
            return{'CANCELLED'}
        if len(destobjs) < 2:
            self.report({'ERROR'},'Requires two or more objects')
            return{'CANCELLED'}
        
        if self.influence != 0.0:
            if self.bounds != 'ONLY':
                transferVertexNormals(
                    self, context, src, destobjs,
                    INFL=self.influence,
                    MAXDIST=self.maxdist,
                    BOUNDS=self.bounds)
            else:
                joinBoundaryVertexNormals(
                    self, context, destobjs,
                    INFL=self.influence,
                    MAXDIST=self.maxdist)
        return {'FINISHED'}



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


