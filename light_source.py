from hashlib import new
from lib2to3 import pygram
from lib2to3.pgen2 import pgen
import math
import pygame as pg
from boundary import Boundary
import numpy as np
from geometry import Point
from ray import Ray

class LightSource:
    """
        LightSource: generate rays and detect the collision
                    pos is the origin of the lightsource
                    dir is the direction of the light source
                    apex is the angle of apex angle centered at the dir, unit: degree
    """
    def __init__(self, pos, dir, apex) -> None:
        self.pos = pos
        self.dir = dir
        self.apex = apex
        self.rays = []
        self.color = (0, 0, 255)
        self.radius = 5
        self.gen_rays()

    def gen_rays(self):
        start_angle = - self.apex / 2
        dir =  self.dir.normalize() 

        for delta_angle in np.arange(0, self.apex, 1):
            angle = start_angle + delta_angle
            rad_angle = math.radians(angle)
            dir_now = Point(math.cos(rad_angle) * dir.x - math.sin(rad_angle) * dir.y, math.sin(rad_angle) * dir.x + math.cos(rad_angle) * dir.y)
            self.rays.append(Ray(self.pos, dir_now))

    def show(self, surface, *boudaries):
        pg.draw.circle(surface, self.color, (self.pos.x, self.pos.y), self.radius)
        for boundary in boudaries:
            for ray in self.rays:
                new_ray = ray.intersect(boundary)
                if new_ray:
                    new_ray.show(surface)
                else:
                    Ray(self.pos, ray.dir * 100000).show(surface)

