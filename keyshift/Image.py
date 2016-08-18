'''
Created on 16/08/2016

@author: George
'''

import pygame

from keyshift.Sprite import Sprite
from keyshift.Resources import Resources

class Image(Sprite):
    def __init__(self, parent):
        super().__init__(parent)

    def set_image(self, image):
        image = Resources.load_image(image)
        self.image = image
        self.recalculate_rect()

    def set_blank(self, w, h, colour=(255, 255, 255, 255)):
        self.image = pygame.Surface((w, h), flags=pygame.SRCALPHA)
        self.image.fill(colour)
        self.recalculate_rect()