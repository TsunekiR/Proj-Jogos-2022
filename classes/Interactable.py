from typing import Optional
import pygame

class Interactable:
  def __init__(self, sprite_before, sprite_after, position, size, condition, on_interacted, constant, item = None):
    self.sprite_before = sprite_before
    self.sprite_after = sprite_after
    self.position = pygame.math.Vector2(*position)
    self.size = size
    self.interacted = False
    self.condition = condition
    self.item = item
    self.on_interacted = on_interacted
    self.constant = constant