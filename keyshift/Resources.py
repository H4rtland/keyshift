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
        :raises: OSError if font file does not exist
        """
        if (font_name, size) in Resources.fonts:
            # Return cached font if available
            return Resources.fonts[(font_name, size)]
        if __debug__:
            # Load from filesystem during development
            filepath = op.join("resource/font/", font_name) + ext
            if op.exists(filepath):
                font = pygame.font.Font(filepath, size)
                Resources.fonts[(font_name, size)] = font
                return font
            raise OSError("{}{} does not exist in resources folder".format(font_name, ext))
        else:
            # Load from resources.zip in release
            zip_path = op.join("font/", font_name) + ext
            if zip_path in Resources.archive.namelist():
                font_data = io.BytesIO(Resources.archive.read(zip_path))
                font = pygame.font.Font(font_data, size)
                Resources.fonts[(font_name, size)] = font
                return font
            raise OSError("{}{} does not exist in resources zip".format(font_name, ext))


    @staticmethod
    def load_image(name):
        """
        Return a surface loaded with image located at path name, or loaded from resources.zip if in release.
        :param name: Filepath to image (no file ext, always .png)
        :return: Image surface
        :raises: OSError if image file does not exist
        """
        if name in Resources.images:
            # Return cached image if available
            return Resources.images[name].copy()
        if __debug__:
            # Load image from filesystem during development
            path = op.join("resource/graphics/", name) + ".png"
            if op.exists(path):
                image = pygame.image.load(path)
                image = image.convert_alpha()
                Resources.images[name] = image
                return image
            raise OSError("{}.png does not exist in resources folder".format(name))
        else:
            # Load image from resources.zip in release
            path = op.join("graphics/", name) + ".png"
            if path in Resources.archive.namelist():
                image_file = Resources.archive.read(path)
                image = pygame.image.load(io.BytesIO(image_file))
                image = image.convert_alpha()
                Resources.images[name] = image
                return image
            raise OSError("{}.png does not exist in resources zip".format(name))


    @staticmethod
    def load_music(filename):
        """
        Load a music file from the resources folder in development mode,
        or from the resources zip in release mode.
        :param filename: Music track filename (with ext)
        :return: BytesIO of file data
        :raises: OSError if file does not exist
        """
        full_path = op.join("resource/music/", filename)
        if __debug__:
            if op.exists(full_path):
                with open(full_path, "rb") as music_file:
                    return io.BytesIO(music_file.read())
            raise OSError("{} does not exist in resources music folder".format(filename))
        else:
            zip_path = op.join("music/", filename)
            if zip_path in Resources.archive.namelist():
                return io.BytesIO(Resources.archive.read(zip_path))
            raise OSError("{} does not exist in resources zip".format(filename))
