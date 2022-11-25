import pygame
from classes.Scene import Scene
from classes.Item import Item
from classes.Wall import Wall
from Items.sprites import potion

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/third_room/0.png'),
  (1280, 720)
)

third_room = Scene("third_room", sprite)

def mount_third_room():
  right_limit = Wall((1233, 0), (47, 720))
  left_limit = Wall((0, 0), (60, 720))
  top_limit = Wall((0, 0), (1280, 60))
  bottom_left_limit = Wall((0, 680), (550, 40))
  bottom_right_limit = Wall((730, 680), (1280, 40))

  third_room.add_wall(right_limit)
  third_room.add_wall(left_limit)
  third_room.add_wall(top_limit)
  third_room.add_wall(bottom_left_limit)
  third_room.add_wall(bottom_right_limit)

  invisibility_potion = Item("invisibility_potion", potion, (600, 300), (30, 30))
  third_room.add_item(invisibility_potion)

mount_third_room()
