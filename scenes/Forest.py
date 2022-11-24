import pygame
from classes.Scene import Scene

sprite = pygame.transform.scale(
  pygame.image.load(f'sprites/background/forest/0.png'),
  (1280, 720),
)

forest = Scene("forest", sprite)

