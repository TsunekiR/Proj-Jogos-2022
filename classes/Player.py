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

    self.sprites = {}
    self.animation_framerate = 0
    self.current_animation_direction = 'down'
    self.current_animation_state = 'idle'

    self.get_animation_sprites()

    self.current_sprite = 0
    self.image = self.sprites[f'{self.current_animation_state}_{self.current_animation_direction}'][self.current_sprite]

  def get_animation_sprites(self):
    animations = [
      ('idle_down', 5),
      ('idle_side', 5),
      ('idle_up', 5),
      ('walking_down', 6),
      ('walking_side', 6),
      ('walking_up', 6),
    ]

    for animation, sprites_count in animations:
      if 'side' in animation:
        self.sprites[animation.replace('side', 'left')] = [
          pygame.transform.scale(
            pygame.image.load(f'sprites/Player/{animation}/{i}.png'),
            self.size
          ) for i in range(sprites_count)
        ]
        self.sprites[animation.replace('side', 'right')] = [
          pygame.transform.scale(
            pygame.transform.flip(
              pygame.image.load(f'sprites/Player/{animation}/{i}.png'),
              True,
              False
            ),
            self.size
          ) for i in range(sprites_count)
        ]
        continue

      self.sprites[animation] = [
        pygame.transform.scale(
          pygame.image.load(f'sprites/Player/{animation}/{i}.png'),
          self.size
        ) for i in range(sprites_count)
      ]
  
  def draw(self, obstacles):
    able = True
    keys = pygame.key.get_pressed()

    if not singleton.transitioning_scene:
      self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])

      self.direction = pygame.math.Vector2(self.dx, self.dy)

      if (self.direction.length() > 0):
        self.direction = self.direction.normalize()

      self.position += self.direction * self.velocity
      self.position.x = floor(self.position.x)
      self.position.y = floor(self.position.y)

    current_animation = f'{self.current_animation_state}_{self.current_animation_direction}'

    if self.direction.length() > 0:
      self.current_animation_state = 'walking'
    else:   
      self.current_animation_state = 'idle'
    
    if self.direction.x == -1: self.current_animation_direction = 'left'
    elif self.direction.x == 1: self.current_animation_direction = 'right'
    elif self.direction.y == -1: self.current_animation_direction = 'up'
    elif self.direction.y == 1: self.current_animation_direction = 'down'
  
    next_animation = f'{self.current_animation_state}_{self.current_animation_direction}'

    self.animation_framerate += 1

    if self.animation_framerate > 10 or current_animation != next_animation:
      self.animation_framerate = 0
      if self.current_sprite < len(self.sprites[next_animation]) - 1:
        self.current_sprite += 1
      else:
        self.current_sprite = 0

      self.image = self.sprites[next_animation][self.current_sprite]

    for obstacle in obstacles:
      if obstacle.enabled and check_collision(self.position, self.size, obstacle.position, obstacle.size):
        able = False

    if not able:
      self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])

      self.direction = pygame.math.Vector2(self.dx, self.dy)

      if (self.direction.length() > 0):
        self.direction = self.direction.normalize()

      self.position += self.direction * self.velocity * -1
      self.position.x = self.position.x
      self.position.y = self.position.y
    
    rect = self.image.get_rect()
    rect.topleft = [*self.position]
    screen.blit(self.image, rect)

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
      self.position += self.direction * velocity * 0.85
      if self.position.x > 1224:
        self.position.x = 1225
      elif self.position.x < 15:
        self.position.x = 15
    elif self.direction.y != 0:
      self.position += self.direction * velocity * 0.75
      if self.position.y < 15:
        self.position.y = 15
      elif self.position.y > 605:
        self.position.y = 605

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, *self.size))