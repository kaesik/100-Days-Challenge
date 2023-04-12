import turtle

import colorgram

# colors = colorgram.extract("image.jpg", 20)
# list_of_colors = []
#
#
# def get_color(index, colors):
#     color = colors[index]
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     return (r, g, b)
#
#
# for index, color in enumerate(colors):
#     list_of_colors.append(get_color(index, colors))
#
# print(list_of_colors)



from turtle import *
import random


list_of_colors = [
    (132, 166, 205), (221, 148, 106), (32, 42, 61),
    (199, 135, 148), (166, 58, 48), (141, 184, 162),
    (39, 105, 157), (237, 212, 90), (150, 59, 66),
    (216, 82, 71), (168, 29, 33), (235, 165, 157),
    (51, 111, 90), (35, 61, 55), (156, 33, 31),
    (17, 97, 71)
]

tom = Turtle()
tom.speed(11)
colormode(255)
tom.pu()
tom.pensize(10)
for col in range(-250, 250, 50):
    for row in range(-250, 250, 50):
        tom.goto(row, col)
        tom.pd()
        tom.dot(20, random.choice(list_of_colors))
        tom.pu()


screen = Screen()
screen.exitonclick()
