from classes import Scene
from scenes.Second import second_scene

first_scene = Scene("purple")

first_scene.add_scene_transition_spot(second_scene, 'top')