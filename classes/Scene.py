from collision import check_collision
import pygame

from singleton import singleton
from screen import screen
from classes.Spot import Spot
from classes.Item import Item
from threading import Timer

class Scene:
  def __init__(self, id, sprite, offset = 0):
    self.id = id
    self.sprite = sprite
    self.offset = offset
    self.position = pygame.math.Vector2(0, 0)
    self.velocity = 10

    self.scene_transition_spots = []
    self.scene_transition_directions = []
    self.neighbor_scenes = []
    self.items = []
    self.interactables = []
    self.walls = []

    self.scene_transition_target = None
    self.scene_transition_direction = None

    self.spots_by_direction = {
      'top':    Spot(((singleton.WINDOW_WIDTH / 2) - (singleton.SPOT_BIGGER_SIZE / 2), 0), (singleton.SPOT_BIGGER_SIZE, singleton.SPOT_SMALLER_SIZE)),
      'bottom': Spot(((singleton.WINDOW_WIDTH / 2) - (singleton.SPOT_BIGGER_SIZE / 2),singleton.WINDOW_HEIGHT - (singleton.SPOT_SMALLER_SIZE)), (singleton.SPOT_BIGGER_SIZE, singleton.SPOT_SMALLER_SIZE)),
      'right':  Spot(((singleton.WINDOW_WIDTH) - (singleton.SPOT_SMALLER_SIZE), (singleton.WINDOW_HEIGHT / 2) - (singleton.SPOT_BIGGER_SIZE / 2)), (singleton.SPOT_SMALLER_SIZE, singleton.SPOT_BIGGER_SIZE)),
      'left':   Spot((0, (singleton.WINDOW_HEIGHT / 2) - (singleton.SPOT_BIGGER_SIZE / 2)), (singleton.SPOT_SMALLER_SIZE, singleton.SPOT_BIGGER_SIZE))
    }

  def reset(self):
    self.__init__(self.id, self.sprite, self.offset)

  def reset_transition_spots(self):
    self.neighbor_scenes = []
    self.scene_transition_directions = []

  def add_scene_transition_spot(self, scene, direction):
    match(direction):
      case 'top':
        scene.position.x = self.position.x
        scene.position.y = self.position.y + singleton.WINDOW_HEIGHT * -1

        # if (self not in scene.neighbor_scenes):
        #   scene.add_scene_transition_spot(self, 'bottom')
      case 'bottom':
        scene.position.x = self.position.x
        scene.position.y = self.position.y + singleton.WINDOW_HEIGHT

        # if (self not in scene.neighbor_scenes):
        #   scene.add_scene_transition_spot(self, 'top')
      case 'right':
        scene.position.x = self.position.x + singleton.WINDOW_WIDTH
        scene.position.y = self.position.y

        # if (self not in scene.neighbor_scenes):
        #   scene.add_scene_transition_spot(self, 'left')
      case 'left':
        scene.position.x = self.position.x + singleton.WINDOW_WIDTH * -1
        scene.position.y = self.position.y

        # if (self not in scene.neighbor_scenes):
        #   scene.add_scene_transition_spot(self, 'right')

    self.neighbor_scenes.append(scene)
    self.scene_transition_directions.append(direction)

  def check_for_scene_transitions(self, player):
    if singleton.transitioning_scene:
      if self.is_out_of_camera():
        singleton.transitioning_scene = False

        current_scene = self.scene_transition_target
        self.scene_transition_target = None
        self.scene_transition_direction = None
        
        return current_scene, None, None, None
      
      direction = pygame.math.Vector2(0, 0)

      match(self.scene_transition_direction):
        case 'top': 
          direction.y = 1
        case 'bottom':
          direction.y = -1
        case 'right':
          direction.x = -1
        case 'left':
          direction.x = 1

      self.position += direction * self.velocity

      if self.scene_transition_target.position != pygame.math.Vector2(0, 0):
        self.scene_transition_target.position += direction * self.velocity
      return self, self.scene_transition_target, direction, self.velocity

    for scene, direction in zip(self.neighbor_scenes, self.scene_transition_directions):
      
      if check_collision(self.spots_by_direction[direction].position, self.spots_by_direction[direction].size, player.position, player.size):
        self.scene_transition_target = scene
        self.scene_transition_direction = direction
      
        singleton.transitioning_scene = True
      
        return self, None, None, None

    return self, None, None, None

  def draw_map(self, scene_transition_target):
    screen.fill('black')
    screen.blit(self.sprite, pygame.Rect(self.position.x - self.offset, self.position.y, 1280, 720))

    if singleton.dialog:
      font = pygame.font.SysFont('Comic Sans MS', 15)
      text = font.render(singleton.dialog, False, (255, 255, 255))
      pygame.draw.rect(screen, 'black', pygame.Rect(50, 50, 600, 40))
      screen.blit(text, (100, 60))

    for item in self.items:
      if item.available:
        relative_position = (item.position.x + self.position.x, item.position.y + self.position.y)
        screen.blit(item.sprite, pygame.Rect(*relative_position, *item.size))

    for interactable in self.interactables:
      relative_position = (interactable.position.x + self.position.x, interactable.position.y + self.position.y)
      if interactable.interacted and interactable.sprite_after:
        screen.blit(interactable.sprite_after, pygame.Rect(*relative_position, *interactable.size))
      elif not interactable.interacted and interactable.sprite_before:
        screen.blit(interactable.sprite_before, pygame.Rect(*relative_position, *interactable.size))

    for wall in self.walls:
      relative_position = (wall.position.x + self.position.x, wall.position.y + self.position.y)

    for scene, direction in zip(self.neighbor_scenes, self.scene_transition_directions):
      screen.blit(scene.sprite, pygame.Rect(scene.position.x - scene.offset, scene.position.y, 1280, 720))

    if scene_transition_target:
      for item in scene_transition_target.items:
        if item.available:
          relative_position = (item.position.x + scene_transition_target.position.x, item.position.y + scene_transition_target.position.y)
          screen.blit(item.sprite, pygame.Rect(*relative_position, *item.size))

      for interactable in scene_transition_target.interactables:
        relative_position = (interactable.position.x + scene_transition_target.position.x, interactable.position.y + scene_transition_target.position.y)
        if interactable.interacted and interactable.sprite_after:
          screen.blit(interactable.sprite_after, pygame.Rect(*relative_position, *interactable.size))
        elif not interactable.interacted and interactable.sprite_before:
          screen.blit(interactable.sprite_before, pygame.Rect(*relative_position, *interactable.size))

      # for wall in scene_transition_target.walls:
      #   relative_position = (wall.position.x + scene_transition_target.position.x, wall.position.y + scene_transition_target.position.y)
      #   pygame.draw.rect(screen, wall.background, pygame.Rect(*relative_position, *wall.size))

    return self.walls

  def is_out_of_camera(self):
    return self.position.x < singleton.WINDOW_WIDTH * -1 or \
           self.position.x > singleton.WINDOW_WIDTH or \
           self.position.y < singleton.WINDOW_HEIGHT * -1 or \
           self.position.y > singleton.WINDOW_HEIGHT

  def add_item(self, item):
    self.items.append(item)
    
  def check_for_item(self, player):
    for item in self.items:
      if item.available:
        if check_collision(player.position, player.size, item.position, item.size):
          item.available = False
          return item
  
  def add_interactable(self, interactable):
    self.interactables.append(interactable)

  def check_for_interactable(self, player):
    for interactable in self.interactables:
      if not interactable.interacted:
        if check_collision(player.position, player.size, interactable.position, interactable.size):
          for item in player.items:
            if item.name == interactable.condition:
              if not interactable.constant:
                interactable.interacted = True
              if interactable.on_interacted:
                interactable.on_interacted()
              if interactable.item:
                return interactable.item

  def add_wall(self, wall):
    self.walls.append(wall)