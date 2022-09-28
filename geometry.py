from cmath import sqrt
import pygame as pg
import math
class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def normalize(self):
        norm = sqrt(self.x **2 + self.y ** 2) 
        return Point(self.x / norm.real, self.y / norm.real)

    def __mul__(self, ratio):
        return Point(self.x * ratio, self.y * ratio)

    def move_to_new(self, x, y):
        return Point(self.x + x, self.y + y)

class Line():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def show(self, surface, color):
            pg.draw.lines(surface, color, False, [(self.a.x, self.a.y), (self.b.x, self.b.y)])