'''
Created on 20/08/2016

@author: George
'''

import pygame

from keyshift.Scene import Scene
from keyshift.Frame import Frame
from keyshift.Text import Text

class EndScene(Scene):
    def __init__(self, engine, score, time):
        super().__init__(engine)

        self.game_over = Text(self)
        self.game_over.set_text("GAME OVER", size=64)
        self.game_over.set_pos(self.engine.width//2-self.game_over.get_width()//2, self.engine.height//4)
        self.add(self.game_over)

        self.press_esc = Text(self)
        self.press_esc.set_text("PRESS ESC TO RETURN TO MAIN MENU")
        self.press_esc.set_pos(self.engine.width//2-self.press_esc.get_width()//2, self.engine.height//4+40)
        self.add(self.press_esc)


        self.stats_frame = Frame(self)

        stats= []

        score_text = Text(self.stats_frame)
        score_text.set_text("SCORE: {}".format(score))
        self.add(score_text)
        stats.append(score_text)

        minutes, seconds = divmod(time, 60)
        time_text = Text(self.stats_frame)
        time_text.set_text("TIME: {}m {}s".format(minutes, seconds))
        self.add(time_text)
        stats.append(time_text)

        for i, stat in enumerate(stats):
            stat.set_pos((self.stats_frame.get_width()-stat.get_width())//2, i*25)

        self.stats_frame.set_pos(self.engine.width//2-self.stats_frame.get_width()//2, self.engine.height//2-self.stats_frame.get_height()//2)


    def key_press(self, key, unicode):
        if key == pygame.K_ESCAPE:
            from keyshift.MainMenuScene import MainMenuScene
            self.engine.set_scene(MainMenuScene)