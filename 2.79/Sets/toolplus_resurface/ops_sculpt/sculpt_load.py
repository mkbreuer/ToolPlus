#==================================================================
#  Copyright (C) 6/27/2014  Blender Sensei (Seth Fentress)
#  ####BEGIN GPL LICENSE BLOCK #####
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
#  ####END GPL LICENSE BLOCK #####
#  To report a bug or suggest a feature visit:
#  Blendersensei.com/forums/zerobrush
#  VISIT Blendersensei.com for more information.
#  SUBSCRIBE at Youtube.com/Blendersensei
# Zero Brush by Blender Sensei (Seth Fentress) Blendersensei.com",
# "version": (1, 0, 0),
# "blender": (7, 0, 1),  
#====================================================================



# LOAD MODUL #    
import bpy
import os
from bpy import *
from bpy.props import *
from bpy_extras.io_utils import ImportHelper

from bl_ui.properties_paint_common import (UnifiedPaintPanel, brush_texture_settings)

# UPDATE BRUSH TEXURE SCALE OPTION #
def SculptBrushScaleUpdater(self, context):

    brushTex = bpy.context.tool_settings.sculpt.brush.texture_slot
        
    #Adjust for percentage display
    val = self.texBrushScale
    val = 3 - (val * 0.03)
    if val == 0:
       val = 0.10
    brushTex.scale[0] = val
    brushTex.scale[1] = val
    brushTex.scale[2] = val
    
    
# CLEAN BRUSH NAME #
def cleanBrushName(fn):
    #Strip selected from name
    newName = ''.join(x for x in fn if x not in 
    ',<>:""[]{}()/\|!@#$%^&*,.?')
    #List of stuff to remove from file name
    toReplace = ['seamless','texture','tex','by:','free', '.com',
    '.net','.org','the','image','photos', 'original','photo', 'tileable']
    #Now remove it.
    newName = newName.lower()
    for bad in toReplace:
        newName = newName.replace(bad, "")
    
    #Recoginze as intentional spaces        
    newName = newName.replace("-", " ")
    newName = newName.replace("_", " ")
    
    #Author kill. Remove all after " by " found.
    sep = " by "
    newName = newName.split(sep, 1)[0]
    newName = newName.title()
    
    #Parenth kill. Remove all after "(" found.
    sep = "("
    newName = newName.split(sep, 1)[0]
    newName = newName.title()
    
    #If name to long get rid of spaces
    if len(newName) > 20:
        newName = newName.replace(" ", "")    
    
    #18 max characters
    newName = newName[:18]
    
    x = 0
    # if first letters blank
    while x < 18:
        if newName[:1] == " ":
            newName = newName[1:]
        else:
            break
        x += 1

    #Add generic if name to short
    if len(newName) < 1:
        newName = "myBrush"
    
    #Seperate new from standard brushes
    newName = "°" + newName    
    return newName
        
               


# LOAD SINGLE BRUSH #
def load_a_brush(context, filepath):
    if os.path.isdir(filepath):
        return
    else:
        try:
            fn = bpy.path.display_name_from_filepath(filepath)
            #create image and load...
            img = bpy.data.images.load(filepath)
            img.use_fake_user =True
            
            #create a texture
            tex = bpy.data.textures.new(name =fn, type='IMAGE')
            #link the img to the texture
            tex.image = img
            
            settings = bpy.context.tool_settings
            #Create New brush
            if bpy.context.mode.startswith('PAINT') is True:
                #switch brush to assure inherited properties
                try:
                    settings.image_paint.brush = bpy.data.brushes["Draw"]
                except:
                    pass
                bpy.ops.brush.add()
                brush = bpy.context.tool_settings.image_paint.brush
                #Set up new brush settings
                bpy.ops.brush.curve_preset(shape='SHARP')
                brush.color = (1, 1, 1)
                brush.strength = 1
                
            elif bpy.context.mode.startswith('SCULPT') is True:
                #switch brush to assure inherited properties
                try:
                    settings.sculpt.brush = bpy.data.brushes["SculptDraw"]
                except:
                    pass
                #Create New brush and assign texture
                bpy.ops.brush.add()
                brush = bpy.context.tool_settings.sculpt.brush
                bpy.ops.brush.curve_preset(shape='SHARP')
                brush.strength = 0.125
                brush.auto_smooth_factor = 0.15
            
            #Clean up brush name from file name
            #Run function, return results to newName
            newName = cleanBrushName(fn)
            
            #Give brush name cleaned filename
            brush.name = newName
            #Assign texture to brush
            brush.texture = tex

            #Give brush texture icon
            brush.use_custom_icon = True
            brush.icon_filepath = filepath
            
            #Change method of brush
            brush.stroke_method = 'DOTS'
            brush.texture_slot.tex_paint_map_mode = 'TILED'
            #Update brush texture scale option
            bpy.data.window_managers["WinMan"].texBrushScale = 85
        except:
            pass
    return {'FINISHED'}


