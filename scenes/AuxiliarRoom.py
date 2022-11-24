import pygame
from classes.Scene import Scene
from classes.Item import Item
from Items.sprites import key

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/auxiliar_room/0.png'),
  (1280, 720)
)

auxiliar_room = Scene("auxiliar_room", sprite)

hallway_key = Item("hallway_key", key, (600, 300), (30, 30))

auxiliar_room.add_item(hallway_key)