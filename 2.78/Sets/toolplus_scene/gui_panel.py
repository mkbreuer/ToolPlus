# ##### BEGIN GPL LICENSE BLOCK #####
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
import bpy
from bpy import*
from bpy.props import *
from . icons.icons import load_icons

from .gui_visual import draw_visual_layout


bpy.types.Scene.tp_panel_type = bpy.props.EnumProperty(                            
                      items = [("layers",  "Layers",   "",  "OOPS",               1),                                 
                               ("rename",  "Rename",   "",  "OUTLINER_DATA_FONT", 2)],  
                               name = "Panel Type", 
                               default = "layers", 
                               description="panel type")


# LAYOUT #
def draw_scene_panel_layout(self, context, layout):
        tp_props = context.window_manager.tp_collapse_menu_layer

        icons = load_icons()     
        #my_button_one = icons.get("icon_image1")
        
        scene = context.scene
     
        col = layout.column(1)

        if context.mode == 'OBJECT': 

            box = col.box().column(1)   

            row = box.row(1)              
            row.alignment = 'CENTER'
            row.prop(context.scene, 'tp_panel_type',  emboss = False, expand = True) #icon_only=True,

            box.separator() 
          
            if scene.tp_panel_type == "layers":          
                
                box = col.box().column(1)
                
                row = box.row()
                col = row.column()
                col.template_list("layers_collection_UL", "", context.scene, "display_layers_collection", context.scene, "display_layers_collection_index", rows = 6)

                col = row.column()
                sub = col.column(1)
                sub.operator("add_layer_from_collection.btn", icon='ZOOMIN', text="")
                sub.operator("remove_layer_from_collection.btn", icon='ZOOMOUT', text="")
                sub.operator("clear_display_layers_collection.btn", icon="X", text="")  
                sub.operator("up_layer_from_collection.btn", icon='TRIA_UP', text="")
                sub.operator("down_layer_from_collection.btn", icon='TRIA_DOWN', text="")        
                         
                sub1= col.column(1)
                sub1.scale_y = 2                
                sub1.operator("select_objects.btn", icon="RESTRICT_SELECT_OFF", text="")                 
                     
                box.separator()    

                objs = bpy.context.scene.objects
                if objs:   
                                  
                    row = box.row(1)
                    row.operator("assign_layer.btn", icon="DISCLOSURE_TRI_RIGHT", text="Assign")                                   
                    row.prop(context.scene, "tp_modly_type", text="")                    
                    row.operator("tp_ops.copy_choosen_mods", text="", icon='PASTEDOWN') 
   
                    row =box.row(1)                
                    row.operator("remove_layer.btn", icon="DISCLOSURE_TRI_DOWN", text="Remove")      
                    
                    sub = row.row(1)                 
                    sub.enabled = context.object.use_display_layer
                    sub.prop(context.scene, "tp_funcly_type", text="")
                                   
                    if tp_props.display_layer_id: 
                        row.prop(tp_props, "display_layer_id", text="", icon="SCRIPTWIN")  
                    else:                  
                        row.prop(tp_props, "display_layer_id", text="", icon="SCRIPTWIN")                                       
                  
                    box.separator()

                    if tp_props.display_layer_id: 
                        
                        col = layout.column(1)
                        
                        box = col.box().column(1) 

                        row = box.row()
                        row.prop(context.object, "use_display_layer")
                        row.prop(context.object, "display_layer")

                        layer_id = context.object.display_layer
                        if layer_id < len(context.scene.display_layers_collection.items()):
                           
                            row = box.row()
                            row.label("Name : " + context.scene.display_layers_collection[layer_id].name)



            if scene.tp_panel_type == "rename":

                obj = context.object
                if obj:   
                
                    box = col.box().column(1)       
                   
                    row = box.row(1)                 
                    row.prop(context.object , "name", text="Name", icon = "COPY_ID") 
                    row.operator("tp_ops.copy_name_to_meshdata", text= "", icon ="PASTEDOWN")

                    row = box.row(1)      
                    row.prop(context.object.data , "name", text="Data", icon = "OUTLINER_DATA_MESH") 
                    row.operator("tp_ops.copy_data_name_to_object", text= "", icon ="COPYDOWN")
                    
                    box.separator()
                    
                    box = col.box().column(1)    
                   
                    row = box.row(1) 
                    row.prop(context.scene,'rno_bool_keepOrder',text='')         
                    row.enabled = False
                    row.operator("object.rno_keep_selection_order", "Respect Selection")


                    box = col.box().column(1)                     

                    row = box.row(1) 
                    row.prop(context.scene,"rno_str_new_name", "Name",)
                    
                    box.separator() 
                            
                    row = box.row(1) 
                    row.prop(context.scene,"rno_bool_numbered")
                    row.prop(context.scene,"rno_str_numFrom")
                    
                    box.separator() 
                            
                    row = box.column(1)
                    row.operator("object.rno_setname", "Set new Name", icon ="FONT_DATA")
               
                    box.separator() 
                                
                    box = col.box().column(1)                     

                    row = box.column(1) 
                    row.prop(context.scene, "rno_str_old_string")
                    row.prop(context.scene, "rno_str_new_string")
                    
                    box.separator()
                    
                    row = box.row(1)         
                    row.operator("object.rno_replace_in_name", "Replace Old String Name")

                    box.separator()

                    box = layout.box().column(1)                     

                    row = box.row(1) 
                    row.prop(context.scene,'rno_bool_keepIndex',text='keep object Index')
                   
                    row = box.column(1)
                    row.prop(context.scene, "rno_str_prefix")
                    row.prop(context.scene, "rno_str_subfix")     
                    
                    box.separator()      




