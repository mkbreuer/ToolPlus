# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
'''
Multiple Mesh Deform add-on

#--- ### Header
bl_info = {
    "name": "MDeform",
    "author": "Witold Jaworski",
    "version": (1, 1, 2),
    "blender": (2, 6, 4),
    "location": "View3D >Specials (W-key), Property shelf",
    "category": "Object",
    "description": "Deforms multiple objects with a single mesh cage",
    "warning": "",
    "wiki_url": "http://airplanes3d.net/scripts-256_e.xml",
    "tracker_url": "http://airplanes3d.net/track-256_e.xml"
    }
'''
#--- ### Change log
#2013-02-26 Witold Jaworski: fixed error which appears when user has modified the bound deformer mesh, and then 
#           pushed [Unvind] button. Now it reverts to the original mesh (however, it clears in this way the user changes 
#           always modify teh unbound deformer mesh!)
#--- ### Imports
import bpy
from bpy.utils import register_module, unregister_module
from bpy.props import StringProperty, EnumProperty, BoolProperty
from sys import exc_info

#--- ### Constants
DEBUG = 0 #Debug flag - just some text printed on the console...
MID = "MDeformer" #default ID of this feature data
#--- ### Helper functions

def get_active_object(context = None):
    """ Returns current active object
        Arguments:
            @context (Context): current context (optional - bpy.context is used by default)
    """
    if not context: 
        context = bpy.context
    return context.object

def set_active_object(obj):
    """ Sets the current active object - program must be in Object Mode!
        Arguments:
            @obj (Object):    new active object
    """
    bpy.context.scene.objects.active = obj

def get_current_mode(context = None):
    """Returns current mode of the 3D View:
        Arguments:
            @context (Context):    current context (optional - as received by the operator)
    """
    if context:
        return context.mode
    else:
        return bpy.context.mode
    
def set_current_mode(new_mode):
    """Sets current mode of the 3D View:
        Arguments:
            @new_mode (string):    one of the modes received from the get_currentmode() function 
    """
    if new_mode == 'EDIT_MESH': 
        new_mode = 'EDIT'
    bpy.ops.object.mode_set(mode = new_mode)

def set_edit_mode():
    """Switches Blender into Edit Mode
    """
    set_current_mode('EDIT')
    
def is_edit_mode(context = None):
    """Returns True, when Blender is in Edit Mode
        Arguments:
            @context (Context):    current context (optional - as received by the operator)
    """
    if context:
        return context.mode == 'EDIT_MESH'
    else:
        return bpy.context.mode == 'EDIT_MESH'
    
            
def set_object_mode():
    """Switches Blender into Object Mode
    """
    set_current_mode('OBJECT')
    
def is_object_mode(context = None):
    """Returns True, when Blender is in the Object Mode
        Arguments:
            @context (Context):    current context (optional - as received by the operator)
    """
    if context:
        return context.mode == 'OBJECT'
    else:
        return bpy.context.mode == 'OBJECT'

def assigned_objects(deformer):
    """Returns list of the objects assigned (through the Mesh Deform modifiers) to the deformer object
       Arguments:
            @deformer (Object):    object, used in the Mesh Deform modifiers
    """
    return list(filter(lambda obj: obj.modifiers.get(MID, None) and obj.modifiers[MID].object == deformer, bpy.context.scene.objects))

def is_deformer_object(obj):
    """ Returns True, when obj is a valid Deformer mesh object
        Arguments:
            @obj (Object):    object to be checked
    """ 
    if obj.modifiers.get(MID, None): #when object contains a mesh deform modifier bearing the MID name - it is not the deformer!
        return False
    else: #deformer is the object used by at least one modifier
        return assigned_objects(obj) != []

def get_object(name, default, context = None):
    """ Returns object, corresponding to the given name
        Arguments:
            @name (string):     object name (may be empty)
            @default (Object):  object to use when the @name is not found
            @context (Context): current context (optional - bpy.context is used by default)
        Remarks: used in Deformer* operators, to resolve the optional deformer name
    """ 
    if not context:
        context = bpy.context
    obj = context.scene.objects.get(name, None)
    if obj:
        return obj
    else:
        return default

def store_mesh(object):
    """Stores current object mesh geometry 'on the side'
        Arguments:
        @object (Object): an object, which mesh has to be preserved
    """
    data = {}
    data['vertices'] = list(map(lambda v: v.co.to_tuple(),object.data.vertices))
    data['edges'] = object.data.edge_keys #it is a helper, Python-defined Mesh property
    data['faces'] = list(map(lambda p: tuple(p.vertices),object.data.polygons))
    object[MID] = data

