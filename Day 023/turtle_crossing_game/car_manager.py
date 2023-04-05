from turtle import Turtle
from random import *
from setup import *


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.pu()
            new_car.seth(180)
            new_car.shapesize(1, 2)
            new_car.goto(300, randrange(-260, 260, 40))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT