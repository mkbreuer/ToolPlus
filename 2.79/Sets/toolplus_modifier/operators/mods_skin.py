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
from bpy.props import *

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

class VIEW3D_TP_Apply_Modifier_Skin(bpy.types.Operator):
    """apply modifier Skin"""
    bl_idname = "tp_ops.apply_mods_skin"
    bl_label = "Apply Skin Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 

        for obj in selected:
            
            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()  

                for modifier in obj.modifiers:    
                    if (modifier.type == 'SKIN'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin.003")
                                          
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  

                for modifier in obj.modifiers:    
                    if (modifier.type == 'SKIN'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin.003")
      
                bpy.ops.object.mode_set(mode=oldmode) 
                                       
        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_Skin(bpy.types.Operator):
    """remove modifier Skin"""
    bl_idname = "tp_ops.remove_mods_skin"
    bl_label = "Remove Skin Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'SKIN'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'SKIN'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}
        


class VIEW3D_TP_Skin_Modifier(bpy.types.Operator):
    """Add a skin modifier"""
    bl_idname = "tp_ops.mod_skin"
    bl_label = "Skin"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            screw = bpy.context.object.modifiers.get("Skin")   
            if not screw :   

                object.modifier_add(type = "SKIN")


        return {'FINISHED'}   



class VIEW3D_TP_Skin_Modifier_Empty(bpy.types.Operator):
    """Add a skin modifier to object with one vertex"""
    bl_idname = "tp_ops.add_skin_empty"
    bl_label = "Skin: Empty"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_center()        

        bpy.ops.mesh.primitive_plane_add(radius=10, view_align=False, enter_editmode=True, location=(0, 0, 0)) 
        bpy.ops.mesh.merge(type='CENTER')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
        bpy.ops.object.modifier_add(type='SKIN')
        bpy.context.object.modifiers["Skin"].use_smooth_shade = True
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.skin_root_mark()
        bpy.ops.object.mode_set(mode = 'OBJECT')

        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subsurf"].levels = 3          

        bpy.ops.object.mode_set(mode = 'EDIT')  
        return {"FINISHED"}



class VIEW3D_TP_Skin_Modifier_Human(bpy.types.Operator):
    """Add a skin modifier to object with one human biped"""
    bl_idname = "tp_ops.add_skin_human"
    bl_label = "Skin: Human"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        bpy.ops.view3d.snap_cursor_to_center()        

        bpy.ops.mesh.primitive_plane_add(radius=10, view_align=False, enter_editmode=True, location=(0, 0, 0)) 
        bpy.ops.mesh.merge(type='CENTER')

        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        bpy.ops.object.modifier_add(type='SKIN')
        bpy.context.object.modifiers["Skin"].use_smooth_shade = True
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.skin_root_mark()        
        bpy.ops.mesh.select_all(action='SELECT')        

        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        bpy.ops.transform.skin_resize(value=(10, 10, 10))
        bpy.ops.transform.translate(value=(-8.55175, 0, 2.91786), constraint_axis=(True, False, True), constraint_orientation='GLOBAL')        

        # heel       
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -1.45893, 2.63078), "constraint_axis":(False, True, True)})

        # knuckle1
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -2.77197, 4.99849), "constraint_axis":(False, True, True)})

        # toe
        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, -17.6862, -5.26157), "constraint_axis":(False, True, True)})

        # feet
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 9.20946, 0), "constraint_axis":(False, True, True)})    
       
        # knuckle2
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 8.47674, 5.26157), "constraint_axis":(False, True, True)})

        # knee
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 45.121), "constraint_axis":(True, False, True)})

        # leg
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(-4.47071, 0, 33.9487), "constraint_axis":(True, False, True)})

        # hip
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(13.0225, 0, 11.0722), "constraint_axis":(True, False, True)})
        bpy.ops.transform.skin_resize(value=(2.5, 2.5, 2.5))  
        bpy.ops.object.skin_root_mark()

        # chest
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 44.9539), "constraint_axis":(True, False, True)})
        bpy.ops.transform.skin_resize(value=(2.5, 2.5, 2.5))  

        
        # chin
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 9.98054), "constraint_axis":(True, False, True)})
        bpy.ops.transform.skin_resize(value=(0.2, 0.2, 0.2))  
       
        # nose1
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 7.20025), "constraint_axis":(True, False, True)})
        bpy.ops.transform.skin_resize(value=(2, 2, 2))       

        # nose2
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 2.5), "constraint_axis":(True, False, True)})
        bpy.ops.transform.skin_resize(value=(1.4, 1.4, 1.4))

        # head
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 10.1), "constraint_axis":(True, False, True)})    
 
        # finger 
        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(-33.8463, 0, -100.9), "constraint_axis":(True, False, True)})
        bpy.ops.transform.skin_resize(value=(0.4, 0.4, 0.4))  

        # wrist
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(2.66087, 0, 16.4383), "constraint_axis":(True, False, True)})

        # elbow
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(8.95826, 0, 22.987), "constraint_axis":(True, False, True)})

        # shoulder
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(3.21316, 0, 27.9946), "constraint_axis":(True, False, True)})

        # chest        
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(19.014, 0, 3.79982), "constraint_axis":(True, False, True)})


        bpy.ops.mesh.select_all(action='SELECT')        
        bpy.ops.mesh.remove_doubles(threshold=1)

        bpy.ops.object.mode_set(mode = 'OBJECT')

        # subsurf
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subsurf"].levels = 3          

        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        for x in range(20):
            bpy.ops.object.modifier_move_up(modifier="Mirror")    

        return {"FINISHED"}



