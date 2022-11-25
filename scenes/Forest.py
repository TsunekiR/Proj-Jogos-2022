import pygame
from classes.Scene import Scene
from classes.Wall import Wall

sprite = pygame.transform.scale(
  pygame.image.load(f'sprites/background/forest/0.png'),
  (1280, 720),
)

forest = Scene("forest", sprite)

def mount_forest():
  left_limit = Wall((0, 0), (0, 720))
  right_limit = Wall((1280, 0), (1280, 720))
  bottom_limit = Wall((0, 720), (1280, 720))
  top_left_limit1 = Wall((0, 0), (200, 0))
  top_left_limit2 = Wall((200, 0), (380, 80))
  top_left_limit3 = Wall((250, 0), (320, 100))
  top_left_limit4 = Wall((330, 100), (60, 20))

  top_right_limit1 = Wall((1080, 0), (200, 0))
  top_right_limit2 = Wall((720, 0), (380, 80))
  top_right_limit3 = Wall((770, 0), (320, 100))
  top_right_limit4 = Wall((800, 100), (70, 20))
  top_right_limit5 = Wall((935, 100), (70, 20))

  forest.add_wall(left_limit)
  forest.add_wall(right_limit)
  forest.add_wall(bottom_limit)
  forest.add_wall(top_left_limit1)
  forest.add_wall(top_left_limit2)
  forest.add_wall(top_left_limit3)
  forest.add_wall(top_left_limit4)
  forest.add_wall(top_right_limit1)
  forest.add_wall(top_right_limit2)
  forest.add_wall(top_right_limit3)
  forest.add_wall(top_right_limit4)
  forest.add_wall(top_right_limit5)

mount_forest()
