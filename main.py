from datetime import datetime
from datetime import timedelta
import time
import pygame

from classes.Player import Player
from monsters.Monster1 import Monster1
from monsters.Monster2 import Monster2
from monsters.Monster3 import Monster3
from scenes.Forest import forest
from scenes.main import map_builders, reset_game
from screen import screen

pygame.init()
pygame.font.init()
current_scene_id = 'forest'
map_builders[current_scene_id]()

change_scene_time = time.ctime()
delay = datetime.now()

clock = pygame.time.Clock()
current_scene = forest
player = Player()

menu = pygame.image.load('UI/Cover.png')
game_over = pygame.image.load('UI/game_over.png')
current_scene_id = None
dead = None
dead2 = None
monster_sprite = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit

  if current_scene_id == None:
    screen.blit(menu, menu.get_rect())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
      difficulty = 1
      current_scene_id = 'forest'
    if keys[pygame.K_2]:
      difficulty = 2
      current_scene_id = 'forest'
    if keys[pygame.K_3]:
      difficulty = 3
      current_scene_id = 'forest'

  elif dead or dead2:
    screen.blit(game_over, game_over.get_rect())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      Monster1.reset()
      Monster2.reset()
      Monster3.reset()
      reset_game()
      map_builders['forest']()
      current_scene = forest
      player = Player()
      dead = None
      dead2 = None
      current_scene_id = None

  else:
    current_scene, scene_transition_target, direction, velocity = current_scene.check_for_scene_transitions(player)

    if current_scene.id == 'forest' and current_scene_id == 'first_room':
      dead = True
      dead2 = True
      continue

    if current_scene.id != current_scene_id:
      change_scene_time = datetime.now()
      delay =datetime.now() + timedelta(0,1)
      current_scene_id = current_scene.id
      map_builders[current_scene_id]()

    # if current_scene.id == 'fourth_room':
      

    if scene_transition_target:
      player.follow_transition(direction, velocity)

    obstacles = current_scene.draw_map(scene_transition_target)

    player.draw(obstacles)
    player.interact(current_scene)

    if difficulty == 2:
      dead = Monster1.act(player, current_scene, delay)
      Monster1.draw(direction, current_scene, delay)
    if difficulty == 3:
      dead = Monster2.act(player, current_scene, delay)
      Monster2.draw(direction, current_scene, delay)

    dead2 = Monster3.act(player, current_scene, delay)
    Monster3.draw(direction, current_scene, delay)

  pygame.display.flip()
  clock.tick(60)
