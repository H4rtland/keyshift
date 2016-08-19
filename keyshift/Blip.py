'''
Created on 18/08/2016

@author: George
'''

import math

from keyshift.Image import Image

class Blip(Image):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_blank(3, 3, (255, 255, 255))
        self.speed = 2.5
        self.angle = 0

    def tick(self, time_passed):
        x = self.x + self.speed*math.sin(self.angle)
        y = self.y + self.speed*math.cos(self.angle)
        self.set_pos(x, y)
        self.dirty = 1