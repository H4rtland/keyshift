'''
Created on 16/08/2016

@author: George
'''

import pygame

from keyshift.Sprite import Sprite
from keyshift.Resources import Resources

class Image(Sprite):
    def __init__(self):
        super().__init__()

    def set_image(self, image):
        image = Resources.load_image(image)