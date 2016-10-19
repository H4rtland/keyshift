'''
Created on 20/08/2016

@author: George
'''

import pygame

from keyshift.Scene import Scene
from keyshift.Frame import Frame
from keyshift.Text import Text

class EndScene(Scene):
    def __init__(self, engine, score, time, killer):
        super().__init__(engine)

        self.game_over = Text(self)
        self.game_over.set_text("GAME OVER", size=64)
        self.game_over.set_pos(self.engine.width//2-self.game_over.width//2, self.engine.height//4)
        self.add(self.game_over)

        self.press_esc = Text(self)
        self.press_esc.set_text("PRESS ESC TO RETURN TO MAIN MENU")
        self.press_esc.set_pos(self.engine.width//2-self.press_esc.width//2, self.engine.height//4+40)
        self.add(self.press_esc)


        self.stats_frame = Frame(self)

        stats = []
        stat_texts = []

        stats.append("SCORE: {}".format(score))

        minutes, seconds = divmod(time, 60)
        stats.append("TIME: {}m {}s".format(minutes, seconds))

        if not killer is "":
            stats.append("KILLER: {}".format(killer))

        for i, stat in enumerate(stats):
            text = Text(self.stats_frame)
            text.set_text(stat)
            self.add(text)
            stat_texts.append(text)

        for i, stat_text in enumerate(stat_texts):
            stat_text.set_pos((self.stats_frame.width-stat_text.width)//2, i*25)

        self.stats_frame.set_pos(self.engine.width//2-self.stats_frame.width//2, self.engine.height//2-self.stats_frame.height//2)


    def key_press(self, key, unicode):
        if key == pygame.K_ESCAPE:
            from keyshift.MainMenuScene import MainMenuScene
            self.engine.set_scene(MainMenuScene)