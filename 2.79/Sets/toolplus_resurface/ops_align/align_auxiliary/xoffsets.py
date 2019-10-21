'''
BEGIN GPL LICENSE BLOCK

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

END GPL LICENSE BLOCK

#############################################################################

xOffsets_alpha_004.py

Usage: 
Basic usage is you choose 2 or 3 "reference points" to work with, the point
will be placed at the vertex nearest the location where you click with the 
Left Mouse Button (except when there are no vertices near the mouse cursor).
1st point set is the "Anchor" (red)
2nd point set is the "Free" (green)
If 3rd point picked, 2nd point becomes "Pivot" (blue)
and 3rd point (last) becomes "Free" point
If you click on an already "selected" point it will be "unselected"

Unselecting points:
For "unselecting" points, the Free > Pivot > Anchor association works in
reverse from selecting points. 
Examples:
If 2 points are selected and Anchor gets unselected, Free (becoming the only 
point selected) becomes the "new" Anchor.
If 3 points are selected and Pivot gets unselected, Free and Anchor remain 
unchanged and Pivot is gone.
If 3 points are selected and Free gets unselected, Anchor remains unchanged,
Pivot becomes the "new" Free.

Direction of Movement
When distance or angle between Anchor and Free is changed, only Free point
will move (away or towards) Anchor to match new value entered.

Modes: 
Translate, Scale (Object mode only), and Rotation.
Translate mode active when only 2 points are picked.
Scale mode active if 2 points picked that are part of same object.
Rotate mode active when 3 points selected.
If Free point is a selected object, all other selected objects will be 
transformed as well (except when in scale mode).

Translate mode:
Without axis lock set Free will move along slope between Anchor and Free. 
With axis lock set, Free is moved along set axis.

Rotation mode:
Rotation mode will not work in Object Mode until axis lock has been set.
When an axis lock is set, the Free point will rotate around that axis 
where it passes throught the Pivot point location.
With no axis lock set in Edit Mode, the Free piont will rotate around the 
"face normal" of Anchor-Pivot-Free "face" coming off the Pivot location.

Scale mode:
Will scale whole object until Free reaches entered distance.

Notes: 
* Cannot select more than 1 point in a given 3D location (Points can't 
share same coordinates).
* If Objects have unapplied scale or rotation, transform might not work as
intended.
* Entering negative values will reverse the direction of the transformation.
For example, If a Z axis lock was applied and the Free vertex was 2 units above 
the Anchor and -3 was entered, the Free vertex would be moved so it was 
located 3 units below the Anchor.

Hotkeys:
LMB = Left Mouse Button, RMB = Right Mouse Button

ESC      exits the add-on
LMB+RMB  exits the add-on
LMB      selects points and activates button
X        sets X-axis lock
Y        sets Y-axis lock
Z        sets Z-axis lock
C        clears axis lock (sets "Spherical" lock in rotation mode)

todo:
* better measurement input panel
* rewrite/refactor code to optimize for modal operation
* redo coding for spherical rotations so it also work in objmode and to
    avoid gimbal lock and divide by zero issues
* prevent selection of non-visible vertices
* add hotkey reference info

#############################################################################
'''

bl_info = {
    "name": "Exact Offsets",
    "author": "nBurn",
    "version": (0, 0, 4),
    "blender": (2, 7, 7),
    "location": "View3D",
    "description": "CAD tool for precisely setting distance scale and rotation of mesh geometry",
    "category": "Mesh"
}

import bpy
import bgl
import blf
import bmesh
from math import fmod, sqrt, degrees, radians, acos
from mathutils import Vector, geometry, Quaternion, Euler
from mathutils.geometry import intersect_line_line_2d
from bpy_extras.view3d_utils import location_3d_to_region_2d

print("Exact Offsets loaded")

currMeasStor = 0.0
newMeasStor = None


# vertex storage class, stores reference point info
class vObjStorage:
    def __init__(self, objNum=-1, vertInd=-1, coor3D=[], coor2D=[], dist2D=-1, refInd=-1):
        self.objNum = objNum
        self.vertInd = vertInd
        self.coor3D = coor3D
        self.coor2D = coor2D
        self.dist2D = dist2D
        self.refInd = refInd
        self.obj = bpy.context.scene.objects # short hand

    def datOut(self): # debug
        return self.objNum, self.vertInd, self.coor3D.copy(), [*self.coor2D], self.dist2D, self.refInd

    def set2D(self):
        region = bpy.context.region
        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D": break
        rv3d = area.spaces[0].region_3d
        self.coor2D = location_3d_to_region_2d(region, rv3d, self.coor3D)

    def update3D(self):
        tmpCoLocal = self.obj[self.objNum].data.vertices[self.vertInd].co
        self.coor3D = self.obj[self.objNum].matrix_world * tmpCoLocal


# stores rotation info
# for passing data from draw_callback_px to external functions
# not as bad as hiding arguments in passed variables, but still seems hackish
class rotationData:
    def __init__(self):
        self.newAngR = 0.0
        self.newAngD = 0.0
        self.angDiffD = 0.0
        self.angDiffR = 0.0
        self.axisLk = ''
        self.pivNorm = [] # pivot normal
        #self.angleEq_0_180 = False
        #self.obj = bpy.context.scene.objects[self.objNum] # short hand

    #def datOut(self): # debug
    #    return self.objNum, self.vertInd, self.coor3D, self.coor2D, self.dist2D

    # placeholder function, 
    # do rotation calculations inside this class?
    #def abcdef123(self):
    #    return


### linear equations ### 

#def getMidpoint2D(x1,y1,x2,y2):
#    return ( (x1+x2)/2 , (y1+y2)/2 )


def getMidpoint3D(x1,y1,z1,x2,y2,z2):
    return Vector([ (x1+x2)/2 , (y1+y2)/2 , (z1+z2)/2 ])


def get_dist_2D(x1,y1,x2,y2):
    return sqrt( abs( ((x2-x1)**2) + ((y2-y1)**2) ) )


def get_dist_3D(x1,y1,z1,x2,y2,z2):
    res = sqrt( abs( ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2) ) )
    return res


def get_slope_3D(self, x1,y1,z1,x2,y2,z2):
    dist3D = get_dist_3D( x1,y1,z1,x2,y2,z2 )
    if dist3D == 0:
        self.report({'ERROR'}, 'Distance between points cannot be zero.')
        return
    xSlope = (x1 - x2) / dist3D
    ySlope = (y1 - y2) / dist3D
    zSlope = (z1 - z2) / dist3D
    return ( xSlope, ySlope, zSlope )


def get_new_pt_3D(x1,y1,z1,slopeX,slopeY,slopeZ,dis3D):
    #newX = (x1 +- ( dis3D * slopeX ) )
    newX = (x1 + ( dis3D * slopeX ) )
    newY = (y1 + ( dis3D * slopeY ) )
    newZ = (z1 + ( dis3D * slopeZ ) )
    return Vector([newX,newY,newZ])


