from scenes.Second import second_scene
from scenes.First import first_scene
from scenes.Third import third_scene

def build_map():
  first_scene.add_scene_transition_spot(second_scene, 'left')
  first_scene.add_scene_transition_spot(third_scene, 'right')
  second_scene.add_scene_transition_spot(first_scene, 'right')
  third_scene.add_scene_transition_spot(first_scene, 'left')
