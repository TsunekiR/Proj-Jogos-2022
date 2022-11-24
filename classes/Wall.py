import pygame

class Wall:
    def __init__ (self, position, size, enabled = True):
        self.position = pygame.math.Vector2(*position)
        self.size = size
        self.enabled = enabled