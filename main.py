import sys
import pygame as pg
from ray import Ray
from boundary import Boundary
from settings import UI_Settings
from geometry import Point
from light_source import LightSource


pg.init()
ui_settings = UI_Settings()
screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
pg.display.set_caption("Game")

# Create Boundary
a = Point(100, 100)
b = Point(500, 100)
source_point = Point(300, 300)
direction =  Point(0, -50)
boudary = Boundary(a, b)
light_source = LightSource(source_point, direction, 360)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    screen.fill(ui_settings.bg_color)

    boudary.show(screen)
    light_source.show(screen, boudary)
    pg.display.flip()