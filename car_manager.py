import random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_AXIS = [range(-260, 260)]
START_LINE = 280


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_movement()
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_creation(self):

        car = Turtle('square')
        car.shapesize(1, 2, 1)
        car.penup()
        car.color(random.choice(COLORS))
        y_cor = random.randint(-240, 240)
        car.goto(START_LINE, y_cor)
        car.setheading(180)
        self.cars.append(car)

    def car_movement(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += 3
