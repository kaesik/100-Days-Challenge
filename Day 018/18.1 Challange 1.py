#DRAW A CIRCLE
from turtle import *

bobby = Turtle()
bobby.shape("turtle")
bobby.color("orange2")

for i in range(4):
    bobby.fd(100)
    bobby.rt(90)

screen = Screen()
screen.exitonclick()