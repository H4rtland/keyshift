import math

from keyshift.modes.Mode import Mode

class Sine(Mode):
    name = "SINE"

    @staticmethod
    def init_blip(blip):
        blip.speed = 2/16

    @staticmethod
    def tick_blip(blip, time_passed):
        blip.life += time_passed

        path_length = math.sqrt((blip.spawn_pos[0]-blip.target_pos[0])**2 + (blip.spawn_pos[1]-blip.target_pos[1])**2)
        expected_life = path_length/(blip.speed*time_passed)

        x = blip.x + time_passed*blip.speed*math.sin(blip.angle)
        y = blip.y + time_passed*blip.speed*math.cos(blip.angle)

        x += (1/15)*(math.sin(blip.angle+(math.pi/2)) * time_passed*math.cos(blip.life/expected_life))
        y += (1/15)*(math.cos(blip.angle+(math.pi/2)) * time_passed*math.cos(blip.life/expected_life))

        blip.set_pos(x, y)
        blip.dirty = 1
