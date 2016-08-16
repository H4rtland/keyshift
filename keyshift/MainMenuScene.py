'''
Created on 16/08/2016

@author: George
'''

import random

from keyshift.Scene import Scene
from keyshift.Text import Text

class MainMenuScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

        self.title_shifts = ["KEYSHIFT"]
        self.title_shift_tick = 16
        self.title_shift_time = 0
        for i in range(0, 100):
            self.title_shifts.append(self.next_title(self.title_shifts[-1]))
        self.title_shifts = self.title_shifts[::-1]

        self.title = Text()
        self.title.set_text(self.title_shifts.pop(0), size=48)
        self.add(self.title)



        self.title.set_pos(self.engine.width//2 - self.title.get_width()//2, self.engine.height//4 - self.title.get_height()//2)


    def tick(self, time_passed):
        if len(self.title_shifts) > 0:
            self.title_shift_time += time_passed
            if self.title_shift_time > self.title_shift_tick:
                self.title_shift_time -= self.title_shift_tick
                self.title.set_text(self.title_shifts.pop(0))
                if len(self.title_shifts) < 20:
                    extra_ms = (20-len(self.title_shifts))
                    self.title_shift_tick = 16 + 15*extra_ms*(1+(extra_ms/100))**2


    def next_title(self, current):
        current = current+ " "
        shift_index = random.randint(0, len(current)-3)
        new = current[0:shift_index] + current[shift_index+1] + current[shift_index] + current[shift_index+2:len(current)]
        return new.replace(" ", "")
