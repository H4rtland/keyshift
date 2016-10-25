'''
Created on 18/08/2016

@author: George
'''

import pygame

class Audio:
    current_music = None
    @staticmethod
    def play_music(name):
        """
        Play the given music file if it is not already playing.
        Suggested file type: .ogg.
        :param name: Music file
        :return: None
        """
        if Audio.current_music == name:
            return
        pygame.mixer.music.load(name)
        pygame.mixer.music.play(-1)
        Audio.current_music = name