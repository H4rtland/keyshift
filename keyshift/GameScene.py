'''
Created on 17/08/2016

@author: George
'''

import math
import random
import time
import inspect

import pygame

import keyshift.modes
from keyshift.modes import *


from keyshift.Scene import Scene
from keyshift.Frame import Frame
from keyshift.Text import Text
from keyshift.Image import Image
from keyshift.Key import Key
from keyshift.Blip import Blip
from keyshift.HeartDisplay import HeartDisplay
# from keyshift.modes.Sine import Sine
from keyshift.modes.Mode import Mode


class GameScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

        self.game_start_time = time.time()

        self.blips = []

        self.time_to_next_blip = 1000
        self.max_time_to_next_blip = 3000

        key_order = list("1234567890-=QWERTYUIOP[]ASDFGHJKL;'#\\ZXCVBNM,./")

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

        x = self.engine.width//2 - self.kb_frame.width//2
        y = self.engine.height//2 - self.kb_frame.height//2
        self.kb_frame.set_pos(x, y)

        self.score = 0
        self.shifting = False
        self.keys_to_remove = []
        self.lives = 5

        interface_pos_y = self.kb_frame.y-172

        self.score_text = Text(self)
        self.score_text.set_text("Score: 0")
        self.score_text.set_pos(self.engine.width//2-self.score_text.width//2, interface_pos_y)
        # self.engine.height//3 originally
        self.add(self.score_text)

        self.imminent_text = Text(self)
        self.imminent_text.set_text("KEYSHIFT IMMINENT", size=64)
        self.imminent_text.set_pos(lambda: self.engine.width//2-self.imminent_text.width//2, interface_pos_y+60)
        self.imminent_text.set_text("")
        self.add(self.imminent_text)

        self.hearts = HeartDisplay(self)
        self.hearts.set_hearts(5)
        self.hearts.set_pos(lambda: self.engine.width//2-self.hearts.width//2, interface_pos_y+30)
        self.hearts.hide()
        self.add(self.hearts)

        self.mode = Mode()
        self.modes = []
        for mode in keyshift.modes.__dict__.values():
            if inspect.ismodule(mode):
                for c in mode.__dict__.values():
                    if inspect.isclass(c):
                        if c is not Mode and issubclass(c, Mode):
                            self.modes.append(c)

        if __debug__:
            self.doing_command = False
            self.command_history = []
            self.current_command = ""
            self.current_command_text = Text(self)
            self.current_command_text.set_text("HI")
            self.current_command_text.set_pos(5, self.engine.height-5-self.current_command_text.height)
            self.current_command_text.set_text("> ")
            self.current_command_text.hide()
            self.add(self.current_command_text)


        r = random.randint
        w = self.engine.width
        h = self.engine.height
        possible_spawns = [(r(0, w), 0),
                           (r(0, w), h),
                           (0, r(0, h)),
                           (w, r(0, h))]
        spawn_pos = random.choice(possible_spawns)
        aiming_for = (r(w//2-50, w//2+50), r(h//2-50, h//2+50))

        """self.b1 = Blip(self)
        self.b1.set_pos(*spawn_pos)
        self.b1.angle = math.atan2(aiming_for[0]-spawn_pos[0], aiming_for[1]-spawn_pos[1])
        self.b1.spawn_pos = spawn_pos
        self.b1.target_pos = aiming_for
        self.add(self.b1)

        self.b2 = Blip(self)
        self.b2.set_pos(*spawn_pos)
        self.b2.angle = math.atan2(aiming_for[0]-spawn_pos[0], aiming_for[1]-spawn_pos[1])
        self.b2.spawn_pos = spawn_pos
        self.b2.target_pos = aiming_for
        self.add(self.b2)
        self.b2.set_blank(4, 4, (255, 0, 0))"""

        self.border_frame = Frame(self)
        self.border_top = Image(self.border_frame)
        self.border_top.set_blank(1366, 1, (255, 255, 255))

        self.border_bottom = Image(self.border_frame)
        self.border_bottom.set_blank(1366, 1, (255, 255, 255))
        self.border_bottom.set_pos(0, 768)

        self.border_left = Image(self.border_frame)
        self.border_left.set_blank(1, 768, (255, 255, 255))

        self.border_right = Image(self.border_frame)
        self.border_right.set_blank(1, 768, (255, 255, 255))
        self.border_right.set_pos(1366, 0)

        self.add(self.border_top)
        self.add(self.border_bottom)
        self.add(self.border_left)
        self.add(self.border_right)

        self.border_frame.set_pos(self.engine.width//2-self.border_frame.width//2,
                                  self.engine.height//2-self.border_frame.height//2)


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
            if key.is_showing():
                key.press()
                for blip in self.blips:
                    if key.key.rect.contains(blip.rect):
                        self.mode.press(self, key)
                        self.remove(blip)
                        self.blips = [b for b in self.blips if b is not blip]
                        self.score += 1
                        self.score_up()
                        break

    def tick(self, time_passed):
        if __debug__:
            if self.doing_command:
                return
        #Mode.tick_blip(self.b1, time_passed)
        #Sine.tick_blip(self.b2, time_passed)
        for key in self.keys:
            self.keys[key].tick(time_passed)
        if self.shifting:
            if len(self.keys_to_remove) > 0:
                key = random.choice(self.keys_to_remove)
                key.label.set_text("")
                self.keys_to_remove = [k for k in self.keys_to_remove if k is not key]
            else:
                labels = list(self.keys.keys())
                keys = list(self.keys.values())
                random.shuffle(labels)
                random.shuffle(keys)
                self.keys = dict(zip(labels, keys))
                for label in self.keys:
                    self.keys[label].label.set_text(label)
                self.shifting = False
                if not self.mode.__class__ is Mode:
                    self.imminent_text.set_text("MODE: {}".format(self.mode.name))
                else:
                    self.imminent_text.set_text("")
                print("Starting mode. ", self.mode, self.mode.name)
        else:
            self.time_to_next_blip -= time_passed
            if self.time_to_next_blip <= 0:
                self.time_to_next_blip = self.max_time_to_next_blip
                blip = Blip(self)
                r = random.randint
                w = self.engine.width
                h = self.engine.height
                ax = (self.engine.width-1366)
                ay = (self.engine.height-768)
                bx = (self.engine.width-1366)/2
                by = (self.engine.height-768)/2
                possible_spawns = [(r(bx, w-bx), 0+by),
                                   (r(bx, w-bx), h-by),
                                   (0+bx, r(by, h-by)),
                                   (w-bx, r(by, h-by))]
                spawn_pos = random.choice(possible_spawns)
                blip.set_pos(*spawn_pos)
                aiming_for = (r(w//2-50, w//2+50), r(h//2-50, h//2+50))
                blip.angle = math.atan2(aiming_for[0]-spawn_pos[0], aiming_for[1]-spawn_pos[1])
                blip.spawn_pos = spawn_pos
                blip.target_pos = aiming_for
                self.add(blip)
                self.blips.append(blip)
                if self.score < 15:
                    blip.life_cost = 0

            to_remove = []
            for blip in self.blips:
                self.mode.tick_blip(blip, time_passed)
                if blip.life < 100:
                    continue

                bx = (self.engine.width-1366)/2
                by = (self.engine.height-768)/2
                x_out = blip.x < bx or blip.x > self.engine.width-bx
                y_out = blip.y < by or blip.y > self.engine.height-by
                if x_out or y_out:
                    self.remove(blip)
                    to_remove.append(blip)
                    #print("Removing blip with life {}".format(blip.life))
                    if self.score >= 15:
                        self.lives -= blip.life_cost

            self.blips = [blip for blip in self.blips if blip not in to_remove]

            self.hearts.set_hearts(self.lives)

            if self.lives < 0:
                from keyshift.EndScene import EndScene
                self.engine.set_scene(EndScene, self.score, int(time.time()-self.game_start_time), self.mode.name)

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
            if self.score >= 30:
                self.mode = random.choice([mode for mode in self.modes if not (mode is self.mode.__class__)])
                # self.imminent_text.set_text("MODE: {}".format(self.mode.name))
                self.mode.start(self)

        if self.score >= 15:
            self.hearts.show()
        else:
            self.hearts.hide()

        self.hearts.set_hearts(self.lives)
