from math import radians
import pygame as pg

class  Scene:
    def __init__(self, screen) -> None:
       self.screen = screen

    def background_gen(self, top_color, bottom_color, steps, target_rect):
        color_step = [(tc - bc) / steps for tc, bc in zip(top_color, bottom_color)]
        for i in range(steps):
            color = [tc - i * step_c for tc, step_c in zip(top_color, color_step)]
            color = [int(c) for c in color]
            step_size = target_rect.height / steps
            sub_rect = pg.Rect(target_rect.left, target_rect.top + (i * step_size), target_rect.width, step_size)
            pg.draw.rect(self.screen, tuple(color), sub_rect)
