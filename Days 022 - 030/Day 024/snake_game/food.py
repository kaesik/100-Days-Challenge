from turtle import Turtle
from setup import *
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randrange(-270, 270, 20)
        y = random.randrange(-270, 270, 20)
        self.seth(random.choice(DIRECTION_LIST))
        self.goto(x, y)

