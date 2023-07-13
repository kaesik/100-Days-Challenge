#DRAW A RANDOM WALK
from turtle import *
import random

tom = Turtle()
tom.speed(11)
colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for angle in range(360):
    if angle % 10 == 0:
        tom.color(random_color())
        tom.circle(100)
        tom.rt(10)


screen = Screen()
screen.exitonclick()