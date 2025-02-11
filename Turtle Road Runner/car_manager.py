import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = turtle.Turtle()
        car.shape("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT