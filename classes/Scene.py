import pygame

from singleton import singleton
from screen import screen


class Scene:
  def __init__(self, background):
    self.background = background
    self.position = pygame.math.Vector2(0, 0)
    self.velocity = 10

    self.scene_transition_spots = []
    self.scene_transition_directions = []
    self.neighbor_scenes = []
    self.items = []
    self.interactables = []

    self.scene_transition_target = None
    self.scene_transition_direction = None

    self.spots_by_direction = {
      'top':    pygame.Rect((singleton.WINDOW_WIDTH / 2) - (singleton.SPOT_BIGGER_SIZE / 2), 0, singleton.SPOT_BIGGER_SIZE, singleton.SPOT_SMALLER_SIZE),
      'bottom': pygame.Rect((singleton.WINDOW_WIDTH / 2) - (singleton.SPOT_BIGGER_SIZE / 2), singleton.WINDOW_HEIGHT, singleton.SPOT_BIGGER_SIZE, singleton.SPOT_SMALLER_SIZE),
      'right':  pygame.Rect(0, (singleton.WINDOW_HEIGHT / 2) - (singleton.SPOT_BIGGER_SIZE / 2), singleton.SPOT_SMALLER_SIZE, singleton.SPOT_BIGGER_SIZE),
      'left':   pygame.Rect(0, (singleton.WINDOW_HEIGHT / 2) - (singleton.SPOT_BIGGER_SIZE / 2), singleton.SPOT_SMALLER_SIZE, singleton.SPOT_BIGGER_SIZE),
    }

  def add_scene_transition_spot(self, scene, direction):
    match(direction):
      case 'top':
        scene.position.x = 0
        scene.position.y = singleton.WINDOW_HEIGHT * -1

        # if (self not in scene.neighbor_scenes):
        #   scene.add_scene_transition_spot(self, 'bottom')
      case 'bottom':
        scene.position.x = 0
        scene.position.y = singleton.WINDOW_HEIGHT

        # if (self not in scene.neighbor_scenes):
        #   scene.add_scene_transition_spot(self, 'top')
      case 'right':
        scene.position.x = singleton.WINDOW_WIDTH
        scene.position.y = 0

        # if (self not in scene.neighbor_scenes):
        #   scene.add_scene_transition_spot(self, 'left')
      case 'left':
        scene.position.x = singleton.WINDOW_WIDTH * -1
        scene.position.y = 0

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
        return current_scene
      
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
      return self

    for scene, direction in zip(self.neighbor_scenes, self.scene_transition_directions):
      collide = self.spots_by_direction[direction].collidepoint(player.position)
      
      if collide:
        self.scene_transition_target = scene
        self.scene_transition_direction = direction
      
        singleton.transitioning_scene = True
      
        return self
    
    return self

  def draw_map(self):
    pygame.draw.rect(screen, self.background, pygame.Rect(*self.position, singleton.WINDOW_WIDTH, singleton.WINDOW_HEIGHT))
    
    for item in self.items:
      if item.available:
        pygame.draw.rect(screen, item.background, pygame.Rect(*item.position, *item.size))

    for interactable in self.interactables:
      if interactable.interacted:
        pygame.draw.rect(screen, interactable.background_after, pygame.Rect(*interactable.position, *interactable.size))
      else:
        pygame.draw.rect(screen, interactable.background_before, pygame.Rect(*interactable.position, *interactable.size))

    for scene, direction in zip(self.neighbor_scenes, self.scene_transition_directions):
      pygame.draw.rect(screen, scene.background, pygame.Rect(*scene.position, singleton.WINDOW_WIDTH, singleton.WINDOW_HEIGHT))
      pygame.draw.rect(screen, (0, 0, 255), self.spots_by_direction[direction])

  def is_out_of_camera(self):
    return self.position.x < singleton.WINDOW_WIDTH * -1 or \
           self.position.x > singleton.WINDOW_WIDTH or \
           self.position.y < singleton.WINDOW_HEIGHT * -1 or \
           self.position.y > singleton.WINDOW_HEIGHT

  def add_item(self, item):
    self.items.append(item)
    
  def check_for_item(self, player_position):
    for item in self.items:
      if item.available:
        if player_position[0] > item.position[0] - 100 and player_position[0] < item.position[0] +100:
          if player_position[1] > item.position[1] - 100 and player_position[1] < item.position[1] + 100:
            item.available = False
            return item
  
  def add_interactable(self, interactable):
    self.interactables.append(interactable)

  def check_for_interactable(self, player_position, player_inventory):
    for interactable in self.interactables:
      if not interactable.interacted:
        print("possible")
        if player_position[0] > interactable.position[0] - 100 and player_position[0] < interactable.position[0] +100:
          if player_position[1] > interactable.position[1] - 100 and player_position[1] < interactable.position[1] + 100:
            print("right position")
            for item in player_inventory:
              print(item)
              if item.name == interactable.condition:
                print("condition met")
                interactable.interacted = True
                if interactable.item:
                  return interactable.item