# for making sure rise over run doesn't get flipped
def slope_check(pt1,pt2):
    cmp = ( pt1[0] >= pt2[0], pt1[1] >= pt2[1], pt1[2] >= pt2[2] )
    return cmp


# todo: split into 2 functions ?
# finds 3D location that shares same slope of line connecting Anchor and
# Free or is on axis line going through Anchor
def get_new_3D_coor(self,lock, ptA, ptF, newDis):
    ptN_1, ptN_2 = (), ()
    if lock == '':
        if newDis == 0:
            return ptA
        origSlope = slope_check(ptA, ptF)
        slope3D = get_slope_3D(self, *ptF, *ptA )
        ptN_1 = get_new_pt_3D( *ptA, *slope3D, newDis )
        ptN_2 = get_new_pt_3D( *ptA, *slope3D, -newDis )
        ptN_1_slp = slope_check( ptA, ptN_1 )
        ptN_2_slp = slope_check( ptA, ptN_2 )
        if   origSlope == ptN_1_slp:
            if newDis > 0:
                return ptN_1
            else:
            # for negative distances
                return ptN_2
        elif origSlope == ptN_2_slp:
            if newDis > 0:
                return ptN_2
            else:
                return ptN_1
        else: # neither slope matches
            self.report({'ERROR'}, 'Slope mismatch. Cannot calculate new point.')
            return []
    elif lock == 'X':
        if ptF[0] > ptA[0]: return Vector([ ptA[0] + newDis, ptF[1], ptF[2] ])
        else: return Vector([ ptA[0] - newDis, ptF[1], ptF[2] ])
    elif lock == 'Y':
        if ptF[1] > ptA[1]: return Vector([ ptF[0], ptA[1] + newDis, ptF[2] ])
        else: return Vector([ ptF[0], ptA[1] - newDis, ptF[2] ])
    elif lock == 'Z':
        if ptF[2] > ptA[2]: return Vector([ ptF[0], ptF[1], ptA[2] + newDis ])
        else: return Vector([ ptF[0], ptF[1], ptA[2] - newDis ])
    else: # neither slope matches
        self.report({'ERROR'}, "Slope mismatch. Can't calculate new point.")
        return []


# takes an axis and two 3D coordinates and returns two 3D coordinates
# finds 3D midpoint between 2 supplied coordinates
# axis determines which coordinates are assigned midpoint values
# if X, Anchor is [AncX,MidY,MidZ] and Free is [FreeX,MidY,MidZ]
# if no lock, returns same two coordinates supplied
def setMoveLockPts(axis,dPts):
    if axis == '':
        return dPts
    else:
        mid3D = getMidpoint3D( *dPts[0].coor3D, *dPts[1].coor3D )
        NewPtLs = [ vObjStorage(), vObjStorage() ]
        if axis == 'X':
            NewPtLs[0].coor3D = Vector([ dPts[0].coor3D[0], mid3D[1], mid3D[2] ])
            NewPtLs[1].coor3D = Vector([ dPts[1].coor3D[0], mid3D[1], mid3D[2] ])
        elif axis == 'Y':
            NewPtLs[0].coor3D = Vector([ mid3D[0], dPts[0].coor3D[1], mid3D[2] ])
            NewPtLs[1].coor3D = Vector([ mid3D[0], dPts[1].coor3D[1], mid3D[2] ])
        elif axis == 'Z':
            NewPtLs[0].coor3D = Vector([ mid3D[0], mid3D[1], dPts[0].coor3D[2] ])
            NewPtLs[1].coor3D = Vector([ mid3D[0], mid3D[1], dPts[1].coor3D[2] ])
        if NewPtLs[0].coor3D == NewPtLs[1].coor3D:
            # axis lock creates identical points, return empty list
            return []
        else:
            for itm in NewPtLs: itm.set2D()
            return NewPtLs


# todo: rework for more general use cases?
# takes an axis and three 3D coordinates and returns three 3D coordinates
# axis determines which of the Free's coordinates are assigned
# to Anchor and Pivot coordinates eg:
# if X, Anchor is [FreeX,AncY,AncZ] and Pivot is [FreeX,PivY,PivZ]
# if no lock, returns same three coordinates supplied
def setAngLockPts(axis,dPts):
    if axis == '':
        return dPts
    else:
        NewPtLs = [ vObjStorage(), vObjStorage(), vObjStorage() ]
        NewPtLs[2].coor3D = dPts[2].coor3D.copy()
        if axis == 'X':
            NewPtLs[0].coor3D = Vector([ NewPtLs[2].coor3D[0], dPts[0].coor3D[1], dPts[0].coor3D[2] ])
            NewPtLs[1].coor3D = Vector([ NewPtLs[2].coor3D[0], dPts[1].coor3D[1], dPts[1].coor3D[2] ])
        elif axis == 'Y':
            NewPtLs[0].coor3D = Vector([ dPts[0].coor3D[0], NewPtLs[2].coor3D[1], dPts[0].coor3D[2] ])
            NewPtLs[1].coor3D = Vector([ dPts[1].coor3D[0], NewPtLs[2].coor3D[1], dPts[1].coor3D[2] ])
        elif axis == 'Z':
            NewPtLs[0].coor3D = Vector([ dPts[0].coor3D[0], dPts[0].coor3D[1], NewPtLs[2].coor3D[2] ])
            NewPtLs[1].coor3D = Vector([ dPts[1].coor3D[0], dPts[1].coor3D[1], NewPtLs[2].coor3D[2] ])
        if NewPtLs[0].coor3D == NewPtLs[1].coor3D or \
        NewPtLs[0].coor3D == NewPtLs[2].coor3D or \
        NewPtLs[1].coor3D == NewPtLs[2].coor3D:
            # axis lock creates identical points, return empty list
            return []
        else:
            for itm in NewPtLs: itm.set2D()
            return NewPtLs


# Aco, Bco, and Cco are 3 float lists or vectors
# takes 3 coordinate lists as arguments
# coordinates must share a common center "pivot" point (co2)
def getLineAngle3D(self,Aco,Bco,Cco):
    Ax = Aco[0] - Bco[0]
    Ay = Aco[1] - Bco[1]
    Az = Aco[2] - Bco[2]
    A = sqrt( (Ax*Ax) + (Ay*Ay) + (Az*Az) )

    Bx = Cco[0] - Bco[0]
    By = Cco[1] - Bco[1]
    Bz = Cco[2] - Bco[2]
    B = sqrt( (Bx*Bx) + (By*By) + (Bz*Bz) )

    top = (Ax*Bx) + (Ay*By) + (Az*Bz)
    if A == 0 or B == 0:
        self.report({'ERROR'}, 'Division by zero.')
        return -1
    res = round(top / (A * B),10)
    if res > 1 or res < -1:
        self.report({'ERROR'}, 'Outside acos range.')
        return -1
    return acos(res)


