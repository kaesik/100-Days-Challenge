from turtle import Turtle
from setup import *


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.setpos(0, 0)
        self.y_move = 5
        self.x_move = 5

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.setpos(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.x_move = 5
        self.y_move = 5
        self.bounce_x()
