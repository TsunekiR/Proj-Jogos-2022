import pygame
from classes.Scene import Scene

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/second_room/0.png'),
  (1280, 720)
)

second_room = Scene("second_room", sprite)