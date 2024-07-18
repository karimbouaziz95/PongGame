from turtle import Turtle

from config import configuration

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.speed(1)
        self.x_direction = 1
        self.y_direction = 1

    def move(self):
        new_x = self.xcor() + 10*self.x_direction
        new_y = self.ycor() + 10*self.y_direction

        self.goto(new_x, new_y)
        if abs(self.ycor()) >= configuration["HEIGHT"]/2 - 15:
            self.y_direction *= -1

    def bounce(self):
        self.x_direction *= -1
        self.speed(self.speed() + 1)