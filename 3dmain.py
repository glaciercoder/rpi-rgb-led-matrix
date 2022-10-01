import sys
import pygame as pg
from boundary import *
from settings import *
from light_source import LightSource
from ticker import Ticker


pg.init()

# import settings
ui_settings = UI_Settings()
ls_settings = Lightsouce_Settings()


# Load Widgets
ticker = Ticker(ui_settings.ticker_time)
light_source = LightSource(ls_settings.init_pos, ls_settings.init_dir, ls_settings.apex)
screen = pg.display.set_mode((ui_settings.width, ui_settings.height))
pg.display.set_caption("3D View")

while True:
    keys = pg.key.get_pressed()
    
    if ticker.check():
        light_source.update(boundaries, keys)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
    screen.fill(ui_settings.bg_color)
    light_source.show(screen, boundaries)
    map.show(screen)
    pg.display.flip()
    ticker.update()