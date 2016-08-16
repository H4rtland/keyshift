'''
Created on 16/08/2016

@author: George
'''

import pygame

class Text(pygame.sprite.DirtySprite):
    fonts = {}
    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0

        self.font_name = "resource/font/PixelCaps.ttf"
        self.size = 16

    def set_text(self, text, font_name=None, size=None):
        if font_name is None:
            font_name = self.font_name
        if size is None:
            size = self.size

        self.font_name = font_name
        self.size = size

        if (font_name, size) in Text.fonts:
            font = Text.fonts[(font_name, size)]
        else:
            font = pygame.font.Font(font_name, size)
            Text.fonts[(font_name, size)] = font

        self.image = font.render(text, 0, (255, 255, 255))
        self.recalculate_rect()
        self.dirty = True

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.recalculate_rect()

    def recalculate_rect(self):
        self.rect = pygame.Rect((self.x, self.y, self.image.get_width(), self.image.get_height()))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()