# floating point math fun!
# if floats aren't equal are they almost equal?
# todo: replace this with Python 3.5's math.isclose() ?
# do recent versions of Blender support it?
def AreFloatsEq(fl_A,fl_B):
    if fl_A == fl_B:
        return True
    else:
        return fl_A > (fl_B * 0.999) and fl_A < (fl_B * 1.001)


# checks if 3 coordinates create an angle that matches the expected angle
def angleMatch3D(self,pt1,pt2,pt3,expAng):
    angMeas = getLineAngle3D(self,pt1,pt2,pt3)
    #print("pt1",pt1) # debug
    #print("pt2",pt2) # debug
    #print("pt3",pt3) # debug
    #print( "expAng ",expAng ) # debug
    #print( "angMeas ",angMeas ) # debug
    return AreFloatsEq(angMeas,expAng)


# Calculates rotation around axis or face normal at Pivot's location.
# Takes two 3D coordinate Vectors (PivC and movCo), rotation angle in
# radians (angleDiffRad), and rotation data storage object (rotDat).
# Aligns movCo to world origin, rotates algined movCo (vecTmp) around
# axis stored in rotDat, then removes world-origin alignment.
def getRotatedPoint(PivC,angleDiffRad,rotDat,movCo):
    axisLk = rotDat.axisLk
    vecTmp = movCo - PivC
    rotVal = []
    if   axisLk == '': # arbitrary axis / spherical rotations
        rotVal = Quaternion(rotDat.pivNorm, angleDiffRad)
    elif axisLk == 'X':
        rotVal = Euler((angleDiffRad,0.0,0.0), 'XYZ')
    elif axisLk == 'Y':
        rotVal = Euler((0.0,angleDiffRad,0.0), 'XYZ')
    elif axisLk == 'Z':
        rotVal = Euler((0.0,0.0,angleDiffRad), 'XYZ')
    vecTmp.rotate(rotVal)
    return vecTmp + PivC


# Finds out whether rotDat.newAngR or negative rotDat.newAngR will
# result in desired rotation angle.
# angleEq_0_180 for 0 and 180 degree starting rotations
def findCorrectRot(self,angleEq_0_180,refPts,rotDat):
    angDiffRad,newAngleRad,axisLk = rotDat.angDiffR,rotDat.newAngR,rotDat.axisLk
    movePt = refPts[2].coor3D
    tmpCo1 = getRotatedPoint(refPts[1].coor3D, angDiffRad,rotDat,movePt)
    tmpCo2 = getRotatedPoint(refPts[1].coor3D,-angDiffRad,rotDat,movePt)
    #print("tmpCo1",tmpCo1,"\ntmpCo2",tmpCo2) # debug
    lockPts = setAngLockPts(axisLk,refPts)
    # is below check needed? is lockPts tested before findCorrectRot called?
    # will be needed for a selection move?
    if lockPts == []:
        lockPts = refPts
        axisLk = ''
        return ()
    else:
        if angleEq_0_180:
            return (tmpCo1, angDiffRad, tmpCo2, -angDiffRad)
        elif angleMatch3D(self,lockPts[0].coor3D,lockPts[1].coor3D,tmpCo1,newAngleRad):
            #print("matched tmpCo1") # debug
            return (tmpCo1, angDiffRad)
        else:
            #print("matched tmpCo2") # debug
            return (tmpCo2, -angDiffRad)


## point finding code ##

def find_closest_vert(obInd,loc,meshObj):
    meshDat = meshObj.data
    size = len(meshDat.vertices)
    closVert = vObjStorage()

    for i, v in enumerate(meshDat.vertices):
        tmpOb = vObjStorage(obInd, i)
        tmpOb.coor3D = meshObj.matrix_world * v.co # global instead of local
        tmpOb.set2D()
        tmpOb.dist2D = get_dist_2D( loc[0], loc[1], tmpOb.coor2D[0], tmpOb.coor2D[1] )
        if closVert.dist2D != -1:
            if closVert.dist2D > tmpOb.dist2D:
                closVert = tmpOb
        else:
            closVert = tmpOb
    return closVert


def find_all(co_find):
    closest = vObjStorage()
    indexLs = []
    objLen = len(bpy.context.scene.objects)
    for i in range(objLen):
        if bpy.context.scene.objects[i].type == 'MESH':
            indexLs.append(i)
    for iNum in indexLs:
        meshC = bpy.context.scene.objects[iNum]
        tempOb = find_closest_vert(iNum, co_find, meshC)
        if closest.dist2D == -1: 
            closest = tempOb
        else: 
            if tempOb.dist2D < closest.dist2D:
                closest = tempOb
    if closest.dist2D < 40:
        return closest
    else:
        return []


### GL drawing code ### 

def draw_font_at_pt(text, pt_co, pt_color):
    font_id = 0
    bgl.glColor4f(*pt_color) # grey
    blf.position(font_id, pt_co[0], pt_co[1], 0)
    blf.size(font_id, 32, 72)
    blf.draw(font_id, text)
    w, h = blf.dimensions(font_id, text)
    return [w, h]


def draw_pt_2D(pt_co, pt_color,sz=8):
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glPointSize(sz)
    bgl.glColor4f(*pt_color)
    bgl.glBegin(bgl.GL_POINTS)
    bgl.glVertex2f(*pt_co)
    bgl.glEnd()
    return


def draw_line_2D (pt_co_1, pt_co_2, pt_color):
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glPointSize(7)
    bgl.glColor4f(*pt_color)
    bgl.glBegin(bgl.GL_LINE_STRIP)
    bgl.glVertex2f( *pt_co_1 )
    bgl.glVertex2f( *pt_co_2 )
    bgl.glEnd()
    return


def draw_box(boxCo, color):
    bgl.glColor4f(*color)
    bgl.glBegin(bgl.GL_LINE_STRIP)
    for coord in boxCo:
        bgl.glVertex2f( coord[0], coord[1] )
    bgl.glVertex2f( boxCo[0][0], boxCo[0][1] )
    bgl.glEnd()
    return


# == 3D View mouse location and button code ==
# Functions outside_loop() and point_inside_loop() for creating the measure
# change "button" in the 3D View taken from patmo141's Vitual Button script:
# https://blenderartists.org/forum/showthread.php?259085

def outside_loop(loopCoords):
    xs = [v[0] for v in loopCoords]
    ys = [v[1] for v in loopCoords]
    maxx = max(xs)
    maxy = max(ys)
    bound = (1.1*maxx, 1.1*maxy)
    return bound


