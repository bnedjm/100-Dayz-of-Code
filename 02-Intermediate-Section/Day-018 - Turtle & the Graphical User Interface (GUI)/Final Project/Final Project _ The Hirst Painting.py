# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

import turtle as turtle

turtle.colormode(255)
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle = Turtle()
screen = Screen()

turtle.hideturtle()
turtle.penup()
turtle.speed("fastest")

turtle.setheading(225)
turtle.fd(300)
turtle.setheading(0)

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.fd(50)
    
    turtle.setheading(90)
    turtle.fd(50)
    turtle.setheading(180)
    turtle.fd(500)
    turtle.setheading(0)

screen.exitonclick()
