'''
Created on 16/08/2016

@author: George
'''

import pygame
import random

from keyshift.Frame import Frame
from keyshift.Scene import Scene
from keyshift.Text import Text
from keyshift.Image import Image
from keyshift.Key import Key
from keyshift.GameScene import GameScene

class MainMenuScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

        #pygame.mixer.music.set_volume
        pygame.mixer.music.load("resource/music/weightless_thoughts.ogg")
        pygame.mixer.music.play()

        self.title_shifts = ["KEYSHIFT"]
        self.title_shift_tick = 16
        self.title_shift_time = 0
        for i in range(0, 100):
            self.title_shifts.append(self.next_title(self.title_shifts[-1]))
        self.title_shifts = self.title_shifts[::-1]

        self.title = Text(self)
        self.title.set_text(self.title_shifts.pop(0), size=128)
        self.add(self.title)

        self.kb_frame = Frame(self)
        widths = [12, 12, 12, 11]
        offsets = [0, 25, 37, 12]
        for j in range(0, 4):
            for i in range(0, widths[j]):
                key = Key(self.kb_frame)
                key.set_pos(offsets[j]+50*i, 50*j)
                #self.add(key)
                #key = Image(self)
                #key.set_image("key")


        self.start_text = Text(self.kb_frame)
        self.start_text.set_text("START", size=16)
        self.start_text.set_pos(50+25+37-self.start_text.get_width()//2, 50+50+25-self.start_text.get_height()//2)
        self.add(self.start_text)

        self.kb_frame.set_pos(self.engine.width//2 - self.kb_frame.get_width()//2, self.engine.height//2 - self.kb_frame.get_height()//2)



        self.title.set_pos(self.engine.width//2 - self.title.get_width()//2, self.engine.height//4 - self.title.get_height()//2)

        self.wait_for_end = 500


    def tick(self, time_passed):
        self.tick_title(time_passed)

    def tick_end(self, time_passed):
        self.tick_title(time_passed)
        if len(self.sprites) == 0:
            self.wait_for_end -= time_passed
            if self.wait_for_end <= 0:
                return True
        else:
            self.sprites.remove(random.choice(list(self.sprites)))


    def key_press(self, key):
        if key == pygame.K_s:
            self.engine.set_scene(GameScene)

        if key == pygame.K_ESCAPE:
            self.engine.running = False


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