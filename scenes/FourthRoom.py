import pygame
from classes.Scene import Scene

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/fourth_room/0.png'),
  (1280, 720)
)

fourth_room = Scene("fourth_room", sprite)