import pygame
from singleton import singleton

class Scene:
  def __init__(self, background):
    self.background = background
    self.position = pygame.math.Vector2(0, 0)
    self.velocity = 10

    self.scene_transition_spots = []
    self.scene_transition_directions = []
    self.neighbor_scenes = []

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

  def draw_map(self, screen):
    pygame.draw.rect(screen, self.background, pygame.Rect(*self.position, singleton.WINDOW_WIDTH, singleton.WINDOW_HEIGHT))

    for scene, direction in zip(self.neighbor_scenes, self.scene_transition_directions):
      pygame.draw.rect(screen, scene.background, pygame.Rect(*scene.position, singleton.WINDOW_WIDTH, singleton.WINDOW_HEIGHT))
      pygame.draw.rect(screen, (0, 0, 255), self.spots_by_direction[direction])

  def is_out_of_camera(self):
    return self.position.x < singleton.WINDOW_WIDTH * -1 or \
           self.position.x > singleton.WINDOW_WIDTH or \
           self.position.y < singleton.WINDOW_HEIGHT * -1 or \
           self.position.y > singleton.WINDOW_HEIGHT

class Player:
  def __init__(self, screen):
    self.screen = screen
    self.dx = 700
    self.dy = 300
    self.position = pygame.math.Vector2(self.dx, self.dy)
    self.velocity = 5
  
  def draw(self):
    keys = pygame.key.get_pressed()

    if not singleton.transitioning_scene:
      self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])

      self.direction = pygame.math.Vector2(self.dx, self.dy)
      self.position += self.direction * self.velocity    

    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.position.x, self.position.y, 60, 60))
