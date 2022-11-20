from typing import Optional
import pygame
from singleton import singleton

class Interactable:
  def __init__(self, background_before, background_after, position, size, condition, item: Optional[str]):
    self.background_before = background_before
    self.background_after = background_after
    self.position = pygame.math.Vector2(*position)
    self.size = size
    self.interacted = False
    self.condition = condition
    self.item = item = None