import pygame

from keyshift.Sprite import Sprite
from keyshift.Resources import Resources

class Image(Sprite):
    def __init__(self, parent):
        super().__init__(parent)

    def set_image(self, image):
        """
        Set the image of this sprite to the image located at the given file path.
        :param image: Path to image file
        :return: None
        """
        image = Resources.load_image(image)
        self.image = image
        self.recalculate_rect()

    def set_blank(self, w, h, colour=(0, 0, 0, 0)):
        """
        Set the image of this sprite to a solid colour of specified width and height.
        Colour also accepts alpha value.
        :param w: surface width
        :param h: surface height
        :param colour: surface colour
        :return:
        """
        self.image = pygame.Surface((w, h), flags=pygame.SRCALPHA)
        self.image.fill(colour)
        self.recalculate_rect()