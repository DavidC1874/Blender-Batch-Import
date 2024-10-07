bl_info = {
    "name": "Batch Import FBX & OBJ",
    "description": "Batch Import Fbx & Obj from selected folder",
    "author": "David",
    "version": (1,0),
    "blender": (2,9,0),
    "location": "View3D",
    "wiki_url": "",
    "category": "Tool" }



import bpy
from bpy.props import StringProperty, CollectionProperty
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper
import os


class Main_Import_Panel(bpy.types.Panel):
    bl_label = "Batch Import OBJ/FBX"
    bl_idname = "Import_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("import.obj")
        row = layout.row()
        row.operator("import.fbx")


#import obj
class Import_OBJ(Operator, ImportHelper):
    bl_idname = "import.obj"
    bl_label = "Import OBJ Files"
    
    # filter subfix .obj
    filename_ext = ".obj"
    filter_glob: StringProperty(
        default="*.obj",
        options={'HIDDEN'})
    files: CollectionProperty(type=bpy.types.PropertyGroup)

    def execute(self, context):
        directory = os.path.dirname(self.filepath)
        
        for file in self.files:
            obj_path = os.path.join(directory, file.name)
            
            bpy.ops.import_scene.obj(filepath=obj_path)
        
        return {'FINISHED'}
    
#import fbx
class Import_FBX(Operator, ImportHelper):
    bl_idname = "import.fbx"
    bl_label = "Import FBX Files"
    
    filename_ext = ".fbx"
    filter_glob: StringProperty(
        default="*.fbx",
        options={'HIDDEN'})
    files: CollectionProperty(type=bpy.types.PropertyGroup)

    def execute(self, context):
        directory = os.path.dirname(self.filepath)
        
        for file in self.files:
            fbx_path = os.path.join(directory, file.name)
            bpy.ops.import_scene.fbx(filepath=fbx_path)
        
        return {'FINISHED'}

classes = [Main_Import_Panel, Import_OBJ, Import_FBX]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
