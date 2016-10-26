'''
Created on 18/08/2016

@author: George
'''

import pygame

from keyshift.Resources import Resources

class Audio:
    current_music = None
    @staticmethod
    def play_music(name):
        """
        Play the given music file if it is not already playing.
        Suggested file type: .ogg.
        :param name: File name
        :return: None
        """
        if Audio.current_music == name:
            return
        music_data = Resources.load_music(name)
        pygame.mixer.music.load(music_data)
        pygame.mixer.music.play(-1)
        Audio.current_music = name