from turtle import Turtle
from setup import *


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.seth(90)
        self.setpos(STARTING_POSITION)

    def up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def died(self):
        self.shape("circle")
        self.color("red")
