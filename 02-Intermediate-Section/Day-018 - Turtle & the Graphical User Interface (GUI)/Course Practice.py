# from turtle import Turtle, Screen
# from turtle import * # this module import method would import everything from the module, it is not advised
import turtle
# timmy = Turtle()
# timmy.shape("circle")
# timmy.color("red")

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# screen = Screen()
# screen.exitonclick()

# import turtle as t # defining Alias name for the turtle library

# from turtle import *

from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
# tim.shape("circle")
# tim.width(10)
tim.speed("fastest")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]

# Dashed line

# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Different shapes

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


# draw_shape(5)

# for sides in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(sides)

# Random walk

def random_walk():
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(25)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple_color = (r, g, b)
    return tuple_color


def spirograph(step):
    for _ in range(int(360/step)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(step)

spirograph(3)

screen = Screen()
screen.exitonclick()
