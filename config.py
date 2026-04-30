from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

gap = 30
screen_dim = Point(280, 280+gap)
grid_size = 28
block_size = screen_dim.x // grid_size
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)