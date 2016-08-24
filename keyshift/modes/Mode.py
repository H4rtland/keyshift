'''
Created on 22/08/2016

@author: George
'''

import math

class Mode:
    easy = 0
    normal = 1
    hard = 2
    insane = 3

    name = ""

    @staticmethod
    def start(scene):
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
