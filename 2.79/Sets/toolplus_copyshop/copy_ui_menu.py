import bpy


class View3D_TP_Copy_Menu(bpy.types.Menu):
    """CopyShop"""
    bl_label = "CopyShop"
    bl_idname = "tp_menu.copyshop_menu"

    def draw(self, context):
        layout = self.layout
            
        layout.operator_context = 'INVOKE_REGION_WIN'

        display_copy = context.user_preferences.addons[__package__].preferences.tab_menu_copy
        if display_copy == 'on':
               
                mode_string = context.mode                
                if mode_string == 'OBJECT':
                    layout.operator("object.duplicate_move", text="Copy", icon="MOD_BOOLEAN")
                    layout.operator("object.duplicate_move_linked", text="Link-Copy", icon="CONSTRAINT_DATA")    
                elif mode_string == 'EDIT_MESH':
                    layout.operator("mesh.duplicate_move", text="Copy", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_CURVE':
                    layout.operator("curve.duplicate_move", text="Copy", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_SURFACE':
                    layout.operator("curve.duplicate_move", text="Copy", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_METABALL':
                    layout.operator("mball.duplicate_move", text="Copy", icon="MOD_BOOLEAN")
                elif mode_string == 'EDIT_ARMATURE':
                    layout.operator("armature.duplicate_move", text="Copy", icon="MOD_BOOLEAN")

                layout.separator()

                layout.operator("tp_ops.copy_to_cursor", text="Copy to Cursor", icon="NEXT_KEYFRAME")

        mode_string = context.mode                
        if mode_string == 'OBJECT':
                
            layout.operator("mft.radialclone", text="Radial Z-Clone", icon="FILE_REFRESH")
            layout.operator("tp_ops.copy_to_mesh", text="Copy to Mesh",icon="UV_FACESEL")        
            
        
            display_arewo = context.user_preferences.addons[__package__].preferences.tab_menu_arewo
            if display_arewo == 'on':

                layout.separator()
                                    
                layout.operator("object.simplearewo", text="ARewO Replicator", icon="FRAME_NEXT") 


            display_array = context.user_preferences.addons[__package__].preferences.tab_menu_array
            if display_array == 'on':

                layout.separator()
                
                layout.menu("tp_menu.copyshop_array_menu", icon="MOD_ARRAY")


            display_array = context.user_preferences.addons[__package__].preferences.tab_menu_optimize
            if display_array == 'on':
                
                layout.separator()
                
                layout.menu("tp_menu.copyshop_optimize_menu", icon="UV_SYNC_SELECT")


            display_origin = context.user_preferences.addons[__package__].preferences.tab_menu_origin
            if display_origin == 'on':

                layout.separator()
                
                layout.menu("tp_menu.copyshop_origin_menu", icon="LAYER_ACTIVE")
                    



class View3D_TP_Copy_Origin_Menu(bpy.types.Menu):
    """Set Origin"""
    bl_label = "Set Origin"
    bl_idname = "tp_menu.copyshop_origin_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("tp_ops.origin_plus_z", text="Top", icon="LAYER_USED")  
        props = layout.operator("object.origin_set", text="Middle", icon="LAYER_USED")
        props.type = 'ORIGIN_GEOMETRY'
        props.center = 'BOUNDS'
        layout.operator("tp_ops.origin_minus_z", text="Bottom", icon="LAYER_USED")


class View3D_TP_Copy_Optimize_Menu(bpy.types.Menu):
    """Optimize"""
    bl_label = "Optimize"
    bl_idname = "tp_menu.copyshop_optimize_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.make_links_data","Set", icon="LINKED").type='OBDATA'
        layout.operator("tp_ops.make_single","Clear", icon="UNLINKED")                        
        layout.operator("object.select_linked", text="S-Linked", icon="RESTRICT_SELECT_OFF")   
        layout.operator("object.join", text="Join all", icon="AUTOMERGE_ON")   



class View3D_TP_Copy_Array_Menu(bpy.types.Menu):
    """ArrayTools"""
    bl_label = "ArrayTools"
    bl_idname = "tp_menu.copyshop_array_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("tp_ops.x_array", text="X Array")    
        layout.operator("tp_ops.y_array", text="Y Array")    
        layout.operator("tp_ops.z_array", text="Z Array")   
        
        

def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.register_module(__name__)

if __name__ == "__main__":
    register()


