'''
Created on 16/08/2016

@author: George
'''

import pygame
from keyshift.MainMenuScene import MainMenuScene

class Keyshift:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()

        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("KEYSHIFT")

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 0))

        self.scene = None
        self.set_scene(MainMenuScene)


        self.mainloop()

    def mainloop(self):
        while self.running:
            time_passed = self.clock.tick_busy_loop(60)
            self.tick(time_passed)
        pygame.quit()

    def tick(self, time_passed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

        self.scene.sprites.clear(self.screen, self.background)
        self.scene.tick(time_passed)
        self.scene.draw(self.screen)

        pygame.display.flip()


    def set_scene(self, scene):
        if not self.scene is None:
            self.scene.end()
        self.scene = scene(self)
        self.scene.start()




if __name__ == "__main__":
    Keyshift()