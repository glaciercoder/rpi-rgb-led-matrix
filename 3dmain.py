import sys
from turtle import distance
from numpy import gradient
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
scene = Scene(screen)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    scene.background_gen((255, 255, 255), (0, 0, 0), 100, pg.Rect(100, 100, 500, 500))
    angles, distances = Frame().recv_data()
    pg.display.flip()

    clock.tick_busy_loop(60)