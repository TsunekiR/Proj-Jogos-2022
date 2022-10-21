import pygame
from singleton import singleton

class Item:
  def __init__(self):
    self.screen = None
    self.dx = 100
    self.dy = 300
    self.position = pygame.math.Vector2(self.dx, self.dy)
    self.available = True
  
  def draw(self):

    if not singleton.transitioning_scene and self.available:
      pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.position.x, self.position.y, 15, 15))
