from turtle import Turtle
from setup import *


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create()
        self.head = self.snake_segments[0]

    def create(self):
        for segment in range(3):
            self.add_segment(((-20 * segment + 10), 10))

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("Green")
        snake_segment.pu()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for segment_number in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[segment_number - 1].xcor()
            y = self.snake_segments[segment_number - 1].ycor()
            self.snake_segments[segment_number].goto(x, y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.seth(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.seth(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.seth(RIGHT)
