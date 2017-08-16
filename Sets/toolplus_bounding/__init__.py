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


bl_info = {
"name": "T+ Bounding", 
"author": "Marvink.k.Breuer (MKB)",
"version": (2, 4),
"blender": (2, 78, 0),
"location": "View3D > TAB Tools > Panel: Bounding / Menu: ADD [SHIFT+A]",
"description": "create bounding geomtry on selected objects",
"warning": "",
"wiki_url": "",
"tracker_url": "",
"category": "ToolPlus"}


# LOAD UI #
from toolplus_bounding.panel    import (VIEW3D_TP_BBOX_MESHES_TOOLS)
from toolplus_bounding.panel    import (VIEW3D_TP_BBOX_MESHES_UI)

# LOAD ICONS #
from . icons.icons              import load_icons
from . icons.icons              import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_bounding'))
   

if "bpy" in locals():
    import imp

    imp.reload(action) 
    imp.reload(boxes) 
    imp.reload(copy) 
    imp.reload(recoplanar) 
    imp.reload(rename)    
    imp.reload(selection)    
    imp.reload(setlocal)    
    imp.reload(spheres)    
    imp.reload(tubes) 
    imp.reload(help) 

    imp.reload(display) 
    imp.reload(fastnavi) 
    imp.reload(material) 
    imp.reload(normals) 
    imp.reload(opengl) 
    imp.reload(purge) 
    imp.reload(silhouette) 
    
    imp.reload(internal) 

else:

    from .operators import action  
    from .operators import boxes                                                                                                                                                                                                                                                         
    from .operators import copy                                                                                
    from .operators import recoplanar                                                                                
    from .operators import rename                                                                                                                       
    from .operators import selection                                                                                                                       
    from .operators import setlocal                                                                                                                       
    from .operators import spheres                                                                                                                       
    from .operators import tubes   
    from .operators import help                                          
       
    from .visuals import display 
    from .visuals import fastnavi  
    from .visuals import material                                          
    from .visuals import normals                                          
    from .visuals import opengl  
    from .visuals import purge  
    from .visuals import silhouette    

    from .internals import internal    
                                 

# LOAD MODULS #   
import bpy
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #
def update_panel_location(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_BBOX_MESHES_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_BBOX_MESHES_TOOLS)   
    except:
        pass    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_BBOX_MESHES_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_BBOX_MESHES_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category        
        bpy.utils.register_class(VIEW3D_TP_BBOX_MESHES_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_BBOX_MESHES_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass



# REGISTRY: PANEL TOOLS # 
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass    


# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('tools',      "Tools",      "Tools"),
               ('url',        "URLs",       "URLs")),
               default='info')

    # TAB LOACATION #           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location)


    # UPDATE: TOOLSETS #
    tab_display_apply = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Apply Transform on', 'enable more tools in panel'), ('off', 'Apply Transform off', 'disable more tools in panel')), default='off', update = update_display_tools)

    tab_display_select = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Select on', 'enable more tools in panel'), ('off', 'Select off', 'disable more tools in panel')), default='off', update = update_display_tools)

    tab_display_visual = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Visual on', 'enable tools in panel'), ('off', 'Visual off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_display_advance = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Advance on', 'enable tools in panel'), ('off', 'Advance off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_display_history = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable more tools in panel'), ('off', 'History off', 'disable more tools in panel')), default='off', update = update_display_tools)


    # UPADTE: PANEL #
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)

    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            row = layout.row()
            row.label(text="Hy, this is Version 2.1 of T+ Bounding!")

            row = layout.column()
            row.label(text="This addon allows you to create different types bounding geometry")
            row.label(text="> primitives: grid, cube, circle, cylinder, cone, torus, sphere & ico")
            row.label(text="> as mesh types: shaded, shadless (transparent), wired only (deleted faces)")
            row.label(text="> also smooth, draw all edges, etc. and add material with changeable color to it.")
            row.label(text="> run select to get the created geometry by name")
            row.label(text="> the further tools: select, transform apply and history can be show or hidden in the panel")
            row.label(text="> you find also 3 buttons in the ADD Mesh Menu [SHIFT+A] at the bottom")


        # LOACATION #
        if self.prefs_tabs == 'location':
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location: MainPanel ")
            
            row= box.row(1)
            row.prop(self, 'tab_location', expand=True)

            box.separator()
                                               
            if self.tab_location == 'tools':
                
                row = box.row(1)                                                
                row.prop(self, "tools_category")
         
            box.separator()


        # TOOLS #
        if self.prefs_tabs == 'tools':

            box = layout.box().column(1)

            row = box.row()
            row.label(text="ToolSet in Panel", icon ="INFO")

            row = box.column_flow(4)
            row.prop(self, 'tab_display_apply', expand=True) 
            row.prop(self, 'tab_display_select', expand=True) 
            row.prop(self, 'tab_display_visual', expand=True) 
            row.prop(self, 'tab_display_advance', expand=True) 
            row.prop(self, 'tab_display_history', expand=True) 

            box.separator() 
            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 

        # WEB #
        if self.prefs_tabs == 'url':
            row = layout.row()
            row.operator('wm.url_open', text = 'GitHub', icon = 'SCRIPTWIN').url = "https://github.com/mkbreuer/ToolPlus"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?435147-Addon-T-Bounding&p=3221535#post3221535"



