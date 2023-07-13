from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: \n"
                                   "(red, orange, yellow, green, blue, purple)\n")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
pos_y = -125
is_race = False

for index in colors:
    race_turtle = Turtle(shape="turtle")
    race_turtle.color(index)
    race_turtle.pu()
    race_turtle.goto(-230, pos_y)
    turtles.append(race_turtle)
    pos_y += 50

if user_bet:
    is_race = True

while is_race:
    for turtle in turtles:

        if turtle.xcor() > 230:
            is_race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_turtle} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)



screen.exitonclick()






