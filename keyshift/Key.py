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

        self.label = Text(self)
        self.label.set_text("")
        self.get_scene().add(self.label)
        self.label.set_pos(10, 4)
        #self.get_scene()

    def set_key(self, key):
        self.label.set_text(key)

    def press(self):
        self.key.image.fill((255, 255, 255, 30))