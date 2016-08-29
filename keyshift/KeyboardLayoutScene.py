'''
Created on 27/08/2016

@author: George
'''

import pygame

from keyshift.Scene import Scene
from keyshift.Frame import Frame
from keyshift.Text import Text
from keyshift.Keyboard import Keyboard
from keyshift.Layouts import layouts, names, order, warning_message

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

        self.warning_message = Text(self.settings_frame)
        self.warning_message.size = 64
        self.warning_message.set_pos(lambda: self.layout_keyboard._x+self.layout_keyboard.get_width()//2-self.warning_message.get_width()//2,
                                     lambda: self.layout_keyboard._y+self.layout_keyboard.get_height()+10)
        self.add(self.warning_message)

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

        unicode = unicode.upper()
        if unicode in self.layout_keyboard.keys.keys():
            key = self.layout_keyboard.keys[unicode]
            if key.is_showing():
                key.press()

    def tick(self, time_passed):
        for key in self.layout_keyboard.keys:
            self.layout_keyboard.keys[key].tick(time_passed)

    def update_selected(self):
        layout_identifier = self.available_layouts[self.chosen_layout]
        pre = "  < " if self.chosen_layout > 0 else "    "
        post = " >" if self.chosen_layout < len(self.available_layouts)-1 else "  "
        self.key_layout_select.set_text(pre + names[layout_identifier] + post)
        self.layout_keyboard.set_layout(layouts[layout_identifier])
        if layout_identifier in warning_message:
            self.warning_message.set_text(warning_message[layout_identifier])
        else:
            self.warning_message.set_text("")