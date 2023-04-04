import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player movement
player = Player()
screen.listen()
screen.onkey(player.crawl_up, 'Up')
screen.onkey(player.crawl_left, 'Left')
screen.onkey(player.crawl_right, 'Right')

# Car_manager
car_manager = CarManager()

# Game play
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.target_reached()
    chance = random.randint(1, 6)
    car_manager.car_movement()
    if chance == 5:
        car_manager.car_creation()

    if player.ycor() == 280:
        car_manager.speed_up()
        print(car_manager.car_speed)

    for car in car_manager.cars:
        if car.distance(player) < 20:
            player.failure()
            game_is_on = False

screen.exitonclick()