def point_inside_loop(loopCoords, mousLoc):
    nverts = len(loopCoords)
    #vectorize our two item tuple
    out = Vector(outside_loop(loopCoords))
    vecMous = Vector(mousLoc)
    intersections = 0
    for i in range(0,nverts):
        a = Vector(loopCoords[i-1])
        b = Vector(loopCoords[i])
        if intersect_line_line_2d(vecMous,out,a,b):
            intersections += 1
    inside = False
    if fmod(intersections,2):
        inside = True
    return inside


def get_box_coor(origin,rWidth,rHeight,xOffset,yOffset):
    coBL = (origin[0]-xOffset), (origin[1]-yOffset)
    coTL = (origin[0]-xOffset), (origin[1]+rHeight+yOffset)
    coTR = (origin[0]+rWidth+xOffset), (origin[1]+rHeight+yOffset)
    coBR = (origin[0]+rWidth+xOffset), (origin[1]-yOffset)
    return [coBL, coTL, coTR, coBR]


def sceneRefresh(edType):
    if bpy.context.scene.objects.active.type != 'MESH':
        for i in bpy.context.scene.objects:
            if i.type == 'MESH':
                bpy.context.scene.objects.active = i
                break
    if bpy.context.scene.objects.active.type == 'MESH':
        sObjs = bpy.context.scene.objects
        scn_selected = []
        if edType != "EDIT_MESH":
            scn_selected = [o for o in range(len(sObjs)) if sObjs[o].select]
            bpy.ops.object.select_all(action='DESELECT')    
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        if scn_selected != []:
            for i in scn_selected: sObjs[i].select = True


# takes vObjStorage type and 3D coordinate list as arguments, 
# calculates difference between their 3D locations
# to determine translation to apply to object in vObjStorage arg
def do_translation( mode,newCo,freeObj,selectLs=[],freeInSel=False ):
    coorChange, oldCo = [0,0,0], [0,0,0]
    if mode == "OBJECT":  # get Free's global coordinates
        oldCo = freeObj.coor3D
    elif mode == "EDIT_MESH":  # get Free's local coordinates
        oldCo = bpy.context.scene.objects[freeObj.objNum].data.vertices[freeObj.vertInd].co
    for i in range(3):
        if oldCo[i] != newCo[i]:
            coorChange[i] = - ( oldCo[i] - newCo[i] )
        else:
            coorChange[i] = 0
    #print("coorChange",coorChange) # debug
    if mode == "OBJECT":
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects[freeObj.objNum].select = True
        bpy.ops.transform.translate(value=(coorChange[0], coorChange[1], coorChange[2]))
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        return Vector([ *coorChange ])
    elif mode == "EDIT_MESH":
        bm = bmesh.from_edit_mesh( bpy.context.edit_object.data )
        activMW = bpy.context.edit_object.matrix_world
        if hasattr(bm.verts, "ensure_lookup_table"): 
            bm.verts.ensure_lookup_table()

        for v2 in selectLs:
            bm.verts[v2].co.x += coorChange[0]
            bm.verts[v2].co.y += coorChange[1]
            bm.verts[v2].co.z += coorChange[2]

        newVertLoc = activMW * bm.verts[freeObj.vertInd].co
        bmesh.update_edit_mesh( bpy.context.scene.objects[freeObj.objNum].data )
        sceneRefresh( mode )
        return newVertLoc


# unused functions. left as placeholder
# originally intended for tidying up  draw_callback_px()
# todo: see what parts of rotation and scale code can be put here?
'''
# supposed to be for scale stuff?
# this looks a lot like  do_translation() ...
def do_scale(freeObj,newCo):
    coorChange = [0,0,0]
    oldCo = freeObj.coor3D
    for i in range(3):
        if oldCo[i] != newCo[i]:
            coorChange[i] = - ( oldCo[i] - newCo[i] )
        else:
            coorChange[i] = 0

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects[freeObj.objNum].select = True
    bpy.ops.transform.translate(value=(coorChange[0], coorChange[1], coorChange[2]))
    bpy.ops.object.select_all(action='DESELECT')
    return


# Send old angle, new angle, freeCo, pivotCo, anchCo
# Receive New 3D Location
def do_rotate():
    return
'''


# finds 0 and 180 degree reference points
# for testing / debug purposes, may use later for UI elements
def draw_pts_0_180(self,ptLs,axisLock,Color):
    AncC = ptLs[0].coor3D
    PivC = ptLs[1].coor3D
    FreC = ptLs[2].coor3D
    region = bpy.context.region
    for area in bpy.context.screen.areas:
        if area.type == "VIEW_3D": break
    rv3d = area.spaces[0].region_3d
    A2P_dis = get_dist_3D( *AncC, *PivC )
    P2F_dis = get_dist_3D( *PivC, *FreC )
    dis180 = A2P_dis + P2F_dis
    co180 = get_new_3D_coor(self,'',AncC, PivC, dis180)
    co000 = get_new_3D_coor(self,'',PivC, AncC, P2F_dis)
    co180_2d, co000_2d = [], []
    
    if axisLock == '':
        co180_2d = location_3d_to_region_2d(region, rv3d, [ co180[0],co180[1],co180[2] ])
        co000_2d = location_3d_to_region_2d(region, rv3d, [ co000[0],co000[1],co000[2] ])
    elif axisLock == 'X':
        co180_2d = location_3d_to_region_2d(region, rv3d, [ FreC[0],co180[1],co180[2] ])
        co000_2d = location_3d_to_region_2d(region, rv3d, [ FreC[0],co000[1],co000[2] ])
    elif axisLock == 'Y':
        co180_2d = location_3d_to_region_2d(region, rv3d, [ co180[0],FreC[1],co180[2] ])
        co000_2d = location_3d_to_region_2d(region, rv3d, [ co000[0],FreC[1],co000[2] ])
    elif axisLock == 'Z':
        co180_2d = location_3d_to_region_2d(region, rv3d, [ co180[0],co180[1],FreC[2] ])
        co000_2d = location_3d_to_region_2d(region, rv3d, [ co000[0],co000[1],FreC[2] ])
    draw_pt_2D( co180_2d, Color )
    draw_pt_2D( co000_2d, Color )


def draw_btn(text, coor2D, mouseLoc, colorOff, colorOn):
    color = colorOff
    offSet = 5
    font_id = 0
    blf.size(font_id, 32, 72)
    w, h = blf.dimensions(font_id, text)
    textCoor = (coor2D[0] - w/2, (coor2D[1] + 5*offSet))
    boxCo = get_box_coor(textCoor, w, h, offSet, offSet)
    
    bgl.glColor4f(*color)
    blf.position(font_id, textCoor[0], textCoor[1], 0.0)
    blf.draw(font_id, text)
    if point_inside_loop(boxCo,mouseLoc):
        color = colorOn
    
    draw_box(boxCo, color)
    return boxCo


