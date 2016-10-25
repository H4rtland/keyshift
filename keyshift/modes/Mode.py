'''
Created on 22/08/2016

@author: George
'''

import math
import random

class Mode:
    """
    Modes control the gameplay behavior.
    When a specific mode is chosen by the game,
    the methods for that mode class are
    used to control motion of the blips,
    key press behaviour, etc for the
    duration of that mode. Also handles
    set up and tear down of that mode.
    """

    easy = 0
    normal = 1
    hard = 2
    insane = 3

    name = ""

    @staticmethod
    def start(scene, engine_width, engine_height):
        """
        Called when the mode is initialised.
        :param scene: Reference to game scene
        :param engine_width:
        :param engine_height:
        :return: None
        """
        pass

    @staticmethod
    def press(scene, key):
        """
        Control what happens to a key when it is pressed.
        :param scene: Reference to game scene
        :param key: The key frame object
        :return: None
        """
        pass

    @staticmethod
    def end(scene):
        """
        Called when the mode ends.
        :param scene: Reference to game scene
        :return: None
        """
        pass

    @staticmethod
    def init_blip(blip):
        """
        Called when a blip is created.
        :param blip: The blip
        :return: None
        """
        pass

    @staticmethod
    def tick_blip(blip, time_passed):
        """
        Control the motion of each blip each frame.
        :param blip: Blip to move
        :param time_passed: Time passed in ms since last frame
        :return: None
        """
        blip.life += time_passed
        x = blip.x + time_passed*blip.speed*math.sin(blip.angle)
        y = blip.y + time_passed*blip.speed*math.cos(blip.angle)
        blip.set_pos(x, y)
        blip.dirty = 1

    @staticmethod
    def blip_spawn_pos(engine_width, engine_height):
        """
        Choose a spawn position for a new blip.
        :param engine_width:
        :param engine_height:
        :return: Spawn position (x, y)
        """
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
        """
        Choose a position that a newly created blip is aiming for.
        Todo: make sure the position is at least within one key
        to prevent blips sliding in between all keys.
        :param engine_width:
        :param engine_height:
        :return: Target position (x, y)
        """
        r = random.randint
        w = engine_width
        h = engine_height
        return (r(w//2-50, w//2+50), r(h//2-50, h//2+50))