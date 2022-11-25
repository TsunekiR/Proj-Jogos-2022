import pygame
from classes.Scene import Scene
from classes.Wall import Wall
from singleton import singleton
from classes.Interactable import Interactable
from Items.sprites import lock

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/second_room/0.png'),
  (1280, 720)
)

first_room = Scene("first_room", sprite)

def mount_first_room():
  left_limit = Wall((0, 0), (63, 720))
  right_top_limit = Wall((1235, 0), (50, 280))
  right_bottom_limit = Wall((1235, 420), (50, 300))
  top_left_limit = Wall((0, 0), (580, 65))
  top_right_limit = Wall((670, 0), (580, 65))
  top_center_limit = Wall((580, 0), (700, 65))
  bottom_left_limit = Wall((0, 680), (575, 40))
  bottom_right_limit = Wall((700, 680), (575, 40))
  bottom_center_limit = Wall((575, 680), (700, 40))

  first_room.add_wall(left_limit)
  first_room.add_wall(right_top_limit)
  first_room.add_wall(right_bottom_limit)
  first_room.add_wall(top_left_limit)
  first_room.add_wall(top_right_limit)
  first_room.add_wall(bottom_left_limit)
  first_room.add_wall(bottom_right_limit)

  def unblocked_forest():
    bottom_center_limit.enabled = False

  blocker_forest = Interactable(lock, None, (625, 675), (30, 30), "forest_key", unblocked_forest, False, None)
  first_room.add_interactable(blocker_forest)

  if not blocker_forest.interacted:
    first_room.add_wall(bottom_center_limit)

  def unblocked_hallway():
    top_center_limit.enabled = False

  blocker_hallway = Interactable(lock, None, (610, 70), (30, 30), "hallway_key", unblocked_hallway, False, None)
  first_room.add_interactable(blocker_hallway)

  if not blocker_hallway.interacted:
    first_room.add_wall(top_center_limit)

mount_first_room()
