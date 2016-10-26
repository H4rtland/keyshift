'''
Created on 16/08/2016

@author: George
'''

import pygame
import zipfile
import os
import os.path as op
import io

class Resources:
    archive = zipfile.ZipFile("resource.zip")
    fonts = {}
    images = {}

    @staticmethod
    def load_font(font_name, size, ext=".ttf"):
        """
        Loads a file from resource/font/ or from resources.zip (todo).
        :param font_name: Font filename (no extension)
        :param size: Size to load font in
        :param ext: Font file extension
        :return: Pygame font
        """
        if (font_name, size) in Resources.fonts:
            # Return cached font if available
            return Resources.fonts[(font_name, size)]
        if __debug__:
            # Load from filesystem during development
            filename = os.path.join("resource/font/", font_name) + ext
            font = pygame.font.Font(filename, size)
            Resources.fonts[(font_name, size)] = font
            return font
        else:
            # Load from resources.zip in release
            pass

    @staticmethod
    def load_image(name):
        """
        Return a surface loaded with image located at path name, or loaded from resources.zip if in release.
        :param name: Filepath to image (no file ext, always .png)
        :return:
        """
        if name in Resources.images:
            # Return cached image if available
            return Resources.images[name].copy()
        if __debug__:
            # Load image from filesystem during development
            path = os.path.join("resource/graphics/", name) + ".png"
            image = pygame.image.load(path)
            image = image.convert_alpha()
            return image
        else:
            # Load image from resources.zip in release
            path = os.path.join("graphics/", name) + ".png"
            imageFile = Resources.archive.read(path)
            image = pygame.image.load(io.BytesIO(imageFile))
            image = image.convert_alpha()
            return image

    @staticmethod
    def load_music(filename):
        """
        Load a music file from the resources folder in development mode,
        or from the resources zip in release mode.
        :param filename: Music track filename (with ext)
        :return: BytesIO of file data
        :raises: IOError if file does not exist
        """
        full_path = op.join("resource/music/", filename)
        if __debug__:
            if op.exists(full_path):
                with open(full_path, "rb") as music_file:
                    return io.BytesIO(music_file.read())
            raise IOError("{} does not exist in resources music folder".format(filename))
        else:
            zip_path = op.join("music/", filename)
            if zip_path in Resources.archive.namelist():
                return io.BytesIO(Resources.archive.read(zip_path))
            raise IOError("{} does not exist in resources zip".format(filename))