# == pop-up dialogue code ==
# todo: update with newer menu code
class changeInputPanel(bpy.types.Operator):
    bl_idname = "object.ms_input_dialog_op"
    bl_label = "Measurement Input Panel"

    float_new_meas = bpy.props.FloatProperty(name="Measurement")

    def execute(self, context):
        global currMeasStor # debug
        #print("currMeasStor:",currMeasStor) # debug
        global newMeasStor
        newMeasStor = self.float_new_meas
        #print("newMeasStor:",newMeasStor) # debug
        return {'FINISHED'}

    def invoke(self, context, event):
        global currMeasStor
        self.float_new_meas = currMeasStor
        return context.window_manager.invoke_props_dialog(self)

class DialogPanel(bpy.types.Panel):
    def draw(self, context):
        self.layout.operator("object.ms_input_dialog_op")


# == core add-on code ==

def draw_callback_px(self, context):
    global currMeasStor, newMeasStor
    colorWhite  = [1.0, 1.0, 1.0, 1.0]
    colorRed    = [1.0, 0.0, 0.0, 0.5]
    colorGreen  = [0.0, 1.0, 0.0, 0.5]
    colorBlue   = [0.0, 0.0, 1.0, 0.5]
    colorYellow = [1.0, 1.0, 0.5, 1.0]
    colorGrey   = [1.0, 1.0, 1.0, 0.4]
    
    if self.canLock:
        if   self.axisLock == 'X':
            draw_font_at_pt ( self.axisLock, [70,70], colorRed )
        elif self.axisLock == 'Y':
            draw_font_at_pt ( self.axisLock, [70,70], colorGreen )
        elif self.axisLock == 'Z':
            draw_font_at_pt ( self.axisLock, [70,70], colorBlue )

    if self.refPtCnt > 0:
        for obI in range(self.refPtCnt):
            self.ref_pts[obI].set2D()
        if self.refPtCnt < 2:
            draw_pt_2D ( self.ref_pts[0].coor2D, colorRed )
        elif self.refPtCnt == 2:  # set up translate mode UI
            lockPts = []
            self.canLock = True
            self.drawBtn = True
            offSet = 5
            draw_pt_2D( self.ref_pts[0].coor2D, colorRed )
            draw_pt_2D( self.ref_pts[1].coor2D, colorGreen )

            # activate scale mode if Anchor and Free attached to same object
            if self.currEdType == "OBJECT":
                if self.ref_pts[0].objNum == self.ref_pts[1].objNum:
                    self.transfMode = "SCALE"

            # assign midpoints if axis lock set
            lockPts = setMoveLockPts(self.axisLock,self.ref_pts)
            if lockPts == []:
                self.report({'ERROR'}, self.axisLock+' axis lock creates identical points')
                lockPts = self.ref_pts
                self.axisLock = ''
            if self.axisLock != '':
                # draw line along given Axis using midpoint between Anchor and Free
                draw_pt_2D( lockPts[0].coor2D, colorRed )
                draw_pt_2D( lockPts[1].coor2D, colorGreen )

            midP = vObjStorage( -1,-1,getMidpoint3D( *self.ref_pts[0].coor3D, *self.ref_pts[1].coor3D ))
            midP.set2D()
            draw_line_2D( lockPts[0].coor2D, lockPts[1].coor2D, colorRed )
            currMeasStor = get_dist_3D( *lockPts[0].coor3D, *lockPts[1].coor3D )
            
            if self.btn_clicked:
                self.btn_clicked = False
                if self.currEdType == "EDIT_MESH" and \
                bpy.context.scene.objects[self.ref_pts[1].objNum].mode != 'EDIT':
                    self.report({'ERROR'}, 'Free must be in active mesh in Edit Mode.')
                else:
                    bpy.ops.object.ms_input_dialog_op('INVOKE_DEFAULT')
                    
            if self.transfMode == "SCALE" and newMeasStor != None and newMeasStor < 0:
                self.report({'ERROR'}, 'Scale input cannot be negative.')
                newMeasStor = None

            self.boxCo = draw_btn(format(currMeasStor, '.2f'), midP.coor2D, self.mouse,colorWhite,colorRed)

        else:  # set up rotation mode UI
            lockPts = []
            self.canLock = True
            self.drawBtn = True
            self.transfMode = "ROTATE"
            offSet = 5
            draw_pt_2D( self.ref_pts[0].coor2D, colorRed )
            draw_pt_2D( self.ref_pts[1].coor2D, colorBlue )
            draw_pt_2D( self.ref_pts[2].coor2D, colorGreen )
            lockPts = setAngLockPts(self.axisLock,self.ref_pts)
            if lockPts == []:
                self.report({'ERROR'}, self.axisLock+' axis lock creates identical points')
                lockPts = self.ref_pts
                self.axisLock = ''
            else:
                draw_pt_2D( lockPts[0].coor2D, colorRed )
                draw_pt_2D( lockPts[1].coor2D, colorBlue )
            
            tmpMidP = getMidpoint3D( *lockPts[0].coor3D, *lockPts[2].coor3D )
            midP = vObjStorage( -1,-1,getMidpoint3D( *tmpMidP, *lockPts[1].coor3D ) )
            midP.set2D()
            
            draw_line_2D( lockPts[0].coor2D, lockPts[1].coor2D, colorRed ) 
            draw_line_2D( lockPts[1].coor2D, lockPts[2].coor2D, colorRed ) 
            #draw_pts_0_180(self,lockPts,self.axisLock,colorYellow) # debug

            lineAngleR = getLineAngle3D(self,lockPts[0].coor3D, lockPts[1].coor3D, lockPts[2].coor3D)
            lineAngleD = degrees( lineAngleR )
            currMeasStor = lineAngleD
            # if angle measure is 0 or 180
            if AreFloatsEq(currMeasStor,0.0) or AreFloatsEq(currMeasStor,180.0):
                self.btn_0_or_180 = True
                if self.btn_0_or_180_mStor != None:
                    newMeasStor = self.btn_0_or_180_mStor

            if self.btn_clicked:
                self.btn_clicked = False
                
                # prevent pop-up if:
                #    Anchor and Free points on same object (object mode)
                #    angle is 0 or 180 and no axis lock set
                if self.currEdType == "OBJECT" and self.ref_pts[0].objNum == self.ref_pts[2].objNum:
                    self.report({'ERROR'}, "Free & Anchor can't be on same object for rotations.")
                elif self.currEdType == "EDIT_MESH" and \
                bpy.context.scene.objects[self.ref_pts[2].objNum].mode != 'EDIT':
                    self.report({'ERROR'}, "Free must be in active mesh in Edit Mode.")
                elif self.axisLock != '':
                    bpy.ops.object.ms_input_dialog_op('INVOKE_DEFAULT')
                elif self.btn_0_or_180 == False: # not flat angle and no axis lock set
                    AncC = self.ref_pts[0].coor3D
                    PivC = self.ref_pts[1].coor3D
                    FreC = self.ref_pts[2].coor3D
                    self.rDat.pivNorm = geometry.normal(AncC,PivC,FreC)
                    bpy.ops.object.ms_input_dialog_op('INVOKE_DEFAULT')
                else:
                    # would need complex angle processing workaround to get
                    # spherical rotations working with flat angles. todo item?
                    # blocking execution for now.
                    self.report({'INFO'}, "Need axis lock for O and 180 degree angles.")

            angMeasStr = format(currMeasStor, '.2f')
            self.boxCo = draw_btn(angMeasStr, lockPts[1].coor2D, self.mouse,colorWhite,colorRed)
    
    if newMeasStor != None:
    
        # Generate list of selected geometry to see if Free was selected for
        # determining whether to run multi-selection transforms and for 
        # restoring selected items after object mode transforms.
        # Does not add Free to selected list in object mode and does not add 
        # Anchor to selected list in either mode.
        freeInSel = False
        selectedLs = []
        sel_backup = []
        Anchor = self.ref_pts[0]
        Free = []
        if self.refPtCnt == 2:
            Free = self.ref_pts[1]
        elif self.refPtCnt == 3:
            Free = self.ref_pts[2]

        if self.currEdType == "OBJECT":
            objLen = len(bpy.context.scene.objects)
            for i in range(objLen):
                if bpy.context.scene.objects[i].select:
                    sel_backup.append(i)
                if bpy.context.scene.objects[i].type == 'MESH':
                    if bpy.context.scene.objects[i].select:
                        if i == Free.objNum:
                            freeInSel = True
                            #print("freeInSel", freeInSel) # debug
                        elif i != Anchor.objNum:
                            selectedLs.append(i)

        elif self.currEdType == "EDIT_MESH":
            bm = bmesh.from_edit_mesh( bpy.context.edit_object.data )
            activMW = bpy.context.edit_object.matrix_world
            inverMW = bpy.context.edit_object.matrix_world.inverted()
            vertCnt = len(bm.verts)
            for v1 in range(vertCnt):
                if bm.verts[v1].select:
                    # todo: add float compare safeguard?
                    # compare ref_pts using vert index instead of coordinates?
                    vGlbCo = activMW * bm.verts[v1].co
                    if vGlbCo != Anchor.coor3D:
                        if vGlbCo == Free.coor3D:
                            freeInSel = True
                            #print("freeInSel", freeInSel) # debug
                        selectedLs.append(v1)

        if freeInSel == False:
            if self.currEdType == "OBJECT":
                selectedLs = [ Free.objNum ]
            elif self.currEdType == "EDIT_MESH":
                selectedLs = [ Free.vertInd ]
        #print("selectedLs",selectedLs) # debug


        # Onto Transformations...

        if self.transfMode == "SCALE":  # ObjMode only
            #print("scale!!!!")
            anchNum = self.ref_pts[0].objNum
            # store Anchor location for use after scale
            anchCo = self.ref_pts[0].coor3D
            scale_factor = newMeasStor / currMeasStor
            # todo: check on axis locks for scales to make sure they work right
            # todo: what happens if scale is zero?
            scaleLkMult, cnstrBlVals = (), ()
            if   self.axisLock ==  '': 
                scaleLkMult, cnstrBlVals = (scale_factor,scale_factor,scale_factor), (True,True,True)
            elif self.axisLock == 'X': 
                scaleLkMult, cnstrBlVals = (scale_factor,1,1), (True,False,False)
            elif self.axisLock == 'Y': 
                scaleLkMult, cnstrBlVals = (1,scale_factor,1), (False,True,False)
            elif self.axisLock == 'Z': 
                scaleLkMult, cnstrBlVals = (1,1,scale_factor), (False,False,True)
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects[anchNum].select = True
            bpy.ops.transform.resize(value=scaleLkMult, constraint_axis=cnstrBlVals)
            bpy.ops.object.select_all(action='DESELECT')
            self.ref_pts[0].update3D()
            # move scaled object so Anchor returns to where it was located
            # before scale was applied
            do_translation( "OBJECT", anchCo, self.ref_pts[0] )
            for obI in range(self.refPtCnt):
                self.ref_pts[obI].update3D()
                self.ref_pts[obI].set2D()
            # restore selected items (except Anchor)
            for ind in sel_backup:
                bpy.context.scene.objects[ind].select = True

        elif self.transfMode == "ROTATE":
            #print("curr angle",currMeasStor)
            #print("new angle",newMeasStor)

            # remove Free from selected list if in Edit Mode 
            # (Free is already removed if in ObjMode)
            if freeInSel:
                if self.currEdType == "EDIT_MESH":
                    selectedLs.remove(self.ref_pts[2].vertInd)

            # workaround for negative rotation angles
            while newMeasStor < 0:
                newMeasStor = newMeasStor + 360
            # fix for angles over 180 degrees
            if newMeasStor > 360:
                newMeasStor = newMeasStor % 360    
            self.rDat.angDiffD = newMeasStor - currMeasStor
            if newMeasStor > 180:
                self.rDat.newAngR = radians(180 - (newMeasStor % 180))
            else:
                self.rDat.newAngR = radians(newMeasStor) 
            self.rDat.angDiffR = radians(self.rDat.angDiffD)
            self.rDat.axisLk = self.axisLock
            freeNum = self.ref_pts[2].objNum
            freeVerIn = self.ref_pts[2].vertInd

            # rotate Free coordinate
            newFreeCoor = ()
            # workaround for straight lines rotations (0 & 180 degree angles)
            # have user pick rotate destination (tCo1 or tCo2) for Free point
            if self.btn_0_or_180:
                self.btn_0_or_180_mStor = newMeasStor
                mouseLoc = self.mouse
                tmpDat = findCorrectRot( self,True,self.ref_pts,self.rDat )
                # below fails if no axis lock set. todo, see if tmpDat check still needed
                if tmpDat != (): 
                    tCo1,tAngRad1,tCo2,tAngRad2 = tmpDat[0],tmpDat[1],tmpDat[2],tmpDat[3]
                    # if potential rotation points are same, rotate automatically
                    if AreFloatsEq(tCo1[0],tCo2[0]) and AreFloatsEq(tCo1[1],tCo2[1]) \
                    and AreFloatsEq(tCo1[2],tCo2[2]):
                        newFreeCoor, self.rDat.angDiffR = tCo1,tAngRad1
                    else:
                        region = bpy.context.region
                        for area in bpy.context.screen.areas:
                            if area.type == "VIEW_3D": break
                        rv3d = area.spaces[0].region_3d
                        tCo1_2D = location_3d_to_region_2d(region, rv3d, tCo1)
                        tCo2_2D = location_3d_to_region_2d(region, rv3d, tCo2)
                        ms_co1_dis = get_dist_2D(*tCo1_2D, *mouseLoc)
                        ms_co2_dis = get_dist_2D(*tCo2_2D, *mouseLoc)
                        # draw both buttons and wait for Lmouse click input
                        # (if btn_0_or_180_click is True)
                        if   ms_co1_dis < ms_co2_dis:
                            draw_pt_2D(tCo1_2D, colorGreen, 14)
                            draw_pt_2D(tCo2_2D, colorGrey)
                            if self.btn_0_or_180_click:
                                #print("Closer to Coor tCo1!")
                                newFreeCoor, self.rDat.angDiffR = tCo1,tAngRad1
                        elif ms_co2_dis < ms_co1_dis:
                            draw_pt_2D(tCo1_2D, colorGrey)
                            draw_pt_2D(tCo2_2D, colorGreen, 14)
                            if self.btn_0_or_180_click:
                                #print("Closer to Coor tCo2!")
                                newFreeCoor, self.rDat.angDiffR = tCo2,tAngRad2
                        else:
                            draw_pt_2D(tCo1_2D, colorGrey)
                            draw_pt_2D(tCo2_2D, colorGrey)
                        self.btn_0_or_180_click = False
                else:
                    #print("0 or 180 findCorrectRot failed!") # debug
                    self.btn_0_or_180_mStor = None
                    self.btn_0_or_180 = False
                    newFreeCoor = ()
            else:
                newFreeCoor, self.rDat.angDiffR = findCorrectRot(self, False,self.ref_pts,self.rDat )

            #print("angRadChng",self.rDat.angDiffR," angDegChng",degrees(self.rDat.angDiffR)) # debug
            
            if newFreeCoor != ():
                pivC = self.ref_pts[1].coor3D
                # reset 2 variables below (btn_0_or_180_mStor and btn_0_or_180)
                # just in case we're coming from btn_0_or_180 code loop
                # todo: find better place for this reset that doesn't break code
                self.btn_0_or_180_mStor = None
                self.btn_0_or_180 = False
                if self.currEdType == "OBJECT":
                    opsAxLock = ()
                    if   self.axisLock == 'X': opsAxLock = (1, 0, 0)
                    elif self.axisLock == 'Y': opsAxLock = (0, 1, 0)
                    elif self.axisLock == 'Z': opsAxLock = (0, 0, 1)
                    elif self.axisLock ==  '': opsAxLock = self.rDat.pivNorm

                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.scene.objects[freeNum].select = True
                    bpy.ops.transform.rotate(value=self.rDat.angDiffR, axis=opsAxLock, constraint_axis=(False, False, False))

                    bpy.ops.object.select_all(action='DESELECT')
                    self.ref_pts[2].update3D()
                    # Free is rotated first
                    do_translation( "OBJECT", newFreeCoor, self.ref_pts[2] )
                    
                    # Code below isn't pretty, but works for now... 
                    # Basically it takes object numbers stored in selectedLs and uses
                    # them to create vObjStorage objects, but using selected object's
                    # origins as "Free vertex" values instead of actual Free vertex.
                    # Then it rotates these "Free vertex" values around Anchor by 
                    # radian value stored in self.rDat.angDiffR
                    # todo: clean this up along with the rest of the selectedLs code
                    if freeInSel:
                        for ob in selectedLs:
                            newOb = vObjStorage( ob, -1, Vector([*bpy.context.scene.objects[ob].location]) )
                            lockPts = setAngLockPts(self.axisLock,[self.ref_pts[0],self.ref_pts[1],newOb] )
                            if (lockPts != []):
                                glbCo = lockPts[2].coor3D
                                tmpCo = getRotatedPoint(pivC,self.rDat.angDiffR,self.rDat,glbCo)
                                bpy.ops.object.select_all(action='DESELECT')
                                bpy.context.scene.objects[ob].select = True
                                bpy.ops.transform.rotate(value=self.rDat.angDiffR, axis=opsAxLock, constraint_axis=(False, False, False))
                                
                                bpy.ops.object.select_all(action='DESELECT')
                                newOb.coor3D = Vector([ *bpy.context.scene.objects[ob].location ])
                                do_translation( "OBJECT", tmpCo, newOb )
                    # restore selected items (except Anchor)
                    for ind in sel_backup:
                        bpy.context.scene.objects[ind].select = True

                elif self.currEdType == "EDIT_MESH":
                    bm.verts[freeVerIn].co = inverMW * Vector( newFreeCoor )
                    # if Free was in a selection, rotate the rest of the selection
                    if freeInSel:
                        newPt = vObjStorage()
                        for v2 in selectedLs:
                            newPt.coor3D = activMW * bm.verts[v2].co
                            lockPts = setAngLockPts(self.axisLock,[self.ref_pts[0],self.ref_pts[1],newPt] )
                            if (lockPts != []):
                                glbCo = lockPts[2].coor3D
                                # can't just send rDat because of findCorrectRot()
                                tmpCo = getRotatedPoint(pivC,self.rDat.angDiffR,self.rDat,glbCo)
                                bm.verts[v2].co = inverMW * tmpCo
                                    
                    bmesh.update_edit_mesh( bpy.context.scene.objects[freeNum].data )  # refresh data?
                
            # update 3D View and coordinates
            sceneRefresh( self.currEdType )
            
            for obI in range(self.refPtCnt):
                self.ref_pts[obI].update3D()
                self.ref_pts[obI].set2D()

        else:  # translate mode #
            newCoor = get_new_3D_coor(self,self.axisLock,self.ref_pts[0].coor3D, self.ref_pts[1].coor3D, newMeasStor)
            #print('newCoor',newCoor) #, self.ref_pts[1] ) # debug
            if self.currEdType == "OBJECT":

                # translate Free object and get store the translation change info
                chngCo = do_translation( "OBJECT", newCoor, self.ref_pts[1] )
                tmpCoLocal = bpy.context.scene.objects[self.ref_pts[1].objNum].data.vertices[self.ref_pts[1].vertInd].co
                tmpGlob = bpy.context.scene.objects[self.ref_pts[1].objNum].matrix_world * tmpCoLocal
                self.ref_pts[1].coor3D = tmpGlob
                self.ref_pts[1].set2D()

                # If more than 1 mesh object was selected and Free was
                # in selection set, translate other selected objects.
                # Use list returned from do_translation operation on
                # Free (chngCo) to do translations
                if freeInSel:
                    for ob in selectedLs:
                        coorChange = [0,0,0]
                        newOb = vObjStorage(ob, -1, Vector([*bpy.context.scene.objects[ob].location]))
                        for i in range(3):
                            coorChange[i] = newOb.coor3D[i] + chngCo[i]
                        do_translation( "OBJECT", coorChange, newOb )
                # restore selected items (except Anchor)
                for ind in sel_backup:
                    bpy.context.scene.objects[ind].select = True

            elif self.currEdType == "EDIT_MESH":
                bm = bmesh.from_edit_mesh( bpy.context.edit_object.data )
                inverMW = bpy.context.edit_object.matrix_world.inverted()
                locCo = inverMW * Vector(newCoor)
                newVertLoc = do_translation( "EDIT_MESH", locCo, self.ref_pts[1],selectedLs,freeInSel )
                self.ref_pts[1].coor3D = newVertLoc
                self.ref_pts[1].set2D()

        newMeasStor = None
        # make sure transforms didn't cause points to overlap
        PtA = self.ref_pts[0].coor3D
        if self.refPtCnt == 2:
            PtB = self.ref_pts[1].coor3D
            if AreFloatsEq(PtA[0],PtB[0]) and AreFloatsEq(PtA[1],PtB[1]) and AreFloatsEq(PtA[2],PtB[2]):
                self.report({'ERROR'}, 'Free and Anchor share same location.')
                self.exitCheck = True
        elif self.refPtCnt == 3:
            PtC = self.ref_pts[2].coor3D
            if AreFloatsEq(PtA[0],PtC[0]) and AreFloatsEq(PtA[1],PtC[1]) and AreFloatsEq(PtA[2],PtC[2]):
                self.report({'ERROR'}, 'Free and Anchor share same location.')
                self.exitCheck = True


