from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP
from lib2to3 import pygram
import sys
import pygame as pg
from ray import Ray
from boundary import Boundary
from settings import UI_Settings
from geometry import Point
from geometry import Line
from geometry import Rectangle
from light_source import LightSource
from ticker import Ticker


pg.init()
ticker = Ticker(20)
ui_settings = UI_Settings()
screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
pg.display.set_caption("Game")

# Create Boundary
a = Point(100, 100)
b = Point(500, 100)
direction =  Point(0, -50)
boundary1 = Boundary(Line(a, b))
boundary2 = Boundary(Rectangle(b, Point(700, 200)), type="Rectangle")
boundaries = [boundary1, boundary2]
light_source = LightSource(Point(300, 300), direction, 360)
target_point = light_source.pos 
while True:
    keys = pg.key.get_pressed()
    
    if ticker.check():
        if keys[pg.K_LEFT]:
                target_point = light_source.pos.move_to_new(-5, 0)
        elif keys[pg.K_RIGHT]:
            target_point = light_source.pos.move_to_new(5, 0)
        elif keys[pg.K_UP]:
            target_point = light_source.pos.move_to_new(0, -5)
        elif keys[pg.K_DOWN]:
            target_point = light_source.pos.move_to_new(0, 5)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
    screen.fill(ui_settings.bg_color)
    for boundary in boundaries:
        boundary.show(screen)
    light_source.update(target_point, boundaries)
    light_source.show(screen, boundaries)
    pg.display.flip()
    ticker.update()