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
#

bl_info = {
    'name': 'Point Overlay',
    'author': 'Dealga McArdle (zeffii), Marvin.K.Breuer (MKB)',
    'version': (0, 0, 1),
    'blender': (2, 6, 7),
    'location': 'VIEW 3D > Tools [T] or Property Shelf [N] > Panel: Point Overlay',
    'description': 'shows point resolution on selected curve /  remove with [ESC]',
    'wiki_url': 'https://github.com/mkbreuer/ToolPlus',
    'tracker_url': '',
    'category': 'Curves'}


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from bpy.types import AddonPreferences, PropertyGroup

import math
import bpy
import bgl
import blf
import mathutils
import bpy_extras
from mathutils import Vector
from mathutils.geometry import interpolate_bezier
from bpy_extras.view3d_utils import location_3d_to_region_2d as loc3d2d


 
 
def get_points(spline, clean=True, res=False):
    cyclic = True
    knots = spline.bezier_points

    if len(knots) < 2: 
        return

    r = (res if res else spline.resolution_u) + 1
    segments = len(knots)
    
    if not spline.use_cyclic_u:
        cyclic = False
        segments -= 1
 
    master_point_list = []
    for i in range(segments):
        inext = (i + 1) % len(knots)
 
        knot1 = knots[i].co
        handle1 = knots[i].handle_right
        handle2 = knots[inext].handle_left
        knot2 = knots[inext].co
        
        bezier = knot1, handle1, handle2, knot2, r
        points = interpolate_bezier(*bezier)
        master_point_list.extend(points)
 
    # some clean up to remove consecutive doubles, this could be smarter...
    if clean:
        old = master_point_list
        good = [v for i, v in enumerate(old[:-1]) if not old[i] == old[i+1]]
        good.append(old[-1])
        return good, cyclic
            
    return master_point_list, cyclic
 
def get_edge_keys(points, cyclic):
    num_points = len(points)
    edges = [[i, i+1] for i in range(num_points-1)]
    if cyclic:
        edges[-1][1] = edges[0][0]

    return edges

def get_total_length(points, edge_keys):
    edge_length = 0
    for edge in edge_keys:
        vert0 = points[edge[0]]
        vert1 = points[edge[1]]
        edge_length += (vert0-vert1).length
    return edge_length


def draw_points(context, points, size, gl_col):
    region = context.region
    rv3d = context.space_data.region_3d
    
    this_object = context.active_object
    matrix_world = this_object.matrix_world  
    
    # needed for adjusting the size of gl_points    
    bgl.glEnable(bgl.GL_POINT_SMOOTH)
    bgl.glPointSize(size)
    bgl.glBlendFunc(bgl.GL_SRC_ALPHA, bgl.GL_ONE_MINUS_SRC_ALPHA)
    
    bgl.glBegin(bgl.GL_POINTS)
    bgl.glColor4f(*gl_col)    
    for coord in points:
        # vector3d = matrix_world * (coord.x, coord.y, coord.z)
        vector3d = matrix_world * coord
        vector2d = loc3d2d(region, rv3d, vector3d)
        bgl.glVertex2f(*vector2d)
    bgl.glEnd()
    
    bgl.glDisable(bgl.GL_POINT_SMOOTH)
    bgl.glDisable(bgl.GL_POINTS)
    return


def draw_callback_px(self, context):
    
    region = context.region
    rv3d = context.space_data.region_3d

    spline = context.active_object.data.splines[0]
    points, cyclic = get_points(spline, clean=True, res=False)


    # added properties for color change
    glColor4f = self.curve_vertcolor    
    bgl.glColor4f(0.2, 0.9, 0.9, 1)        
    draw_points(context, points, 2, glColor4f)        

    # restore opengl defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
   
    return


# create 4 verts, string them together to make 4 edges.  
if False:  
    Verts, Edges = [], []
      
    profile_mesh = bpy.data.meshes.new("Base_Profile_Data")  
    profile_mesh.from_pydata(Verts, Edges, [])  
    profile_mesh.update()  
      
    profile_object = bpy.data.objects.new("Base_Profile", profile_mesh)  
    profile_object.data = profile_mesh  
      
    scene = bpy.context.scene  
    scene.objects.link(profile_object)  
    profile_object.select = True  



