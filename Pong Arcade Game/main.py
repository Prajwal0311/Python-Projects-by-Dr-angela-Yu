import time
from turtle import Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

scoreboard = ScoreBoard()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


def go_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)


def go_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)


def w_key():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)


def s_key():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="Down", fun=go_down)
screen.onkey(key="w", fun=w_key)
screen.onkey(key="s", fun=s_key)

game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    ball.move()

    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # No collision detected with right Paddle
    if ball.xcor() > 380:
        ball.clear_pos()
        scoreboard.l_point()

    # No Collision detected with left paddle
    if ball.xcor() < -380:
        ball.clear_pos()
        scoreboard.r_point()

screen.exitonclick()
