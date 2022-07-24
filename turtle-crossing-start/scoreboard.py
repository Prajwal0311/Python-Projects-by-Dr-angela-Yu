from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-265, +265)
        self.update_scoreboard()

    def increase_level(self):

        self.level += 1

    def update_scoreboard(self):
        self.write(f"level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over!", align='center', font=('Courier', 60, 'bold'))