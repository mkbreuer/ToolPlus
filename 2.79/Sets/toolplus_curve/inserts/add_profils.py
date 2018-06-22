# ##### BEGIN GPL LICENSE BLOCK #####
#
#
#  This program is free software; you can redistribute it and / or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
# Contributed to by
# Pontiac, Fourmadmen, varkenvarken, tuga3d, meta-androcto, metalliandy, dreampainter & cotejrp1, mkbreuer #


bl_info = {
    "name": "Edge Profiles",
    "author": "mkbreuer (MKB) / Profils: Gert De Roost",
    "version": (0, 1, 0),
    "blender": (2, 7, 9),
    "location": "3D View",
    "description": "add profils as mesh or bezier curve",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/",
    "tracker_url": "",
    "category": "Add Mesh"}


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *


import bmesh
import math
from mathutils import *
from bpy.props import (BoolProperty, BoolVectorProperty, FloatProperty, FloatVectorProperty)


def add_bevel_1(width, height, depth):
    verts = [(-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, -1.0, 0.0), (1.0, -0.3751969337463379, 0.0), (-0.3491460382938385, 1.0, 2.0809221012996204e-08)]
    #edge = [[1, 0], [4, 3], [3, 2], [1, 4], [2, 0]]
    faces = [(4, 1, 0, 2, 3)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_bevel_2(width, height, depth):
    verts = [(1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, -0.5, 0.0), (-0.5000003576278687, 1.0, 0.0)]
    #edge = [[0, 1], [2, 1], [2, 4], [4, 3], [3, 0]]
    faces = [(3, 0, 1, 2, 4)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_car(width, height, depth):
    verts = [(0.318389892578125, 1.0, 0.0), (-1.0, -0.5971899628639221, 0.0), (-1.18287193775177, -0.6410936117172241, 0.0), (-1.3258801698684692, -0.7632342576980591, 0.0), (-1.397850751876831, -0.9369865655899048, 0.0), (-1.3830950260162354, -1.124475121498108, 0.0), (-1.2848296165466309, -1.2848297357559204, 0.0), (-1.124475121498108, -1.3830950260162354, 0.0), (-0.9369868040084839, -1.397850751876831, 0.0), (-0.7632343173027039, -1.3258802890777588, 0.0), (-0.6410936117172241, -1.18287193775177, 0.0), (-0.5971899628639221, -0.9999999403953552, 0.0), (0.5971899628639221, -1.0, 0.0), (0.6410936117172241, -1.18287193775177, 0.0), (0.7632342576980591, -1.3258801698684692, 0.0), (0.9369865655899048, -1.397850751876831, 0.0), (1.124475121498108, -1.3830950260162354, 0.0), (1.2848297357559204, -1.2848296165466309, 0.0), (1.3830950260162354, -1.124475121498108, 0.0), (1.397850751876831, -0.9369866251945496, 0.0), (1.3258802890777588, -0.7632343173027039, 0.0), (1.18287193775177, -0.6410936117172241, 0.0), (0.9999999403953552, -0.5971899628639221, 0.0), (-0.34839022159576416, 1.0, 0.0), (-0.3564126491546631, 0.8980657458305359, 0.0), (-0.38028228282928467, 0.798641562461853, 0.0), (-0.41941142082214355, 0.7041753530502319, 0.0), (-0.47283661365509033, 0.6169934272766113, 0.0), (-0.5392423868179321, 0.5392422676086426, 0.0), (-0.6169934272766113, 0.47283655405044556, 0.0), (-0.7041752338409424, 0.4194115400314331, 0.0), (-0.7986413836479187, 0.38028228282928467, 0.0), (-0.8980656862258911, 0.3564126491546631, 0.0), (-0.9999999403953552, 0.34839022159576416, 0.0), (1.0, 0.05357992649078369, 0.0), (1.187248945236206, 0.13114100694656372, 0.0), (1.2648100852966309, 0.3183899223804474, 0.0), (1.187248945236206, 0.5056389570236206, 0.0), (1.0, 0.5831999778747559, 0.0), (0.812751054763794, 0.5056389570236206, 0.0)]
   #edge = [[11, 10], [10, 9], [9, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [22, 21], [21, 20], [20, 19], [19, 18], [18, 17], [17, 16], [16, 15], [15, 14], [14, 13], [13, 12], [12, 11], [0, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 1], [0, 39], [39, 38], [38, 37], [37, 36], [36, 35], [35, 34], [34, 22]]
    faces = [(21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 0, 39, 38, 37, 36, 35, 34, 22)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_cornice(width, height, depth):
    verts = [(-1.0, 1.0, 0.0), (1.0, 0.5895997285842896, 0.0), (0.979913592338562, 0.7164203524589539, 0.0), (0.9216204881668091, 0.8308269381523132, 0.0), (0.8308268785476685, 0.9216205477714539, 0.0), (0.7164204716682434, 0.979913592338562, 0.0), (0.5895997881889343, 1.0, 0.0), (-1.0, -0.5895997285842896, 0.0), (-0.979913592338562, -0.7164203524589539, 0.0), (-0.9216204881668091, -0.8308269381523132, 0.0), (-0.8308268785476685, -0.9216205477714539, 0.0), (-0.7164204716682434, -0.979913592338562, 0.0), (-0.5895997881889343, -1.0, 0.0), (1.0, 0.4883997440338135, 0.0), (0.5400593280792236, 0.4155522584915161, 0.0), (0.12514060735702515, 0.20414066314697266, 0.0), (-0.2041407823562622, -0.12514078617095947, 0.0), (-0.4155522584915161, -0.5400589108467102, 0.0), (-0.4883997440338135, -0.9999998807907104, 0.0)]
    #edge = [[0, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [12, 11], [11, 10], [10, 9], [9, 8], [8, 7], [7, 0], [1, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 12]]
    faces = [(11, 10, 9, 8, 7, 0, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 12)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_double(width, height, depth):
    verts = [(-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (0.25, 1.0, 0.0), (0.2867075800895691, 0.7682373523712158, 0.0), (0.39323723316192627, 0.5591610670089722, 0.0), (0.5591611862182617, 0.39323723316192627, 0.0), (0.7682371139526367, 0.28670763969421387, 0.0), (0.9999999403953552, 0.25, 0.0), (0.25, -1.0, 0.0), (0.2867075800895691, -0.7682373523712158, 0.0), (0.39323723316192627, -0.5591610670089722, 0.0), (0.5591611862182617, -0.39323723316192627, 0.0), (0.7682371139526367, -0.28670763969421387, 0.0), (0.9999999403953552, -0.25, 0.0)]
    #edge = [[1, 0], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 7]]
    faces = [(2, 1, 0, 8, 9, 10, 11, 12, 13, 7, 6, 5, 4, 3)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_inlay_1(width, height, depth):
    verts = [(1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (-0.25, 1.0, 0.0), (-0.1888207197189331, 0.6137288808822632, 0.0), (-0.011271238327026367, 0.2652684450149536, 0.0), (0.26526856422424316, -0.011271357536315918, 0.0), (0.6137285232543945, -0.18882060050964355, 0.0), (0.9999998807907104, -0.25, 0.0)]
   #edge = [[0, 1], [2, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]]
    faces = [(8, 0, 1, 2, 3, 4, 5, 6, 7)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_inlay_2(width, height, depth):
    verts = [(-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.04894345998764038, 0.6909831166267395, 0.0), (0.19098299741744995, 0.4122147560119629, 0.0), (0.41221487522125244, 0.19098293781280518, 0.0), (0.6909828186035156, 0.048943519592285156, 0.0), (0.9999999403953552, 0.0, 0.0), (1.0, -0.5999999642372131, 0.0), (0.5999999046325684, -1.0, 3.552713678800501e-15)]
   #edge = [[1, 0], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 9], [9, 8], [8, 7]])
    faces = [(2, 1, 0, 9, 8, 7, 6, 5, 4, 3)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_inlay_3(width, height, depth):
    verts = [(-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (-0.11880004405975342, 1.0, 0.0), (-0.0640420913696289, 0.6542719006538391, 0.0), (0.09487175941467285, 0.34238582849502563, 0.0), (0.3423859477043152, 0.09487169981002808, 0.0), (0.6542716026306152, -0.0640420913696289, 0.0), (0.707249104976654, -0.07243290543556213, 0.0), (0.8007224798202515, -0.10118907690048218, 0.0), (0.882461667060852, -0.15488168597221375, 0.0), (0.9459754228591919, -0.22924678027629852, 0.0), (0.9862202405929565, -0.3183790445327759, 0.0), (0.9999998807907104, -0.4152000844478607, 0.0), (0.9999999403953552, -0.7647900581359863, 0.0), (0.988487958908081, -0.8374738693237305, 0.0), (0.9550788402557373, -0.9030429720878601, 0.0), (0.9030429124832153, -0.9550788402557373, 0.0), (0.8374739289283752, -0.988487958908081, 0.0), (0.7647900581359863, -0.9999999403953552, 0.0)]
   #edge = [[1, 0], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [12, 11], [11, 10], [10, 9], [9, 8], [8, 7], [7, 6], [0, 18], [18, 17], [17, 16], [16, 15], [15, 14], [14, 13], [13, 12]]
    faces = [(11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 18, 17, 16, 15, 14, 13, 12)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_norman(width, height, depth):
    verts = [(0.4435911178588867, 0.7137556076049805, 0.0), (0.6942288875579834, 0.5462849140167236, 0.0), (0.8616995811462402, 0.29564735293388367, 0.0), (0.9205076694488525, 1.4901161193847656e-08, 0.0), (0.8616998195648193, -0.2956472635269165, 0.0), (0.6942288875579834, -0.5462850332260132, 0.0), (0.4435913562774658, -0.7137556076049805, 0.0), (0.12949275970458984, -0.7725633382797241, 0.0), (0.12949275970458984, 0.7725633382797241, 0.0), (0.12949275970458984, 0.9999998807907104, 0.0), (-0.9205074310302734, 1.0, 0.0), (-0.9205074310302734, -1.0, 0.0), (0.12949275970458984, -1.0, 0.0)]
   #edge = [[9, 8], [0, 8], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [12, 7], [10, 9], [10, 11], [12, 11]]
    faces = [(7, 12, 11, 10, 9, 8, 0, 1, 2, 3, 4, 5, 6)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_nose_1(width, height, depth):
    verts = [(-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, 0.6000000238418579, 0.0), (0.9804226160049438, 0.7236067652702332, 0.0), (0.923606812953949, 0.8351141214370728, 0.0), (0.835114061832428, 0.9236068725585938, 0.0), (0.7236068844795227, 0.9804226160049438, 0.0), (0.6000000834465027, 1.0, 0.0), (1.0, -0.6000000238418579, 0.0), (0.9804226160049438, -0.7236067652702332, 0.0), (0.923606812953949, -0.8351141214370728, 0.0), (0.835114061832428, -0.9236068725585938, 0.0), (0.7236068844795227, -0.9804226160049438, 0.0), (0.6000000834465027, -1.0, 0.0)]
   #edge = [[1, 0], [1, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [0, 13], [13, 12], [12, 11], [11, 10], [10, 9], [9, 8], [8, 2]]
    faces = [(7, 1, 0, 13, 12, 11, 10, 9, 8, 2, 3, 4, 5, 6)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_nose_2(width, height, depth):
    verts = [(-1.0, -1.0, 0.0), (1.0, 0.010400176048278809, 0.0), (-1.0, 1.0, 0.0), (1.0, -0.010400176048278809, 0.0), (0.9505475163459778, 0.301830530166626, 0.0), (0.8070307374000549, 0.5834981203079224, 0.0), (0.5834980010986328, 0.8070307970046997, 0.0), (0.30183082818984985, 0.950547456741333, 0.0), (-0.01040009967982769, 1.0, 0.0), (0.9505475163459778, -0.301830530166626, 0.0), (0.8070307374000549, -0.5834981203079224, 0.0), (0.5834980010986328, -0.8070307970046997, 0.0), (0.30183082818984985, -0.950547456741333, 0.0), (-0.01040009967982769, -1.0, 0.0)]
   #edge= [[10, 9], [2, 0], [2, 8], [11, 10], [8, 7], [7, 6], [12, 11], [6, 5], [5, 4], [13, 12], [4, 3], [0, 13], [9, 1], [1, 3]]
    faces = [(4, 5, 6, 7, 8, 2, 0, 13, 12, 11, 10, 9, 1, 3)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_quad(width, height, depth):
    verts = [(1.0, 0.5, 0.0), (1.0, -0.5, 0.0), (-1.0, -0.5, 0.0), (-0.5, 1.0, 0.0), (-0.5244717597961426, 0.8454915285110474, 0.0), (-0.5954915285110474, 0.7061073780059814, 0.0), (-0.7061074376106262, 0.5954914689064026, 0.0), (-0.8454914093017578, 0.5244717597961426, 0.0), (-0.9999999403953552, 0.5, 0.0), (-0.8454915285110474, -0.5244717597961426, 0.0), (-0.7061073780059814, -0.5954915285110474, 0.0), (-0.5954914689064026, -0.7061074376106262, 0.0), (-0.5244717597961426, -0.8454914093017578, 0.0), (-0.5, -0.9999999403953552, 0.0), (0.8454915285110474, -0.5244717597961426, 0.0), (0.7061073780059814, -0.5954915285110474, 0.0), (0.5954914689064026, -0.7061074376106262, 0.0), (0.5244717597961426, -0.8454914093017578, 0.0), (0.5, -0.9999999403953552, 0.0), (0.8454915285110474, 0.5244717597961426, 0.0), (0.7061073780059814, 0.5954915285110474, 0.0), (0.5954914689064026, 0.7061074376106262, 0.0), (0.5244717597961426, 0.8454914093017578, 0.0), (0.5, 0.9999999403953552, 0.0)]
   #edge = [[16, 17], [11, 12], [21, 22], [10, 11], [3, 4], [14, 15], [4, 5], [9, 10], [5, 6], [19, 20], [6, 7], [2, 9], [7, 8], [15, 16], [8, 2], [1, 14], [12, 13], [20, 21], [0, 19], [17, 18], [18, 13], [1, 0], [22, 23], [23, 3]]
    faces = [(4, 5, 6, 7, 8, 2, 9, 10, 11, 12, 13, 18, 17, 16, 15, 14, 1, 0, 19, 20, 21, 22, 23, 3)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_round_50(width, height, depth):
    verts = [(1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, 0.25, 0.0), (0.9632923603057861, 0.48176270723342896, 0.0), (0.8567626476287842, 0.6908389329910278, 0.0), (0.6908390522003174, 0.8567626476287842, 0.0), (0.48176267743110657, 0.9632924199104309, 0.0), (0.24999982118606567, 1.0, 0.0)]
   #edges = [[0, 1], [2, 1], [2, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 0]]
    faces = [(3, 0, 1, 2, 8, 7, 6, 5, 4)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_round_75(width, height, depth):
    verts = [(1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, -0.5, 0.0), (0.9265847206115723, -0.03647461533546448, 0.0), (0.7135252952575684, 0.38167792558670044, 0.0), (0.38167804479599, 0.7135252952575684, 0.0), (-0.036474645137786865, 0.9265848398208618, 0.0), (-0.5000003576278687, 1.0, 0.0)]
   #edge = [[0, 1], [2, 1], [2, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 0]]
    faces = [(3, 0, 1, 2, 8, 7, 6, 5, 4)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_round_100(width, height, depth):
    verts = [(1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, -1.0, 0.0), (0.9021129608154297, -0.3819658160209656, 0.0), (0.6180341243743896, 0.17557036876678467, 0.0), (0.17557036876678467, 0.6180340051651001, 0.0), (-0.38196635246276855, 0.9021131992340088, 0.0), (-0.9999995827674866, 1.0, 0.0)]
   #edge = [[0, 1], [2, 1], [2, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 0]]
    faces = [(3, 0, 1, 2, 8, 7, 6, 5, 4)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_round_up(width, height, depth):
    verts = [(0.5483438968658447, -1.0005161762237549, -1.8124410416930914e-08), (-0.9516561031341553, -1.0005161762237549, -1.8124410416930914e-08), (-0.9516561031341553, 0.9994838237762451, -1.8124410416930914e-08), (0.5483438968658447, -0.5005161762237549, -1.8124410416930914e-08), (0.07300214469432831, 0.9994838237762451, -1.8124410416930914e-08), (0.07013797014951706, 1.0005161762237549, 1.8124410416930914e-08), (0.7626547813415527, -0.2912794351577759, 1.4395173053571853e-08), (0.9097340106964111, -0.014108240604400635, 1.8124410416930914e-08), (0.9516561031341553, 0.26670801639556885, 1.8124410416930914e-08), (0.8862746953964233, 0.5475244522094727, 1.8124410416930914e-08), (0.7000843286514282, 0.7855889797210693, 1.8124410416930914e-08), (0.4214304983615875, 0.9446582794189453, 1.8124410416930914e-08)]
   #edge = [[0, 1], [2, 1], [2, 4], [3, 0], [6, 3], [4, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [11, 5]]
    faces = [(3, 0, 1, 2, 4, 5, 11, 10, 9, 8, 7, 6)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_shoe(width, height, depth):
    verts = [(1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0003929138183594, -0.9976814389228821, 5.032443004893139e-05), (1.0003929138183594, -0.7371903657913208, 5.032443004893139e-05), (0.9147418737411499, -0.30456674098968506, 5.032443004893139e-05), (0.6661726236343384, 0.08570900559425354, 5.032443004893139e-05), (0.2790168523788452, 0.39543354511260986, 5.032443004893139e-05), (-0.20882701873779297, 0.5942887663841248, 5.032443004893139e-05), (-0.5, 0.6628096699714661, 5.032443004893139e-05), (-0.5, 1.0, -1.504686224507168e-07)]
   #edge = [[0, 1], [2, 1], [9, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [9, 10], [2, 10], [0, 3]]
    faces = [(3, 0, 1, 2, 10, 9, 8, 7, 6, 5, 4)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces

def add_smooth(width, height, depth):
    verts = [(0.9736814498901367, -0.9802608489990234, 0.0), (-1.0263185501098633, -0.9802608489990234, 0.0), (-1.0263185501098633, 1.0197391510009766, 0.0), (-0.010030746459960938, 0.03312969207763672, 1.2079226507921703e-13), (-1.010030746459961, 1.0199980735778809, 1.0658141036401503e-13), (-0.9610872864723206, 0.7241128087043762, 1.0727693961019164e-13), (-0.819047749042511, 0.4453444480895996, 1.0929543945228937e-13), (-0.5978158712387085, 0.2241126298904419, 1.1243933437316347e-13), (-0.3190479278564453, 0.08207321166992188, 1.1640086680989037e-13), (-0.0100308358669281, 0.03312969207763672, 1.2079226507921703e-13), (0.0010576248168945312, 0.022419452667236328, 1.0658141036401503e-13), (0.9740920066833496, -0.9775805473327637, 1.2079226507921703e-13), (0.9521141052246094, -0.6685634851455688, 1.2009673583304042e-13), (0.8100746870040894, -0.38979536294937134, 1.180782359909427e-13), (0.5888428092002869, -0.16856354475021362, 1.14934334293805e-13), (0.31007444858551025, -0.026523947715759277, 1.1097280185707811e-13), (0.0010578334331512451, 0.022419452667236328, 1.0658141036401503e-13)]
   #edge = [[0, 1], [2, 1], [2, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 3], [10, 16], [16, 15], [15, 14], [14, 13], [13, 12], [12, 11], [0, 11], [3, 10]]
    faces = [(11, 0, 1, 2, 4, 5, 6, 7, 8, 9, 3, 10, 16, 15, 14, 13, 12)]
    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height
    return verts, faces



class VIEW3D_TP_EDGE_PROFIL(bpy.types.Operator):

    bl_idname = "tp_ops.edge_profil"
    bl_label = "Edge Profiles"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    profil_list = [ ("profil_01"  ,"Bevel_1"   ,"" ,''   ,1), 
                    ("profil_02"  ,"Bevel_2"   ,"" ,''   ,2), 
                    ("profil_03"  ,"Car"       ,"" ,''   ,3), 
                    ("profil_04"  ,"Cornice"   ,"" ,''   ,4),
                    ("profil_05"  ,"Double"    ,"" ,''   ,5),                   
                    ("profil_06"  ,"Inlay_1"   ,"" ,''   ,6),                   
                    ("profil_07"  ,"Inlay_2"   ,"" ,''   ,7),                   
                    ("profil_08"  ,"Inlay_3"   ,"" ,''   ,8),                  
                    ("profil_09"  ,"Norman"    ,"" ,''   ,9),                  
                    ("profil_10"  ,"Nose_1"    ,"" ,''   ,10),                  
                    ("profil_11"  ,"Nose_2"    ,"" ,''   ,11),                  
                    ("profil_12"  ,"Quad"      ,"" ,''   ,12),                  
                    ("profil_13"  ,"Round_50"  ,"" ,''   ,13),                  
                    ("profil_14"  ,"Round_75"  ,"" ,''   ,14),                  
                    ("profil_15"  ,"Round_100" ,"" ,''   ,15),                  
                    ("profil_16"  ,"Round_Up"  ,"" ,''   ,16),                  
                    ("profil_17"  ,"Shoe"      ,"" ,''   ,17),                  
                    ("profil_18"  ,"Smooth"    ,"" ,''   ,18)]                  
    
    profil_typ = bpy.props.EnumProperty(name = "Profil Type", default = "profil_01", items = profil_list)

    convert_to_curve = BoolProperty(name="Convert to Curve", default=True)

    width = FloatProperty( name="Width X", description="Box Width", min=0.01, max=100.0, default=1.0,)
    height = FloatProperty(name="Height", description="Box Height", min=0.01, max=100.0, default=1.0,)
    depth = FloatProperty(name="Depth Y", description="Box Depth", min=0.01, max=100.0, default=1.0,)
    layers = BoolVectorProperty(name="Layers", description="Object Layers", size=20, options={'HIDDEN', 'SKIP_SAVE'})

    # generic transform props
    view_align = BoolProperty(name="Align to View", default=False)
    location = FloatVectorProperty(name="Location", subtype='TRANSLATION')
    rotation = FloatVectorProperty(name="Rotation", subtype='EULER')


    def draw(self, context):      
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(1)             
      
        box.separator()
      
        row = box.row(1)  
        row.prop(self, 'profil_typ')  
        row.prop(self, 'convert_to_curve', "", icon="IPO_BEZIER")  
     
        box.separator()
     
        row = box.column(1)  
      
        row.prop(self, 'width')  
        row.prop(self, 'depth')   

        row.separator()
        row.prop(self, 'view_align')  
        
        row.separator()

        row.prop(self, 'location')  

        row.separator()

        row.prop(self, 'rotation')  

        row.separator()


    def execute(self, context):
        scene = bpy.context.scene        
        
        if self.profil_typ == "profil_01":            
            verts_loc, faces = add_bevel_1(self.width, self.height, self.depth)            
            mesh = bpy.data.meshes.new(name="Bevel_1")

        if self.profil_typ == "profil_02":
            verts_loc, faces = add_bevel_1(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Bevel_2")

        if self.profil_typ == "profil_03":
            verts_loc, faces = add_car(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Car")

        if self.profil_typ == "profil_04":
            verts_loc, faces = add_cornice(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Cornice")

        if self.profil_typ == "profil_05":
            verts_loc, faces = add_double(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Double")

        if self.profil_typ == "profil_06":
            verts_loc, faces = add_inlay_1(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Inlay_1")

        if self.profil_typ == "profil_07":
            verts_loc, faces = add_inlay_2(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Inlay_2")

        if self.profil_typ == "profil_08":
            verts_loc, faces = add_inlay_3(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Inlay_3")

        if self.profil_typ == "profil_09":
            verts_loc, faces = add_norman(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Norman")

        if self.profil_typ == "profil_10":
            verts_loc, faces = add_nose_1(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="nose_1")

        if self.profil_typ == "profil_11":
            verts_loc, faces = add_nose_1(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="nose_2")

        if self.profil_typ == "profil_12":
            verts_loc, faces = add_quad(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Quad")

        if self.profil_typ == "profil_13":
            verts_loc, faces = add_round_50(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="round_50")

        if self.profil_typ == "profil_14":
            verts_loc, faces = add_round_75(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Round_75")

        if self.profil_typ == "profil_15":
            verts_loc, faces = add_round_100(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="Round_100")

        if self.profil_typ == "profil_16":
            verts_loc, faces = add_round_up(self.width, self.height, self.depth)   
            mesh = bpy.data.meshes.new(name="round_up")

        if self.profil_typ == "profil_17":
            verts_loc, faces = add_shoe(self.width, self.height, self.depth)  
            mesh = bpy.data.meshes.new(name="shoe")

        if self.profil_typ == "profil_18":
            verts_loc, faces = add_smooth(self.width, self.height, self.depth)  
            mesh = bpy.data.meshes.new(name="Smooth")


        bm = bmesh.new()

        for v_co in verts_loc:
            bm.verts.new(v_co)

        bm.verts.ensure_lookup_table()
        for f_idx in faces:
            bm.faces.new([bm.verts[i] for i in f_idx])

        bm.to_mesh(mesh)
        mesh.update()

        # add the mesh as an object into the scene with this utility module
        from bpy_extras import object_utils
        object_utils.object_data_add(context, mesh, operator=self)


        if self.convert_to_curve == True:
            bpy.ops.object.convert(target='CURVE')

            if context.mode == 'OBJECT':
                bpy.ops.object.mode_set(mode='EDIT')  
                bpy.ops.curve.spline_type_set(type='BEZIER')
                bpy.context.object.data.show_normal_face = True
                bpy.context.scene.tool_settings.normal_size = 0.25            
                bpy.ops.object.mode_set(mode='OBJECT') 

        return {'FINISHED'}


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()