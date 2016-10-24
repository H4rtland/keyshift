'''
Created on 22/08/2016

@author: George
'''

import math
import random

class Mode:
    easy = 0
    normal = 1
    hard = 2
    insane = 3

    name = ""

    @staticmethod
    def start(scene, engine_width, engine_height):
        pass

    @staticmethod
    def press(scene, key):
        pass

    @staticmethod
    def end(scene):
        pass

    @staticmethod
    def init_blip(blip):
        pass

    @staticmethod
    def tick_blip(blip, time_passed):
        blip.life += time_passed
        x = blip.x + time_passed*blip.speed*math.sin(blip.angle)
        y = blip.y + time_passed*blip.speed*math.cos(blip.angle)
        #path_length = math.sqrt((blip.spawn_pos[0]-blip.target_pos[0])**2 + (blip.spawn_pos[1]-self.target_pos[1])**2)
        #expected_life = path_length/self.speed
        #x += math.sin(self.life/expected_life)
        #y += math.cos(self.life/expected_life)
        blip.set_pos(x, y)
        blip.dirty = 1

    @staticmethod
    def blip_spawn_pos(engine_width, engine_height):
        r = random.randint
        w = engine_width
        h = engine_height
        ax = (w-1366)
        ay = (h-768)
        bx = (w-1366)/2
        by = (h-768)/2
        possible_spawns = [(r(bx, w-bx), 0+by),
                           (r(bx, w-bx), h-by),
                           (0+bx, r(by, h-by)),
                           (w-bx, r(by, h-by))]
        spawn_pos = random.choice(possible_spawns)
        return spawn_pos

    @staticmethod
    def blip_aiming_for(engine_width, engine_height):
        r = random.randint
        w = engine_width
        h = engine_height
        return (r(w//2-50, w//2+50), r(h//2-50, h//2+50))