from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment(START_POS[_])

    def add_segment(self, position):
        temp = Turtle("square")
        temp.color("white")
        temp.penup()
        temp.goto(position)
        self.segments.append(temp)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            self.segments[idx].goto(self.segments[idx - 1].xcor(), self.segments[idx - 1].ycor())
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
