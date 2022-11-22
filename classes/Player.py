import pygame

from screen import screen
from singleton import singleton


class Player:
  def __init__(self):
    self.dx = 700
    self.dy = 300
    self.position = pygame.math.Vector2(self.dx, self.dy)
    self.velocity = 5
    self.items = []
    self.size = (60, 60)
  
  def draw(self):
    keys = pygame.key.get_pressed()

    if not singleton.transitioning_scene:
      self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])

      self.direction = pygame.math.Vector2(self.dx, self.dy)
      self.position += self.direction * self.velocity    

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))

  def interact(self, current_scene):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
      item = current_scene.check_for_item(self)

      if not item:
        item = current_scene.check_for_interactable(self)

      if item:
        self.add_item(item)

  def add_item(self, item):
    self.items.append(item)
    for item in self.items:
      print(item.name)

  def follow_transition(self, direction, velocity):
    self.dx = direction[0]
    self.dy = direction[1]
    
    self.direction = pygame.math.Vector2(self.dx, self.dy)
    self.position += self.direction * velocity * 0.925

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))