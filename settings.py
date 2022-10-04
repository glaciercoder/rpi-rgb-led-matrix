import imp
from geometry import Point

class UI_Settings:
    def __init__(self) -> None:
        self.width = 1200
        self.height = 800
        self.bg_color = (100, 100, 100)

        self.ticker_time = 20

class Lightsouce_Settings:
    def __init__(self) -> None:
        self.apex =40
        self.init_pos = Point(30, 30)
        self.init_dir = Point(0, -1)