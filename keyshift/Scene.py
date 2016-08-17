'''
Created on 16/08/2016

@author: George
'''

import pygame

class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.sprites = pygame.sprite.LayeredDirty(())
        self.ending = False

    def start(self):
        pass

    def end(self):
        self.ending = True

    def do_tick(self, time_passed):
        if self.ending:
            end_status = self.tick_end(time_passed)
            if end_status:
                self.engine.next_scene()
        else:
            self.tick(time_passed)

    def tick(self, time_passed):
        pass

    def tick_end(self, time_passed):
        return True

    def add(self, sprite):
        self.sprites.add(sprite)

    def draw(self, surface):
        self.sprites.draw(surface)

    def key_press(self, key):
        pass