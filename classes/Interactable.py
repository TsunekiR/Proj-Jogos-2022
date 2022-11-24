from typing import Optional
import pygame
from singleton import singleton

class Interactable:
  def __init__(self, sprite_before, sprite_after, position, size, condition, on_interacted, item: Optional[str]):
    self.sprite_before = sprite_before
    self.sprite_after = sprite_after
    self.position = pygame.math.Vector2(*position)
    self.size = size
    self.interacted = False
    self.condition = condition
    self.item = item = None
    self.on_interacted = on_interacted