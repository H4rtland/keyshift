import math

class Frame:
    """
    Container for holding multiple sprites.
    Can also hold frames.
    """
    def __init__(self, parent):
        self.parent = parent
        if isinstance(self.parent, Frame):
            self.parent.add(self)
        self.sprites = []
        self._x = 0
        self._y = 0
        self.showing = True

    def add(self, sprite):
        """
        Add a sprite to this frame.
        :param sprite: Sprite to add
        :return: None
        """
        self.sprites.append(sprite)

    def set_pos(self, x, y):
        """
        Set the position of this frame relative to parent.
        Accepts numerical values or functions/lambdas that
        return a numerical value.
        Recalculates position of children.
        :param x: Value/lambda x position
        :param y: Value/lambda y position
        :return: None
        """
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
        """
        Get the scene this frame is in.
        :return: Scene
        """
        return self.parent.get_scene()

    def recalculate_rect(self):
        """
        Call recalculate_rect on all children.
        :return: None
        """
        for sprite in self.sprites:
            sprite.recalculate_rect()

    def show(self):
        """
        Set visible to True.
        Updates children.
        :return: None
        """
        self.showing = True
        self.recalculate_rect()

    def hide(self):
        """
        Set visible to False.
        Updates children.
        :return: None
        """
        self.showing = False
        self.recalculate_rect()

    def is_showing(self):
        """
        Returns if frame is visible and parent is visible.
        :return: boolean
        """
        return self.showing and self.parent.is_showing()

    def shift_left(self):
        """
        Shift all children so that there is no left padding.
        This method is never called but it was probably
        written for a good reason.
        :return: None
        """
        min_x = float("inf")
        for child in self.sprites:
            min_x = min(min_x, child._x)
        for child in self.sprites:
            child._x -= min_x
        self.recalculate_rect()

    def remove(self):
        """
        Remove all children.
        :return: None
        """
        for sprite in self.sprites:
            sprite.remove()