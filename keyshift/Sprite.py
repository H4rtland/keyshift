'''
Created on 16/08/2016

@author: George
'''

import pygame
from keyshift.Frame import Frame

class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        if isinstance(self.parent, Frame):
            self.parent.add(self)

        self._x = 0
        self._y = 0

        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect((self.x, self.y, 0, 0))

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.recalculate_rect()

    def recalculate_rect(self):
        self.rect = pygame.Rect((self.x, self.y, self.image.get_width(), self.image.get_height()))
        self.dirty = 1

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    @property
    def x(self):
        _x = self._x
        if callable(_x):
            _x = _x()
        return self.parent.x + _x

    @property
    def y(self):
        _y = self._y
        if callable(_y):
            _y = _y()
        return self.parent.y + _y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    def get_scene(self):
        return self.parent.get_scene()

    def show(self):
        self.visible = True
        self.dirty = 1

    def hide(self):
        self.visible = False
        self.dirty = 1

    def is_visible(self):
        return self.visible and self.parent.is_visible()