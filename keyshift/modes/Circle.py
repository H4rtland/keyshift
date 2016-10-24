import math

from keyshift.modes.Mode import Mode

class Circle(Mode):
    name = "2pi"

    @staticmethod
    def start(scene, engine_width, engine_height):
        total_keys = len(scene.keys)
        x_offset = engine_width//2 - scene.kb_frame._x
        y_offset = engine_height//2 - scene.kb_frame._y
        print(x_offset, y_offset)
        for index, key in enumerate(scene.keys.values()):
            key.set_pos(x_offset+(340*math.sin(2*math.pi*index/total_keys)-key.width//2),
                        y_offset+(340*math.cos(2*math.pi*index/total_keys))-key.height//2)

    @staticmethod
    def end(scene):
        for key in scene.keys.values():
            key.reset_position()