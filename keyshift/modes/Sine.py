'''
Created on 24/08/2016

@author: George
'''

import math

from keyshift.modes.Mode import Mode

class Sine(Mode):
    name = "SINE"

    @staticmethod
    def tick_blip(blip, time_passed):
        blip.life += time_passed

        path_length = math.sqrt((blip.spawn_pos[0]-blip.target_pos[0])**2 + (blip.spawn_pos[1]-blip.target_pos[1])**2)
        expected_life = path_length/(blip.speed*time_passed)

        """new_x = ((blip.target_pos[0]-blip.spawn_pos[0]) * (blip.life/expected_life))
        new_y = ((blip.target_pos[1]-blip.spawn_pos[1]) * (blip.life/expected_life))
        dx = ((blip.target_pos[0]-blip.spawn_pos[0]) * (time_passed/expected_life))
        dy = ((blip.target_pos[1]-blip.spawn_pos[1]) * (time_passed/expected_life))

        norm = math.sqrt(dx**2 + dy**2)

        x = blip.spawn_pos[0] + (new_x * (2.5/norm))# + 25*(math.sin(blip.angle+(math.pi/2)) * math.sin(blip.life/expected_life))
        y = blip.spawn_pos[1] + (new_y * (2.5/norm))# + 25*(math.cos(blip.angle+(math.pi/2)) * math.sin(blip.life/expected_life))"""

        x = blip.x + time_passed*blip.speed*math.sin(blip.angle)
        y = blip.y + time_passed*blip.speed*math.cos(blip.angle)

        x += (1/15)*(math.sin(blip.angle+(math.pi/2)) * time_passed*math.cos(blip.life/expected_life))
        y += (1/15)*(math.cos(blip.angle+(math.pi/2)) * time_passed*math.cos(blip.life/expected_life))

        blip.set_pos(x, y)
        blip.dirty = 1
