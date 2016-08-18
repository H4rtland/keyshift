'''
Created on 18/08/2016

@author: George
'''

import pygame

class Audio:
    current_music = None
    @staticmethod
    def play_music(name):
        if Audio.current_music == name:
            return
        pygame.mixer.music.load(name)
        pygame.mixer.music.play(-1)
        Audio.current_music = name