# PROPS #
class Dropdown_BBox_Props(bpy.types.PropertyGroup):

    display_bbox_set = bpy.props.BoolProperty(name = "Display Setting", description = "Display Setting", default = False)
    display_bcyl_set = bpy.props.BoolProperty(name = "Display Setting", description = "Display Setting", default = False)
    display_bext_set = bpy.props.BoolProperty(name = "Display Setting", description = "Display Setting", default = False)

    display_visual = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_grid = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_aoccl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_world_set = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_meshlint_toggle = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_addmods = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_apply = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    display_select = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_transform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    display_rename = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    



# PROPS FOR PANEL #
class Dropdown_BBox_Panel_Props(bpy.types.PropertyGroup):

    ### BOUNDING CUBE ###
    tp_geom_box = bpy.props.EnumProperty(
        items=[("tp_bb1"    ,"Grid"   ,"add grid plane"  ),
               ("tp_bb2"    ,"Cube"    ,"add a cube"     )],
               name = "ObjectType",
               default = "tp_bb2",    
               description = "choose objecttype")

    # GRID #
    subX = bpy.props.IntProperty(name="X Subdiv", description="set vertices value",  min=2, max=100, default=0, step=1)
    subY = bpy.props.IntProperty(name="Y Subdiv", description="set vertices value",  min=2, max=100, default=0, step=1)
    subR = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)            

    bgrid_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bgrid_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bgrid_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CUBE #
    scale = FloatVectorProperty(name="scale", default=(1.0, 1.0, 1.0), subtype='TRANSLATION', description="scaling" )
    rotation = FloatVectorProperty(name="Rotation", subtype='EULER')

    bcube_rad = FloatProperty(name="Radius",  default=1.0, min=0.01, max=100, description="xyz scaling")

    bcube_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcube_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcube_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # generic transform props
    view_align = BoolProperty(name="Align to View", default=False)
    location = FloatVectorProperty(name="Location", subtype='TRANSLATION')
    rotation = FloatVectorProperty(name="Rotation",subtype='EULER')
    layers = BoolVectorProperty(name="Layers", size=20, subtype='LAYER', options={'HIDDEN', 'SKIP_SAVE'}) 
            
    # TOOLS #
    box_subdiv_use = bpy.props.BoolProperty(name="Subdivide",  description="activate subdivide", default=False) 
    box_subdiv = bpy.props.IntProperty(name="Loops", description="How many?", default=1, min=0, max=20, step=1)                   
    box_subdiv_smooth = bpy.props.FloatProperty(name="Smooth",  description="smooth subdivide", default=0.0, min=0.0, max=1.0)                    

    box_sphere_use = bpy.props.BoolProperty(name="Use Sphere",  description="activate to sphere", default=False) 
    box_sphere = bpy.props.FloatProperty(name="Sphere",  description="transform to sphere", default=1, min=0, max=1) 

    box_bevel_use = bpy.props.BoolProperty(name="Use Bevel",  description="activate bevel", default=False) 
    box_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    box_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1, min=0, max=1)
    box_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=1.5, min=0, max=100)
    box_verts_use = bpy.props.BoolProperty(name="Use Vertices",  description="activate vertex extrusion", default=False)     


    # BOX #
    box_dim = bpy.props.BoolProperty(name="Copy",  description="deactivate scale", default=True) 
    box_dim_apply = bpy.props.BoolProperty(name="Apply",  description="applyscale", default=True) 

    box_rota = bpy.props.BoolProperty(name="Copy Rotation",  description="deactivate copy rotation", default=True) 

    box_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )], 
               name = "MeshType",
               default = "tp_00",    
               description = "change meshtype")

    box_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    box_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    box_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    box_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)  

    # MATERIAL #
    box_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    box_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    box_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    box_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Widget Orientation",
               default = "tp_w0",    
               description = "widget orientation")



    ### BOUNDING CYLINDER ###
    tp_geom_tube = bpy.props.EnumProperty(
        items=[("tp_add_cyl"   ,"Tube"   ,"add cylinder" ),
               ("tp_add_cone"  ,"Cone"   ,"add cone"     ),
               ("tp_add_circ"  ,"Circle" ,"add circle"   ),
               ("tp_add_tor"  ,"Torus"  ,"add torus"  )],
               name = "ObjectType",
               default = "tp_add_cyl",    
               description = "change objecttype")

    tube_fill = bpy.props.EnumProperty(
        items=[("NOTHING"   ,"Nothing"  ,""   ),
               ("NGON"      ,"Ngon"     ,""   ),
               ("TRIFAN"    ,"Triangle" ,""   )],
               name = "",
               default = "NGON",    
               description = "change fill type")
                   
    # CIRCLE #
    bcirc_res = bpy.props.IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bcirc_rad = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)

    bcirc_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcirc_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcirc_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CYLINDER #
    bcyl_res = bpy.props.IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bcyl_rad = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)
    bcyl_dep = bpy.props.FloatProperty(name="Depth", description="set depth value", default=1.0, min=0.01, max=100)

    bcyl_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcyl_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcyl_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CONE #
    bcon_res = bpy.props.IntProperty(name="Verts", description="vertices value",  min=3, max=80, default=12)
    bcon_res1 = bpy.props.FloatProperty(name="Bottom", description="set bottom value",  min=0.01, max=100, default=2.5)
    bcon_res2 = bpy.props.FloatProperty(name="Top", description="set top value",  min=0.01, max=100, default=1.0)
    bcon_depth = bpy.props.FloatProperty(name="Depth", description="set depth value",  min=1, max=100, default=2)

    bcon_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcon_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcon_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # TORUS #
    btor_seg1 = bpy.props.IntProperty(name="Major Segments", description="set value",  min=1, max=100, default=51) 
    btor_seg2 = bpy.props.IntProperty(name="Minor Segments", description="set value",  min=1, max=100, default=15)
    btor_siz1 = bpy.props.FloatProperty(name="Major Radius", description="set value", default=1.13, min=0.01, max=1000)
    btor_siz2 = bpy.props.FloatProperty(name="Minor Radius", description="set value", default=0.78, min=0.01, max=1000)

    btor_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    btor_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    btor_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)


    # TOOLS #
    bvl_pipe_use = bpy.props.BoolProperty(name="Use Pipe",  description="activate pipe", default=False) 
    bvl_pipe_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=1.5, min=0.01, max=1000)

    bvl_bevel_use = bpy.props.BoolProperty(name="Use Bevel",  description="activate bevel", default=False) 
    bvl_select_all = bpy.props.BoolProperty(name="All",  description="use bevel on each edge", default=False) 
    bvl_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    bvl_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1, min=0, max=1)
    bvl_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=1.5, min=0, max=1000) 
    bvl_verts_use = bpy.props.BoolProperty(name="Vertices",  description="activate vertex extrusion", default=False) 

    bvl_extrude_use = bpy.props.BoolProperty(name="Use Extrude",  description="activate extrusion", default=False) 
    bvl_extrude_offset = bpy.props.FloatProperty(name="Extrude",  description="extrude on local z axis", default=10, min=0.01, max=1000) 

    # TUBE #
    tube_dim = bpy.props.BoolProperty(name="Copy",  description="deactivate scale", default=True) 
    tube_dim_apply = bpy.props.BoolProperty(name="Apply",  description="apply scale", default=True) 

    tube_rota = bpy.props.BoolProperty(name="Rotation",  description="deactivate copy rotation", default=True)

    tube_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )],
               name = "MeshType",
               default = "tp_00",    
               description = "change meshtype")

    tube_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    tube_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    tube_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    tube_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)  

    # MATERIAL #
    tube_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    tube_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    tube_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    tube_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Widget Orientation",
               default = "tp_w0",    
               description = "widget orientation")



    ### BOUNDING SPHERE ###
    tp_geom_sphere = bpy.props.EnumProperty(
        items=[("tp_add_sph"  ,"Sphere" ,"add sphere" ),
               ("tp_add_ico"  ,"Ico"    ,"add ico"    )],
               name = "ObjectType",
               default = "tp_add_sph",    
               description = "change objectype")

    # SPHERE #
    bsph_seg = bpy.props.IntProperty(name="Segments",  description="set value", min=1, max=100, default=32) 
    bsph_rig = bpy.props.IntProperty(name="Rings",  description="set value",  min=1, max=100, default=16) 
    bsph_siz = bpy.props.FloatProperty(name="Size",  description="set value", default=1.00, min=0.01, max=100) 

    bsph_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bsph_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bsph_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # ICO #
    bico_div = bpy.props.IntProperty(name="Subdiv",  description="set value", min=1, max=5, default=2) 
    bico_siz = bpy.props.FloatProperty(name="Size",  description="set value", default=1.00, min=0.01, max=100) 

    bico_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bico_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bico_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # TOOLS # 
    sphere_dim = bpy.props.BoolProperty(name="Copy Scale",  description="deactivate copy scale", default=True) 
    sphere_dim_apply = bpy.props.BoolProperty(name="Apply Scale",  description="apply copied scale", default=True) 

    sphere_rota = bpy.props.BoolProperty(name="Copy Rotation",  description="deactivate copy rotation", default=True) 

    sphere_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )],
               name = "MeshType",
               default = "tp_00",    
               description = "change meshtype")

    sphere_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    sphere_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    sphere_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    sphere_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)    

    # MATERIAL #
    sph_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    sph_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    sph_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    sph_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Widget Orientation",
               default = "tp_w0",    
               description = "widget orientation")
               

    ### BOUNDING SELECTIONS ###
    types_sel =  [("tp_01"  ,"Box"     ," "   ,""  ,1),
                  ("tp_02"  ,"Grid"    ," "   ,""  ,2), 
                  ("tp_03"  ,"Circle"  ," "   ,""  ,3),
                  ("tp_04"  ,"Tube"    ," "   ,""  ,4),
                  ("tp_05"  ,"Cone"    ," "   ,""  ,5),
                  ("tp_06"  ,"Sphere"  ," "   ,""  ,6),
                  ("tp_06"  ,"Ico"     ," "   ,""  ,7),
                  ("tp_06"  ,"Torus"   ," "   ,""  ,8)]
    
    tp_sel = bpy.props.EnumProperty(name = "Select ObjectType", default = "tp_01", description = "select all bounding geometry in the scene", items = types_sel)

    types_meshtype =[("tp_01"   ,"Shaded"      ,"select shaded"     ),
                     ("tp_02"   ,"Shadeless"   ,"select shadeless"  ),
                     ("tp_03"   ,"Wired"       ,"select wired mesh" )]
         
    tp_sel_meshtype = bpy.props.EnumProperty(name = "Select MeshType", default = "tp_01", description = "select choosen meshtype", items = types_meshtype)

    tp_extend = bpy.props.BoolProperty(name="Extend Selection",  description="extend selection", default=False) 

    tp_link = bpy.props.BoolProperty(name="LinkData",  description="activate link object data", default=False) 

    ### BOUNDING ACTIONS ###
    lock_mode = bpy.props.StringProperty(default="")
    select_mode = bpy.props.StringProperty(default="")





