from turtle import Turtle
from setup import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(f"{str(self.l_score)}", False, ALIGN, FONT)
        self.goto(100, 200)
        self.write(f"{str(self.r_score)}", False, ALIGN, FONT)

    def add_score_l(self):
        self.clear()
        self.l_score += 1
        self.update()

    def add_score_r(self):
        self.clear()
        self.r_score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E   O V E R", False, ALIGN, FONT)
