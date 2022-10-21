from tkinter import Y
import pygame
from singleton import singleton

class Item:
  def __init__(self, background, position, size):
    self.background = background
    self.position = pygame.math.Vector2(*position)
    self.size = size
    self.available = True
