'''
Created on 27/08/2016

@author: George
'''

from keyshift.Frame import Frame
from keyshift.Key import Key

class Keyboard(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.keys = {}

    def set_layout(self, layout):
        for child in self.sprites:
            child.remove()
        for row, (offset, labels) in enumerate(layout):
            for i, label in enumerate(labels):
                key = Key(self)
                key.set_key(label)
                key.set_pos(offset*50+i*50, row*50)
                #self.get_scene().add(key)
                self.keys[label] = key