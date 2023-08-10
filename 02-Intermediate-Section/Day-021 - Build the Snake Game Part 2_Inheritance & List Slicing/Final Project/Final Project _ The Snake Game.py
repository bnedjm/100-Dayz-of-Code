from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

# Control
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

we_playing = True

while we_playing:

    screen.update()
    time.sleep(0.1)

    # Movement
    snake.move()

    # Collusion
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Collusion with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        we_playing = False
        score.game_over()

    # Collusion with tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            we_playing = False
            score.game_over()



screen.exitonclick()
