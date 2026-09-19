import bpy, os
# Run from Blender Scripting. Save your current work first: this clears the scene.
folder = os.path.dirname(os.path.abspath(__file__))
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=os.path.join(folder, 'models', 'complete_chess_set.glb'))
bpy.context.scene.unit_settings.system='METRIC'
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(folder, 'CROWN_chess_set.blend'))
