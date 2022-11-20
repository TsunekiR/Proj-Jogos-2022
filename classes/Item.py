import pygame
from singleton import singleton

class Item:
  def __init__(self, name, background, position, size):
    self.name = name
    self.background = background
    self.position = pygame.math.Vector2(*position)
    self.size = size
    self.available = True
