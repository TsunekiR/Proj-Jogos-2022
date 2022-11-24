import pygame
from singleton import singleton

class Item:
  def __init__(self, name, sprite, position, size):
    self.name = name
    self.sprite = sprite
    self.position = pygame.math.Vector2(*position)
    self.size = size
    self.available = True
