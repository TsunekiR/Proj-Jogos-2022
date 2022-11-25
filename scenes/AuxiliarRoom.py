import pygame
from threading import Timer
from classes.Scene import Scene
from singleton import singleton
from classes.Item import Item
from classes.Interactable import Interactable
from Items.sprites import key
from classes.Wall import Wall

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/auxiliar_room/0.png'),
  (1280, 720)
)

auxiliar_room = Scene("auxiliar_room", sprite)

right_limit = Wall((1233, 0), (47, 720))
left_top_limit = Wall((0, 0), (60, 240))
left_bottom_limit = Wall((0, 420), (60, 300))
top_limit = Wall((0, 0), (1280, 60))
bottom_limit = Wall((0, 680), (1280, 40))

auxiliar_room.add_wall(right_limit)
auxiliar_room.add_wall(left_top_limit)
auxiliar_room.add_wall(left_bottom_limit)
auxiliar_room.add_wall(top_limit)
auxiliar_room.add_wall(bottom_limit)

hallway_key = Item("hallway_key", key, (600, 300), (30, 30))

def crack_interaction():
  singleton.dialog = 'A crack on the wall? Wonder why...'
  s = Timer(3.0, singleton.reset_dialog)
  s.start()


dialog = Interactable(None, None, (600, 30), (80, 80), 'dialog', crack_interaction, True, None)

auxiliar_room.add_item(hallway_key)
auxiliar_room.add_interactable(dialog)