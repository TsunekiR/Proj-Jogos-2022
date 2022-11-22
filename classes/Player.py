from math import floor
from collision import check_collision
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
    self.size = (40, 100)
  
  def draw(self, obstacles):
    able = True
    keys = pygame.key.get_pressed()

    if not singleton.transitioning_scene:
      self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])

      self.direction = pygame.math.Vector2(self.dx, self.dy)
      self.position += self.direction * self.velocity
      self.position.x = floor(self.position.x)
      self.position.y = floor(self.position.y)

    for obstacle in obstacles:
      if check_collision(self.position, self.size, obstacle.position, obstacle.size):
        able = False

    if not able:
      self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])

      self.direction = pygame.math.Vector2(self.dx, self.dy)
      self.position += self.direction * self.velocity * -1
      self.position.x = floor(self.position.x)
      self.position.y = floor(self.position.y)
    # print(self.position.y)

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

    if self.direction.x != 0:
      self.position += self.direction * velocity * 0.9457364341
      if self.position.x > 1224:
        self.position.x = 1225
      elif self.position.x < 15:
        self.position.x = 15
    elif self.direction.y != 0:
      self.position += self.direction * velocity * 0.8150684932
      if self.position.y < 15:
        self.position.y = 15
      elif self.position.y > 605:
        self.position.y = 605

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))