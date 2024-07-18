from turtle import Turtle
from config import configuration

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.initial_x_position = 0
        self.initial_y_position = configuration["HEIGHT"]/2 - 25
        self.goto(self.initial_x_position, self.initial_y_position)
        self.score_player_left = 0
        self.score_player_right = 0
        #self.write("Game over.", move=False, align="center", font=('Arial', 20, 'normal'))
        self.write("Score", move=False, align="center", font=('Arial', 20, 'normal'))
        self.goto(self.xcor(), self.ycor() - 20)
        self.write(f"{self.score_player_left} : {self.score_player_right}", move=False, align="center", font=('Arial', 20, 'normal'))

    def update_score_player_left(self):
        self.score_player_left += 1
        self.update_score_board()

    def update_score_player_right(self):
        self.score_player_right += 1
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(self.initial_x_position, self.initial_y_position)
        self.write("Score", move=False, align="center", font=('Arial', 20, 'normal'))
        self.goto(self.xcor(), self.ycor() - 20)
        self.write(f"{self.score_player_left} : {self.score_player_right}", move=False, align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game over.", move=False, align="center", font=('Arial', 20, 'normal'))
