from asyncio import FastChildWatcher
from hashlib import new
from json.encoder import INFINITY
from lib2to3 import pygram
from lib2to3.pgen2 import pgen
import math
import pygame as pg
from boundary import Boundary
import numpy as np
from geometry import Point, Rectangle
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
        self.rays.clear()
        start_angle = - self.apex / 2
        dir =  self.dir.normalize() 

        for delta_angle in np.arange(0, self.apex, 3):
            angle = start_angle + delta_angle
            rad_angle = math.radians(angle)
            dir_now = Point(math.cos(rad_angle) * dir.x - math.sin(rad_angle) * dir.y, math.sin(rad_angle) * dir.x + math.cos(rad_angle) * dir.y)
            self.rays.append(Ray(self.pos, dir_now))

    def show(self, surface, boundaries):
        self.gen_rays()
        pg.draw.circle(surface, self.color, (self.pos.x, self.pos.y), self.radius)
        for ray in self.rays:
            distances = []
            minimum_dist = INFINITY
            final_ray = None
            for boundary in boundaries:
                intersections = ray.intersect(boundary)
                if intersections:
                    for intersection in intersections:
                        if intersection[1] < minimum_dist:
                            minimum_dist = intersection[1] 
                            final_ray = intersection[0]
            if final_ray:
                final_ray.show(surface)

    def update(self, point, boundaries):
        delta_ray = Ray(self.pos, point - self.pos)
        if_intersect = False
        for boundary in boundaries:
            if delta_ray.intersect(boundary, segment=True):
                # print("deltaray:")
                # print(delta_ray)
                # intersections =  delta_ray.intersect(boundary, segment=True)
                # for intersect in intersections:
                #     print(intersect)

                if_intersect = True
                break
        if not if_intersect:
            self.pos = point