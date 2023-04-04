from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.setheading(90)
        self.color('green')
        self.scoreboard = Scoreboard()

    def crawl_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def crawl_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def crawl_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def target_reached(self):
        if self.ycor() > FINISH_LINE_Y:
            self.scoreboard.clear()
            self.scoreboard.level_up()
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

    def failure(self):
        self.home()
        self.write('GAME OVER', align='center', font=('Roboto', 44, 'normal'))
