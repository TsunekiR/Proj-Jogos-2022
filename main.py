import pygame

from classes.Player import Player
from monsters.Monster1 import Monster1
from scenes.Forest import forest
from scenes.main import map_builders

pygame.init()
current_scene_id = 'forest'
map_builders[current_scene_id]()

clock = pygame.time.Clock()
current_scene = forest
player = Player()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit
  
  current_scene, scene_transition_target, direction, velocity = current_scene.check_for_scene_transitions(player)

  if current_scene.id != current_scene_id:
    current_scene_id = current_scene.id
    map_builders[current_scene_id]()

  if scene_transition_target:
    player.follow_transition(direction, velocity)

  obstacles = current_scene.draw_map(scene_transition_target)

  player.draw(obstacles)
  player.interact(current_scene)

  pygame.display.flip()
  clock.tick(60)
