"""
    Ticker class used to control pygame frames
"""
from os import curdir
from re import T


class Ticker:
    def __init__(self, frames_per_move) -> None:
        self.frames_per_move = frames_per_move
        self.current_frame = frames_per_move

    def check(self):
        if self.current_frame == 0:
            self.current_frame = self.frames_per_move
            return True

    def update(self):
        if self.current_frame > 0:
            self.current_frame -= 1