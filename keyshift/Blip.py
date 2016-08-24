'''
Created on 18/08/2016

@author: George
'''

import math

import pygame

from keyshift.Image import Image

class Blip(Image):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_blank(4, 4, (0, 0, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 255), (2, 2), 2)
        self.speed = 2.5/16
        self.angle = 0
        self.life_cost = 1
        self.life = 0
        self.spawn_pos = (0, 0)
        self.target_pos = (0, 0)

    """def tick(self, time_passed):
        self.life += time_passed
        x = self.x + self.speed*math.sin(self.angle)
        y = self.y + self.speed*math.cos(self.angle)
        path_length = math.sqrt((self.spawn_pos[0]-self.target_pos[0])**2 + (self.spawn_pos[1]-self.target_pos[1])**2)
        expected_life = path_length/self.speed
        x += math.sin(self.life/expected_life)
        y += math.cos(self.life/expected_life)
        self.set_pos(x, y)
        self.dirty = 1"""