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
from bpy import *


# LOAD UI #
from toolplus_curve.cuv_panel           import (VIEW3D_TP_Curve_Compact_TOOLS)
from toolplus_curve.cuv_panel           import (VIEW3D_TP_Curve_Compact_UI)

from toolplus_curve.layouts.ui_insert   import (VIEW3D_TP_Curve_Insert_Panel_TOOLS)
from toolplus_curve.layouts.ui_insert   import (VIEW3D_TP_Curve_Insert_Panel_UI)

from toolplus_curve.layouts.ui_info     import (VIEW3D_TP_Curve_Info_Panel_TOOLS)
from toolplus_curve.layouts.ui_info     import (VIEW3D_TP_Curve_Info_Panel_UI)

from toolplus_curve.layouts.ui_select   import (VIEW3D_TP_Curve_Select_Panel_TOOLS)
from toolplus_curve.layouts.ui_select   import (VIEW3D_TP_Curve_Select_Panel_UI)

from toolplus_curve.layouts.ui_convert  import (VIEW3D_TP_Curve_Convert_Panel_TOOLS)
from toolplus_curve.layouts.ui_convert  import (VIEW3D_TP_Curve_Convert_Panel_UI)

from toolplus_curve.layouts.ui_draw     import (VIEW3D_TP_Curve_Draw_Panel_TOOLS)
from toolplus_curve.layouts.ui_draw     import (VIEW3D_TP_Curve_Draw_Panel_UI)

from toolplus_curve.layouts.ui_edit     import (VIEW3D_TP_Curve_Edit_Panel_TOOLS)
from toolplus_curve.layouts.ui_edit     import (VIEW3D_TP_Curve_Edit_Panel_UI)

from toolplus_curve.layouts.ui_bevel    import (VIEW3D_TP_Curve_Bevel_Panel_TOOLS)
from toolplus_curve.layouts.ui_bevel    import (VIEW3D_TP_Curve_Bevel_Panel_UI)

from toolplus_curve.layouts.ui_taper    import (VIEW3D_TP_Curve_Taper_Panel_TOOLS)
from toolplus_curve.layouts.ui_taper    import (VIEW3D_TP_Curve_Taper_Panel_UI)

from toolplus_curve.layouts.ui_utils    import (VIEW3D_TP_Curve_Utility_Panel_TOOLS)
from toolplus_curve.layouts.ui_utils    import (VIEW3D_TP_Curve_Utility_Panel_UI)

from toolplus_curve.layouts.ui_set      import (VIEW3D_TP_Curve_Set_Panel_TOOLS)
from toolplus_curve.layouts.ui_set      import (VIEW3D_TP_Curve_Set_Panel_UI)

from toolplus_curve.layouts.ui_type     import (VIEW3D_TP_Curve_Type_Panel_TOOLS)
from toolplus_curve.layouts.ui_type     import (VIEW3D_TP_Curve_Type_Panel_UI)

from toolplus_curve.layouts.ui_history  import (VIEW3D_TP_Curve_History_Panel_TOOLS)
from toolplus_curve.layouts.ui_history  import (VIEW3D_TP_Curve_History_Panel_UI)



# REGISTRY PANELS #
panels_layouts = ( VIEW3D_TP_Curve_Compact_UI,         VIEW3D_TP_Curve_Compact_TOOLS,
                   VIEW3D_TP_Curve_Insert_Panel_UI,    VIEW3D_TP_Curve_Insert_Panel_TOOLS,
                   VIEW3D_TP_Curve_Info_Panel_UI,      VIEW3D_TP_Curve_Info_Panel_TOOLS,
                   VIEW3D_TP_Curve_Select_Panel_UI,    VIEW3D_TP_Curve_Select_Panel_TOOLS,
                   VIEW3D_TP_Curve_Convert_Panel_UI,   VIEW3D_TP_Curve_Convert_Panel_TOOLS,
                   VIEW3D_TP_Curve_Draw_Panel_UI,      VIEW3D_TP_Curve_Draw_Panel_TOOLS,
                   VIEW3D_TP_Curve_Edit_Panel_UI,      VIEW3D_TP_Curve_Edit_Panel_TOOLS,
                   VIEW3D_TP_Curve_Bevel_Panel_UI,     VIEW3D_TP_Curve_Bevel_Panel_TOOLS,
                   VIEW3D_TP_Curve_Taper_Panel_UI,     VIEW3D_TP_Curve_Taper_Panel_TOOLS,
                   VIEW3D_TP_Curve_Utility_Panel_UI,   VIEW3D_TP_Curve_Utility_Panel_TOOLS,
                   VIEW3D_TP_Curve_Set_Panel_UI,       VIEW3D_TP_Curve_Set_Panel_TOOLS,
                   VIEW3D_TP_Curve_Type_Panel_UI,      VIEW3D_TP_Curve_Type_Panel_TOOLS,
                   VIEW3D_TP_Curve_History_Panel_UI,     VIEW3D_TP_Curve_History_Panel_TOOLS)

def update_panel_location(self, context):
    try:
        for panel in panels_layouts:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_panel_location == 'tools':
            
            if context.user_preferences.addons[__package__].preferences.tab_panel_layout == 'compact':     
                    
                VIEW3D_TP_Curve_Compact_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                bpy.utils.register_class(VIEW3D_TP_Curve_Compact_TOOLS)
            else:        
                VIEW3D_TP_Curve_Insert_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Info_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Select_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Convert_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Draw_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Edit_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Bevel_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Taper_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Utility_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Set_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_Type_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location
                VIEW3D_TP_Curve_History_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_location

                bpy.utils.register_class(VIEW3D_TP_Curve_Insert_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Info_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Select_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Convert_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Draw_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Edit_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Bevel_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Taper_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Utility_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Set_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_Type_Panel_TOOLS)
                bpy.utils.register_class(VIEW3D_TP_Curve_History_Panel_TOOLS)


        if context.user_preferences.addons[__package__].preferences.tab_panel_location == 'ui':

            if context.user_preferences.addons[__package__].preferences.tab_panel_layout == 'compact':
                bpy.utils.register_class(VIEW3D_TP_Curve_Compact_UI)
            else:
                bpy.utils.register_class(VIEW3D_TP_Curve_Insert_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Info_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Select_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Convert_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Draw_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Edit_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Bevel_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Taper_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Utility_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Set_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_Type_Panel_UI)
                bpy.utils.register_class(VIEW3D_TP_Curve_History_Panel_UI)

    except:
        pass




# LOAD UI: CUSTOM #       
from toolplus_curve.layouts.ui_custom      import (VIEW3D_TP_Custom_Panel_TOOLS)
from toolplus_curve.layouts.ui_custom      import (VIEW3D_TP_Custom_Panel_UI)

# REGISTRY PANEL: CUSTOM #
panel_custom = (VIEW3D_TP_Custom_Panel_UI, VIEW3D_TP_Custom_Panel_TOOLS)

def update_panel_custom(self, context):
    try:
        for panel in panel_custom:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_location_custom == 'tools':
         
            VIEW3D_TP_Custom_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_custom
            bpy.utils.register_class(VIEW3D_TP_Custom_Panel_TOOLS)
        
        if context.user_preferences.addons[__package__].preferences.tab_location_custom == 'ui':
            bpy.utils.register_class(VIEW3D_TP_Custom_Panel_UI)

        if context.user_preferences.addons[__package__].preferences.tab_location_custom == 'off':  
            return None

    except:
        pass





