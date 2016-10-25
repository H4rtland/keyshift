'''
Created on 17/08/2016

@author: George
'''

import math

class Frame:
    def __init__(self, parent):
        self.parent = parent
        if isinstance(self.parent, Frame):
            self.parent.add(self)
        self.sprites = []
        self._x = 0
        self._y = 0
        self.showing = True

    def add(self, sprite):
        self.sprites.append(sprite)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        for sprite in self.sprites:
            sprite.recalculate_rect()

    @property
    def width(self):
        w = 0
        for sprite in self.sprites:
            x = sprite._x
            if callable(x):
                x = x()
            w = max(w, x + sprite.width)
        return w

    @property
    def height(self):
        h = 0
        for sprite in self.sprites:
            y = sprite._y
            if callable(y):
                y = y()
            h = max(h, y + sprite.height)
        return h

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

    def recalculate_rect(self):
        for sprite in self.sprites:
            sprite.recalculate_rect()

    def show(self):
        self.showing = True
        self.recalculate_rect()

    def hide(self):
        self.showing = False
        self.recalculate_rect()

    def is_showing(self):
        return self.showing and self.parent.is_showing()

    def shift_left(self):
        min_x = float("inf")
        for child in self.sprites:
            min_x = min(min_x, child._x)
        for child in self.sprites:
            child._x -= min_x
        self.recalculate_rect()

    def remove(self):
        for sprite in self.sprites:
            sprite.remove()