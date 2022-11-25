import pygame
from classes.Scene import Scene
from classes.Wall import Wall

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/second_room/0.png'),
  (1280, 720)
)

second_room = Scene("second_room", sprite)

def mount_second_room():
  left_limit = Wall((0, 0), (63, 720))
  right_top_limit = Wall((1235, 0), (50, 280))
  right_bottom_limit = Wall((1235, 420), (50, 300))
  top_left_limit = Wall((0, 0), (580, 65))
  top_right_limit = Wall((670, 0), (580, 65))
  top_center_limit = Wall((580, 0), (700, 65))
  bottom_left_limit = Wall((0, 680), (575, 40))
  bottom_right_limit = Wall((700, 680), (575, 40))
  bottom_center_limit = Wall((575, 680), (700, 40))

  second_room.add_wall(left_limit)
  second_room.add_wall(right_top_limit)
  second_room.add_wall(right_bottom_limit)
  second_room.add_wall(top_left_limit)
  second_room.add_wall(top_right_limit)
  second_room.add_wall(bottom_left_limit)
  second_room.add_wall(bottom_right_limit)

mount_second_room()
