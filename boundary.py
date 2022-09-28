from lib2to3 import pygram
from operator import imod
from turtle import color
from re import X
import sys
import pygame as pg
from settings import UI_Settings
from geometry import Point
import collision
class Boundary:
    """
        Class for boudary, consists of two points
        Boudary type can be 'Line', 'Rectangle', 'Circle'
        For 'line': *points accept two points as the end points
        For 'Rectangle': *points accept two points as leftup corner and rightdown corner
        For 'Circle': *points accept two points as origin and radius
    """
    def __init__(self, *points, type = 'Line') -> None:
        self.a = points[0]
        self.b = points[1]
        self.type = type
        self.color = (245, 164, 96)

    def show(self, surface):
        if self.type == 'Line':
            pg.draw.lines(surface, self.color, False, [(self.a.x, self.a.y), (self.b.x, self.b.y)])
        elif self.type == 'Rectangle':
            pg.draw.rect(surface, self.color, pg.Rect(a.x, a.y, b.x, b.y))
        elif self.type == 'Circle':
            pg.draw.circle(surface, self.color, (a.x, a.y), b.x)

if __name__ == '__main__':
    pg.init()
    ui_settings = UI_Settings()
    screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
    pg.display.set_caption("Boundary test")

    # Create Boundary
    a = Point(100, 100)
    b = Point(500, 100)
    boudary = Boundary(a, b)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill(ui_settings.bg_color)

        boudary.show(screen)
        pg.display.flip()
        
