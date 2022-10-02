import sys
import pygame as pg
from boundary import *
from settings import *
from light_source import LightSource
from ticker import Ticker
import socket

pg.init()

# import settings
ui_settings = UI_Settings()
ls_settings = Lightsouce_Settings()

# Load Map
map = BoundaryMaker('./maps/map1.svg')
boundaries = map.boundaries_gen()

# Load Widgets
ticker = Ticker(ui_settings.ticker_time)
light_source = LightSource(ls_settings.init_pos, ls_settings.init_dir, ls_settings.apex)
screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
pg.display.set_caption("2D View")

while True:
    keys = pg.key.get_pressed()
    
    # Update position
    if ticker.check():
        light_source.update(boundaries, keys)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
    screen.fill(ui_settings.bg_color)
    # Update rays
    light_source.show(screen, boundaries)
    light_source.send_data()
    map.show(screen)
    pg.display.flip()
    ticker.update()