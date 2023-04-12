from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from setup import *
import time

# SCREEN SETUP
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.bgpic("pong.png")
screen.tracer(0)

# OBJECTS
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

# CONTROLS
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# GAME
game_on = True
while game_on:
    time.sleep(TIMER)
    screen.update()
    ball.move()

    # DETECT COLLISION WITH TOP/BOTTOM WALL
    if ball.ycor() > 260 or ball.ycor() < -240:
        ball.bounce_y()

    # DETECT COLLISION WITH PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.x_move += 1
        ball.y_move += 1
        ball.bounce_x()

    # DETECT COLLISION WITH LEFT/RIGHT WALL
    if ball.xcor() > 380:
        score.add_score_l()
        ball.reset_pos()
    elif ball.xcor() < -380:
        score.add_score_r()
        ball.reset_pos()

screen.exitonclick()
