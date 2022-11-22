import pygame

from classes.Player import Player
from screen import screen
from scenes.First import first_scene
from scenes.main import build_map

pygame.init()
build_map()

clock = pygame.time.Clock()
current_scene = first_scene
player = Player()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit
  
  current_scene, scene_transition_target , direction, velocity = current_scene.check_for_scene_transitions(player)
  if scene_transition_target:
    player.follow_transition(direction, velocity)

  current_scene.draw_map(scene_transition_target)

  player.draw()
  player.interact(current_scene)

  pygame.display.flip()
  clock.tick(60)