# LAYOUT #
def draw_smartjoin_panel_layout(self, context, layout):

        if context.mode == 'OBJECT': 

            col = layout.column(1)

            box = col.box().column(1)
            
            row =box.row(1)
            row.operator('sjoin.join', "Smart Join", icon="LOCKVIEW_ON")
            row.operator('sjoin.separate', "Separate", icon="LOCKVIEW_OFF")

            row =box.row(1)
            row.operator('sjoin.expand', "Expand", icon="PASTEDOWN")
            row.operator('sjoin.collapse', "Collapse", icon="COPYDOWN")

            row =box.row(1)            
            row.operator('sjoin.join_add', "Add 2 Smart", icon="PASTEFLIPUP")
            row.operator('sjoin.update_rec', "Update", icon="LOAD_FACTORY")         

            box.separator() 



# LAYOUT #
def draw_modifier_type_panel_layout(self, context, layout):
          
        box = layout.box().column(1)
 
        row = box.row(1)            
        row.prop(context.scene, "tp_mods_type", text="")
        row.prop(context.scene, "tp_func_type", text="")

        row = box.row(1)
        row.operator("tp_ops.copy_choosen_mods", text="CopyDial", icon='PASTEDOWN') 
        row.operator("tp_ops.mods_by_type", text="RunTypes", icon='FRAME_NEXT')                            
       
        box.separator() 



# PANEL #
class VIEW3D_TP_Scene_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Scene_Panel_TOOLS"
    bl_label = "T+Scene"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_context = 'objectmode'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'


        display_modly = context.user_preferences.addons[__package__].preferences.tab_display_modly
        if display_modly == 'on':   

            draw_scene_panel_layout(self, context, layout) 


        display_smjoint = context.user_preferences.addons[__package__].preferences.tab_display_smjoint
        if display_smjoint == 'on':

            draw_smartjoin_panel_layout(self, context, layout)


        display_modtl = context.user_preferences.addons[__package__].preferences.tab_display_modtl
        if display_modtl == 'on':   
            
            draw_modifier_type_panel_layout(self, context, layout) 


        display_visual = context.user_preferences.addons[__package__].preferences.tab_display_visual
        if display_visual == 'on':

            draw_visual_layout(self, context, layout)     




# PANEL #
class VIEW3D_TP_Scene_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Scene_Panel_UI"
    bl_label = "T+Scene"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_context = 'objectmode'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'  


        display_modly = context.user_preferences.addons[__package__].preferences.tab_display_modly
        if display_modly == 'on':   

            draw_scene_panel_layout(self, context, layout) 


        display_smjoint = context.user_preferences.addons[__package__].preferences.tab_display_smjoint
        if display_smjoint == 'on':

            draw_smartjoin_panel_layout(self, context, layout)
 
 
        display_modtl = context.user_preferences.addons[__package__].preferences.tab_display_modtl
        if display_modtl == 'on':   
            
            draw_modifier_type_panel_layout(self, context, layout) 


        display_visual = context.user_preferences.addons[__package__].preferences.tab_display_visual
        if display_visual == 'on':

            draw_visual_layout(self, context, layout)     
