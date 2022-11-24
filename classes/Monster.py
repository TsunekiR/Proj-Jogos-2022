from copy import deepcopy
from datetime import datetime
from datetime import timedelta
import pygame
from screen import screen
from collision import check_collision
from singleton import singleton

class Monster:
  def __init__(self, name, position, velocity, size, location, behavior, neutralizer) -> None:
    self.name = name
    self.position = pygame.math.Vector2(*position)
    self.backupPosition = deepcopy(self.position)
    self.velocity = velocity
    self.size = size
    self.location = location
    self.backupLocation = deepcopy(location)
    self.behavior = behavior
    self.neutralizer = neutralizer
    self.neutralized = False
    self.started = False
    self.firstInteraction = False

  def draw(self, direction, current_scene, delay):
    if current_scene.id == self.location and not self.started:
      self.started = True
      self.firstInteraction = True

    if not singleton.transitioning_scene and self.firstInteraction and self.location == current_scene.id and self.started:
      pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))

    if not singleton.transitioning_scene and self.neutralized and self.location == current_scene.id and self.started:
      pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))

    if not singleton.transitioning_scene and datetime.now() > delay and self.location == current_scene.id and self.started:
      self.firstInteraction = False
      pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))
    else:
      if direction and self.location == current_scene.id and not self.neutralized:
        self.position.x = singleton.WINDOW_WIDTH/2 + (direction[0] * singleton.WINDOW_WIDTH/2) - self.size[0]/2
        self.position.y = singleton.WINDOW_HEIGHT/2 + (direction[1] * singleton.WINDOW_HEIGHT/2) -  self.size[1]/2


  def act(self, player, current_scene, delay):
    hasNeutralizer = False

    for item in player.items:
      if item.name == self.neutralizer:
        hasNeutralizer = True
        self.neutralized = True

    if not singleton.transitioning_scene and self.started and not hasNeutralizer:
      self.location = current_scene.id

    if not singleton.transitioning_scene and datetime.now() > delay and self.started:

      if self.behavior == "follow" and not hasNeutralizer:

        distancex = abs(self.position.x - player.position.x)
        distancey = abs(self.position.y - player.position.y)

        proportionx = distancex / (distancex + distancey + 0.00001)
        proportiony = distancey / (distancex + distancey + 0.00001)

        signx = -1 if self.position.x < player.position.x else 1
        signy = -1 if self.position.y < player.position.y else 1

        self.position.x += -1 * signx * self.velocity * proportionx
        self.position.y += -1 * signy * self.velocity * proportiony

  def reset(self):
    if self.location != self.backupLocation:
      self.position = deepcopy(self.backupPosition)
      self.location = deepcopy(self.backupLocation)
      self.started = False
      self.firstInteraction = False
