import sys
from turtle import distance
import pygame as pg
from boundary import *
from settings import *
from light_source import LightSource
from ticker import Ticker
from frame import Frame

pg.init()

# import settings
ui_settings = UI_Settings()
ls_settings = Lightsouce_Settings()


# Load Widgets
ticker = Ticker(ui_settings.ticker_time)
screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
pg.display.set_caption("3D View")

while True:
    keys = pg.key.get_pressed()
    angles, distances = Frame().recv_data()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
    screen.fill(ui_settings.bg_color)
    pg.display.flip()
    ticker.update()