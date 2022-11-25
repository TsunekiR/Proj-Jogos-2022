import pygame
from classes.Scene import Scene
from classes.Wall import Wall

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/hallway/0.png'),
  (1280, 720)
)

hallway = Scene("hallway", sprite)

def mount_hallway():
  left_limit = Wall((0, 0), (400, 720))
  right_limit = Wall((850, 0), (1280, 720))

  hallway.add_wall(left_limit)
  hallway.add_wall(right_limit)

mount_hallway()
