from turtle import Screen
from snake import Snake
from food import Food
from setup import *
import time

# SCREEN SETUP
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.bgpic("background.png")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# GAME
while True:
    screen.update()
    time.sleep(TIMER)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) <= 15:
        food.refresh()


screen.exitonclick()
