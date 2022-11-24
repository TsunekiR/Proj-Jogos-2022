import pygame
from classes.Scene import Scene

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/hallway/0.png'),
  (1280, 720)
)

hallway = Scene("hallway", sprite)