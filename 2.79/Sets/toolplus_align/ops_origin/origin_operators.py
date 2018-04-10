# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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
#


# LOAD MODUL #
import bpy
from bpy import*

##################################
###  Origin to Corners on Top  ###
##################################

class View3D_TP_Origin_CubeBack_CornerTop_Minus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubeback_cornertop_minus_xy"  
    bl_label = "Origin to -XY Corner / Top of Cubeback"  
  
    def execute(self, context):

        if context.mode == 'OBJECT':         
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o                 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z

                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.z+=c
                     x.co.x-=a

                o.location.y-=b 
                o.location.z-=c
                o.location.x+=a          
                
        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z

            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c
                 x.co.x-=a

            o.location.y-=b 
            o.location.z-=c
            o.location.x+=a          
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeBack_CornerTop_Plus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubeback_cornertop_plus_xy"  
    bl_label = "Origin to +XY Corner / Top of Cubeback"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 
                
                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.z+=c
                     x.co.x+=a

                o.location.y-=b
                o.location.z-=c
                o.location.x-=a          

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object

            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c
                 x.co.x+=a

            o.location.y-=b
            o.location.z-=c
            o.location.x-=a          
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_CornerTop_Minus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_cornertop_minus_xy"  
    bl_label = "Origin to -XY Corner / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o              

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.z+=c
                     x.co.x-=a
                     
                o.location.y+=b 
                o.location.z-=c  
                o.location.x+=a                    

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c
                 x.co.x-=a
                 
            o.location.y+=b 
            o.location.z-=c  
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_CornerTop_Plus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_cornertop_plus_xy"  
    bl_label = "Origin to +XY Corner / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.z+=c
                     x.co.x+=a
                     
                o.location.y+=b
                o.location.z-=c  
                o.location.x-=a                    

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c
                 x.co.x+=a
                 
            o.location.y+=b
            o.location.z-=c  
            o.location.x-=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}




#####################################
###  Origin to Corners on Bottom  ###
#####################################

class View3D_TP_Origin_CubeFront_CornerBottom_Minus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_cornerbottom_minus_xy"  
    bl_label = "Origin to -XY Corner / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.z-=c
                     x.co.x-=a
                     
                o.location.y+=b
                o.location.z+=c 
                o.location.x+=a            

        else:            

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c
                 x.co.x-=a
                 
            o.location.y+=b
            o.location.z+=c 
            o.location.x+=a            
            bpy.ops.object.mode_set(mode = 'EDIT')
        
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_CornerBottom_Plus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_cornerbottom_plus_xy"  
    bl_label = "Origin to +XY Corner / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.z-=c
                     x.co.x+=a
                     
                o.location.y+=b 
                o.location.z+=c  
                o.location.x-=a              

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c
                 x.co.x+=a
                 
            o.location.y+=b 
            o.location.z+=c  
            o.location.x-=a              
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}




class View3D_TP_Origin_CubeBack_CornerBottom_Minus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubeback_cornerbottom_minus_xy"  
    bl_label = "Origin to -XY Corner / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
               
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o
                                
                init=0
                for x in o.data.vertices:
                     if init==0:            
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.z-=c
                     x.co.x-=a
                     
                o.location.y-=b 
                o.location.z+=c  
                o.location.x+=a                    

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:            
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c
                 x.co.x-=a
                 
            o.location.y-=b 
            o.location.z+=c  
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
     
        return {'FINISHED'}



class View3D_TP_Origin_CubeBack_CornerBottom_Plus_XY(bpy.types.Operator):  
    bl_idname = "tp_ops.cubeback_cornerbottom_plus_xy"  
    bl_label = "Origin to +XY Corner / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.z-=c
                     x.co.x+=a
                     
                o.location.y-=b 
                o.location.z+=c  
                o.location.x-=a                    

        else:


            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c
                 x.co.x+=a
                 
            o.location.y-=b 
            o.location.z+=c  
            o.location.x-=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}


###############################################
###  Origin to the Middle of the Top Edges  ###
###############################################


