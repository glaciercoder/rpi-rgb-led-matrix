from dis import dis
from math import radians
from math import sin
import pygame as pg
import numpy as np

class  Scene:
    def __init__(self, screen) -> None:
       self.screen = screen
       self.h_gain = 32000
       self.rect_width = 15
       self.background = './maps/background.png'
       self.color_nearest = (30,144,255)
       self.color_farthest = (25, 25, 112)

    # this function will be called just once
    def background_gen(self, top_color, bottom_color, steps, target_rect, mode='top'):
        if mode == 'top':
            color_step = [(tc - bc) / steps for tc, bc in zip(top_color, bottom_color)]
        else:
            color_step = [(bc - tc) / steps for tc, bc in zip(top_color, bottom_color)]
        for i in range(steps):
            if mode == 'top':
                color = [tc - i * step_c for tc, step_c in zip(top_color, color_step)]
            else:
                color = [tc + i * step_c for tc, step_c in zip(top_color, color_step)]
            step_size = target_rect.height / steps
            sub_rect = pg.Rect(target_rect.left, target_rect.top + (i * step_size), target_rect.width, step_size)
            pg.draw.rect(self.screen, tuple(color), sub_rect)

    def blit_background(self):
        background = pg.image.load(self.background).convert()
        self.screen.blit(background, (0, 0))
    
    # return the x positions, heights of the rectangles, D is client windows width
    def _get_rect(self, angles, distances, D):
        distances = [float(distance) for distance in distances]
        apex = max(angles)
        angles = [radians(angle - apex / 2) for angle in angles]
        x = [D * angle / radians(apex) + D / 2 for angle in angles]
        h = [self.h_gain / distance for distance in distances]    
        return x, h

    def _get_color(self, Hs):
        h_min = min(Hs)
        h_max = max(Hs)
        delta_c = []
        colors = []
        for i in range(0, 3):
            delta_c.append((self.color_farthest[i] - self.color_nearest[i]) / (h_max - h_min))
        for H in Hs:
            c = [self.color_nearest[i] + (h_max - H) * delta_c[i] for i in range(0, 3)] 
            colors.append(tuple(c))
        return colors

    def scene_gen(self, angles, distances, D, window_height ):
        self.blit_background()
        xs, hs = self._get_rect(angles, distances, D)
        print(hs)
        # Xs = np.arange(0, D-self.rect_width, self.rect_width)
        # Hs = np.interp(Xs, xs, hs)
        colors = self._get_color(hs)
        for X, H, c in zip(xs, hs, colors):
            rect = pg.Rect(X, (window_height - H) / 2, self.rect_width, H)
            pg.draw.rect(self.screen, c, rect)