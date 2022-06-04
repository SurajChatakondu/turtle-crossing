from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    # Create a turtle player
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # Moving the turtle with user input
    def move(self):
        self.forward(MOVE_DISTANCE)

    # To restart as the level goes up
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # To detect the finish line and trigger level up
    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
