368# ##### BEGIN GPL LICENSE BLOCK #####
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
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  


class VIEW3D_MT_SnapSet_Menu_Pencil(bpy.types.Menu):
    bl_label = "Annotate"
    bl_idname = "VIEW3D_MT_SnapSet_Menu_Pencil"

    def draw(self, context):
        layout = self.layout
      
        addon_prefs = context.preferences.addons[__package__].preferences
        layout.scale_y = addon_prefs.pie_scale_y_b4 #1   

        icons = load_icons()  
        
        button_snap_annotate = icons.get("icon_snap_annotate")
        layout.operator("wm.tool_set_by_id", text="Free", icon_value=button_snap_annotate.icon_id).name = "builtin.annotate"

        button_snap_annotate_line = icons.get("icon_snap_annotate_line")
        layout.operator("wm.tool_set_by_id", text="Line", icon_value=button_snap_annotate_line.icon_id).name = "builtin.annotate_line"

        button_snap_annotate_polygon = icons.get("icon_snap_annotate_polygon")
        layout.operator("wm.tool_set_by_id", text="Polygon", icon_value=button_snap_annotate_polygon.icon_id).name = "builtin.annotate_polygon"

        button_snap_annotate_eraser = icons.get("icon_snap_annotate_eraser")
        layout.operator("wm.tool_set_by_id", text="Eraser", icon_value=button_snap_annotate_eraser.icon_id).name = "builtin.annotate_eraser"

        layout.separator()
        
        layout.operator("gpencil.data_add", text="Add Layer", icon="ADD")
        layout.operator("gpencil.layer_remove", text="Remove Layer", icon="REMOVE")

        layout.separator()

        layout.operator("gpencil.data_unlink", text="Data Unlink", icon="UNLINKED")


      




