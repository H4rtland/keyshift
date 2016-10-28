from keyshift.modes.Mode import Mode

class Break(Mode):
    name = "BREAK"

    @staticmethod
    def press(scene, key):
        key.hide()

    @staticmethod
    def end(scene):
        for key in scene.keys.values():
            key.show()