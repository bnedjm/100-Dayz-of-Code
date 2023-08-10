from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()

score = Score()

screen.listen()
screen.onkey(paddle_r.go_up, key="Up")
screen.onkey(paddle_r.go_down, key="Down")
screen.onkey(paddle_l.go_up, key="w")
screen.onkey(paddle_l.go_down, key="s")

we_playing = True

while we_playing:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collusion with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collusion with paddles
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Collusion to detect when paddles miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_score_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.update_score_r()

screen.exitonclick()
