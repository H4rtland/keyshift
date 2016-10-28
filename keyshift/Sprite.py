import pygame
from keyshift.Frame import Frame

class Sprite(pygame.sprite.DirtySprite):
    """
    Convenience wrapper around pygame's DirtySprite.
    Handles positioning and visibility relative to parent.
    """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        if isinstance(self.parent, Frame):
            self.parent.add(self)

        self._x = 0
        self._y = 0

        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect((self.x, self.y, 0, 0))
        self.showing = True

    def set_pos(self, x, y):
        """
        Set position of sprite relative to parent.
        Accepts numerical values or a function/lambda with no arguments
        that returns a numerical value.
        :param x: Value/lambda for x position
        :param y: Value/lambda for y position
        :return: None
        """
        self.x = x
        self.y = y
        self.recalculate_rect()

    def recalculate_rect(self):
        """
        Recalculate rect based on global position of sprite.
        Updates visibility.
        :return:
        """
        self.rect = pygame.Rect((self.x, self.y, self.image.get_width(), self.image.get_height()))
        self.visible = self.is_showing()
        self.dirty = 1

    @property
    def width(self):
        return self.image.get_width()

    @property
    def height(self):
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
        """
        Get the scene this sprite is in.
        :return:
        """
        return self.parent.get_scene()

    def show(self):
        """
        Set visibility to True
        :return:
        """
        self.showing = True
        self.recalculate_rect()

    def hide(self):
        """
        Set visibility to False
        :return:
        """
        self.showing = False
        self.recalculate_rect()

    def is_showing(self):
        """
        Return if this sprite is visible.
        Accounts for visibility of parent sprite/frame.
        :return:
        """
        return self.showing and self.parent.is_showing()

    def remove(self):
        """
        Remove this sprite from the scene it's in.
        :return:
        """
        self.get_scene().remove(self)