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
from frame import Frame
class LightSource:
    """
        LightSource: generate rays and detect the collision
                    pos is the origin of the lightsource
                    dir is the direction of the light source
                    apex is the angle of apex angle centered at the dir, unit: degree
    """
    def __init__(self, settings)-> None:
        self.pos = settings.init_pos
        self.dir = settings.init_dir
        self.target_point = Point(0, 0)
        self.apex = settings.apex
        self.rays = []
        self.angles = np.arange(0, self.apex+settings.delta_angle, settings.delta_angle)
        self.distances = []
        self.color = (0, 0, 255)
        self.radius = 5

    def gen_rays(self, boundaries):
        self.distances.clear()
        self.rays.clear()
        start_angle = - self.apex / 2
        for delta_angle in self.angles:
            dir_now = self.dir.rotate(math.radians(start_angle + delta_angle))
            ray = Ray(self.pos, dir_now)
            minimum_dist = INFINITY
            final_ray = ray
            for boundary in boundaries:
                intersections = ray.intersect(boundary)
                if intersections:
                    for intersection in intersections:
                        if intersection[1] < minimum_dist:
                            minimum_dist = intersection[1] 
                            final_ray = intersection[0]
            self.rays.append(final_ray)
            self.distances.append(minimum_dist)

    def show(self, surface, boundaries):
        self.gen_rays(boundaries)
        pg.draw.circle(surface, self.color, (self.pos.x, self.pos.y), self.radius)
        for ray in self.rays:
            ray.show(surface)

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

    def send_data(self):
        frame = Frame()
        frame.update_data(self.angles, self.distances)
        frame.send_data()



