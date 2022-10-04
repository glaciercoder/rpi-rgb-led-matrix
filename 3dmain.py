import sys
from turtle import distance
import pygame as pg
from boundary import *
from settings import *
from light_source import LightSource
from frame import Frame
from scene import Scene
pg.init()

# import settings
ui_settings = UI_Settings()
ls_settings = Lightsouce_Settings()


# Load Widgets
clock = pg.time.Clock()
screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
pg.display.set_caption("3D View")
background = pg.image.load('./maps/background.png').convert()
screen.blit(background, (0, 0))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    angles, distances = Frame().recv_data()
    
    pg.display.flip()

    clock.tick_busy_loop(60)