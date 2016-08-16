'''
Created on 16/08/2016

@author: George
'''

import pygame
import zipfile
import os
import io

class Resources:
    archive = zipfile.ZipFile("resource.zip")
    fonts = {}
    images = {}

    @staticmethod
    def load_font(font_name, size, ext=".ttf"):
        if (font_name, size) in Resources.fonts:
            return Resources.fonts[(font_name, size)]
        if __debug__:
            filename = os.path.join("resource/font/", font_name) + ext
            font = pygame.font.Font(filename, size)
            Resources.fonts[(font_name, size)] = font
            return font
        else:
            pass

    @staticmethod
    def load_image(name):
        if name in Resources.images:
            return Resources.images[name].copy()
        if __debug__:
            path = os.path.join("resource/graphics/", name)
            image = pygame.image.load(path)
            image = image.convert_alpha()
            return image
        else:
            path = os.path.join("graphics/", name)
            imageFile = Resources.archive.read(path)
            image = pygame.image.load(io.BytesIO(imageFile))
            image = image.convert_alpha()
            return image