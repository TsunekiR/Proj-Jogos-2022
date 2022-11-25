class Singleton:
  def __init__(self):
    self.WINDOW_WIDTH = 1280
    self.WINDOW_HEIGHT = 720

    self.SPOT_BIGGER_SIZE = 90
    self.SPOT_SMALLER_SIZE = 10

    self.transitioning_scene = False
    self.transitioning_direction = None

    self.has_final_key = False
    self.has_hallway_key = False
    self.has_picaxe = False
    self.has_invisibility_cloak = False
    self.dialog = None

  def reset_dialog(self):
    self.dialog = None

singleton = Singleton()