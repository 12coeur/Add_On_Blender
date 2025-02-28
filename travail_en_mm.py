import bpy

bl_info = {
    "name": "Travail en mm",
    "blender": (4, 3, 0),
    "category": "Scene",
    "description": "Configure la scène pour travailler en millimètres."
}

def configurer_scene_mm():
    """Configure la scène Blender pour travailler en millimètres."""
    scene = bpy.context.scene
    units = scene.unit_settings
    
    # Définir les unités en millimètres
    units.system = 'METRIC'
    units.scale_length = 0.001  # 1 unité Blender = 1 mm
    units.length_unit = 'MILLIMETERS'
    
    # Activer la grille millimétrique
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.overlay.grid_scale = 0.001  # Grille en mm
                    space.overlay.show_axis_x = True
                    space.overlay.show_axis_y = True
                    space.overlay.show_axis_z = True
                    break

def definir_workspace_mm():
    """Créer un espace de travail nommé 'Travail en mm'."""
    workspace = bpy.context.workspace
    workspace.name = "Travail en mm"

class ConfigurerSceneMMOperator(bpy.types.Operator):
    """Configure la scène pour un travail en millimètres."""
    bl_idname = "scene.configurer_mm"
    bl_label = "Configurer scène en mm"
    
    def execute(self, context):
        configurer_scene_mm()
        definir_workspace_mm()
        self.report({'INFO'}, "Scène configurée en mm")
        return {'FINISHED'}

class ScenePanel(bpy.types.Panel):
    """Ajoute un panneau dans l'onglet Scène."""
    bl_label = "Travail en mm"
    bl_idname = "SCENE_PT_travail_en_mm"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scene.configurer_mm", text="Configurer la scène en mm")

class TravailEnMMPreferences(bpy.types.AddonPreferences):
    bl_idname = "scene.travail_en_mm"
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Configuration de l'espace de travail en mm")

# Enregistrement de l'opérateur et du panneau dans Blender
def register():
    bpy.utils.register_class(ConfigurerSceneMMOperator)
    bpy.utils.register_class(ScenePanel)
    bpy.utils.register_class(TravailEnMMPreferences)

def unregister():
    bpy.utils.unregister_class(ConfigurerSceneMMOperator)
    bpy.utils.unregister_class(ScenePanel)
    bpy.utils.unregister_class(TravailEnMMPreferences)

if __name__ == "__main__":
    register()