# ADD TO DEFAULT MENU #  
from .icons.icons import load_icons 
def draw_bound_item(self, context):
    icons = load_icons()

    layout = self.layout

    layout.separator()    

    button_bbox = icons.get("icon_bbox") 
    layout.operator("tp_ops.bbox_cube", text="Boundig Boxes", icon_value=button_bbox.icon_id)  

    button_bcyl = icons.get("icon_bcyl") 
    layout.operator("tp_ops.bbox_cylinder",text="Boundig Tubes", icon_value=button_bcyl.icon_id)

    button_bsph = icons.get("icon_bsph") 
    layout.operator("tp_ops.bbox_sphere",text="Boundig Spheres", icon_value=button_bsph.icon_id)


# ADD TO DEFAULT SPECIAL MENU [W] #  
from .icons.icons import load_icons 
def draw_recoplanar_item(self, context):
    icons = load_icons()

    layout = self.layout

    layout.separator()    

    button_relocal = icons.get("icon_relocal") 
    layout.operator("tp_ops.set_new_local", icon_value=button_relocal.icon_id) 

    button_recenter = icons.get("icon_recenter") 
    layout.operator("tp_ops.recenter", icon_value=button_recenter.icon_id)  

    button_reposition = icons.get("icon_reposition") 
    layout.operator("tp_ops.reposition", icon_value=button_reposition.icon_id)
  
    button_bloc = icons.get("icon_bloc") 
    layout.operator("tp_ops.copy_local_transform", icon_value=button_bloc.icon_id ) 



