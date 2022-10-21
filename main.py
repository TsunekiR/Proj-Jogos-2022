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
  
  current_scene = current_scene.check_for_scene_transitions(player)
  current_scene.draw_map()

  player.draw()

  pygame.display.flip()
  clock.tick(60)