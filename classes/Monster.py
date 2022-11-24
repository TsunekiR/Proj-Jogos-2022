import pygame
from screen import screen
from collision import check_collision

class Monster:
  def __init__(self, name, position, velocity, size, location, behavior, neutralizer) -> None:
    self.name = name
    self.position = pygame.math.Vector2(*position)
    self.velocity = velocity
    self.size = size
    self.location = location
    self.behavior = behavior
    self.neutralizer = neutralizer

  def draw(self):
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))


  def act(self, player):
    item = False

    for item in player.items:
      if item.name == "Item1":
        item = True

    if self.behavior == "follow" and not item:
      distancex = abs(self.position.x - player.position.x)
      distancey = abs(self.position.y - player.position.y)

      proportionx = distancex / (distancex + distancey)
      proportiony = distancey / (distancex + distancey)

      signx = -1 if self.position.x < player.position.x else 1
      signy = -1 if self.position.y < player.position.y else 1

      self.position.x += -1 * signx * self.velocity * proportionx
      self.position.y += -1 * signy * self.velocity * proportiony