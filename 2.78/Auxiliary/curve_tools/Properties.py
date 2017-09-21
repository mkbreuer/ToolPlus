import time

import bpy
from bpy.props import *




class CurveTools2SelectedObject(bpy.types.PropertyGroup):
    name = StringProperty(name = "name", default = "??")

    
    @staticmethod
    def UpdateThreadTarget(lock, sleepTime, selectedObjectNames, selectedBlenderObjectNames):
        time.sleep(sleepTime)
        
        newSelectedObjectNames = []
        
        for name in selectedObjectNames:
            if name in selectedBlenderObjectNames: newSelectedObjectNames.append(name)
            
        for name in selectedBlenderObjectNames:
            if not (name in selectedObjectNames): newSelectedObjectNames.append(name)
            
        # sometimes it still complains about the context
        try:
            nrNewSelectedObjects = len(newSelectedObjectNames)
            bpy.context.scene.curvetools.NrSelectedObjects = nrNewSelectedObjects
            
            selectedObjects = bpy.context.scene.curvetools.SelectedObjects
            selectedObjects.clear()
            for i in range(nrNewSelectedObjects): selectedObjects.add()
            for i, newSelectedObjectName in enumerate(newSelectedObjectNames):
                selectedObjects[i].name = newSelectedObjectName
        except: pass

        
    @staticmethod
    def GetSelectedObjectNames():
        selectedObjects = bpy.context.scene.curvetools.SelectedObjects
        
        rvNames = []
        selectedObjectValues = selectedObjects.values()
        for selectedObject in selectedObjectValues: rvNames.append(selectedObject.name)
        
        return rvNames
        
        
    @staticmethod
    def GetSelectedBlenderObjectNames():
        blenderSelectedObjects = bpy.context.selected_objects
        
        rvNames = []
        for blObject in blenderSelectedObjects: rvNames.append(blObject.name)
        
        return rvNames
        
