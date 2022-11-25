import pygame
from classes.Scene import Scene
from classes.Wall import Wall
from classes.Interactable import Interactable
from classes.Item import Item
from singleton import singleton
from threading import Timer
from Items.sprites import barrels, key

sprite = pygame.transform.scale(
  pygame.image.load('sprites/background/fourth_room/0.png'),
  (1280, 720)
)

fourth_room = Scene("fourth_room", sprite)

def mount_fourth_room():
  left_top_limit = Wall((0, 0), (63, 280))
  left_bottom_limit = Wall((0, 420), (63, 720))
  right_limit = Wall((1235, 0), (50, 720))
  top_limit = Wall((0, 0), (1280, 65))
  bottom_left_limit = Wall((0, 680), (550, 40))
  bottom_center_limit = Wall((550, 680), (700, 40))
  bottom_right_limit = Wall((700, 680), (575, 40))

  fourth_room.add_wall(left_top_limit)
  fourth_room.add_wall(left_bottom_limit)
  fourth_room.add_wall(right_limit)
  fourth_room.add_wall(top_limit)
  fourth_room.add_wall(bottom_left_limit)
  fourth_room.add_wall(bottom_right_limit)

  def unblocked_forest():
    singleton.dialog = 'It opened a hole through!'
    s = Timer(3.0, singleton.reset_dialog)
    s.start()

  blocker_forest = Interactable(None, None, (625, 675), (30, 30), "picaxe", unblocked_forest, False, None)
  fourth_room.add_interactable(blocker_forest)

  if not blocker_forest.interacted:
    fourth_room.add_wall(bottom_center_limit)

  def got_picaxe():
    singleton.dialog = 'A picaxe? Maybe I could...'
    s = Timer(3.0, singleton.reset_dialog)
    bottom_center_limit.enabled = False
    s.start()

  picaxe = Item('picaxe', barrels, (-500, -500), (0, 0))
  forest_key = Item('forest_key', key, (200, 100), (30, 30))
  barrels_int = Interactable(barrels, barrels, (700, 200), (40, 40), "dialog", got_picaxe, False, picaxe)

  fourth_room.add_interactable(barrels_int)
  fourth_room.add_item(forest_key)

mount_fourth_room()