class VIEW3D_TP_Skin_Modifier_Animal(bpy.types.Operator):
    """Add a skin modifier to object with one vertex"""
    bl_idname = "tp_ops.add_skin_animal"
    bl_label = "Skin: Empty"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
      
        bpy.ops.view3d.snap_cursor_to_center()        

        bpy.ops.mesh.primitive_plane_add(radius=10, view_align=False, enter_editmode=True, location=(0, 0, 0)) 
        bpy.ops.mesh.merge(type='CENTER')

        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        bpy.ops.object.modifier_add(type='SKIN')
        bpy.context.object.modifiers["Skin"].use_smooth_shade = True
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.skin_root_mark()        
        bpy.ops.mesh.select_all(action='SELECT')        

        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        bpy.ops.transform.skin_resize(value=(10, 10, 10))
        bpy.ops.transform.translate(value=(-17.1322, -37.2628, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL')        
     
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 1.31477, 3.46248), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 3.94616, 7.65407), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 6.22604, 9.1684), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 5.06193, 21.3253), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 1.43073, 20.1507), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -11.3891, 30.0805), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 2.6566, 26.627), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 17.1321, -25.9945, 25.6244), "constraint_axis":(True, True, True)})

        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(-13.7779, -94.1869, -140.977), "constraint_axis":(True, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 5.39806, 10.4072), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, 4.78163, 7.62542), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -4.08398, 30.9747), "constraint_axis":(False, True, True)})        
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -2.23752, 40.8848), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -13.1433, 25.5702), "constraint_axis":(True, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 13.7779, 13.1216, 21.9105), "constraint_axis":(True, True, True)})

        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":( 0, 146.49, -47.0935), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -1.56142, 20.6632), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -3.90362, 19.7263), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -26.532, 17.3794), "constraint_axis":(False, True, True)})   
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -22.7376, -7.30551), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -91.3968, -6.02191), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -11.4068, 3.6391), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -10.5264, 5.58046), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -10.1513, 5.9657), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -16.0199, 3.78235), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -15.1327, 1.67267), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -10.8348, -6.85899), "constraint_axis":(False, True, True)})
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":( 0, -12.9082, -39.7826), "constraint_axis":(False, True, True)})


        bpy.ops.mesh.select_all(action='SELECT')        
        bpy.ops.mesh.remove_doubles(threshold=3)

        bpy.ops.object.mode_set(mode = 'OBJECT')

        # subsurf
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subsurf"].levels = 3          

        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        for x in range(20):
            bpy.ops.object.modifier_move_up(modifier="Mirror")          

        return {"FINISHED"}





    
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()