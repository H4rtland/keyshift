'''
Created on 22/08/2016

@author: George
'''

from keyshift.modes.Mode import Mode

class Break:
    name = "BREAK"

    @staticmethod
    def press(scene, key):
        key.hide()

    @staticmethod
    def end(scene):
        for key in scene.keys.values():
            key.show()