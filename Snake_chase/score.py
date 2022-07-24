from turtle import Turtle

ALIGN = "center"
FONT = ('Courier ', 22, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)

    def increse_score(self):
        self.score += 1
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over!",align=ALIGN,font=('Courier', 29 , 'bold'))

