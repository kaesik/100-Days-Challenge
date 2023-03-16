#DRAW A RANDOM WALK
from turtle import *
import random

tom = Turtle()
tom.shape("turtle")
tom.color("orange2")
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tom.color(r, g, b)


def random_turn(turtle):
    turn = [turtle.rt(90), turtle.lt(90)]
    return random.choice(turn)


while True:
    random_color()
    tom.fd(20)
    random_turn(tom)


screen = Screen()
screen.exitonclick()