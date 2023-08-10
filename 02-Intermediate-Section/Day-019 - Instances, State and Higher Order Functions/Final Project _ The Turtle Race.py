from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:\t")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y = -100

for _ in range(6):
    turtle = Turtle("turtle")
    turtle.speed("fastest")
    turtle.penup()
    turtle.color(colors[_])
    turtle.goto(x=-230, y=y)
    y += 40
    turtles.append(turtle)

if bet:
    racing = True

while racing:

    for turtle in turtles:

        if turtle.xcor() > 220:
            winner = turtle.pencolor()

            if bet == winner:
                print(f"You've won! the {winner} turtle is the winner!")
            else:
                print(f"You've lost! the {winner} turtle is the winner!")
            racing = False

        rand_dist = random.randint(0, 10)
        turtle.fd(rand_dist)

screen.exitonclick()