def restore_mesh(object):
    """Restores the object mesh geometry from previously preserved data (by store_mesh())
        Arguments:
        @object (Object): an object, which mesh has to be restored
        
        Remarks:removes the whole current mesh! 
                When object contains no stored data - changes nothing.
        Assumption: the object is the active object!
    """
    data = object.get(MID,None)
    if data:
        vertices = list(map(lambda c: tuple(c), data['vertices']))
        edges = list(map(lambda c: tuple(c), data['edges']))
        faces = list(map(lambda c: tuple(c), data['faces']))
        mesh = object.data
        cmode = get_current_mode()
        #delete the current mesh:
        set_object_mode()
        if len(vertices) == len(mesh.vertices): #if number of vertices has been not changed:
            for i in range(len(vertices)): #set the previous coordinates!
                mesh.vertices[i].co = vertices[i]
        else: #I do not know why, but something is wrong with the mesh obtained in the way below
              #(Blender cannot loop cut it, and crashes during later operations...) 
            actobj = get_active_object()
            set_active_object(object) #switch to this object:
            set_edit_mode() #enter its edit mode...
            bpy.ops.mesh.select_all(action = 'SELECT')
            bpy.ops.mesh.delete(type = 'VERT')
            set_object_mode() #required to invoke from_pydata()
            #create the stored mesh:
            object.data.from_pydata(vertices, edges, faces)
            #restore current mode
            set_active_object(actobj)
             
        set_current_mode(cmode)
        #remove stored data:
        del object[MID]
        
def delete_mesh(object):
    """Removes the previously preserved data (by store_mesh())
        Arguments:
        @object (Object): an object, which mesh has to be restored
    """
    if object.get(MID,None): del object[MID]
    
#--- ### Core operations
def assign (objects, deformer):
    """ Prepends in objects the Mesh Deform modifiers
        Arguments:
            @objects (list of Object):    objects to be applied
            @deformer (Object): the object, to be referenced in the Mesh Deform modifier
            
    """
    actobj = get_active_object()
    for obj in objects:
        if obj != deformer and not obj.modifiers.get(MID,None): #prepend Mesh Deform modifiers to each selected object, which does not contain it:
            set_active_object(obj)
            bpy.ops.object.modifier_add(type='MESH_DEFORM')
            mod = obj.modifiers[-1]
            mod.object = deformer
            mod.name = MID
            while obj.modifiers[0] != mod:
                bpy.ops.object.modifier_move_up(modifier = mod.name)
                
    set_active_object(actobj) #restore the initial state

def clear(objects, deformer = None, apply = False, show_func = None):
    """ Removes/Applies all the Mesh Deform modifiers connected to the deformer
        Arguments:
            @objects (list of Object):  objects to be applied
            @deformer (Object):         the object referenced by the Mesh Deform Modifiers (may be None)
            @apply (bbol):              True, when to apply these modifiers. False, when just remove them
            @show_func:                 Optional: the bpy.types.Operator.report() function for diagnostic messages
    """
    actobj = get_active_object()
    cmode = get_current_mode()
    
    set_object_mode() #modifiers can be removed in the object mode
    
    errcount = 0
    for obj in objects:
        set_active_object(obj)
        try:
            if apply:
                bpy.ops.object.modifier_apply(modifier = MID)
            else:
                bpy.ops.object.modifier_remove(modifier = MID)
        except:
            errcount += 1
            args = (MID, obj.name, exc_info()[1])
            msg = "The '%s' modifer is not removed from object named '%s' due to: '%s'" % args
            if show_func:
                show_func(type={'WARNING'}, message=msg)
            else:    
                print(msg) #show it at least in the system console...

    if deformer and is_bound(deformer) and errcount == 0:
        if apply: #just delete the stored mesh  
            delete_mesh(deformer) 
        else: #unbind the modifiers and restore the mesh:       
            unbind(deformer)
        
    set_active_object(actobj)
    set_current_mode(cmode)    

def bind(deformer):
    """ Binds all the Mesh Deform modifiers connected to the deformer to their meshes
        Arguments:
            @deformer (Object): the object referenced by the Mesh Deform Modifier
    """
    actobj = get_active_object()
    cmode = get_current_mode()
    
    store_mesh(deformer)
    
    objects = assigned_objects(deformer)
    set_object_mode()
    for obj in objects:
        mod = obj.modifiers.get(MID,None)
        if mod and mod.is_bound == False:
            set_active_object(obj)
            bpy.ops.object.meshdeform_bind(modifier = MID)
    
    set_active_object(actobj)
    set_current_mode(cmode)    
    
