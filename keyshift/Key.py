'''
Created on 17/08/2016

@author: George
'''

import pygame

from keyshift.Image import Image


class Key(Image):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_image("key")
        self.blank_key = self.image.copy()

    def press(self):
        self.image.fill((255, 255, 255, 30))