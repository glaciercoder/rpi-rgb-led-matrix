from asyncio import FastChildWatcher
from http.client import ImproperConnectionState
import random
from tkinter.messagebox import RETRY
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

    def __repr__(self) -> str:
        return 'Intersection:({},{}), ({},{})'.format(self.pos.x, self.pos.y, self.dir.x, self.dir.y)

    def show(self, surface):
        pg.draw.lines(surface, self.color, False, [(self.pos.x, self.pos.y), (self.pos.x + self.dir.x, self.pos.y + self.dir.y)])

    # get the intersection point of two lines, return the intersection point and the distance
    def _interset_line(self, line, segment=False):
            x1 = line.a.x
            y1 = line.a.y
            x2 = line.b.x
            y2 = line.b.y
            x3 = self.pos.x
            y3 = self.pos.y
            x4 = self.pos.x + self.dir.x
            y4 = self.pos.y + self.dir.y
            not_parrel = ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
            if not_parrel:
                uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / not_parrel
                uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / not_parrel
                if (uA >= 0 and uA <= 1) and uB >= 0: 
                    if segment and uB > 1:
                        return None
                    a = Point(x1 + (uA * (x2-x1)), y1 + (uA * (y2-y1)))
                    pos = self.pos
                    dir = Point(a.x - self.pos.x, a.y - self.pos.y)
                    return (Ray(pos, dir), uB)
                else:
                    return None

    """
        segment to choose whether use a segment model
        return a list of tuple
    """
    def intersect(self, boundary, segment = False):
        if boundary.type == 'Line':
            intersection =  self._interset_line(boundary.geo, segment)
            return [intersection] if intersection else None
        elif boundary.type == 'Rectangle':
            lines = boundary.geo.get_side(self.pos)
            intersections = []
            for line in lines:
                intersection = self._interset_line(line, segment)
                if intersection:
                    intersections.append(intersection)
            return intersections if intersections else None