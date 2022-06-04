from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.keeping_score()

    def keeping_score(self):
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def level_increase(self):
        self.clear()
        self.level += 1
        self.keeping_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