def is_bound(deformer):
    """ Returns True, when specified deformer object is bound to the meshes
        Arguments:
            @deformer (Object):    a deformer object
    """
    return (deformer.get(MID, None) != None)

def unbind(deformer):
    """ Unbinds all the Mesh Deform modifiers connected to the deformer to their meshes
        Arguments:
            @deformer (Object): the object referenced by the Mesh Deform Modifier
    """
    actobj = get_active_object()
    cmode = get_current_mode()
    
    objects = assigned_objects(deformer)
    set_object_mode()
    for obj in objects:
        mod = obj.modifiers.get(MID,None)
        if mod and mod.is_bound == True:
            set_active_object(obj)
            bpy.ops.object.meshdeform_bind(modifier = MID)

    restore_mesh(deformer)
    
    set_active_object(actobj)
    set_current_mode(cmode)    
    
#--- ### Operators
class DeformerSet(bpy.types.Operator):
    ''' Prepends to selected objects a Mesh Deform modifier (assigned to the active object) '''
    bl_idname = "mesh.deformer_set" #
    bl_label = "Set Deformer"
    bl_description = "Prepends to selected objects a Mesh Deform modifier assigned to the active object"
    # bl_options = {'REGISTER', 'UNDO'} #Set this options, if you want to update  
    #                                  parameters of this operator interactively 
    #                                  (in the Tools pane) 
    #--- parameters
    deformer_name = StringProperty(name="deformer", description="Object name, used in the assigned Mesh Deform modifiers", default = "")

    #--- Blender interface methods
    @classmethod
    def poll(cls,context):
        return (is_object_mode(context))

    def invoke(self, context, event):
        #input validation: 
        if context.selected_objects:
            if len(context.selected_objects) < 2:
                self.report(type={'ERROR'}, message="Select at least two objects")
                return {'CANCELLED'}
            else:
                #parameters adjusted, run the command!    
                return self.execute(context)
        else:
            self.report(type={'ERROR'}, message="Nothing is selected")
            return {'CANCELLED'}
        
    def execute(self,context):
        deformer = get_object(self.deformer_name,get_active_object(context),context)
        before = len(assigned_objects(deformer))
        assign(context.selected_objects, deformer)
        after = len(assigned_objects(deformer))
        if after > before:
            self.report(type={'INFO'}, message="%d new object(s) assigned to '%s'" % ((after - before), deformer.name))
        else:
            self.report(type={'WARNING'}, message="no new objects assigned to '%s'" % deformer.name)
        return {'FINISHED'}
    
class DeformerClear(bpy.types.Operator):
    ''' Clears this Deformer, optionally applying deformation to associated objects '''
    bl_idname = "mesh.deformer_clear" #
    bl_label = "Clear Deformer"
    bl_description = "Clears this Deformer, optionally applying deformation to associated objects"
    # bl_options = {'REGISTER', 'UNDO'} #Set this options, if you want to update  
    #                                  parameters of this operator interactively 
    #                                  (in the Tools pane) 
    #--- parameters
    deformer_name = StringProperty(name="deformer", description="Object name, used in the assigned Mesh Deform modifiers", default = "")
    apply = BoolProperty(name="apply", description="Apply the Mesh Deform modifiers to objects, before removing?", default = False)

    #--- Blender interface methods
    @classmethod
    def poll(cls,context):
        return (is_object_mode(context) or is_edit_mode(context))

    def invoke(self, context, event):
        #input validation: 
        if context.selected_objects or is_edit_mode():
            #parameters adjusted, run the command!    
            return self.execute(context)
        else:
            self.report(type={'ERROR'}, message="Nothing is selected")
            return {'CANCELLED'}
        
    def execute(self,context):
        deformer = get_object(self.deformer_name,get_active_object(context),context)
        if is_deformer_object(deformer): #Clear whole deformer 
            objects = assigned_objects(deformer)
            before = len(objects)
            clear(objects, deformer, self.apply, self.report)    
            after = len(assigned_objects(deformer))
            if after < before:
                self.report(type={'INFO'}, message="%d object(s) disconnected from '%s'" % ((before - after), deformer.name))
                if after > 0:
                    self.report(type={'WARNING'}, message="%d object(s) still assigned to '%s', analyze the previous messages for details" % (after, deformer.name))
            else:
                self.report(type={'WARNING'}, message="no objects disconnected from '%s'" % deformer.name)
        else:
            clear(context.selected_objects, None)
            
        return {'FINISHED'}

