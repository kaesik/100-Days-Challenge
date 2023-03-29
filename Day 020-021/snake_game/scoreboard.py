from turtle import Turtle
from setup import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Current Score: {self.score}", False, ALIGN, FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E   O V E R", False, ALIGN, FONT)
