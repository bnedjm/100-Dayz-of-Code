from turtle import Turtle

ALIGNMENT = "left"
FONT = ("MS Serif", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
