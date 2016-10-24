'''
Created on 17/08/2016

@author: George
'''

import pygame

from keyshift.Frame import Frame
from keyshift.Text import Text
from keyshift.Image import Image


class Key(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.key = Image(self)
        self.key.set_image("key")
        self.blank_key = self.key.image.copy()
        self.get_scene().add(self.key)

        self.highlight = Image(self)
        self.highlight.set_image("key_inner")
        self.highlight.hide()
        self.get_scene().add(self.highlight)

        self.label = Text(self)
        self.label.set_text("")
        self.get_scene().add(self.label)
        self.label.set_pos(10, 4)
        #self.get_scene()

        self.press_time = 0

        self.default_position = (0, 0)

    def set_key(self, key):
        self.label.set_text(key)

    def press(self):
        #self.key.image.fill((255, 255, 255, 30))
        self.highlight.show()
        self.key.hide()
        self.press_time = 1
        self.label.set_pos(11, 6)
        self.label.set_text(self.label.current_text, size=24)
        #self.highlight.image.fill((255, 255, 255, 35), special_flags=pygame.BLEND_RGBA_MULT)

    def tick(self, time_passed):
        if self.press_time > 0:
            self.press_time += time_passed
        if self.press_time >= 100:
            self.highlight.hide()
            self.key.show()
            self.label.set_pos(10, 4)
            self.press_time = 0
            self.label.set_text(self.label.current_text, size=32)

    def reset_position(self):
        self.set_pos(*self.default_position)