# REGISTRY #
import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_panel_location(None, bpy.context)
    update_display_tools(None, bpy.context)

    # TO MENU
    bpy.types.INFO_MT_mesh_add.append(draw_bound_item) 
    bpy.types.VIEW3D_MT_object_specials.append(draw_recoplanar_item) 
   
    # PROPS
    bpy.types.WindowManager.bbox_window = bpy.props.PointerProperty(type = Dropdown_BBox_Props)    
    bpy.types.WindowManager.tp_props_bbox = bpy.props.PointerProperty(type = Dropdown_BBox_Panel_Props)      

    # RENAME #
    bpy.types.Scene.rno_list_selection_ordered = bpy.props.EnumProperty(name="selection orderer", items=[])    
    bpy.types.Scene.rno_str_new_name = bpy.props.StringProperty(name="New name", default='')
    bpy.types.Scene.rno_str_old_string = bpy.props.StringProperty(name="Old string", default='')
    bpy.types.Scene.rno_str_new_string = bpy.props.StringProperty(name="New string", default='')
    bpy.types.Scene.rno_str_numFrom = bpy.props.StringProperty(name="from", default='')
    bpy.types.Scene.rno_str_prefix = bpy.props.StringProperty(name="Prefix", default='')
    bpy.types.Scene.rno_str_subfix = bpy.props.StringProperty(name="Subfix", default='')    
    bpy.types.Scene.rno_bool_numbered = bpy.props.BoolProperty(name='numbered', default=True)
    bpy.types.Scene.rno_bool_keepOrder = bpy.props.BoolProperty(name='keep selection order')
    bpy.types.Scene.rno_bool_keepIndex = bpy.props.BoolProperty(name='keep object Index', default=True)


def unregister():

    # PROPS    
    del bpy.types.WindowManager.bbox_window
    del bpy.types.WindowManager.tp_props_bbox

    # RENAME # 
    del bpy.types.Scene.rno_str_new_name
    del bpy.types.Scene.rno_str_old_string
    del bpy.types.Scene.rno_str_new_string
    del bpy.types.Scene.rno_bool_keepOrder
    del bpy.types.Scene.rno_bool_numbered
    del bpy.types.Scene.rno_list_selection_ordered
    del bpy.types.Scene.rno_str_prefix
    del bpy.types.Scene.rno_str_subfix
    del bpy.types.Scene.rno_bool_keepIndex 

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()


if __name__ == "__main__":
    register()
        
        











