import sys
from numpy import rec
import pygame as pg
from settings import UI_Settings
from geometry import Point
from geometry import Line
from geometry import Rectangle

class Boundary:
    """
        Class for boudary, consists of two points
        Boudary type can be 'Line', 'Rectangle', 'Circle'
    """
    def __init__(self, geometry, type = 'Line') -> None:
        self.geo = geometry
        self.type = type
        
    def show(self, surface):
        self.geo.show(surface)

if __name__ == '__main__':
    pg.init()
    ui_settings = UI_Settings()
    screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
    pg.display.set_caption("Boundary test")

    # Create Boundary
    a = Point(100, 100)
    b = Point(500, 100)
    c = Point(700, 200)
    rect = Rectangle(b, c)
    boudary = Boundary(Line(a, b))
    boudary2 = Boundary(rect, type='Rectangle')
    boundary3 = Boundary(Line(b, c))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill(ui_settings.bg_color)

        boudary.show(screen)
        boudary2.show(screen)
        boundary3.show(screen)
        pg.display.flip()
        
