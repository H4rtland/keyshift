'''
Created on 19/08/2016

@author: George
'''

import pygame

from keyshift.Image import Image
from keyshift.Resources import Resources

class HeartDisplay(Image):
    def __init__(self, parent):
        super().__init__(parent)
        self.heart_image = Resources.load_image("heart")
        self.heart_image = pygame.transform.scale(self.heart_image, (16, 16))

    def set_hearts(self, hearts):
        hearts = max(hearts, 0)
        self.set_blank(hearts*16, 16)
        for i in range(0, hearts):
            self.image.blit(self.heart_image, (16*i, 0))
        self.dirty = 1