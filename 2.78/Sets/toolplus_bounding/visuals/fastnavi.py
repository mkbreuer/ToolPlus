# space_view_3d_display_tools.py Copyright (C) 2014, Jordi Vall-llovera
#
# Multiple display tools for fast navigate/interact with the viewport
#
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
# ***** END GPL LICENCE BLOCK *****

#bl_info = {
#    "name": "Display Tools",
#    "author": "Jordi Vall-llovera Medina, Jhon Wallace",
#    "version": (1, 6, 0),
#    "blender": (2, 7, 0),
#    "location": "Toolshelf",
#    "description": "Display tools for fast navigate/interact with the viewport",
#    "warning": "",
#    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/\
#    3D_interaction/Display_Tools",
#    "tracker_url": "",
#    "category": "User Changed"}

#"""
#Additional links:
#    Author Site: http://www.jordiart.com
#"""

import bpy

from bpy.props import IntProperty, BoolProperty, FloatProperty, EnumProperty

# init delay variables
bpy.types.Scene.Delay = bpy.props.BoolProperty(
        default = False,
        description = "Activate delay return to normal viewport mode")

bpy.types.Scene.DelayTime = bpy.props.IntProperty(
        default = 30,
        min = 1,
        max = 500,
        soft_min = 10,
        soft_max = 250,
        description = "Delay time to return to normal viewport\
         mode after move your mouse cursor")

bpy.types.Scene.DelayTimeGlobal = bpy.props.IntProperty(
        default = 30,
        min = 1,
        max = 500,
        soft_min = 10,
        soft_max = 250,
        description = "Delay time to return to normal viewport\
         mode after move your mouse cursor")

#init variable for fast navigate
bpy.types.Scene.EditActive = bpy.props.BoolProperty(
        default = True,
        description = "Activate for fast navigate in edit mode too")

#Fast Navigate toggle function
def trigger_fast_navigate(trigger):
    scene = bpy.context.scene
    scene.FastNavigateStop = False
    
    if trigger == True:
        trigger = False
    else:
        trigger = True

#Control how to display particles during fast navigate
def display_particles(mode):
    scene = bpy.context.scene
    
    if mode == True:
        for particles in bpy.data.particles:
            if particles.type == 'EMITTER':
                particles.draw_method = 'DOT'
                particles.draw_percentage = 100
            else:
                particles.draw_method = 'RENDER'  
                particles.draw_percentage = 100
    else:
        for particles in bpy.data.particles:
            if particles.type == 'EMITTER':
                particles.draw_method = 'DOT'
                particles.draw_percentage = scene.ParticlesPercentageDisplay
            else:
                particles.draw_method = 'RENDER'  
                particles.draw_percentage = scene.ParticlesPercentageDisplay

#Do repetitive fast navigate related stuff         
def fast_navigate_stuff(self, context, event):    
    scene = bpy.context.scene
    view = context.space_data
        
    if bpy.context.area.type != 'VIEW_3D':
        return self.cancel(context)    
                          
    if event.type == 'ESC' or event.type == 'RET' or event.type == 'SPACE':
        return self.cancel(context)
     
    if scene.FastNavigateStop == True:
        return self.cancel(context)    
    
    #fast navigate while orbit/panning
    if event.type == 'MIDDLEMOUSE':
        if scene.Delay == True:
            if scene.DelayTime < scene.DelayTimeGlobal:
                scene.DelayTime += 1
        view.viewport_shade = scene.FastMode
        self.mode = False
        
    #fast navigate while transform operations
    if event.type == 'G' or event.type == 'R' or event.type == 'S': 
        if scene.Delay == True:
            if scene.DelayTime < scene.DelayTimeGlobal:
                scene.DelayTime += 1
        view.viewport_shade = scene.FastMode
        self.mode = False
     
    #fast navigate while menu popups or duplicates  
    if event.type == 'W' or event.type == 'D' or event.type == 'L'\
        or event.type == 'U' or event.type == 'I' or event.type == 'M'\
        or event.type == 'A' or event.type == 'B': 
        if scene.Delay == True:
            if scene.DelayTime < scene.DelayTimeGlobal:
                scene.DelayTime += 1
        view.viewport_shade = scene.FastMode
        self.mode = False
    
    #fast navigate while numpad navigation
    if event.type == 'NUMPAD_PERIOD' or event.type == 'NUMPAD_1'\
        or event.type == 'NUMPAD_2' or event.type == 'NUMPAD_3'\
        or event.type == 'NUMPAD_4' or event.type == 'NUMPAD_5'\
        or event.type == 'NUMPAD_6' or event.type == 'NUMPAD_7'\
        or event.type == 'NUMPAD_8' or event.type == 'NUMPAD_9': 
        if scene.Delay == True:
            if scene.DelayTime < scene.DelayTimeGlobal:
                scene.DelayTime += 1
        view.viewport_shade = scene.FastMode
        self.mode = False
        
    #fast navigate while zooming with mousewheel too
    if event.type == 'WHEELUPMOUSE' or event.type == 'WHEELDOWNMOUSE':
        scene.DelayTime = scene.DelayTimeGlobal
        view.viewport_shade = scene.FastMode
        self.mode = False
        
    if event.type == 'MOUSEMOVE': 
        if scene.Delay == True:
            if scene.DelayTime == 0:
                scene.DelayTime = scene.DelayTimeGlobal
                view.viewport_shade = scene.OriginalMode 
                self.mode = True
        else:
            view.viewport_shade = scene.OriginalMode 
            self.mode = True
    
    if scene.Delay == True:
        scene.DelayTime -= 1   
        if scene.DelayTime == 0:
            scene.DelayTime = scene.DelayTimeGlobal
            view.viewport_shade = scene.OriginalMode 
            self.mode = True
        
    if scene.ShowParticles == False:
        for particles in bpy.data.particles:
            if particles.type == 'EMITTER':
                particles.draw_method = 'NONE'
            else:
                particles.draw_method = 'NONE'    
    else:
        display_particles(self.mode)   
    
