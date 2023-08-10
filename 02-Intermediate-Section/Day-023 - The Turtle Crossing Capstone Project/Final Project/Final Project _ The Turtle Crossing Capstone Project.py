import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars_ = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_.create_cars()
    cars_.move_cars()

    # Collusion with cars
    for car in cars_.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Finish line
    if player.hits_top():
        player.reset_position()
        score.increase_score()
        cars_.level_up()

screen.exitonclick()
