'''
Created on 16/08/2016

@author: George
'''

import pygame

class Sprite(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0

        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect((self.x, self.y, 0, 0))

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.recalculate_rect()

    def recalculate_rect(self):
        self.rect = pygame.Rect((self.x, self.y, self.image.get_width(), self.image.get_height()))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()