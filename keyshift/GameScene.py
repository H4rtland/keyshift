'''
Created on 17/08/2016

@author: George
'''

import math
import random
import pygame
import time

from keyshift.Scene import Scene
from keyshift.Frame import Frame
from keyshift.Text import Text
from keyshift.Image import Image
from keyshift.Key import Key
from keyshift.Blip import Blip
from keyshift.HeartDisplay import HeartDisplay
from keyshift.modes.Mode import Mode
from keyshift.modes.Break import Break



class GameScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

        self.game_start_time = time.time()

        self.blips = []

        self.time_to_next_blip = 1000
        self.max_time_to_next_blip = 3000

        key_order = list("1234567890-=QWERTYUIOP[]ASDFGHJKL;'#\ZXCVBNM,./")

        self.keys = {}
        self.last_5_presses = [0, 0, 0, 0, 0]

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

        self.score = 0
        self.shifting = False
        self.keys_to_remove = []
        self.lives = 5

        interface_pos_y = self.kb_frame.y-172

        self.score_text = Text(self)
        self.score_text.set_text("Score: 0")
        self.score_text.set_pos(self.engine.width//2-self.score_text.get_width()//2, interface_pos_y) # self.engine.height//3
        self.add(self.score_text)



        self.imminent_text = Text(self)
        self.imminent_text.set_text("KEYSHIFT IMMINENT", size=64)
        self.imminent_text.set_pos(lambda: self.engine.width//2-self.imminent_text.get_width()//2, interface_pos_y+60)
        self.imminent_text.set_text("")
        self.add(self.imminent_text)

        self.hearts = HeartDisplay(self)
        self.hearts.set_hearts(5)
        self.hearts.set_pos(lambda: self.engine.width//2-self.hearts.get_width()//2, interface_pos_y+30)
        self.hearts.hide()
        self.add(self.hearts)

        self.mode = Break()

        if __debug__:
            self.doing_command = False
            self.command_history = []
            self.current_command = ""
            self.current_command_text = Text(self)
            self.current_command_text.set_text("HI")
            self.current_command_text.set_pos(5, self.engine.height-5-self.current_command_text.get_height())
            self.current_command_text.set_text("> ")
            self.current_command_text.hide()
            self.add(self.current_command_text)

    def key_press(self, key, unicode):
        if key == pygame.K_ESCAPE:
            from keyshift.MainMenuScene import MainMenuScene
            self.engine.set_scene(MainMenuScene)
        if __debug__:
            if key == pygame.K_BACKQUOTE:
                self.doing_command = not self.doing_command
                if self.doing_command:
                    self.current_command_text.show()
                    for command in self.command_history:
                        command.show()
                else:
                    self.current_command_text.hide()
                    for command in self.command_history:
                        command.hide()
                return
            if self.doing_command:
                if key == pygame.K_BACKSPACE:
                    self.current_command = self.current_command[:-1]
                elif key == pygame.K_RETURN:
                    c = self.current_command.lower().split(" ")
                    if c[0] == "set_score":
                        if len(c) > 1:
                            if c[1].isdigit():
                                self.score = int(c[1])
                                self.score_up()
                    if c[0] == "set_imminent":
                        self.imminent_text.set_text(" ".join(c[1:]).upper(), size=64)
                    t = Text(self)
                    t.set_text(self.current_command)
                    self.add(t)
                    self.command_history.append(t)
                    self.current_command = ""
                else:
                    if len(unicode) == 1:
                        self.current_command += unicode
                self.current_command_text.set_text("> " + self.current_command)
                for i, command in enumerate(self.command_history[::-1]):
                    command.set_pos(5, self.engine.height-5-64-(32*i))
                return
        if len(self.last_5_presses) > 0:
            if time.time() - self.last_5_presses[0] < 1:
                return
        self.last_5_presses.append(time.time())
        if len(self.last_5_presses) > 5:
            self.last_5_presses = self.last_5_presses[1:]
        unicode = unicode.upper()
        if unicode in self.keys:
            key = self.keys[unicode]
            if key.is_visible():
                key.press()
                for blip in self.blips:
                    if key.key.rect.contains(blip.rect):
                        self.mode.press(self, key)
                        self.remove(blip)
                        self.blips = [b for b in self.blips if not b is blip]
                        self.score += 1
                        self.score_up()
                        break

    def tick(self, time_passed):
        if __debug__:
            if self.doing_command:
                return
        for key in self.keys:
            self.keys[key].tick(time_passed)
        if self.shifting:
            if len(self.keys_to_remove) > 0:
                key = random.choice(self.keys_to_remove)
                key.label.set_text("")
                self.keys_to_remove = [k for k in self.keys_to_remove if not k is key]
            else:
                labels = list(self.keys.keys())
                keys = list(self.keys.values())
                random.shuffle(labels)
                random.shuffle(keys)
                self.keys = dict(zip(labels, keys))
                for label in self.keys:
                    self.keys[label].label.set_text(label)
                self.shifting = False
                self.imminent_text.set_text("")
        else:
            self.time_to_next_blip -= time_passed
            if self.time_to_next_blip <= 0:
                self.time_to_next_blip = self.max_time_to_next_blip
                blip = Blip(self)
                r = random.randint
                w = self.engine.width
                h = self.engine.height
                possible = [(r(0, w), 0),
                            (r(0, w), h),
                            (0, r(0, h)),
                            (w, r(0, h))]
                pos = random.choice(possible)
                blip.set_pos(*pos)
                aiming_for = (r(w//2-50, w//2+50), r(h//2-50, h//2+50))
                blip.angle = math.atan2(aiming_for[0]-pos[0], aiming_for[1]-pos[1])
                self.add(blip)
                self.blips.append(blip)
                if self.score < 15:
                    blip.life_cost = 0

            to_remove = []
            for blip in self.blips:
                blip.tick(time_passed)
                if blip.x+blip.get_width() < 0 or blip.x > self.engine.width or blip.y+blip.get_height() < 0 or blip.y > self.engine.height:
                        self.remove(blip)
                        to_remove.append(blip)
                        if self.score >= 15:
                            self.lives -= blip.life_cost

            self.blips = [blip for blip in self.blips if not blip in to_remove]

            self.hearts.set_hearts(self.lives)

            if self.lives < 0:
                from keyshift.EndScene import EndScene
                self.engine.set_scene(EndScene, self.score, int(time.time()-self.game_start_time))

    def tick_end(self, time_passed):
        for sprite in self.sprites:
            self.remove(sprite)
            sprite.dirty = 1
        return True

    def score_up(self):
        self.score_text.set_text("Score: {}".format(self.score))
        if (self.score+2) % 15 == 0:
            self.imminent_text.set_text("KEYSHIFT IMMINENT", size=64)
        if self.score % 15 == 0:
            self.imminent_text.set_text(" KEYSHIFTING NOW ", size=64)
            self.shifting = True
            self.keys_to_remove = list(self.keys.values())
            self.lives = 5
            self.mode.end(self)

        if self.score >= 15:
            self.hearts.show()
        else:
            self.hearts.hide()

        self.hearts.set_hearts(self.lives)