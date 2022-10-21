import pygame

from singleton import singleton
from screen import screen

class Player:
  def __init__(self):
    self.dx = 700
    self.dy = 300
    self.position = pygame.math.Vector2(self.dx, self.dy)
    self.velocity = 5
  
  def draw(self):
    keys = pygame.key.get_pressed()

    if not singleton.transitioning_scene:
      self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])

      self.direction = pygame.math.Vector2(self.dx, self.dy)
      self.position += self.direction * self.velocity    

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, 60, 60))
