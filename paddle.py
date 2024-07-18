from turtle import Turtle
from config import configuration


class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed("fast")
        self.goto(pos_x, pos_y)

    def move_up(self):
        if self.ycor() < configuration["HEIGHT"]/2 - 40:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -configuration["HEIGHT"]/2 + 60:
            self.goto(self.xcor(), self.ycor() - 20)
