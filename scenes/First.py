from classes.Scene import Scene
from scenes.Second import second_scene
from Items.Item1 import item1

first_scene = Scene("purple")

# first_scene.add_scene_transition_spot(second_scene, 'top')
first_scene.add_item(item1)