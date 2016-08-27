'''
Created on 27/08/2016

@author: George
'''

import pygame

from keyshift.Scene import Scene
from keyshift.Frame import Frame
from keyshift.Text import Text
from keyshift.Keyboard import Keyboard
from keyshift.Layouts import layouts, names, order

class KeyboardLayoutScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

        self.settings_frame = Frame(self)

        key_layout_label = Text(self.settings_frame)
        key_layout_label.set_text("> KEY LAYOUT")
        key_layout_label.set_pos(0, 0)
        self.add(key_layout_label)

        self.available_layouts = order
        self.chosen_layout = 0

        self.key_layout_select = Text(self.settings_frame)
        self.key_layout_select.set_pos(0, 20)
        self.add(self.key_layout_select)

        #language_layout_label = Text(self.settings_frame)
        #language_layout_label.set_text("LANGUAGE")
        #language_layout_label.set_pos(0, 60)
        #self.add(language_layout_label)

        self.layout_keyboard = Keyboard(self.settings_frame)
        self.layout_keyboard.set_pos(275, 0)

        self.update_selected()

        self.settings_frame.set_pos(self.engine.width//2-self.settings_frame.get_width()//2, self.engine.height//2-self.settings_frame.get_height()//2)


    def key_press(self, key, unicode):
        if key == pygame.K_ESCAPE:
            from keyshift.MainMenuScene import MainMenuScene
            self.engine.set_scene(MainMenuScene)

        if key == pygame.K_RIGHT:
            if self.chosen_layout < len(self.available_layouts)-1:
                self.chosen_layout += 1
                self.update_selected()
        if key == pygame.K_LEFT:
            if self.chosen_layout > 0:
                self.chosen_layout -= 1
                self.update_selected()

    def update_selected(self):
        pre = "  < " if self.chosen_layout > 0 else "    "
        post = " >" if self.chosen_layout < len(self.available_layouts)-1 else "  "
        self.key_layout_select.set_text(pre + names[self.available_layouts[self.chosen_layout]] + post)
        self.layout_keyboard.set_layout(layouts[self.available_layouts[self.chosen_layout]])