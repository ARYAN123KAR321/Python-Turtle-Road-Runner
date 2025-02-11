import time
import random
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()
    if random.randint(1, 6) == 1:
        car_manager.create_car()

    screen.listen()
    screen.onkeypress(player.move_up, "Up")

    if player.player.ycor() >= 280:
        player.reset_position()
        scoreboard.increase_score()
        car_manager.increase_speed()

    for car in car_manager.cars:
        if car.distance(player.player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()