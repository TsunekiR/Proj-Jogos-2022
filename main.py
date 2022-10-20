import os, sys
import pygame
from scenes.main import build_map
from scenes.First import first_scene
from classes import Player
from singleton import singleton

pygame.init()
build_map()

screen = pygame.display.set_mode((singleton.WINDOW_WIDTH, singleton.WINDOW_HEIGHT))
clock = pygame.time.Clock()
current_scene = first_scene
player = Player(screen)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit
  
  current_scene = current_scene.check_for_scene_transitions(player)
  current_scene.draw_map(screen)

  player.draw()

  pygame.display.flip()
  clock.tick(60)