class VIEW3D_TP_Curve_Point_Overlay(bpy.types.Operator):
    bl_idname = "tp_ops.curve_point_overlay"
    bl_label = "Point Overlay"
    bl_description = "Show point Resolution / Remove with [ESC]"
    #bl_options = {'REGISTER', 'UNDO'}

    bpy.types.Scene.curve_vertcolor = bpy.props.FloatVectorProperty(name="OUT", default=(0.2, 0.9, 0.9, 1), size=4, subtype="COLOR", min=0, max=1)
    
    # to addon preferences
    def modal(self, context, event):
        context.area.tag_redraw()

        if event.type in {'ESC'}: 
            bpy.types.SpaceView3D.draw_handler_remove(self._handle_diamonds, 'WINDOW')
            return {'CANCELLED'}

        return {'PASS_THROUGH'}


    def invoke(self, context, event):

        if context.area.type == 'VIEW_3D':
                    
            # the arguments we pass the the callback
            args = (self, context)


            # color change in the panel
            scene = bpy.context.scene
            self.curve_vertcolor = scene.curve_vertcolor

                       
            # color change in the panel
            scene = bpy.context.scene
            self.curve_vertcolor = scene.curve_vertcolor
            
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle_diamonds = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
            
            # To store the handle, the class should be used rather than the class instance (you may use self.__class__),
            # so we can access the variable from outside, e.g. to remove the drawback on unregister()

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, 
            "View3D not found, cannot run operator")
            #context.area.tag_redraw()            
            return {'CANCELLED'}
    




# DRAW UI LAYOUT #
class draw_panel_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        col = layout.column(1)  

        box = col.box().column(1)   
     
        box.separator() 

        row = box.row(1)                   

        if context.mode == 'EDIT_CURVE':
            row.operator("tp_ops.curve_point_overlay", text="Run  [ESC]", icon='KEYTYPE_JITTER_VEC')   
        else:
            row.operator("tp_ops.curve_point_overlay", text="Run  [ESC]", icon='KEYTYPE_BREAKDOWN_VEC')   
        
        sub = row.row(1) 
        sub.scale_x = 0.15          
        sub.prop(context.scene, "curve_vertcolor", text="")
        
        box.separator() 
       
        row = box.row(1)          
        row.prop(context.object.data, "resolution_u", text="Points")         

        box.separator() 


# LOAD UI: PANEL #
class VIEW3D_TP_Panel_Curve_Point_Overlay_TOOLS(bpy.types.Panel, draw_panel_layout):
    bl_category = "Tools"
    bl_idname = "VIEW3D_TP_Panel_Curve_Point_Overlay_TOOLS"
    bl_label = "Point Overlay"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_Panel_Curve_Point_Overlay_UI(bpy.types.Panel, draw_panel_layout):
    bl_idname = "VIEW3D_TP_Panel_Curve_Point_Overlay_UI"
    bl_label = "Point Overlay"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}




# PANEL REGISTRY # 
panels = (VIEW3D_TP_Panel_Curve_Point_Overlay_UI, VIEW3D_TP_Panel_Curve_Point_Overlay_TOOLS)

def update_panel_curvepoint(self, context):
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_location_curvepoint == 'tools':
         
            VIEW3D_TP_Panel_Curve_Point_Overlay_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tab_category_curvepoint
            bpy.utils.register_class(VIEW3D_TP_Panel_Curve_Point_Overlay_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_curvepoint == 'ui':
            bpy.utils.register_class(VIEW3D_TP_Panel_Curve_Point_Overlay_UI)

    except:
        pass



# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
     
    tab_location_curvepoint = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='ui', update = update_panel_curvepoint)

    tab_category_curvepoint = StringProperty(name = "TAB Category", description = "new name equal new tab category", default = 'Tools', update = update_panel_curvepoint)

    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)
         
        row = box.row(1)   
        row.label("Panel Location: ", icon="ARROW_LEFTRIGHT")
        row.prop(self, 'tab_location_curvepoint', expand=True)
        
        if self.tab_location_curvepoint == 'tools':

            box.separator()           
           
            row = box.row()
            row.prop(self, "tab_category_curvepoint")



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

    bpy.types.Scene.curve_vertcolor = bpy.props.FloatVectorProperty(name="OUT", default=(0.2, 0.9, 0.9, 1), size=4, subtype="COLOR", min=0, max=1)

def unregister():   
    bpy.utils.unregister_module(__name__)

    del bpy.types.Scene.curve_vertcolor

if __name__ == "__main__":
    register()

