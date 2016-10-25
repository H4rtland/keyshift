import math

from keyshift.modes.Mode import Mode

class Circle(Mode):
    name = "2PI"

    @staticmethod
    def start(scene, engine_width, engine_height):
        total_keys = len(scene.keys)

        for index, key in enumerate(scene.keys.values()):
            key.set_pos(340+(340*math.sin(2*math.pi*index/total_keys)),
                        340+(340*math.cos(2*math.pi*index/total_keys)))
        scene.kb_frame.recalculate_rect()

    @staticmethod
    def end(scene):
        for key in scene.keys.values():
            key.reset_position()
        scene.kb_frame.recalculate_rect()