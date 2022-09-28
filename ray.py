from http.client import ImproperConnectionState
import random
from boundary import Boundary
from geometry import Point
from geometry import Line
import pygame as pg
class Ray:
    """
        class for ray, pos denotes the source point and dir denotes the direction
        dir is also given by Point
    """
    def __init__(self, pos, dir) -> None:
        self.pos = pos
        self.dir = dir
        self.color = (255, 255, 255)

    def show(self, surface):
        pg.draw.lines(surface, self.color, False, [(self.pos.x, self.pos.y), (self.pos.x + self.dir.x, self.pos.y + self.dir.y)])

    def intersect(self, boundary):
        if boundary.type == 'Line':
            x1 = boundary.a.x
            y1 = boundary.a.y
            x2 = boundary.b.x
            y2 = boundary.b.y
            x3 = self.pos.x
            y3 = self.pos.y
            x4 = self.pos.x + self.dir.x
            y4 = self.pos.y + self.dir.y
            not_parrel = ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
            if not_parrel:
                uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / not_parrel
                uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / not_parrel
                if (uA >= 0 and uA <= 1) and uB >= 0: 
                    a = Point(x1 + (uA * (x2-x1)), y1 + (uA * (y2-y1)))
                    pos = self.pos
                    dir = Point(a.x - self.pos.x, a.y - self.pos.y)
                    return Ray(pos, dir)
                else:
                    return None