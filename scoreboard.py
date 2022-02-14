from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.setposition((0, 320))
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition((0, 0))
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)