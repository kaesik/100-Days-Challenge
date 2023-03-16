#DRAW A DASHED LINE
from turtle import *

bob = Turtle()
bob.shape("turtle")
bob.color("orange2")

for i in range(20):
    bob.fd(10)
    bob.pu()
    bob.fd(10)
    bob.pd()

screen = Screen()
screen.exitonclick()