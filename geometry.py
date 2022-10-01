from cmath import sqrt
from re import A, X
import pygame as pg
import math
class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def normalize(self):
        norm = sqrt(self.x **2 + self.y ** 2) 
        return Point(self.x / norm.real, self.y / norm.real)
    
    # rotate couterclockwise, in rad
    def rotate(self, theta):
        return Point(math.cos(theta) * self.x - math.sin(theta) * self.y, math.sin(theta) * self.x + math.cos(theta) * self.y)

    def __mul__(self, ratio):
        return Point(self.x * ratio, self.y * ratio)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def __repr__(self) -> str:
        return "x:{},y:{}".format(self.x, self.y)

    def move_to_new(self, x, y):
        return Point(self.x + x, self.y + y)

class Line():
    """
        Line: a line segment, a, b for its end point
    """
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.color = (245, 164, 96)

    def show(self, surface):
            pg.draw.lines(surface, self.color, False, [(self.a.x, self.a.y), (self.b.x, self.b.y)])

class Rectangle:
    """
        Rectange: a rectangle, init by its left corener and right corner a and b
    """
    def __init__(self, a, b) -> None:
        self.p1 = a
        self.p3 = b
        self.p2 = self.p1.move_to_new(self.p3.x - self.p1.x, 0)
        self.p4 = self.p1.move_to_new(0, self.p3.y - self.p1.y)
        self.l1 = Line(self.p1, self.p2)
        self.l2 = Line(self.p2, self.p3)
        self.l3 = Line(self.p3, self.p4)
        self.l4 = Line(self.p4, self.p1)
        self.color = (127, 255, 212)

    def show(self, surface):
        pg.draw.rect(surface, self.color, pg.Rect(self.p1.x, self.p1.y, self.p3.x - self.p1.x, self.p3.y - self.p1.y), 2)

    # Return the possip3le collision side
    def get_side(self, p):
        if p.x <= self.p1.x:
            if p.y <= self.p1.y:
                return [self.l1, self.l4] 
            elif p.y > self.p1.y and p.y <= self.p4.y:
                return [self.l4] 
            else:
                return [self.l3, self.l4]
        elif p.x > self.p1.x and p.x <= self.p2.x:
            if p.y <= self.p1.y:
                return [self.l1]
            else:
                return [self.l3]
        else:
            if p.y <= self.p1.y:
                return [self.l2, self.l1] 
            elif p.y > self.p1.y and p.y <= self.p4.y:
                return [self.l2] 
            else:
                return [self.l2, self.l3]


        