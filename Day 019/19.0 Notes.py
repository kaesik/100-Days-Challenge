from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_fd():
    tom.fd(50)

def turn_rt():
    tom.rt(30)

def turn_lt():
    tom.lt(30)

screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="a", fun=turn_lt)
screen.onkey(key="d", fun=turn_rt)
screen.exitonclick()