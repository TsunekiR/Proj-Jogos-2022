from classes.Item import Item
from Items.Item1 import item1
from scenes.First import first_scene
from classes.Scene import Scene

def item_associator(screen):
  item1.screen = screen
  first_scene.add_item(item1)