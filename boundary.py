from doctest import REPORTING_FLAGS
from fileinput import filename
from operator import imod
from re import L
import re
import sys
from numpy import isin, rec
import pygame as pg
from settings import UI_Settings
from geometry import Point
from geometry import Line
from geometry import Rectangle
from svg.path import parse_path
import svg.path.path

from xml.dom import minidom

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


class BoundaryMaker:
    """
        Class for boundary making, digest svg file and generate boundaries
    """
    def __init__(self, fila_name) -> None:
        self.file = fila_name
        self.boundaries = []

    def boundaries_gen(self):
        print('Generating Map:......')
        pic = minidom.parse(self.file)
        # Get rectangles
        rects = [(float(rect.getAttribute('x')), float(rect.getAttribute('y')), float(rect.getAttribute('width')), float(rect.getAttribute('height'))) for rect in pic.getElementsByTagName('rect')]
        for rect in rects:
            rectangle = Rectangle(Point(rect[0], rect[1]), Point(rect[0] + rect[2], rect[1] + rect[3]))
            rect_bound = Boundary(rectangle, type='Rectangle')
            self.boundaries.append(rect_bound)

        # Get lines
        path_strings = [path.getAttribute('d') for path in pic.getElementsByTagName('path')]
        for path_string in path_strings:
            path = parse_path(path_string)
            for e in path:
                if isinstance(e, svg.path.path.Line):
                    line = Line(Point(e.start.real, e.start.imag), Point(e.end.real, e.end.imag))
                    line_bound = Boundary(line)
                    self.boundaries.append(line_bound)

        pic.unlink()
        print('Map generated, elements:')
        for boundary in self.boundaries:
            print(boundary.geo)
        return self.boundaries

    def show(self, surface):
        for boundary in self.boundaries:
            boundary.show(surface)

if __name__ == '__main__':
    pg.init()
    ui_settings = UI_Settings()
    screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
    pg.display.set_caption("Boundary test")

    map  = BoundaryMaker('./maps/box_pic.svg')
    boundaries = map.boundaries_gen()
    # Create Boundary
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill(ui_settings.bg_color)
        map.show(screen)
        pg.display.flip()
        