# UI: HOTKEY MENU PIE # 
class VIEW3D_MT_SnapSet_Menu_Pie(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Menu_Pie"

    def draw(self, context):
        layout = self.layout
       
        addon_prefs = context.preferences.addons[__package__].preferences

        icons = load_icons()  

        layout.operator_context = 'INVOKE_REGION_WIN'

        # from space_view3d.py
        obj = context.active_object
        object_mode = 'OBJECT' if obj is None else obj.mode
        has_pose_mode = (
            (object_mode == 'POSE') or
            (object_mode == 'WEIGHT_PAINT' and context.pose_object is not None)
        )

        tool_settings = context.tool_settings

        # Mode & Transform Settings
        scene = context.scene



        # PIE MENU LAYOUT #
        pie = layout.menu_pie()      


        #Box 1 L
        row = pie.split().column()
        row.scale_x = addon_prefs.pie_scale_x_b1 #1.1       
        row.scale_y = addon_prefs.pie_scale_y_b1 #1  

        if addon_prefs.use_internal_icon_btd == True:
            row.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon=addon_prefs.icon_btd) 
        else:
            button_snap_active = icons.get("icon_snap_active")            
            row.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon_value=button_snap_active.icon_id) 

        
        #Box 2 R
        row = pie.split().column()
        row.scale_x = addon_prefs.pie_scale_x_b2 #1.1          
        row.scale_y = addon_prefs.pie_scale_y_b2 #1
        
        if addon_prefs.use_internal_icon_bte == True:
            row.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon=addon_prefs.icon_bte)
        else:           
            button_snap_closest = icons.get("icon_snap_closest")
            row.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon_value=button_snap_closest.icon_id)
            
       
        #Box 3 B
        row = pie.split().column()
        row.scale_x = addon_prefs.pie_scale_x_b3 #1.1         
        row.scale_y = addon_prefs.pie_scale_y_b3 #1
        
        if addon_prefs.use_internal_icon_btc == True:     
            row.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon=addon_prefs.icon_btc) 
        else:       
            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon_value=button_snap_cursor.icon_id) 

     
        #Box 4 T 
        box = pie.split().column(align = False)

        if addon_prefs.pie_menu_box4 == True:
            box.scale_x = 1.2           
            
            row = box.row(align = False)          
            button_snap_annotate = icons.get("icon_snap_annotate")                
            row.menu("VIEW3D_MT_SnapSet_Menu_Pencil", text='Pencil Tools', icon_value=button_snap_annotate.icon_id) 
       
        else:
            box.scale_x = addon_prefs.pie_scale_b_b4 #0.65

            row = box.row(align = False)
            row.scale_x = addon_prefs.pie_scale_x_b4 #1          
            row.scale_y = addon_prefs.pie_scale_y_b4 #1                       
           
            if addon_prefs.pie_menu_box4_transform == True: 

                button_snap_move = icons.get("icon_snap_move")
                row.operator("wm.tool_set_by_id", text=" ", icon_value=button_snap_move.icon_id).name = "builtin.move"
                
                button_snap_rotate = icons.get("icon_snap_rotate")                
                row.operator("wm.tool_set_by_id", text=" ", icon_value=button_snap_rotate.icon_id).name = "builtin.rotate"

                button_snap_scale = icons.get("icon_snap_scale")
                row.operator("wm.tool_set_by_id", text=" ", icon_value=button_snap_scale.icon_id).name = "builtin.scale"

                button_snap_measure = icons.get("icon_snap_measure")                
                row.operator("wm.tool_set_by_id", text=" ", icon_value=button_snap_measure.icon_id).name = "builtin.measure"   
            
            button_snap_annotate = icons.get("icon_snap_annotate")   
            if addon_prefs.pie_menu_box4_menu_name == False:                              
                row.menu("VIEW3D_MT_SnapSet_Menu_Pencil", text="Pencil Tools", icon_value=button_snap_annotate.icon_id)            
            else:
                row.menu("VIEW3D_MT_SnapSet_Menu_Pencil", text=" ", icon_value=button_snap_annotate.icon_id)            
                

            if addon_prefs.pie_menu_box5 == False or addon_prefs.pie_menu_box4_pivots == False: 

                row = box.row(align = False)     
                row.scale_x = addon_prefs.pie_scale_x_b4 #1          
                row.scale_y = addon_prefs.pie_scale_y_b4 #1  

                if bpy.context.scene.tool_settings.transform_pivot_point == 'BOUNDING_BOX_CENTER':   
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_BOUNDBOX", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="BOUNDING_BOX_CENTER"
                else:
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_BOUNDBOX").tpc_pivot="BOUNDING_BOX_CENTER"
                    
                if bpy.context.scene.tool_settings.transform_pivot_point == 'CURSOR':                   
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_CURSOR", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="CURSOR"
                else:
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_CURSOR").tpc_pivot="CURSOR"
                
                if bpy.context.scene.tool_settings.transform_pivot_point == 'ACTIVE_ELEMENT':              
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_ACTIVE", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="ACTIVE_ELEMENT"
                else:                
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_ACTIVE").tpc_pivot="ACTIVE_ELEMENT"

                if bpy.context.scene.tool_settings.transform_pivot_point == 'INDIVIDUAL_ORIGINS':               
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_INDIVIDUAL", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="INDIVIDUAL_ORIGINS"
                else:
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_INDIVIDUAL").tpc_pivot="INDIVIDUAL_ORIGINS"

                if bpy.context.scene.tool_settings.transform_pivot_point == 'MEDIAN_POINT':       
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_MEDIAN", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="MEDIAN_POINT" 
                else:                
                    row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_MEDIAN").tpc_pivot="MEDIAN_POINT" 



        #Box 5 LT
        box = pie.split().column(align = False)
              
        if addon_prefs.pie_menu_box5 == True:   

            box.scale_x = 1.2

            # Snap
            show_snap = False
            if obj is None:
                show_snap = True
            else:
                if (object_mode not in {
                        'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT',
                        'PAINT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_GPENCIL'
                }) or has_pose_mode:
                    show_snap = True
                else:

                    from bl_ui.properties_paint_common import UnifiedPaintPanel
                    paint_settings = UnifiedPaintPanel.paint_settings(context)

                    if paint_settings:
                        brush = paint_settings.brush
                        if brush and brush.stroke_method == 'CURVE':
                            show_snap = True

            if show_snap:
                snap_items = bpy.types.ToolSettings.bl_rna.properties["snap_elements"].enum_items
                snap_elements = tool_settings.snap_elements
                if len(snap_elements) == 1:
                    text = "Snap"

                    if tool_settings.snap_elements == {'INCREMENT'}:
                        text='Increment'             
                    elif tool_settings.snap_elements == {'VERTEX'}:
                        text='Vertex'                                                           
                    elif tool_settings.snap_elements == {'EDGE'}:
                        text='Edge'                      
                    elif tool_settings.snap_elements == {'FACE'}:
                        text='Face'   
                    elif tool_settings.snap_elements == {'VOLUME'}:
                        text='Volume'  
                    else: 
                        text='Snap'                    

                    for elem in snap_elements:
                        icon = snap_items[elem].icon
                        break
                else:
                    text = "MixSnap"
                    icon = 'NONE'
                del snap_items, snap_elements
                
                row = box.row(align=True)                      
                row.popover(panel="VIEW3D_PT_snapping", icon=icon, text=text)                  
                row.prop(tool_settings, "use_snap", text="")
      

            # Proportional editing
            if object_mode in {'EDIT', 'PARTICLE_EDIT', 'SCULPT_GPENCIL', 'EDIT_GPENCIL', 'OBJECT'}:

                kw = {}
                if object_mode == 'OBJECT':
                    attr = "use_proportional_edit_objects"
                else:
                    attr = "use_proportional_edit"

                    if tool_settings.use_proportional_edit:
                        if tool_settings.use_proportional_connected:
                            kw["icon"] = 'PROP_CON'
                        elif tool_settings.use_proportional_projected:
                            kw["icon"] = 'PROP_PROJECTED'
                        else:
                            kw["icon"] = 'PROP_ON'
                    else:
                        kw["icon"] = 'PROP_OFF'
             
                if tool_settings.proportional_edit_falloff == 'SMOOTH':
                    text='Smooth'
                    icon='SMOOTHCURVE'                
                elif tool_settings.proportional_edit_falloff == 'SPHERE':    
                    text='Sphere'                    
                    icon='SPHERECURVE'
                elif tool_settings.proportional_edit_falloff == 'ROOT':    
                    text='Root'                    
                    icon='ROOTCURVE'
                elif tool_settings.proportional_edit_falloff == 'INVERSE_SQUARE':    
                    text='Inverse Square'                    
                    icon='INVERSESQUARECURVE'
                elif tool_settings.proportional_edit_falloff == 'SHARP':    
                    text='Sharp'                    
                    icon='SHARPCURVE'
                elif tool_settings.proportional_edit_falloff == 'LINEAR':    
                    text='Linear'                    
                    icon='LINCURVE'                                    
                elif tool_settings.proportional_edit_falloff == 'CONSTANT':    
                    text='Constant'                    
                    icon='NOCURVE'                                      
                elif tool_settings.proportional_edit_falloff == 'RANDOM':    
                    text='Random'                    
                    icon='RNDCURVE'                                      
                else:
                    text='Proportional'                    
                    icon=''    
   
                row = box.row(align=True)
                row.popover(panel="VIEW3D_PT_proportional_edit", text=text, icon=icon)
                row.prop(tool_settings, attr, icon_only=True, **kw, text="")


        else:
            box.scale_x = addon_prefs.pie_scale_b_b5 #0.65
        
            row = box.row(align = False)  
            row.scale_x = addon_prefs.pie_scale_x_b5 #1          
            row.scale_y = addon_prefs.pie_scale_y_b5 #1    

            if bpy.context.scene.tool_settings.snap_elements == {'VERTEX'}:            
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VERTEX", emboss = addon_prefs.tpc_use_emposs).tpc_snape="VERTEX"       
            else:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VERTEX").tpc_snape="VERTEX"        

            if bpy.context.scene.tool_settings.snap_elements == {'EDGE'}:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_EDGE", emboss = addon_prefs.tpc_use_emposs).tpc_snape="EDGE"        
            else:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_EDGE").tpc_snape="EDGE"        

            if bpy.context.scene.tool_settings.snap_elements == {'FACE'}:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_FACE", emboss = addon_prefs.tpc_use_emposs).tpc_snape="FACE"
            else:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_FACE").tpc_snape="FACE" 
              
     
            row = box.row(align = False)
            row.scale_x = addon_prefs.pie_scale_x_b5 #1          
            row.scale_y = addon_prefs.pie_scale_y_b5 #1     

            if bpy.context.scene.tool_settings.snap_elements == {'VOLUME'}:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VOLUME", emboss = addon_prefs.tpc_use_emposs).tpc_snape="VOLUME" 
            else:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VOLUME").tpc_snape="VOLUME"  

            if bpy.context.scene.tool_settings.snap_elements == {'INCREMENT'}:                                    
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_INCREMENT", emboss = addon_prefs.tpc_use_emposs).tpc_snape="INCREMENT"        
            else:
                row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_INCREMENT").tpc_snape="INCREMENT"        
            
            if bpy.context.scene.tool_settings.use_snap == True:                                    
                row.operator("tpc_ot.snap_use", text=" ", icon = "SNAP_ON", emboss = addon_prefs.tpc_use_emposs).mode="unuse_snap"        
            else:
                row.operator("tpc_ot.snap_use", text=" ", icon = "SNAP_OFF").mode="use_snap"    


        #Box 6 RT 
        box = pie.split().column(align = False)   

        if addon_prefs.pie_menu_box6 == True:                             

            box.scale_x = 1.2

            row = box.row(align = False)       
          
            # Pivot
            if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL'} or has_pose_mode:

                if bpy.context.scene.tool_settings.transform_pivot_point == 'BOUNDING_BOX_CENTER':
                    text='Bounding Box'
                    icon='PIVOT_BOUNDBOX'                
                elif bpy.context.scene.tool_settings.transform_pivot_point == 'CURSOR':    
                    text='3D Cursor'                    
                    icon='PIVOT_CURSOR'
                elif bpy.context.scene.tool_settings.transform_pivot_point == 'INDIVIDUAL_ORIGINS':    
                    text='Individual Origins'                    
                    icon='PIVOT_INDIVIDUAL'
                elif bpy.context.scene.tool_settings.transform_pivot_point == 'MEDIAN_POINT':    
                    text='Median Point'                    
                    icon='PIVOT_MEDIAN'
                elif bpy.context.scene.tool_settings.transform_pivot_point == 'ACTIVE_ELEMENT':    
                    text='Active Element'                    
                    icon='PIVOT_ACTIVE'
                else:
                    text='Pivot Point'
                    icon='PIVOT_MEDIAN'   
                    
                row = box.row(align = False)  
                row.popover(panel="VIEW3D_PT_pivot_point", text=text, icon=icon)

            row = box.row(align = False)  

            # Orientation
            if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL'} or has_pose_mode:
                
                if bpy.context.scene.transform_orientation_slots[0].type == 'GLOBAL':
                    text='Global'
                    icon='ORIENTATION_GLOBAL'                
                elif bpy.context.scene.transform_orientation_slots[0].type == 'LOCAL':    
                    text='Local'                    
                    icon='ORIENTATION_LOCAL'
                elif bpy.context.scene.transform_orientation_slots[0].type == 'NORMAL':    
                    text='Normal'                    
                    icon='ORIENTATION_NORMAL'
                elif bpy.context.scene.transform_orientation_slots[0].type == 'GIMBAL':    
                    text='Gimbal'                    
                    icon='ORIENTATION_GIMBAL'
                elif bpy.context.scene.transform_orientation_slots[0].type == 'VIEW':    
                    text='View'                    
                    icon='ORIENTATION_VIEW'
                elif bpy.context.scene.transform_orientation_slots[0].type == 'CURSOR':    
                    text='Cursor'                    
                    icon='ORIENTATION_CURSOR'                                                                       
                else:
                    text='Orientation'                    
                    icon='ORIENTATION_GLOBAL'    

                orient_slot = scene.transform_orientation_slots[0]
                row.popover(panel="VIEW3D_PT_transform_orientations", text=text, icon=icon)


        else:
            box.scale_x = addon_prefs.pie_scale_b_b6 #0.75  

            row = box.row(align = False)
            row.scale_x = addon_prefs.pie_scale_x_b6 #1          
            row.scale_y = addon_prefs.pie_scale_y_b6 #1     
          
            if bpy.context.scene.transform_orientation_slots[0].type == 'GLOBAL':         
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GLOBAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="GLOBAL"        
            else:        
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GLOBAL").tpc_axis="GLOBAL"        

            if bpy.context.scene.transform_orientation_slots[0].type == 'LOCAL':   
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_LOCAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="LOCAL"
            else:
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_LOCAL").tpc_axis="LOCAL"

            if bpy.context.scene.transform_orientation_slots[0].type == 'NORMAL':   
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_NORMAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="NORMAL"
            else:    
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_NORMAL").tpc_axis="NORMAL"

          
            row = box.row(align = False)  
            row.scale_x = addon_prefs.pie_scale_x_b6 #1    
            row.scale_x = addon_prefs.pie_scale_y_b6 #1    
                 
            if bpy.context.scene.transform_orientation_slots[0].type == 'GIMBAL':   
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GIMBAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="GIMBAL"
            else:    
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GIMBAL").tpc_axis="GIMBAL"                 

            if bpy.context.scene.transform_orientation_slots[0].type == 'VIEW':   
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_VIEW", emboss = addon_prefs.tpc_use_emposs).tpc_axis="VIEW"
            else:    
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_VIEW").tpc_axis="VIEW"    

            if bpy.context.scene.transform_orientation_slots[0].type == 'CURSOR':   
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_CURSOR", emboss = addon_prefs.tpc_use_emposs).tpc_axis="CURSOR"
            else:    
                row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_CURSOR").tpc_axis="CURSOR"    


        #Box 7 LB 
        row = pie.split().column()                  
        row.scale_x = addon_prefs.pie_scale_x_b7 #1.1                      
        row.scale_y = addon_prefs.pie_scale_y_b7 #1  
        
        if context.mode == 'OBJECT':
            if addon_prefs.tpc_use_place_modal == True:
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tpc_ot.snapset_modal", text="PlaceM", icon_value=button_snap_place.icon_id).mode = "PLACE"

            if addon_prefs.tpc_use_place == True:
                if addon_prefs.use_internal_icon_btb == True:   
                    row.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon=addon_prefs.icon_btb)
                else:
                    button_snap_place = icons.get("icon_snap_place")
                    row.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon_value=button_snap_place.icon_id)

        else:
            if addon_prefs.tpc_use_retopo_modal == True:              
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tpc_ot.snapset_modal", text="RetopoM", icon_value=button_snap_retopo.icon_id).mode = "RETOPO"   

            if addon_prefs.tpc_use_retopo == True:
                if addon_prefs.use_internal_icon_btf == True:   
                    row.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon=addon_prefs.icon_btf)    
                else:
                    button_snap_retopo = icons.get("icon_snap_retopo")
                    row.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon_value=button_snap_retopo.icon_id)    
           
          

        #Box 8 RB
        row = pie.split().column()                  
        row.scale_x = addon_prefs.pie_scale_x_b8 #1.1                     
        row.scale_y = addon_prefs.pie_scale_y_b8 #1
        
        if addon_prefs.tpc_use_grid_modal == True:
            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tpc_ot.snapset_modal", text="GridM", icon_value=button_snap_grid.icon_id).mode = "GRID"

        if addon_prefs.tpc_use_grid == True:
            if addon_prefs.use_internal_icon_bta == True:  
                row.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon=addon_prefs.icon_bta)
            else:
                button_snap_grid = icons.get("icon_snap_grid")
                row.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon_value=button_snap_grid.icon_id)