class xOffsets(bpy.types.Operator):
    """Select vertices with the mouse"""
    bl_idname = "view3d.xoffsets_main"
    bl_label = "Exact Offsets"
    
    # Only launch Add-On when active object is a MESH and Blender
    # is in OBJECT mode or EDIT_MESH mode.
    @classmethod
    def poll(self, context):
        if context.mode == 'OBJECT' or context.mode == 'EDIT_MESH':
            return bpy.context.scene.objects.active.type == 'MESH'
        else:
            return False

    def modal(self, context, event):
        context.area.tag_redraw()
        self.currEdType = context.mode

        if event.type in {'A', 'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'NUMPAD_1', 'NUMPAD_2', 'NUMPAD_3', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_7', 'NUMPAD_8', 'NUMPAD_9', 'NUMPAD_5', 'TAB'}:
            return {'PASS_THROUGH'}

        if event.type == 'MOUSEMOVE':
            self.mouse = (event.mouse_region_x, event.mouse_region_y)

        if event.type == 'RIGHTMOUSE':
            if self.LmousePressed:
                bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
                return {'CANCELLED'}
            else:
                return {'PASS_THROUGH'}

        if event.type == 'LEFTMOUSE':
            self.LmousePressed = event.value == 'PRESS'

        if event.type == 'LEFTMOUSE' and event.value == 'RELEASE':
            click_loc = (event.mouse_region_x, event.mouse_region_y)
            if self.drawBtn and point_inside_loop(self.boxCo,click_loc):
                self.btn_clicked = True
            # need to skip drawing new_angle buttons until after new measure
            # entered. wait until btn_0_or_180_mStor set thru btn_clicked code
            elif self.btn_0_or_180_mStor != None:
                self.btn_0_or_180_click = True
            else:
                found_pt = find_all( click_loc )
                if found_pt != []:
                    # make sure selected point isn't already in ref_pts
                    dupeFound = False
                    dupeRef = -1
                    if self.ref_pts != []:
                        for rp in range(self.refPtCnt):
                            if [*self.ref_pts[rp].coor3D] == [*found_pt.coor3D]:
                                dupeFound = True
                                dupeRef = self.ref_pts[rp].refInd
                                break
                    if dupeFound: # remove the found ref pt
                        #print('dupeRef',dupeRef) # debug
                        self.transfMode = ""
                        self.axisLock = ''
                        self.btn_0_or_180 = False
                        # hackery or smart, you decide...
                        if dupeRef != self.refPtCnt - 1:
                            ind = [0,1,2][:self.refPtCnt]
                            ind.remove(dupeRef)
                            for i in range(len(ind)):
                                self.ref_pts[i] = vObjStorage(*self.ref_pts[ind[i]].datOut() )
                                self.ref_pts[i].refInd = i
                        self.refPtCnt -= 1
        
                    else:
                        if self.refPtCnt < 3:
                            self.ref_pts[self.refPtCnt] = found_pt
                            self.ref_pts[self.refPtCnt].refInd = self.refPtCnt
                            ''' Debug code 
                            ptFndStr = str(found_pt.coor3D)
                            ptFndStr = ptFndStr.replace("<Vector ","Vector(")
                            ptFndStr = ptFndStr.replace(">",")")
                            print("Ref_pt_" + str(self.refPtCnt) +' =',ptFndStr) # debug
                            '''
                            #print( [i for i in found_pt.coor3D] )
                            self.refPtCnt += 1

        if event.type == 'C' and event.value == 'PRESS':
            #print("Pressed C!\n") # debug
            if self.canLock:
                self.axisLock = ''
                self.btn_0_or_180_mStor = None
                self.btn_0_or_180 = False

        if event.type == 'X' and event.value == 'PRESS':
            #print("Pressed X!\n") # debug
            if self.canLock:
                self.axisLock = 'X'
                self.btn_0_or_180_mStor = None
                self.btn_0_or_180 = False

        if event.type == 'Y' and event.value == 'PRESS':
            #print("Pressed Y!\n") # debug
            if self.canLock:
                self.axisLock = 'Y'
                self.btn_0_or_180_mStor = None
                self.btn_0_or_180 = False

        if event.type == 'Z' and event.value == 'PRESS':
            #print("Pressed Z!\n") # debug
            if self.canLock:
                self.axisLock = 'Z'
                self.btn_0_or_180_mStor = None
                self.btn_0_or_180 = False

        if event.type == 'ESC':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            #print("\n\n\n  Add-On Exited!\n") # debug
            return {'CANCELLED'}
            
        if self.exitCheck:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            self.LmousePressed = False
            self.currEdType = ""  # current Blender Editor Type
            self.transfMode = ""  # transform mode
            self.rDat = rotationData()
            self.mouse = (-5000,-5000)
            self.ref_pts = [ [],[],[] ]
            self.refPtCnt = 0
            self.canLock = False  # can axis locks be applied?
            self.axisLock = ''  # default: no axis lock
            self.boxCo = []
            self.drawBtn = False
            self.btn_clicked = False
            self.btn_0_or_180 = False
            self.btn_0_or_180_click = False
            self.btn_0_or_180_mStor = None
            self.exitCheck = False

            #print("Exact Offsets started!") # debug
            # refresh the viewport
            sceneRefresh(context.mode)

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}


def register():
    bpy.utils.register_class(xOffsets)
    bpy.utils.register_class(changeInputPanel)

def unregister():
    bpy.utils.unregister_class(xOffsets)
    bpy.utils.unregister_class(changeInputPanel)

if __name__ == "__main__":
    register()
