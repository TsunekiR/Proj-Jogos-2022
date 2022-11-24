class Singleton:
  def __init__(self):
    self.WINDOW_WIDTH = 1280
    self.WINDOW_HEIGHT = 720

    self.SPOT_BIGGER_SIZE = 50
    self.SPOT_SMALLER_SIZE = 10

    self.transitioning_scene = False
    self.transitioning_direction = None


singleton = Singleton()