class VIEW3D_TP_Load_Single_Brush(bpy.types.Operator, ImportHelper):
    bl_idname = "tp_ops.load_single_brush"  
    bl_label = "Brush"
    bl_description = "Load an image (png, jpeg, tiff, etc..) as a brush"
    
    @classmethod
    def poll(cls, context):
        return context.active_object != None
    def execute(self, context):
        return load_a_brush(context, self.filepath)





# LOAD BRUSH FOLDER #
def loadbrushes(context, filepath):
    if os.path.isdir(filepath):
        directory = filepath 
    else:
        #is a file, find parent directory    
        li = filepath.split(os.sep)
        directory = filepath.rstrip(li[-1])
        
    files = os.listdir(directory)
    for f in files:
        try:
            fn = f[3:]
            #create image and load...
            img = bpy.data.images.load(filepath = directory +os.sep + f)
            img.use_fake_user =True
            #create a texture
            tex = bpy.data.textures.new(name =fn, type='IMAGE')
            tex.use_fake_user =True
            #link the img to the texture
            tex.image = img
        except:
            pass
        
        settings = bpy.context.tool_settings
        #Create New brush
        if bpy.context.mode.startswith('PAINT') is True:
            #switch brush to assure inherited properties
            try:
                settings.image_paint.brush = bpy.data.brushes["Draw"]
            except:
                pass
            bpy.ops.brush.add()
            brush = bpy.context.tool_settings.image_paint.brush
            bpy.ops.brush.curve_preset(shape='SHARP')
            #Set up new brush settings
            brush.color = (1, 1, 1)
            
        elif bpy.context.mode.startswith('SCULPT') is True:
            #switch brush to assure inherited properties
            try:
                settings.sculpt.brush = bpy.data.brushes["SculptDraw"]
            except:
                pass
            #Create New brush and assign texture
            bpy.ops.brush.add()
            brush = bpy.context.tool_settings.sculpt.brush
            bpy.ops.brush.curve_preset(shape='SHARP')
            brush.strength = 0.125
            brush.auto_smooth_factor = 0.15
                   
        #Clean up brush name from file name
        fn = bpy.path.display_name_from_filepath(directory +os.sep + f)
        newName = cleanBrushName(fn)
        
        #Give brush name of file name
        brush.name = newName
        brush.texture = tex
            
        #Give brush texture icon
        brush.use_custom_icon = True
        brush.icon_filepath = directory +os.sep + f
        
        #Change method of brush
        brush.stroke_method = 'DOTS'
        brush.texture_slot.tex_paint_map_mode = 'TILED'
        
    #Update brush texture scale option
    bpy.data.window_managers["WinMan"].texBrushScale = 85
    return {'FINISHED'}


class VIEW3D_TP_Import_Brushes(bpy.types.Operator, ImportHelper):
    bl_idname = "tp_ops.load_brushes"  
    bl_label = "Brushes"
    bl_description = "Load a folder of images (png, jpeg, tiff, etc..) as brushes"

    @classmethod
    def poll(cls, context):
        return context.active_object != None

    def execute(self, context):
        return loadbrushes(context, self.filepath)






class VIEW3D_TP_Brush_Ops_Menu(bpy.types.Operator):
    """Select Brush"""
    bl_idname = "tp_ops.select_brush"
    bl_label = "Select Brush"
    bl_options = {'DEFAULT_CLOSED'}
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def draw(self, context):
        layout = self.layout

        settings = UnifiedPaintPanel.paint_settings(context)
        brush = settings.brush

        flow = layout.column_flow(columns=2)
        for brush in bpy.data.brushes:
            if context.sculpt_object:
                if brush.use_paint_sculpt:
                   
                    row = flow.row(1)
                    row.label(icon_value=row.icon(brush))
                   
                    props = row.operator("wm.context_set_id", text=brush.name)
                    props.data_path = "tool_settings.sculpt.brush"
                    props.value = brush.name

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.invoke_props_popup(self, event)
        return {'FINISHED'}            




class VIEW3D_TP_Brush_Menu(bpy.types.Menu):
    """Sculpt Brush"""
    bl_idname = "SCULPT_MT_brush_menu"
    bl_label = "Sculpt Brush"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        flow = layout.column_flow(columns=4)
        for brush in bpy.data.brushes:
            if brush.use_paint_sculpt:
                col = flow.column()
                props = col.operator("wm.context_set_id", text=brush.name)
                props.data_path = "tool_settings.sculpt.brush"
                props.value = brush.name
                




# PROPERTIES: BRUSH LOAD #
class ZeroBrush_Load_Properties(bpy.types.PropertyGroup):
    
    #Set property for texture brush scale.
    bpy.types.WindowManager.texBrushScale = bpy.props.IntProperty( name="Texture Scale",  description = "Scales the texture this brush is using",  default = 100,  subtype="PERCENTAGE", min=0, max=100,  update = SculptBrushScaleUpdater)
    

     
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

    bpy.types.WindowManager.tp_props_zerobrush = PointerProperty(type = ZeroBrush_Load_Properties)     

def unregister():   
    bpy.utils.unregister_module(__name__)

    try:
        del bpy.types.WindowManager.tp_props_zerobrush
    except:
        pass

if __name__ == "__main__":
    register()







