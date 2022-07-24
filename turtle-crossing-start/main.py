import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
new_car = CarManager()

scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=player1.move_turtle, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car.create_car()  # every 0.1 seconds new car is created
    new_car.move_car()

    for car in new_car.all_cars:
        if car.distance(player1) < 20:
            screen.clear()
            scoreboard.game_over()
            game_is_on = False

    if player1.is_at_finish():
        new_car.fasten_cars()
        scoreboard.clear()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        player1.start_turtle()




screen.exitonclick()
