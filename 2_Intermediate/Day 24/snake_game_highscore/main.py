from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
from setup import *
import time

# SCREEN SETUP
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# GAME
game_on = True
while game_on:
    screen.update()
    time.sleep(TIMER)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) <= 15:
        score.add_score()
        snake.extend()
        food.refresh()

    # DETECT COLLISION WITH WALLS
    if -280 > snake.head.xcor() or snake.head.xcor() > 280 or -280 > snake.head.ycor() or snake.head.ycor() > 280:
        score.reset()
        snake.reset()

    # DETECT COLLISION WITH TAIL
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()


screen.exitonclick()
