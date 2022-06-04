# Tackling the turtle crossing game in steps::
# Step 1: Setting up screen
# Step 2: Setting up a player and movement input from user
# Step 3: Generating cars and giving them motion
# Step 4: Detecting collision of player with cars
# Step 5: Keeping a scoreboard
# Step 6: Increasing the speed and updating scoreboard as player levels up
# Step 7: game over sequence and finishing touches with ...
# attributes like player positioning, speed, update rate, colors etc

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

# Creating objects from the classes
participant = Player()
car_manager = CarManager()
score_board = Scoreboard()

# Taking user input to control the turtle
screen.listen()
screen.onkey(participant.move, "Up")

# To switch off the animation and looping the methods inside classes
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()

    # detect collision
    for car in car_manager.cars:
        if car.distance(participant) < 20:
            game_is_on = False
            score_board.game_over()

    # detect successful crossing
    if participant.at_finish_line():
        participant.go_to_start()
        car_manager.level_up()
        score_board.level_increase()

screen.exitonclick()
