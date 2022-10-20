from scenes.First import first_scene
from scenes.Second import second_scene

def build_map():
  first_scene.add_scene_transition_spot(second_scene, 'top')