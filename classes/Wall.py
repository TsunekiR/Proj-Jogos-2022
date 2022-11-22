import pygame

class Wall:
    def __init__ (self, background, position, size):
        self.background = background
        self.position = pygame.math.Vector2(*position)
        self.size = size