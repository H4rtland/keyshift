from keyshift.Sprite import Sprite
from keyshift.Resources import Resources

class Text(Sprite):
    def __init__(self, parent):
        super().__init__(parent)

        self.x = 0
        self.y = 0

        self.font_name = "coders_crux"
        self.size = 32

        self.current_text = ""

    def set_text(self, text, font_name=None, size=None, colour=(255, 255, 255)):
        """
        Renders text to the image of this sprite.
        :param text: One line string to render
        :param font_name: Font name (Located in resource/font, don't include file extension)
        :param size: Font size
        :return: None
        """
        if font_name is None:
            font_name = self.font_name
        if size is None:
            size = self.size

        self.current_text = text

        self.font_name = font_name
        self.size = size

        font = Resources.load_font(font_name, size)

        self.image = font.render(text, 0, colour)
        self.recalculate_rect()
        self.dirty = True