#Fast Navigate operator
class FastNavigate(bpy.types.Operator):
    """Operator that runs Fast navigate in modal mode"""
    bl_idname = "view3d.fast_navigate_operator"
    bl_label = "Fast Navigate"
    trigger = BoolProperty(default = False)
    mode = BoolProperty(default = False)

    def modal(self, context, event):     
        scene = bpy.context.scene
        view = context.space_data
        
        if scene.EditActive == True:     
            fast_navigate_stuff(self, context ,event)
            return {'PASS_THROUGH'}       
        else:
            obj = context.active_object
            if obj: 
                if obj.mode != 'EDIT':
                    fast_navigate_stuff(self, context ,event)
                    return {'PASS_THROUGH'}            
                else:
                    return {'PASS_THROUGH'}        
            else:
                fast_navigate_stuff(self, context ,event)
                return {'PASS_THROUGH'}
     
    def execute(self, context):
        context.window_manager.modal_handler_add(self)
        trigger_fast_navigate(self.trigger)
        scene = bpy.context.scene
        scene.DelayTime = scene.DelayTimeGlobal
        return {'RUNNING_MODAL'}
    
    def cancel(self, context):
        scene = context.scene
        for particles in bpy.data.particles:
            particles.draw_percentage = scene.InitialParticles
        return {'CANCELLED'}

#Fast Navigate Stop
def fast_navigate_stop(context):
    scene = bpy.context.scene
    scene.FastNavigateStop = True

#Fast Navigate Stop Operator
class FastNavigateStop(bpy.types.Operator):
    '''Stop Fast Navigate Operator'''
    bl_idname = "view3d.fast_navigate_stop"
    bl_label = "Stop"    
    FastNavigateStop = IntProperty(name = "FastNavigateStop", 
		description = "Stop fast navigate mode",
		default = 0)

    def execute(self,context):
        fast_navigate_stop(context)
        return {'FINISHED'}
    


    
#Init properties for scene
bpy.types.Scene.FastNavigateStop = bpy.props.BoolProperty(
        name = "Fast Navigate Stop", 
        description = "Stop fast navigate mode",
        default = False)

bpy.types.Scene.OriginalMode = bpy.props.EnumProperty(
        items = [('TEXTURED', 'Texture', 'Texture display mode'), 
            ('SOLID', 'Solid', 'Solid display mode')], 
        name = "Normal",
        default = 'SOLID')

bpy.types.Scene.BoundingMode = bpy.props.EnumProperty(
        items = [('BOX', 'Box', 'Box shape'), 
            ('SPHERE', 'Sphere', 'Sphere shape'),
            ('CYLINDER', 'Cylinder', 'Cylinder shape'),
            ('CONE', 'Cone', 'Cone shape')], 
        name = "BB Mode")

bpy.types.Scene.FastMode = bpy.props.EnumProperty(
        items = [('WIREFRAME', 'Wireframe', 'Wireframe display'), 
            ('BOUNDBOX', 'Bounding Box', 'Bounding Box display')], 
        name = "Fast")
        
bpy.types.Scene.ShowParticles = bpy.props.BoolProperty(
        name = "Show Particles", 
        description = "Show or hide particles on fast navigate mode",
		default = True)

bpy.types.Scene.ParticlesPercentageDisplay = bpy.props.IntProperty(
        name = "Display", 
        description = "Display only a percentage of particles",
		default = 25,
        min = 0,
        max = 100,
        soft_min = 0,
        soft_max = 100,
        subtype = 'FACTOR')
    
bpy.types.Scene.InitialParticles = bpy.props.IntProperty(
        name = "Count for initial particle setting before enter fast navigate", 
        description = "Display a percentage value of particles",
		default = 100,
        min = 0,
        max = 100,
        soft_min = 0,
        soft_max = 100)


#Set Render Settings
def set_render_settings(conext):
    scene = bpy.context.scene
    render = bpy.context.scene.render
    view = bpy.context.space_data
    render.simplify_subdivision = 0
    render.simplify_shadow_samples = 0
    render.simplify_child_particles = 0
    render.simplify_ao_sss = 0

class DisplaySimplify(bpy.types.Operator):
    '''Display scene simplified'''
    bl_idname = "view3d.display_simplify"
    bl_label = "Reset"
    
    Mode = EnumProperty(
        items = [('WIREFRAME', 'Wireframe', ''), 
            ('BOUNDBOX', 'Bounding Box', '')], 
        name = "Mode")
        
    ShowParticles = BoolProperty(
        name = "ShowParticles", 
        description = "Show or hide particles on fast navigate mode",
		default = True)
    
    ParticlesPercentageDisplay = IntProperty(
        name = "Display", 
        description = "Display a percentage value of particles",
		default = 25,
        min = 0,
        max = 100,
        soft_min = 0,
        soft_max = 100,
        subtype = 'FACTOR')

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        set_render_settings(context)
        return {'FINISHED'}



# register the classes
def register():

    bpy.utils.register_module(__name__) 
    pass 

def unregister():
    bpy.utils.unregister_module(__name__)
    pass 

if __name__ == "__main__": 
    register() 

