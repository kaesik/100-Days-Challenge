from turtle import Turtle
from setup import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pu()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Current Score: {self.score}  High Score: {self.high_score}", False, ALIGN, FONT)

    def add_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()
