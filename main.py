'''
Created on 16/08/2016

@author: George
'''

import sys
import os
import configparser

import pygame

from keyshift.MainMenuScene import MainMenuScene

class Keyshift:
    def __init__(self):
        pygame.mixer.pre_init(frequency=4000)
        pygame.init()

        # Check for config file or create with default values
        if not os.path.exists("keyshift.ini"):
            config = configparser.ConfigParser()
            config["screen"] = {
                "window_width":pygame.display.Info().current_w,
                "window_height":pygame.display.Info().current_h,
                "fullscreen":True,
            }
            config["layout"] = {
                "key_layout":"iso_105",
            }
            with open("keyshift.ini", "w") as configfile:
                config.write(configfile)

        self.config = configparser.ConfigParser()
        self.config.read("keyshift.ini")


        pygame.mouse.set_visible(False)

        self.running = True
        self.clock = pygame.time.Clock()

        flags = 0
        if self.config.getboolean("screen", "fullscreen"):
            flags = pygame.FULLSCREEN

        self.width = int(self.config["screen"]["window_width"])
        self.height = int(self.config["screen"]["window_height"])
        self.screen = pygame.display.set_mode((self.width, self.height), flags)
        pygame.display.set_caption("KEYSHIFT")

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 0))

        self.scene = None
        self.next_scene_class = None
        self.next_scene_args = ()
        self.set_scene(MainMenuScene)


        self.mainloop()

    def mainloop(self):
        while self.running:
            time_passed = self.clock.tick_busy_loop(120)
            self.tick(time_passed)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

    def tick(self, time_passed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                #print(event.scancode, event.key, event.unicode, pygame.key.name(event.key))
                #print(event.dict)
                #print(dir(event))

                # French keyboards
                unicode = event.unicode
                if event.key == 91 and event.unicode == "":
                    unicode = "¨"

                #if event.unicode == "¨" and not event.key == 91:
                #    unicode = pygame.key.name(event.key)
                self.scene.key_press(event.key, unicode)

        self.scene.sprites.clear(self.screen, self.background)
        self.scene.do_tick(time_passed)
        self.scene.draw(self.screen)

        pygame.display.flip()


    def set_scene(self, scene, *args):
        if not self.scene is None:
            self.scene.end()

        self.next_scene_class = scene
        self.next_scene_args = args
        if self.scene is None:
            self.next_scene()

    def next_scene(self):
        self.screen.fill((0, 0, 0))
        self.scene = self.next_scene_class(self, *self.next_scene_args)
        self.scene.start()



if __name__ == "__main__":
    Keyshift()