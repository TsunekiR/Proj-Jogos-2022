import pygame
from singleton import singleton

class Item:
  def __init__(self, screen, scene):
    self.scene = scene
    self.screen = screen
    self.dx = 100
    self.dy = 300
    self.position = pygame.math.Vector2(self.dx, self.dy)
    self.available = True
  
  def draw(self, current_scene):

    if not singleton.transitioning_scene and self.available and self.scene == current_scene:
      pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.position.x, self.position.y, 15, 15))
