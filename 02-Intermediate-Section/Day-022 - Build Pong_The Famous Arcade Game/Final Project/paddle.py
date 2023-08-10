from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_y_position)

    def go_up(self):
        y_ = self.ycor() + 20
        self.goto(self.xcor(), y_)

    def go_down(self):
        y_ = self.ycor() - 20
        self.goto(self.xcor(), y_)
