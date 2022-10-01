from asyncio import FastChildWatcher
from hashlib import new
from json.encoder import INFINITY
from lib2to3 import pygram
from lib2to3.pgen2 import pgen
import pygame as pg
from boundary import Boundary
import numpy as np
from geometry import Point, Rectangle
from ray import Ray
import math

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
        self.target_point = Point(0, 0)
        self.apex = apex
        self.rays = []
        self.color = (0, 0, 255)
        self.radius = 5
        self.gen_rays()

    def gen_rays(self):
        self.rays.clear()
        start_angle = - self.apex / 2
        for delta_angle in np.arange(0, self.apex, 3):
            dir_now = self.dir.rotate(math.radians(start_angle + delta_angle))
            self.rays.append(Ray(self.pos, dir_now))

    def show(self, surface, boundaries):
        self.gen_rays()
        pg.draw.circle(surface, self.color, (self.pos.x, self.pos.y), self.radius)
        for ray in self.rays:
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

    def update(self, boundaries, keys):
        if keys[pg.K_LEFT]:
            self.dir = Point(-1, 0)
            self.target_point = Point(-5, 0)
        elif keys[pg.K_RIGHT]:
            self.dir = Point(1, 0)
            self.target_point = Point(5, 0)
        elif keys[pg.K_UP]:
            self.dir = Point(0, -1)
            self.target_point = Point(0, -5)
        elif keys[pg.K_DOWN]:
            self.dir = Point(0, 1)
            self.target_point = Point(0, 5)
        delta_ray = Ray(self.pos, self.target_point)
        if_intersect = False
        for boundary in boundaries:
            if delta_ray.intersect(boundary, segment=True):
                if_intersect = True
                break
        if not if_intersect:
            self.pos = self.pos.move_to_new(self.target_point.x, self.target_point.y)
        self.target_point.x = 0
        self.target_point.y = 0