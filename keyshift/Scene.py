'''
Created on 16/08/2016

@author: George
'''

import pygame

class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.sprites = pygame.sprite.LayeredDirty(())

    def start(self):
        pass

    def end(self):
        pass

    def tick(self, time_passed):
        pass

    def add(self, sprite):
        self.sprites.add(sprite)

    def draw(self, surface):
        self.sprites.draw(surface)
