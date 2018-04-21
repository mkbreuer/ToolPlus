import bpy
import addon_utils

class VIEW3D_TP_Machine_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Machine_Menu"
    bl_label = "MESHmachine"

    def draw(self, context):
        layout = self.layout

        layout.scale_y = 1.2

        meshmaschine_addon = "MESHmachine" 
        state = addon_utils.check(meshmaschine_addon)
        if not state[0]:   
            layout.label("Please activate MESHmachine")    
        else:   
            # MAIN -------------------------------------------------------

            # Fuse
            op = layout.operator("machin3.fuse", text="Fuse")
            op.width = 0
            op.reverse = False

            # Chamfer Width
            op = layout.operator("machin3.change_width", text="Width")
            op.width = 0

            # Flatten
            layout.operator("machin3.flatten", text="Flatten")

            # UN-TOOLS -------------------------------------------------------
            layout.separator()

            # Unf*ck
            op = layout.operator("machin3.unfuck", text="Unf*ck")
            op.propagate = 0
            op.width = 0

            # Unfuse
            op = layout.operator("machin3.unfuse", text="Unfuse")

            # Refuse
            op = layout.operator("machin3.refuse", text="Refuse")
            op.width = 0
            op.reverse = False
            op.init = True

            # Unbevel
            op = layout.operator("machin3.unbevel", text="Unbevel")

            # Unchamfer
            layout.operator("machin3.unchamfer", text="Unchamfer")

            # CORNER TOOLS -------------------------------------------------------
            layout.separator()

            # Turn Corner
            layout.operator("machin3.turn_corner", text="Turn Corner")

            # Quad Corner
            layout.operator("machin3.quad_corner", text="Quad Corner")



class VIEW3D_TP_Machine_Align_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Machine_Align_Menu"
    bl_label = "MESHmachine"

    def draw(self, context):
        layout = self.layout

        layout.scale_y = 1.2

        meshmaschine_addon = "MESHmachine" 
        state = addon_utils.check(meshmaschine_addon)
        if not state[0]:   
            layout.label("Please activate MESHmachine")    
        else:   
            # MAIN -------------------------------------------------------

            # Fuse
            op = layout.operator("machin3.fuse", text="Fuse")
            op.width = 0
            op.reverse = False

            # Chamfer Width
            op = layout.operator("machin3.change_width", text="Width")
            op.width = 0

            # Flatten
            layout.operator("machin3.flatten", text="Flatten")

            # UN-TOOLS -------------------------------------------------------
            layout.separator()

            # Unf*ck
            op = layout.operator("machin3.unfuck", text="Unf*ck")
            op.propagate = 0
            op.width = 0

            # Unfuse
            op = layout.operator("machin3.unfuse", text="Unfuse")

            # Refuse
            op = layout.operator("machin3.refuse", text="Refuse")
            op.width = 0
            op.reverse = False
            op.init = True

            # Unbevel
            op = layout.operator("machin3.unbevel", text="Unbevel")

            # Unchamfer
            layout.operator("machin3.unchamfer", text="Unchamfer")

            # CORNER TOOLS -------------------------------------------------------
            layout.separator()

            # Turn Corner
            layout.operator("machin3.turn_corner", text="Turn Corner")

            # Quad Corner
            layout.operator("machin3.quad_corner", text="Quad Corner")

                