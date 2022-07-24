from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_turtle()

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def start_turtle(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        return False
