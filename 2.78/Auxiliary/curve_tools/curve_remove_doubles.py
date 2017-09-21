import bpy, mathutils


bl_info = {
    'name': 'Curve Remove Dobles',
    'author': 'Michael Soluyanov',
    'version': (1, 0),
    'blender': (2, 7, 8),
    'location': 'View3D > Specials (W) > Remove Dobles',
    'description': 'Adds comand "Remove Dobles" for curves',
    'category': 'Object'
}

def CurveRemvDbsOperator(obj, distance=0.01):
    dellist=[]
    for spline in obj.data.splines: 
        if(len(spline.bezier_points)>2):
            for i in range(0, len(spline.bezier_points)): 
                
                
                if(i==0):
                    ii=len(spline.bezier_points)-1;
                else:        
                    ii=i-1;
                    
                dot = spline.bezier_points[i];
                dot1 = spline.bezier_points[ii];   
                    
                while (dot1 in dellist and dot1!=dot):
                    ii-=1;
                    if(ii<0): 
                        ii=len(spline.bezier_points)-1;
                    dot1 = spline.bezier_points[ii]; 
                    
                if (dot.select_control_point and dot1.select_control_point and (i!=0 or spline.use_cyclic_u)):   
                    if (dot.co-dot1.co).length<distance:
                        dot1.handle_right_type= "FREE"
                        dot1.handle_right=dot.handle_right
                        dot1.co=(dot.co+dot1.co)/2
                        dellist.append(dot)

    
    bpy.ops.curve.select_all(action='DESELECT')

    for dot in dellist:
        dot.select_control_point=True
        
    count=len(dellist)
    
    bpy.ops.curve.delete(type='VERT')
    
    bpy.ops.curve.select_all(action='SELECT')
    
    return count
    


class CurveRemvDbs(bpy.types.Operator):
    bl_idname = 'curve.remove_doubles'
    bl_label = 'Remove Doubles'
    bl_options = {'REGISTER', 'UNDO'}

    distance = bpy.props.FloatProperty(name='Distance', default=0.01, min=0.0001, max=10.0, step=1)

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'CURVE')

    def execute(self, context):
        removed=CurveRemvDbsOperator(context.active_object, self.distance)
        self.report({'INFO'}, "Removed %d bezier points" % removed)
        return {'FINISHED'}




def menu_func(self, context):
    self.layout.operator(CurveRemvDbs.bl_idname, text='Remove Doubles')

def panel_func(self, context):
    layout = self.layout
    col = layout.column(align=True)
    col.operator(CurveRemvDbs.bl_idname, text='Remove Doubles')
    
def register():   
    bpy.utils.register_class(CurveRemvDbs)    

    bpy.types.VIEW3D_PT_tools_curveedit.append(panel_func)
    bpy.types.VIEW3D_MT_edit_curve_specials.append(menu_func)

def unregister(): 
    bpy.utils.unregister_class(CurveRemvDbs)  

    bpy.types.VIEW3D_PT_tools_curveedit.remove(panel_func)
    bpy.types.VIEW3D_MT_edit_curve_specials.remove(menu_func)

if __name__ == "__main__":
    register()


