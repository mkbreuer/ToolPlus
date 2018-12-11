# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Copyright (C) 2014-2017 script authors.
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


import os, sys, time

import bpy

# Trick to pass though some log messages (filtered in stdout parser from calling script).
def log(s):
    print("[log]" + s)

def log_object(o):
    print("[log]" + repr(o))
    
def generateThumb(objFile, size):
    log("### START THUMBNAIL GEN ############################")
    log("Start generating: " + objFile)
    
    log("Import mesh")

    bpy.ops.import_scene.obj(filepath = objFile)

    # Give all imported objects one name (tricky ...)
    for obj in bpy.context.selected_objects:
        obj.name = "OBJ"
        
    log("Prepare mesh")
        
    # Join them to single mesh.
    OBJ = bpy.data.objects["OBJ"]
    bpy.context.scene.objects.active = bpy.data.objects["OBJ"]
    bpy.ops.object.join()
    
    # Apply location.
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    
    # Determine OBJ dimensions.
    maxDimension = 1.0
    scaleFactor = maxDimension / max(OBJ.dimensions)

    # Scale uniformly.
    OBJ.scale = (scaleFactor,scaleFactor,scaleFactor)
    
    # Center pivot.
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')

    # Move object to origin.
    bpy.ops.object.location_clear()
    
    # Move mesh up by half of Z dimension
    dimX = OBJ.dimensions[0]/2
    dimY = OBJ.dimensions[1]/2
    dimZ = OBJ.dimensions[2]/2
    OBJ.location = (0,0,dimZ)
    
    # Make smooth.
    bpy.ops.object.shade_smooth()
    
    log("Prepare camera")
    
    # Manual adjustments to CAMERAS.
    CAMERAS = bpy.data.objects["cameras"]
    scalevalue = 1
    camScale = 0.5+(dimX*scalevalue+dimY*scalevalue+dimZ*scalevalue)/3
    CAMERAS.scale = (camScale,camScale,camScale)
    CAMERAS.location = (0,0,dimZ)
    
    log("Set material")
    
    # Assign scene specific material to it, previously 
    # removing all material slots.    
    for ob in bpy.context.selected_editable_objects:
        ob.active_material_index = 0
    for _ in range(len(ob.material_slots)):
        bpy.ops.object.material_slot_remove({'object': ob})
    bpy.context.active_object.active_material = bpy.data.materials["material"]
    
    log("Prepare scene")
    
    # Set output filename.
    bpy.context.scene.render.filepath = os.path.splitext(objFile)[0]
    
    # Configure output size.
    bpy.context.scene.render.resolution_x = int(size)
    bpy.context.scene.render.resolution_y = int(size)
    
    log("Render")
    
    # Render thumbnail
    bpy.ops.render.render(write_still = True)

    log("### COMPLETED THUMBNAIL GEN ############################")

def generate():
    objFile = ""
    size = 128
    
    for arg in sys.argv:
        if arg.startswith("obj:"):
            objFile = arg[4:]
        if arg.startswith("size:"):
            size = arg[5:]

    generateThumb(objFile, size)   
