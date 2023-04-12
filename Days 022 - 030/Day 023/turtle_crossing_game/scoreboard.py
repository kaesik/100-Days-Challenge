from turtle import Turtle
from setup import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(-200, 250)
        self.color("black")
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", False, ALIGN, FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E   O V E R", False, ALIGN, FONT_GAMEOVER)
