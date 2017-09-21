__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



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
#

#bl_info = {
#    "name": "Distribute Objects",
#    "author": "Oscurart, CodemanX",
#    "version": (3,1),
#    "location": "View3D > Tools > Oscurart Tools",
#    "description": "Space Objects between there Origins",
#    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Oscurart_Tools",
#    "category": "User Changed"}



import bpy
from bpy import *


## ------------------------------------ SELECTION --------------------------------------
bpy.selection_osc=[]

def select_osc():
    if bpy.context.mode == "OBJECT":
        obj = bpy.context.object
        sel = len(bpy.context.selected_objects)

        if sel == 0:
            bpy.selection_osc=[]
        else:
            if sel == 1:
                bpy.selection_osc=[]
                bpy.selection_osc.append(obj)
            elif sel > len(bpy.selection_osc):
                for sobj in bpy.context.selected_objects:
                    if (sobj in bpy.selection_osc) == False:
                        bpy.selection_osc.append(sobj)

            elif sel < len(bpy.selection_osc):
                for it in bpy.selection_osc:
                    if (it in bpy.context.selected_objects) == False:
                        bpy.selection_osc.remove(it)

class OscSelection(bpy.types.Header):
    
    bl_label = "Selection Osc"
    bl_space_type = "VIEW_3D"

    def __init__(self):
        select_osc()

    def draw(self, context):
        """
        layout = self.layout
        row = layout.row()
        row.label("Sels: "+str(len(bpy.selection_osc)))
        """  

##=============== DISTRIBUTE ======================    


def ObjectDistributeOscurart (self, X, Y, Z):
    if len(bpy.selection_osc[:]) > 1:
        # VARIABLES
        dif = bpy.selection_osc[-1].location-bpy.selection_osc[0].location
        chunkglobal = dif/(len(bpy.selection_osc[:])-1)
        chunkx = 0
        chunky = 0
        chunkz = 0
        deltafst = bpy.selection_osc[0].location
        
        #ORDENA
        for OBJECT in bpy.selection_osc[:]:          
            if X:  OBJECT.location.x=deltafst[0]+chunkx
            if Y:  OBJECT.location[1]=deltafst[1]+chunky
            if Z:  OBJECT.location.z=deltafst[2]+chunkz
            chunkx+=chunkglobal[0]
            chunky+=chunkglobal[1]
            chunkz+=chunkglobal[2]
    else:  
        self.report({'ERROR'}, "Selection is only 1!")      
    
class DialogDistributeOsc(bpy.types.Operator):
    """Space Objects between there Origins"""
    bl_idname = "object.distribute_osc"
    bl_label = "Distribute Objects"       
    Boolx = bpy.props.BoolProperty(name="X")
    Booly = bpy.props.BoolProperty(name="Y")
    Boolz = bpy.props.BoolProperty(name="Z")
    
    def execute(self, context):
        ObjectDistributeOscurart(self, self.Boolx,self.Booly,self.Boolz)
        return {'FINISHED'}
    def invoke(self, context, event):
        self.Boolx = True
        self.Booly = True
        self.Boolz = True        
        return context.window_manager.invoke_props_dialog(self)


