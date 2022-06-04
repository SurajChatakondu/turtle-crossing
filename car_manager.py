from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

# Generate cars one by one
    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.hideturtle()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            y_cor = random.randint(-250, 250)
            car.goto(300, y_cor)
            car.showturtle()
            self.cars.append(car)

# Giving motion to the cars
    def move_cars(self):
        for each_car in self.cars:
            each_car.backward(self.car_speed)

# Speed increment upon level up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
