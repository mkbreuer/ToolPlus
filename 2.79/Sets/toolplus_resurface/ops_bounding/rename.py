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
    "name": "vtools Rename objects Tool",
    "author": "Antonio Mendoza",
    "version": (0, 0, 1),
    "blender": (2, 72, 0),
    "location": "View3D > Panel Tools > Object Utils Tab",
    "warning": "",
    "description": "Batch renaming objects keeping selection order",
    "category": "Object",
}
"""

import bpy
import math 
import threading
from bpy.props import StringProperty, BoolProperty, IntProperty, CollectionProperty, FloatProperty, EnumProperty

    
def setName(p_objects, p_newName, p_startIn=0, p_numDigits=3, p_numbered=False):
    id = p_startIn
    cont = 1
    numberDigits = p_numDigits
    replacingName = p_newName
    
    if p_numbered == True:
         replacingName += ".000"    
 
    for obj in p_objects:
        
        if p_startIn == 0 or p_numbered == False:
            obj.name = replacingName
        else:
            addZero = 0    
            for i in range(1,numberDigits):
                mod = int(id / (pow(10,i)))
                if mod == 0:
                    addZero += 1
 
            newNameId = str(id)
            for i in range(0,addZero):
                newNameId = '0' + newNameId
               
            oldName = obj.name
            obj.name = ''
            newName = p_newName + '.' + newNameId
            obj.name = newName
            id += 1
            
 
def replace(p_objects, p_findString, p_replaceString=''):
    exist = 0
    if p_findString != '':
        for obj in p_objects:
            obj.name = obj.name.replace(p_findString, p_replaceString)
            
def hasId (p_name):
    
    
    idFound = False
    i = len(p_name) - 1
    str = p_name[i]
    str_res = ""
    
    while p_name[i].isnumeric() and i >= 0:
        str_res = p_name[i] + str_res
        i = i - 1
        

    if i < 0 or not str_res.isnumeric():
        idFound = False
        i = - 1
        
    return i

def addPrefixSubfix(p_objects,p_prefix='',p_subfix='',p_keepId=True):
    
    for obj in p_objects:
        obj.name = p_prefix + obj.name
        if p_keepId == True:
            id = hasId(obj.name)
            if id >= 0:
                obj.name = obj.name[:id] + p_subfix + obj.name[id:]
            else:
                obj.name = obj.name + p_subfix
        else:
            obj.name = obj.name + p_subfix   


def copyNametoData(p_objects):    
    for obj in p_objects:
        if obj.type == 'MESH':
            obj.data.name = obj.name
            
class RNO_OP_setName(bpy.types.Operator):
    """Set new name"""
    bl_idname = "object.rno_setname"
    bl_label = "Set new name"

    selection_list = []
           
    def execute(self,context):
        newName = context.scene.rno_str_new_name
        numbered = context.scene.rno_bool_numbered
        startIn = 1
        numDigits = 3
        
        if context.scene.rno_str_numFrom != '':
            startIn = int(context.scene.rno_str_numFrom)
            numDigits = len(context.scene.rno_str_numFrom)
            
        if context.scene.rno_bool_keepOrder == True:
            setName(self.selection_list,newName, p_startIn=startIn,p_numDigits=numDigits, p_numbered=numbered)
        else:
            setName(bpy.context.selected_objects, newName, p_startIn=startIn,p_numDigits=numDigits, p_numbered=numbered)
        
        return{'FINISHED'}


class RNO_OP_replaceInName(bpy.types.Operator):
    """replace"""
    bl_idname = "object.rno_replace_in_name"
    bl_label = "replace"
        
    def execute(self,context):
        oldName = context.scene.rno_str_old_string
        newName = context.scene.rno_str_new_string        
        replace(bpy.context.selected_objects,oldName, newName)        
        return{'FINISHED'}
      
      
class RNO_OP_addSubfixPrefix(bpy.types.Operator):
    """Add subfix / Prefix"""
    bl_idname = "object.rno_add_subfix_prefix"
    bl_label = "Add subfix / Prefix"
        
    def execute(self,context):
        prefix = context.scene.rno_str_prefix
        subfix = context.scene.rno_str_subfix
        keepIndex = context.scene.rno_bool_keepIndex                 
        addPrefixSubfix(bpy.context.selected_objects,p_prefix=prefix,p_subfix=subfix,p_keepId=keepIndex)        
        return{'FINISHED'}
      

class RNO_PN_EndSelectionOrder(bpy.types.Operator):
    """leave selection order"""
    bl_idname = "object.rno_end_selection_order"
    bl_label = "leave selection order"
    
    def execute(self,context):
        context.scene.rno_bool_keepOrder = False
        return {'FINISHED'}

      
class RNO_OP_copyNameToDataName(bpy.types.Operator):
    """Copy object name to mesh data name"""
    bl_idname = "object.copynametodata"
    bl_label = "Copy object name to mesh data name"
        
    def execute(self,context):
        copyNametoData(bpy.context.selected_objects)        
        return{'FINISHED'}

    
class RNO_PN_KeepSelectionOrder(bpy.types.Operator):
    """respect selection order Start / Finish"""
    bl_idname = "object.rno_keep_selection_order"
    bl_label = "respect selection order Start / Finish"
    
    num_selected = 0
    selection_list = []    
  
    def getSelectionList(self):
        return self.selection_list
    
    def findObject(self, p_object, p_list):
        
        found = False
        for obj in p_list:
            if obj.name == p_object.name:
                found = True
                break            
        return found
    
    def removeUnselecteds(self, p_oldList, p_newList):
        
        for obj in p_oldList:
            found = self.findObject(obj, p_newList)
            if found == False:
                p_oldList.remove(obj)
                
        return p_oldList
                          
    def sortList(self):
        
        objects = bpy.context.selected_objects
        num_sel = len(objects)
        num_sortElements = len(self.selection_list)
        
        if num_sel < num_sortElements:
            self.removeUnselecteds(self.selection_list,objects)
            
        else:
            for obj in objects:
                found = self.findObject(obj,self.selection_list)
                
                if found == False:
                    self.selection_list.append(obj)
        
        return True
        
    def execute(self,context):
        
        if context.scene.rno_bool_keepOrder == False:
            bpy.ops.object.select_all(action='DESELECT')
            context.scene.rno_bool_keepOrder = True
            self.active = False
            
            #print("------------------ INIT -----------------------")
            
        else:
            context.scene.rno_bool_keepOrder = False
            #print("------------------ END -----------------------")
            
        context.window_manager.modal_handler_add(self)            
        return {'RUNNING_MODAL'}
        
         
    def modal(self, context, event):
       
        active = context.scene.rno_bool_keepOrder 
        if active == True:
            self.sortList()
            return {'PASS_THROUGH'}
        else:
            return {'FINISHED'} 
              
        return {'PASS_THROUGH'}



class VIEW3D_TP_Copy_Name_to_Meshdata(bpy.types.Operator):
    """Copy Object-Name to Mesh-Data-Name"""
    bl_idname = "tp_ops.copy_name_to_meshdata"
    bl_label = "Copy Object-Name to Mesh-Data-Name"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        selected = bpy.context.selected_objects 

        for obj in selected:     
            obj.data.name = obj.name
            
        return{'FINISHED'}
    

class VIEW3D_TP_Copy_Dataname_to_Object(bpy.types.Operator):
    """Copy Mesh-Data-Name to Object-Name"""
    bl_idname = "tp_ops.copy_data_name_to_object"
    bl_label = "Copy Mesh-Data-Name to Object-Name"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        selected = bpy.context.selected_objects 

        for obj in selected:     
            obj.name = obj.data.name

        return {'FINISHED'}  
  
  
        
def register():
    bpy.utils.register_module(__name__)
           
def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()