class DeformerBind(bpy.types.Operator):
    ''' Binds/Unbinds the Mesh Deform modifiers associated with the active object '''
    bl_idname = "mesh.deformer_bind" #
    bl_label = "Bind Deformer"
    bl_description = "Binds/Unbinds the Mesh Deform modifiers associated with the active object"
    # bl_options = {'REGISTER', 'UNDO'} #Set this options, if you want to update  
    #                                  parameters of this operator interactively 
    #                                  (in the Tools pane) 
    #--- parameters
    deformer_name = StringProperty(name="deformer", description="Object name, used in the assigned Mesh Deform modifiers", default = "")
    action = EnumProperty(name="action", description="Action to be taken", items=[('BIND',"Bind","Bind meshes to the deformer"),
                                                                                  ('UNBIND',"Unbind","Unbind meshes from the deformer"),
                                                                                  ('TOGGLE',"Toggle","Switch the meshes to the alternate state")], 
                          default = 'TOGGLE')
    #--- Blender interface methods
    @classmethod
    def poll(cls,context):
        return (is_edit_mode(context))

    def invoke(self, context, event):
        #input validation: 
        deformer = get_object(self.deformer_name,get_active_object(context),context)
        if is_deformer_object(deformer): 
            return self.execute(context)
        else:
            self.report(type={'ERROR'}, message="No deformed objects found")
            return {'CANCELLED'}
            
        
    def execute(self,context):
        deformer = get_object(self.deformer_name,get_active_object(context),context)
        
        if self.action == 'TOGGLE':
            do_bind = not is_bound(deformer)
        else:
            do_bind = self.action == 'BIND'
            
        if do_bind and not is_bound(deformer):
            bind(deformer)
            self.report(type={'INFO'}, message="Deformer is active")
        if not do_bind and is_bound(deformer):
            unbind(deformer)
            #any attempt to deselect the selected by default vertices causes Blender to crash!
            self.report(type={'INFO'}, message="Deformer is inactive")
         
        return {'FINISHED'}
"""    
class DeformerPanel(bpy.types.Panel):
    #in PROPERTIES window none of the operators work!
    bl_space_type = 'VIEW_3D' #'PROPERTIES'
    bl_region_type = 'UI' #'WINDOW'
    #bl_context = "modifier"
    bl_label = "Deformer"
    #bl_options = {'HIDE_HEADER'}
    
    #--- methods    
    @classmethod
    def poll(cls, context):
        #show this panel in Object Mode, only:
        return (context.mode == 'EDIT_MESH' and is_deformer_object(context.object))
   
    def draw(self, context):
        layout = self.layout
        if context.object:
            objects = assigned_objects(context.object)
            if len(objects) > 0:
                info = "%d associated objects"  % len(objects)
                layout.label(text=info)
                #if is_bound(context.object):
                #    layout.label(text="their Mesh Deform modifiers are bound")
                #else:
                #    layout.label(text="their Mesh Deform modifiers are unbound")
                #Every operator, invoked from this panel, does not work!
                if is_bound(context.object):
                    layout.operator(DeformerBind.bl_idname, text = "Unbind objects") 
                    row = layout.row()
                    row.column().operator(DeformerClear.bl_idname, text= "Remove").apply = False
                    row.column().operator(DeformerClear.bl_idname, text= "Apply").apply = True
                else:   
                    layout.operator(DeformerBind.bl_idname, text = "Bind objects")
                    row = layout.row()
                    row.column().operator(DeformerClear.bl_idname, text= "Remove").apply = False
"""                    
                
#--- ### API interface functions
def object_menu_draw(self, context):
    self.layout.operator_context = 'INVOKE_REGION_WIN'
    obj = context.object
    if obj:
        if obj.modifiers.get(MID, None):
            self.layout.operator(DeformerClear.bl_idname, "Clear Deformer")
        else:
            self.layout.operator(DeformerSet.bl_idname, "Set Deformer")

def mesh_menu_draw(self, context):
    self.layout.operator_context = 'INVOKE_REGION_WIN'
    if is_deformer_object(context.object):
        if is_bound(context.object):
            self.layout.operator(DeformerBind.bl_idname, "Unbind Deformer")
            self.layout.operator(DeformerClear.bl_idname, "Apply Deformer").apply = True
        else:
            self.layout.operator(DeformerBind.bl_idname, "Bind Deformer")
            
        self.layout.operator(DeformerClear.bl_idname, "Remove Deformer").apply = False
            
    

def register():
    register_module(__name__)
    bpy.types.VIEW3D_MT_object_specials.prepend(object_menu_draw)
    bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(mesh_menu_draw)
    
def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_specials.remove(mesh_menu_draw)
    bpy.types.VIEW3D_MT_object_specials.remove(object_menu_draw)
    unregister_module(__name__)
    
if __name__ == "__main__":
    register()
        
        
