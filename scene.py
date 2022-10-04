from math import radians
import pygame as pg

class  Scene:
    def __init__(self, screen) -> None:
       self.screen = screen

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