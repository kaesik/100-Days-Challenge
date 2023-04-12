#DRAW A RANDOM WALK
import turtle
from turtle import *
import random

tom = Turtle()
tom.shape("turtle")
tom.color("orange2")
tom.pensize(10)
turtle.speed(100)
colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


while True:
    tom.color(random_color())
    tom.fd(20)
    tom.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()