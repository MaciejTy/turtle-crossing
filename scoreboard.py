FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto( -150, 270)
        self.write(f"Level: {self.score}", align="center", font=("Courier", 20, "normal"))

    def score_up(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))