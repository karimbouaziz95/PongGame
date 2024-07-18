from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

from config import configuration

screen = Screen()
screen.setup(width=configuration["WIDTH"], height=configuration["HEIGHT"])
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

paddle_r = Paddle(configuration["WIDTH"]/2 - 20, 0)
paddle_l = Paddle(-(configuration["WIDTH"]/2 - 20), 0)
ball = Ball()
game_is_on = True
screen.onkeypress(key="Up", fun=paddle_r.move_up)
screen.onkeypress(key="Down", fun=paddle_r.move_down)
screen.onkeypress(key="w", fun=paddle_l.move_up)
screen.onkeypress(key="s", fun=paddle_l.move_down)

scoreboard = Scoreboard()
initial_sleep = 0.07
while game_is_on:
    time.sleep(initial_sleep)
    screen.update()
    ball.move()
    if (
        (abs(ball.xcor() - paddle_r.xcor()) < 20 and abs(ball.ycor() - paddle_r.ycor()) < 65) or
        (abs(ball.xcor() - paddle_l.xcor()) < 20 and abs(ball.ycor() - paddle_l.ycor()) < 65)
    ):
        ball.bounce()
        if initial_sleep >= 0.02:
            initial_sleep -= 0.01

    elif abs(ball.xcor()) > configuration["WIDTH"]/2:
        #game_is_on = False
        if ball.xcor() < 0:
            scoreboard.update_score_player_right()
        elif ball.xcor() > 0:
            scoreboard.update_score_player_left()
        ball.goto(0, 0)
        ball.x_direction *= -1
        initial_sleep = 0.07


screen.update()
screen.exitonclick()