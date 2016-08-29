'''
Created on 16/08/2016

@author: George
'''

import pygame
import random
import math

import sys

from keyshift.Frame import Frame
from keyshift.Scene import Scene
from keyshift.Text import Text
from keyshift.Image import Image
from keyshift.Key import Key
from keyshift.GameScene import GameScene
from keyshift.Audio import Audio
from keyshift.Resources import Resources
from keyshift.Keyboard import Keyboard
from keyshift.Layouts import layouts
from keyshift.KeyboardLayoutScene import KeyboardLayoutScene

class MainMenuScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)


        Audio.play_music("resource/music/weightless_thoughts.ogg")

        self.title_shifts = ["KEYSHIFT"]
        self.title_shift_tick = 16
        self.title_shift_time = 0
        for i in range(0, 100):
            self.title_shifts.append(self.next_title(self.title_shifts[-1]))
        self.title_shifts = self.title_shifts[::-1]

        self.title = Text(self)
        self.title.set_text(self.title_shifts.pop(0), size=128)
        self.add(self.title)

        self.fps = Text(self)
        self.fps.set_pos(1, 1)


        self.keyboard = Keyboard(self)
        self.keyboard.set_layout(layouts[self.engine.config["layout"]["key_layout"]], no_label=True)
        self.start_key = random.choice(list(self.keyboard.keys.keys()))
        sk = self.keyboard.keys[self.start_key]

        self.start_text = Text(self.keyboard)
        self.start_text.set_text("START", size=16)
        self.start_text.set_pos(sk.x+24-self.start_text.get_width()//2, sk.y+24-self.start_text.get_height()//2)
        self.add(self.start_text)

        self.keyboard.set_pos(self.engine.width//2 - self.keyboard.get_width()//2, self.engine.height//2 - self.keyboard.get_height()//2)



        self.title.set_pos(self.engine.width//2 - self.title.get_width()//2, self.engine.height//4 - self.title.get_height()//2)

        self.wait_for_end = 500

        self.a = Image(self)
        self.a.set_blank(100, 100, colour=(0, 0, 0))
        self.a.set_pos(300, 0)
        #self.add(self.a)
        self.steps = 0

        self.spacebar_frame = Frame(self.keyboard)
        self.spacebar = Image(self.spacebar_frame)
        self.spacebar.set_blank(288, 47)
        key_image = Resources.load_image("key")
        self.spacebar.image.blit(key_image, (0, 0), area=(0, 0, 40, 57))
        self.spacebar.image.blit(key_image, (288-40, 0), area=(7, 0, 47, 47))
        pygame.draw.line(self.spacebar.image, (255, 255, 255), (15, 0), (288-15, 0))
        pygame.draw.line(self.spacebar.image, (255, 255, 255), (15, 46), (288-15, 46))
        self.spacebar_frame.set_pos(50*3, 50*4)
        self.add(self.spacebar)

        self.spacebar_text = Text(self.spacebar_frame)
        self.spacebar_text.set_text("CHANGE KEYBOARD LAYOUT", size=16)
        self.spacebar_text.set_pos(288//2-self.spacebar_text.get_width()//2, 47//2-self.spacebar_text.get_height()//2)
        self.add(self.spacebar_text)



    def tick(self, time_passed):
        self.tick_title(time_passed)
        for key in self.keyboard.keys:
            self.keyboard.keys[key].tick(time_passed)
        self.fps.set_text("{0:.02f}".format(self.engine.clock.get_fps()))


    def tick_end(self, time_passed):
        self.tick_title(time_passed)
        for key in self.keyboard.keys:
            self.keyboard.keys[key].tick(time_passed)
        if len(self.sprites) == 0:
            self.wait_for_end -= time_passed
            if self.wait_for_end <= 0:
                return True
        else:
            self.sprites.remove(random.choice(list(self.sprites)))


    def key_press(self, key, unicode):
        unicode = unicode.upper()
        if unicode in self.keyboard.keys:
            if unicode == self.start_key:
                #from keyshift.EndScene import EndScene
                self.engine.set_scene(GameScene)
            self.keyboard.keys[unicode].press()

        if key == pygame.K_ESCAPE:
            self.engine.running = False

        if key == pygame.K_SPACE:
            self.engine.set_scene(KeyboardLayoutScene)


    def next_title(self, current):
        orig = current
        while True:
            current = current+ " "
            shift_index = random.randint(0, len(current)-3)
            new = current[0:shift_index] + current[shift_index+1] + current[shift_index] + current[shift_index+2:len(current)]
            if new == "KEYSHIFT" or "SHIT" in new or new == orig:
                continue
            return new.replace(" ", "")

    def tick_title(self, time_passed):
        if len(self.title_shifts) > 0:
            self.title_shift_time += time_passed
            if self.title_shift_time > self.title_shift_tick:
                self.title_shift_time -= self.title_shift_tick
                self.title.set_text(self.title_shifts.pop(0))
                if len(self.title_shifts) < 20:
                    extra_ms = (20-len(self.title_shifts))
                    self.title_shift_tick = 16 + 10*extra_ms*(1+(extra_ms/100))**2