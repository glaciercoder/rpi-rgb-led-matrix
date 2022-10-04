from dis import dis
from math import radians
from math import sin
import pygame as pg
import numpy as np

class  Scene:
    def __init__(self, screen) -> None:
       self.screen = screen
       self.h0 = 32000
       self.rect_width = 10
       self.background = './maps/background.png'

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
        a = D / ((distances[0] + distances[-1]) * sin(radians(apex / 2)))
        b = D * distances[0] / (distances[0] + distances[-1])
        x = []
        h = []
        for distance, angle in zip(distances, angles):
            e = a * distance * sin(angle) + b 
            if e >= 0:
                x.append(e)
                h.append(self.h0 / distance)
        return x, h
        
    def scene_gen(self, angles, distances, D, window_height ):
        self.blit_background()
        xs, hs = self._get_rect(angles, distances, D)
        print(hs)
        Xs = np.arange(0, D-self.rect_width, self.rect_width)
        Hs = np.interp(Xs, xs, hs)
        for X, H in zip(Xs, Hs):
            rect = pg.Rect(X, (window_height - H) / 2, self.rect_width, H)
            pg.draw.rect(self.screen,(30,144,255), rect)