class View3D_TP_Origin_CubeBack_EdgeTop_Minus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubeback_edgetop_minus_y"  
    bl_label = "Origin to -Y Edge / Top of Cubeback"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.z+=c 
                                 
                o.location.y-=b 
                o.location.z-=c                 
            
        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c 
                             
            o.location.y-=b 
            o.location.z-=c                 
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}




class View3D_TP_Origin_CubeBack_EdgeTop_Plus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubeback_edgetop_plus_y"  
    bl_label = "Origin to +Y Edge / Top of Cubeback"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
 
            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.z+=c 
                                 
                o.location.y+=b 
                o.location.z-=c                  
            
        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c 
                             
            o.location.y+=b 
            o.location.z-=c                  
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_EdgeTop_Minus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgetop_minus_x"  
    bl_label = "Origin to -X Edge / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.x-=a
                     x.co.z+=c 
                                 
                o.location.x+=a 
                o.location.z-=c                     

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x-=a
                 x.co.z+=c 
                             
            o.location.x+=a 
            o.location.z-=c                     
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_EdgeTop_Plus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgetop_plus_x"  
    bl_label = "Origin to +X Edge / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o               

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.x+=a
                     x.co.z+=c 
                                 
                o.location.x-=a 
                o.location.z-=c                   

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x+=a
                 x.co.z+=c 
                             
            o.location.x-=a 
            o.location.z-=c                   
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}





##################################################
###  Origin to the Middle of the Bottom Edges  ###
##################################################


class View3D_TP_Origin_CubeFront_EdgeBottom_Minus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgebottom_minus_y"  
    bl_label = "Origin to -Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 
                
                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.z-=c 
                                 
                o.location.y+=b 
                o.location.z+=c              

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c 
                             
            o.location.y+=b 
            o.location.z+=c              
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}




class View3D_TP_Origin_CubeFront_EdgeBottom_Plus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgebottom_plus_y"  
    bl_label = "Origin to +Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o
            
                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.z-=c 
                                 
                o.location.y-=b 
                o.location.z+=c           

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c 
                             
            o.location.y-=b 
            o.location.z+=c           
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_EdgeBottom_Minus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgebottom_minus_x"  
    bl_label = "Origin to -X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.x-=a
                     x.co.z-=c 
                                 
                o.location.x+=a 
                o.location.z+=c                    

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x-=a
                 x.co.z-=c 
                             
            o.location.x+=a 
            o.location.z+=c                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}




class View3D_TP_Origin_CubeFront_EdgeBottom_Plus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgebottom_plus_x"  
    bl_label = "Origin to +X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.x+=a
                     x.co.z-=c
                                 
                o.location.x-=a 
                o.location.z+=c                    

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x+=a
                 x.co.z-=c
                             
            o.location.x-=a 
            o.location.z+=c                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}




################################################
###  Origin to the Middle of the Side Edges  ###
################################################


class View3D_TP_Origin_CubeFront_EdgeMiddle_Minus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgemiddle_minus_y"  
    bl_label = "Origin to -Y Edge / Middle of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.x-=a 
                                 
                o.location.y+=b 
                o.location.x+=a              

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.x-=a 
                             
            o.location.y+=b 
            o.location.x+=a              
            bpy.ops.object.mode_set(mode = 'EDIT')                        
            
        return {'FINISHED'}




class View3D_TP_Origin_CubeFront_EdgeMiddle_Plus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgemiddle_plus_y"  
    bl_label = "Origin to +Y Edge / Middle of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':            

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 
                    
                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y-=b
                     x.co.x+=a 
                                 
                o.location.y+=b 
                o.location.x-=a            

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.x+=a 
                             
            o.location.y+=b 
            o.location.x-=a            
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}




class View3D_TP_Origin_CubeFront_EdgeMiddle_Minus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgemiddle_minus_x"  
    bl_label = "Origin to -X Edge / Middle of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':   
                    
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o                

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.x-=a 
                                 
                o.location.y-=b 
                o.location.x+=a                    

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.x-=a 
                             
            o.location.y-=b 
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}


