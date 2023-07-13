from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_fd():
    tom.fd(20)

def move_bk():
    tom.bk(20)

def turn_rt():
    tom.rt(20)

def turn_lt():
    tom.lt(20)

def clear():
    tom.reset()


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="a", fun=turn_lt)
screen.onkey(key="d", fun=turn_rt)
screen.onkey(key="c", fun=clear)
screen.exitonclick()