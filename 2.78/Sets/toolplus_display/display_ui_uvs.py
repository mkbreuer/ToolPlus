import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons
    
EDIT = ["EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']


class VIEW3D_TP_UVS_Panel_TOOLS(bpy.types.Panel):

    bl_category = "Shade / UVs"
    bl_idname = "VIEW3D_TP_UVS_Panel_TOOLS"
    bl_label = "UVs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        draw_uvs_panel_layout(self, context, layout) 


class VIEW3D_TP_UVS_Panel_UI(bpy.types.Panel):
    #bl_context = "mesh_edit"
    bl_idname = "VIEW3D_TP_UVS_Panel_UI"
    bl_label = "UVs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if GEOM:
                return isModelingMode and context.mode not in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        draw_uvs_panel_layout(self, context, layout) 




def draw_uvs_panel_layout(self, context, layout):
    tp = context.window_manager.tp_collapse_menu_display  

    icons = load_icons()


    if context.mode == 'OBJECT':

        box = layout.box().column(1) 

        obj = context.active_object
        if obj:
            row = box.row()   
            row.template_list("MESH_UL_uvmaps_vcols", "uvmaps", context.object.data, "uv_textures", context.object.data.uv_textures, "active_index", rows=2)
       
            row = row.column(1)
            row.operator("mesh.uv_texture_add", icon='ZOOMIN', text="")
            row.operator("mesh.uv_texture_remove", icon='ZOOMOUT', text="")                  
            if context.space_data.viewport_shade == 'SOLID':
                row.prop(context.space_data, "show_textured_solid", icon='TEXTURE_SHADED', text="")

            box.separator() 
            box.separator() 

        else:
            pass


                       
        row = box.column(1) 
        row.operator("uv.uv_equalize" , text ="UV Equalize", icon = 'MOD_UVPROJECT')           
        row.operator("uthe.main_operator", text = "UV HardEdges", icon = 'MOD_EDGESPLIT')



    if context.mode == 'EDIT_MESH':
        
        box = layout.box().column(1) 
          
        row = box.column(1)
        row.label(text="UV Mapping:")

        box.separator()
        
        row = box.row(1)        
        row.operator("mesh.mark_seam").clear = False
        row.operator("mesh.mark_seam", text="Clear Seam").clear = True

        box.separator()
        box.separator()
                    
     
        row = box.row(1)    
        
        if tp.display_unwrap:
            row.prop(tp, "display_unwrap", text="Unwrap", icon='TRIA_DOWN_BAR')
        else:
            row.prop(tp, "display_unwrap", text="Unwrap", icon='TRIA_UP_BAR')          
       

        if tp.display_uvmagic:
            row.prop(tp, "display_uvmagic", text="Magic UVs", icon='TRIA_DOWN_BAR')
        else:
            row.prop(tp, "display_uvmagic", text="Magic UVs", icon='TRIA_UP_BAR')          


        box.separator()
           

        row = box.row(1)    

        if tp.display_unwrap:

            #box = layout.box().column(1) 
          
            row = box.row(1)
            row.operator("uv.unwrap", text="Unwrap")
            row.operator("uv.reset",text="Reset")
                            
            row = box.row(1)
            row.operator("uv.smart_project", text="Smart UV Project")
                            
            row = box.row(1)
            row.operator("uv.lightmap_pack", text="Lightmap Pack")
                            
            row = box.row(1)
            row.operator("uv.follow_active_quads", text="Follow Active Quads")

            box.separator()                                         
            box.separator()                                         
            
            row = box.row(1)
            row.operator("uv.cube_project", text="Cube Project")
            
            row = box.row(1)
            row.operator("uv.cylinder_project", text="Cylinder Project")

            row = box.row(1)
            row.operator("uv.sphere_project", text="Sphere Project")

            row = box.row(1)
            row.operator("uv.tube_uv_unwrap", text="Tube Project")                

            box.separator()
            box.separator()
                                                       
            row = box.row(1)
            row.operator("uv.project_from_view", text="Project from View").scale_to_bounds = False

            row = box.row(1)
            row.operator("uv.project_from_view", text="Project from View > Bounds").scale_to_bounds = True 
            
            box.separator()       



        if tp.display_uvmagic:
            
            box = layout.box().column(1) 
                        
            row = box.column(1)
            row.operator("uv.cpuv_copy_uv")
            row.operator("uv.cpuv_paste_uv")
            row.operator("uv.flip_rotate")
            row.operator("uv.transfer_uv_copy")
            row.operator("uv.transfer_uv_paste")
            row.operator("uv.cpuv_selseq_copy_uv")
            row.operator("uv.cpuv_selseq_paste_uv")

            row.operator("uv.cpuv_uvmap_copy_uv_op")
            row.operator("uv.cpuv_uvmap_paste_uv_op")

            box.separator()  