class View3D_TP_Origin_CubeFront_EdgeMiddle_Plus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_edgemiddle_plus_x"  
    bl_label = "Origin to +X Edge / Middle of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         b=x.co.y
                         c=x.co.z

                         init=1
                     
                     elif x.co.x < a:
                         a=x.co.x
                         
                     elif x.co.y < b:
                         b=x.co.y
                     
                     elif x.co.z < c:
                         c=x.co.z
                         
                for x in o.data.vertices:
                     x.co.y+=b
                     x.co.x+=a 
                                 
                o.location.y-=b 
                o.location.x-=a                  

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.x+=a 
                             
            o.location.y-=b 
            o.location.x-=a                  
            bpy.ops.object.mode_set(mode = 'EDIT')

            
        return {'FINISHED'}


######################################
###  Origin to the Middle of Side  ### 
######################################


class View3D_TP_Origin_CubeFront_Side_Minus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_side_minus_y"  
    bl_label = "Origin to -Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o               

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.y
                         init=1
                     elif x.co.y<a:
                         a=x.co.y
                         
                for x in o.data.vertices:
                     x.co.y-=a
                                 
                o.location.y+=a             
        
        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.y
                     init=1
                 elif x.co.y<a:
                     a=x.co.y
                     
            for x in o.data.vertices:
                 x.co.y-=a
                             
            o.location.y+=a             
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_Side_Plus_Y(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_side_plus_y"  
    bl_label = "Origin to +Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o                 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.y
                         init=1
                     elif x.co.y<a:
                         a=x.co.y
                         
                for x in o.data.vertices:
                     x.co.y+=a
                                 
                o.location.y-=a             

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.y
                     init=1
                 elif x.co.y<a:
                     a=x.co.y
                     
            for x in o.data.vertices:
                 x.co.y+=a
                             
            o.location.y-=a             
            bpy.ops.object.mode_set(mode = 'EDIT')                        
            
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_Side_Minus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_side_minus_x"  
    bl_label = "Origin to -X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o                 

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         init=1
                     elif x.co.x<a:
                         a=x.co.x
                         
                for x in o.data.vertices:
                     x.co.x-=a
                                 
                o.location.x+=a                   
                bpy.ops.object.mode_set(mode = 'EDIT')
                bpy.ops.object.editmode_toggle()

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     init=1
                 elif x.co.x<a:
                     a=x.co.x
                     
            for x in o.data.vertices:
                 x.co.x-=a
                             
            o.location.x+=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')

        return {'FINISHED'}




class View3D_TP_Origin_CubeFront_Side_Plus_X(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_side_plus_x"  
    bl_label = "Origin to +X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 

                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 
                
                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.x
                         init=1
                     elif x.co.x<a:
                         a=x.co.x
                         
                for x in o.data.vertices:
                     x.co.x+=a
                                 
                o.location.x-=a                   

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     init=1
                 elif x.co.x<a:
                     a=x.co.x
                     
            for x in o.data.vertices:
                 x.co.x+=a
                             
            o.location.x-=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
            
            
        return {'FINISHED'}




class View3D_TP_Origin_CubeFront_Side_Minus_Z(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_side_minus_z"  
    bl_label = "Origin to -Z Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob
                 
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o                

                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.z
                         init=1
                     elif x.co.z<a:
                         a=x.co.z
                         
                for x in o.data.vertices:
                     x.co.z-=a
                                 
                o.location.z+=a                   

        else:

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z-=a
                             
            o.location.z+=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
                    
        return {'FINISHED'}



class View3D_TP_Origin_CubeFront_Side_Plus_Z(bpy.types.Operator):  
    bl_idname = "tp_ops.cubefront_side_plus_z"  
    bl_label = "Origin to +Z Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':        

            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob 
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o 
                
                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.z
                         init=1
                     elif x.co.z<a:
                         a=x.co.z
                         
                for x in o.data.vertices:
                     x.co.z+=a
                                 
                o.location.z-=a                       
        
        else: 
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z+=a
                             
            o.location.z-=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
       
        return {'FINISHED'}

 

# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()