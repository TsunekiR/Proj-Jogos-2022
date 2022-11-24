from scenes.Forest import *
from scenes.CastleEntry import *
from scenes.FirstRoom import *
from scenes.AuxiliarRoom import *
from scenes.Hallway import *
from scenes.SecondRoom import *
from scenes.ThirdRoom import *
from scenes.FourthRoom import *

def build_forest():
  forest.reset_transition_spots()
  forest.add_scene_transition_spot(castle_entry, 'top')

def build_castle_entry():
  castle_entry.reset_transition_spots()
  castle_entry.add_scene_transition_spot(forest, 'bottom')
  castle_entry.add_scene_transition_spot(first_room, 'top')

def build_first_room():
  castle_entry.reset_transition_spots()
  first_room.add_scene_transition_spot(castle_entry, 'bottom')
  first_room.add_scene_transition_spot(auxiliar_room, 'right')
  first_room.add_scene_transition_spot(hallway, 'top')

def build_auxiliar_room():
  auxiliar_room.reset_transition_spots()
  auxiliar_room.add_scene_transition_spot(first_room, 'left')

def build_hallway():
  hallway.reset_transition_spots()
  hallway.add_scene_transition_spot(first_room, 'bottom')
  hallway.add_scene_transition_spot(second_room, 'top')

def build_second_room():
  second_room.reset_transition_spots()
  second_room.add_scene_transition_spot(hallway, 'bottom')
  second_room.add_scene_transition_spot(third_room, 'top')
  second_room.add_scene_transition_spot(fourth_room, 'right')

def build_third_room():
  third_room.reset_transition_spots()
  third_room.add_scene_transition_spot(second_room, 'bottom')


def build_fourth_room():  
  fourth_room.add_scene_transition_spot(second_room, 'right')
  fourth_room.add_scene_transition_spot(auxiliar_room, 'top')

map_builders = {
  forest.id: build_forest,
  castle_entry.id: build_castle_entry,
  first_room.id: build_first_room,
  auxiliar_room.id: build_auxiliar_room,
  hallway.id: build_hallway,
  second_room.id: build_second_room,
  third_room.id: build_third_room,
  fourth_room.id: build_fourth_room,
}
