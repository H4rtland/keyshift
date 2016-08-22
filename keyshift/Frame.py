'''
Created on 17/08/2016

@author: George
'''

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

    def get_width(self):
        w = 0
        for sprite in self.sprites:
            w = max(w, sprite._x + sprite.get_width())
        return w

    def get_height(self):
        w = 0
        for sprite in self.sprites:
            w = max(w, sprite._y + sprite.get_height())
        return w

    @property
    def x(self):
        return self.parent.x + self._x

    @property
    def y(self):
        return self.parent.y + self._y

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