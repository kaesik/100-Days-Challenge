from turtle import Turtle
from setup import *


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(5, 1)
        self.turtlesize(5, 1)
        self.pu()
        self.setpos(position)

    def up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y)

