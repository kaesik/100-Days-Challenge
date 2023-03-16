#DRAW A TRIANGLE, SQUARE, PENTAGON, HEXAGON, HEPTAGON, OCTAGON, NONAGON AND DECAGON
from turtle import *
import random

rex = Turtle()
rex.shape("turtle")
rex.color("orange2")
colormode(255)

for a in range(10):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rex.color((r, g, b))
    for b in range(a+3):
        rex.fd(50)
        rex.rt(360/(a+3))

screen = Screen()
screen.exitonclick()