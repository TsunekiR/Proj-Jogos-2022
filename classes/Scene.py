from collision import check_collision
import pygame

from singleton import singleton
from screen import screen
from classes.Spot import Spot

class Scene:
  def __init__(self, id, background):
    self.id = id
    self.background = background
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
    pygame.draw.rect(screen, self.background, pygame.Rect(*self.position, singleton.WINDOW_WIDTH, singleton.WINDOW_HEIGHT))

    for item in self.items:
      if item.available:
        relative_position = (item.position.x + self.position.x, item.position.y + self.position.y)
        pygame.draw.rect(screen, item.background, pygame.Rect(*relative_position, *item.size))

    for interactable in self.interactables:
      relative_position = (interactable.position.x + self.position.x, interactable.position.y + self.position.y)
      if interactable.interacted:
        pygame.draw.rect(screen, interactable.background_after, pygame.Rect(*relative_position, *interactable.size))
      else:
        pygame.draw.rect(screen, interactable.background_before, pygame.Rect(*relative_position, *interactable.size))

    for wall in self.walls:
      relative_position = (wall.position.x + self.position.x, wall.position.y + self.position.y)
      pygame.draw.rect(screen, wall.background, pygame.Rect(*relative_position, *wall.size))

    for scene, direction in zip(self.neighbor_scenes, self.scene_transition_directions):
      pygame.draw.rect(screen, scene.background, pygame.Rect(*scene.position, singleton.WINDOW_WIDTH, singleton.WINDOW_HEIGHT))
      pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(self.spots_by_direction[direction].position, self.spots_by_direction[direction].size))

    if scene_transition_target:
      for item in scene_transition_target.items:
        if item.available:
          relative_position = (item.position.x + scene_transition_target.position.x, item.position.y + scene_transition_target.position.y)
          pygame.draw.rect(screen, item.background, pygame.Rect(*relative_position, *item.size))

      for interactable in scene_transition_target.interactables:
        relative_position = (interactable.position.x + scene_transition_target.position.x, interactable.position.y + scene_transition_target.position.y)
        if interactable.interacted:
          pygame.draw.rect(screen, interactable.background_after, pygame.Rect(*relative_position, *interactable.size))
        else:
          pygame.draw.rect(screen, interactable.background_before, pygame.Rect(*relative_position, *interactable.size))

      for wall in scene_transition_target.walls:
        relative_position = (wall.position.x + scene_transition_target.position.x, wall.position.y + scene_transition_target.position.y)
        pygame.draw.rect(screen, wall.background, pygame.Rect(*relative_position, *wall.size))

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
              interactable.interacted = True
              if interactable.item:
                return interactable.item

  def add_wall(self, wall):
    self.walls.append(wall)