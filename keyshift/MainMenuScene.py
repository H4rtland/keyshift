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
        #self.add(self.fps)

        """self.kb_frame = Frame(self)
        widths = [12, 12, 12, 11]
        offsets = [0, 25, 37, 12]
        for j in range(0, 4):
            for i in range(0, widths[j]):
                key = Key(self.kb_frame)
                key.set_pos(offsets[j]+50*i, 50*j)
                #self.add(key)
                #key = Image(self)
                #key.set_image("key")"""

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
                #key.set_key(label)
                self.keys[label] = key

        self.start_key = random.choice(list(self.keys.keys()))
        sk = self.keys[self.start_key]

        self.start_text = Text(self.kb_frame)
        self.start_text.set_text("START", size=16)
        self.start_text.set_pos(sk.x+24-self.start_text.get_width()//2, sk.y+24-self.start_text.get_height()//2)
        self.add(self.start_text)

        self.kb_frame.set_pos(self.engine.width//2 - self.kb_frame.get_width()//2, self.engine.height//2 - self.kb_frame.get_height()//2)



        self.title.set_pos(self.engine.width//2 - self.title.get_width()//2, self.engine.height//4 - self.title.get_height()//2)

        self.wait_for_end = 500

        self.a = Image(self)
        self.a.set_blank(100, 100, colour=(0, 0, 0))
        self.a.set_pos(300, 0)
        #self.add(self.a)
        self.steps = 0
        #for i in range(0, 45):
        #    pygame.draw.arc(a.image, (255, 255, 255), (25-i, 25-i, 50-i, 50-i), 0, math.pi/2, 2)
        #for i in range(0, 90*100):
        #    pygame.draw.line(a.image, (255, 255, 255), (50, 50), (50+40*math.cos(math.pi*i/180/100), 50+40*math.sin(math.pi*i/180/100)))
        #for x in range(0, 100):
        #    for y in range(0, 100):
        #        if (x-50)**2 + (y-50)**2 < 40**2:
        #            if math.atan2((x-50), (y-50)) < math.pi/2:
        #                self.a.image.set_at((x, y), (255, 255, 255))

        self.spacebar_frame = Frame(self.kb_frame)
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
        for key in self.keys:
            self.keys[key].tick(time_passed)
        self.fps.set_text("{0:.02f}".format(self.engine.clock.get_fps()))


    def tick_end(self, time_passed):
        self.tick_title(time_passed)
        for key in self.keys:
            self.keys[key].tick(time_passed)
        if len(self.sprites) == 0:
            self.wait_for_end -= time_passed
            if self.wait_for_end <= 0:
                return True
        else:
            self.sprites.remove(random.choice(list(self.sprites)))


    def key_press(self, key, unicode):
        unicode = unicode.upper()
        if unicode in self.keys:
            if unicode == self.start_key:
                #from keyshift.EndScene import EndScene
                self.engine.set_scene(GameScene)
            self.keys[unicode].press()

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