from turtle import Screen
from snake import Snake

import time
from Food import Food
from score import ScoreBoard

score = ScoreBoard()

food = Food()

screen = Screen()

# TO SETUP THE SCREEN
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
game_is_on = True
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.increse_score()
    if snake.head.xcor() >= 285 or snake.head.xcor() <= -285 or snake.head.ycor() >= 285 or snake.head.ycor() <= -285:
        game_is_on = False
        score.game_over()

    for segment in snake.segment:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
