from turtle import Turtle

ALIGNMENT = "center"
FONT = ("MS Serif", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.score_r, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.score_l, align=ALIGNMENT, font=FONT)

    def update_score_r(self):
        self.score_r += 1
        self.update_score()

    def update_score_l(self):
        self.score_l += 1
        self.update_score()
