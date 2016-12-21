import pygame
import random

from keyshift.modes.Mode import Mode

class Corsair(Mode):
    """
    Each key has a colour (R G or B) associated with it.
    Each blip has a colour. Must match key colour to
    blip colour. Unsure if I want to keep this,
    would prefer if game remained black and white.
    """
    name = "CORSAIR"
    colours = {}

    @staticmethod
    def start(scene, engine_width, engine_height):
        Corsair.colours = {}
        for key in scene.keys.values():
            Corsair.colours[key] = random.choice([(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)])


    @staticmethod
    def key_push(key):
        key.label.set_text(key.label.current_text, size=24, colour=Corsair.colours[key])


    @staticmethod
    def end(scene):
        for key in scene.keys.values():
            key.label.set_text(key.label.current_text, size=32, colour=(255, 255, 255))