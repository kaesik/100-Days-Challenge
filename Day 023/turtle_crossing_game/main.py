import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from setup import *

# SCREEN SETUP
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# OBJECTS
player = Player()
manager = CarManager()
score = Scoreboard()

# CONTROLS
screen.listen()
screen.onkeypress(player.up, "Up")

# GAME
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    manager.create_car()
    manager.move()
    screen.update()

# DETECTS NEXT LEVEL
    if player.ycor() >= FINISH_LINE_Y:
        score.add_score()
        manager.level_up()
        player.goto(STARTING_POSITION)

# DETECT COLLISION WITH CARS
    for car in manager.all_cars:
        if car.distance(player) < 30:
            player.died()
            score.game_over()
            game_is_on = False

screen.exitonclick()