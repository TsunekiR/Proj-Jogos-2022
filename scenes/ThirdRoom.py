import pygame
from classes.Scene import Scene

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/third_room/0.png'),
  (1280, 720)
)

third_room = Scene("third_room", sprite)