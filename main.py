from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP
from lib2to3 import pygram
import sys
import pygame as pg
from ray import Ray
from boundary import Boundary
from settings import *
from geometry import Point
from geometry import Line
from geometry import Rectangle
from light_source import LightSource
from ticker import Ticker


pg.init()

# import settings
ui_settings = UI_Settings()
ls_settings = Lightsouce_Settings()
ticker = Ticker(ui_settings.ticker_time)
screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
pg.display.set_caption("Game")

# Create Boundary
a = Point(100, 100)
b = Point(500, 100)
boundary1 = Boundary(Line(a, b))
boundary2 = Boundary(Rectangle(b, Point(700, 200)), type="Rectangle")
boundaries = [boundary1, boundary2]
light_source = LightSource(ls_settings.init_pos, ls_settings.init_dir, ls_settings.apex)
while True:
    keys = pg.key.get_pressed()
    
    if ticker.check():
        light_source.update(boundaries, keys)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
    screen.fill(ui_settings.bg_color)
    for boundary in boundaries:
        boundary.show(screen)
    light_source.show(screen, boundaries)
    pg.display.flip()
    ticker.update()