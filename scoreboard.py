from turtle import Turtle

# from player import Player

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-290, 270)
        self.level = 1
        self.write(f'Level: {self.level}', align='left', font=('Roboto', 18, 'normal'))

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', align='left', font=('Roboto', 18, 'normal'))

