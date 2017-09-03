bl_info = {
    "name": "BRM_SmartTools",
    "category": "Mesh",
    "author": "Bram Eulaers",
    "description": "context sensitive modeling tools"
    }

import bpy

class BRM_SmartConnect(bpy.types.Operator):
    """BRM_SmartConnect"""
    bl_idname = "brm.smartconnect"
    bl_label = "BRM_SmartConnect"
    bl_options = {"UNDO"}
    def execute(self, context):  

        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False):
            bpy.ops.mesh.subdivide()
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False):
            bpy.ops.mesh.vert_connect_path()

        return {'FINISHED'}

class BRM_SmartBevel(bpy.types.Operator):
    """BRM_SmartBevel"""
    bl_idname = "brm.smartbevel"
    bl_label = "BRM_SmartBevel"
    def execute(self, context):  

        #VERTEX
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False):
            bpy.ops.mesh.bevel('INVOKE_DEFAULT', vertex_only=True)
        
        #EDGE
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False):
            bpy.ops.mesh.bevel('INVOKE_DEFAULT', vertex_only=False)
        
        #FACE
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
            bpy.ops.mesh.bevel('INVOKE_DEFAULT', vertex_only=False)


        return {'FINISHED'}

class BRM_SmartExtrude(bpy.types.Operator):
    """BRM_SmartExtrude"""
    bl_idname = "brm.smartextrude"
    bl_label = "BRM_SmartExtrude"
    def execute(self, context):  

        #VERTEX - nothing happens, as it would only create broken geometry.
        
        #EDGE - extrude using regular move commands. Edge extention mode essentially.
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False):
            bpy.ops.mesh.extrude_region_move('INVOKE_DEFAULT')
        
        #FACE - extrude along normal at even lengths - most useful mode in my opinion
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
            fextrude = bpy.ops.mesh.extrude_region_shrink_fatten('INVOKE_DEFAULT',TRANSFORM_OT_shrink_fatten={"use_even_offset":True})

        return {'FINISHED'}

class BRM_SmartDelete(bpy.types.Operator):
    """BRM_SmartDelete"""
    bl_idname = "brm.smartdelete"
    bl_label = "BRM Smart Delete"
    bl_options = {"UNDO"}
    def execute(self, context):  

        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
            bpy.ops.mesh.delete(type='FACE')
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False):
            bpy.ops.mesh.dissolve_edges()
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False):
            bpy.ops.mesh.dissolve_verts()
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(BRM_SmartExtrude)
    bpy.utils.register_class(BRM_SmartBevel)
    bpy.utils.register_class(BRM_SmartConnect)
    bpy.utils.register_class(BRM_SmartDelete)
    
def unregister():
    bpy.utils.unregister_class(BRM_SmartExtrude)
    bpy.utils.unregister_class(BRM_SmartBevel)
    bpy.utils.unregister_class(BRM_SmartConnect)
    bpy.utils.unregister_class(BRM_SmartDelete)
    
if __name__ == "__main__":
    register()