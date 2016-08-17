'''
Created on 17/08/2016

@author: George
'''

import pygame

from keyshift.Scene import Scene
from keyshift.Frame import Frame
from keyshift.Image import Image
from keyshift.Key import Key

class GameScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

        key_order = list("1234567890-=QWERTYUIOP[]ASDFGHJKL;'#\ZXCVBNM,./")

        self.keys = {}

        self.kb_frame = Frame(self)
        widths = [12, 12, 12, 11]
        offsets = [0, 25, 37, 12]
        for j in range(0, 4):
            for i in range(0, widths[j]):
                key = Key(self.kb_frame)
                key.set_pos(offsets[j]+50*i, 50*j)
                label = key_order.pop(0)
                key.set_key(label)
                self.keys[label] = key



        self.kb_frame.set_pos(self.engine.width//2 - self.kb_frame.get_width()//2, self.engine.height//2 - self.kb_frame.get_height()//2)

    def key_press(self, key, unicode):
        if key == pygame.K_ESCAPE:
            from keyshift.MainMenuScene import MainMenuScene
            self.engine.set_scene(MainMenuScene)
        unicode = unicode.upper()
        if unicode in self.keys:
            self.keys[unicode].press()