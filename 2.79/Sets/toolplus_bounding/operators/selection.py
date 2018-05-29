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


# LOAD CACHE #
from toolplus_bounding.caches.cache      import  (settings_load)
from toolplus_bounding.caches.cache      import  (settings_write)


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *



# MAIN OPERATOR #
class VIEW3D_TP_BBoxSelection(bpy.types.Operator):
    """Select all existing boundings in the scene"""
    bl_idname = "tp_ops.bbox_select_box"
    bl_label = "Select all BBox"     
    bl_options = {'REGISTER', 'UNDO'}

    # SELECTIONS #
    types_sel =  [("tp_01"  ,"Box"     ," "   ,""  ,1),
                  ("tp_02"  ,"Grid"    ," "   ,""  ,2), 
                  ("tp_03"  ,"Circle"  ," "   ,""  ,3),
                  ("tp_04"  ,"Tube"    ," "   ,""  ,4),
                  ("tp_05"  ,"Cone"    ," "   ,""  ,5),
                  ("tp_06"  ,"Sphere"  ," "   ,""  ,6),
                  ("tp_06"  ,"Ico"     ," "   ,""  ,7),
                  ("tp_06"  ,"Torus"   ," "   ,""  ,8)]
    
    tp_sel = bpy.props.EnumProperty(name = "Select Boundings", default = "tp_01", description = "select all bounding geometry in the scene", items = types_sel)

    types_meshtype =[("tp_01"   ,"Shaded"      ,"select shaded"     ),
                     ("tp_02"   ,"Shadeless"   ,"select shadeless"  ),
                     ("tp_03"   ,"Wired"       ,"select wired mesh" )]
         
    tp_sel_meshtype = bpy.props.EnumProperty(name = "Select Boundings", default = "tp_01", description = "select choosen meshtype", items = types_meshtype)
    tp_extend = bpy.props.BoolProperty(name="Extend Selection",  description="extend selection", default=False) 
    tp_link = bpy.props.BoolProperty(name="LinkData",  description="activate link object data", default=False) 
    tp_select_rename = BoolProperty(name="Select ReName", default=False, description="uncheckt: select by default names / checkt: select by custom names")
    tp_select_custom = bpy.props.StringProperty(name="Pattern", default="*custom*", description="select by pattern / *everything / starting* / *contains* / ?singel / [abc] / [! non-abc]")

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    # EXECUTE MAIN OPERATOR #    
    def execute(self, context): 
        
        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
 
        settings_write(self) # custom props  

        selected = bpy.context.selected_objects        

        for obj in selected:

            if self.tp_select_rename == False:


                if self.tp_sel == "tp_01":

                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern= "*_box_shaded", extend=self.tp_extend)           

                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_box_shadeless", extend=self.tp_extend)      

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_box_wired", extend=self.tp_extend)   

                elif self.tp_sel == "tp_02":
                    
                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern="*_grid_shaded", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_grid_shadeless", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_grid_wired", extend=self.tp_extend)

                elif self.tp_sel == "tp_03":
                    
                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern="*_circle_shaded", extend=self.tp_extend)
          
                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_circle_shadeless", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_circle_wired", extend=self.tp_extend)

                elif self.tp_sel == "tp_04":

                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern="*_tube_shaded", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_tube_shadeless", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_tube_wired", extend=self.tp_extend)

                elif self.tp_sel == "tp_05":
                    
                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern="*_cone_shaded", extend=self.tp_extend) 

                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_cone_shadeless", extend=self.tp_extend) 

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_cone_wired", extend=self.tp_extend) 

                elif self.tp_sel == "tp_06":
                    
                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern="*_sphere_shaded", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_sphere_shadeless", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_sphere_wired", extend=self.tp_extend)

                elif self.tp_sel == "tp_07":

                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern="*_ico_shaded", extend=self.tp_extend)            

                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_ico_shadeless", extend=self.tp_extend)    

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_ico_wired", extend=self.tp_extend)    

                elif self.tp_sel == "tp_08":

                    if self.tp_sel_meshtype == "tp_01":
                        bpy.ops.object.select_pattern(pattern="*_torus_shaded", extend=self.tp_extend)
                    
                    elif self.tp_sel_meshtype == "tp_02":
                        bpy.ops.object.select_pattern(pattern="*_torus_shadeless", extend=self.tp_extend)

                    elif self.tp_sel_meshtype == "tp_03":
                        bpy.ops.object.select_pattern(pattern="*_torus_wired", extend=self.tp_extend)

            
            else:

                bpy.ops.object.select_pattern(pattern = self.tp_select_custom, extend=self.tp_extend)  


            # display: link
            for i in range(self.tp_link):         
                bpy.ops.object.make_links_data(type='OBDATA')
                
            
        return {'FINISHED'}     




# FREEZE OPERATOR #
class VIEW3D_TP_Freeze(bpy.types.Operator):
    """restrict select object from selection"""
    bl_idname = "tp_ops.freeze_restrict"
    bl_label = "Freeze Selection"
    bl_options = {'INTERNAL'}   
  
    def get_hideSelectObjects(self, object_list):
        for i in object_list:
            i.hide_select = True
        bpy.ops.object.select_all(action='DESELECT')
        return True 

    def execute(self, context):
        selected = bpy.context.selected_objects
        n = len(selected)
        if n > 0:
            self.get_hideSelectObjects(selected)
            self.report({'INFO'}, "%d Object%s frozen." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        return{'FINISHED'} 


# UNFREEZE OPERATOR #
class VIEW3D_TP_Unfreeze(bpy.types.Operator):
    """unrestrict all object in the scene via selected meshdata"""
    bl_idname = "tp_ops.unfreeze_restrict"
    bl_label = "Unfreeze All"
    bl_options = {'INTERNAL'}    

    def get_dehideSelectObjects(self, object_list):
        hidedObjs = []
        for i in object_list:
            if i.hide_select == True:
                i.hide_select = False
                hidedObjs.append(i)
        return hidedObjs

    def get_highlightObjects(self, selection_list):    
       for i in selection_list:
            bpy.data.objects[i.name].select = True 

    def execute(self, context):
        selected = bpy.data.objects
        bpy.ops.object.select_all(action='DESELECT')        
        n = len(selected)
        if n > 0:
            freezed_array = self.get_dehideSelectObjects(selected)
            self.get_highlightObjects(freezed_array)
            self.report({'INFO'}, "%d Object%s released." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        
        return{'FINISHED'} 




def register():
    bpy.utils.register_module(__name__)
     
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()






















