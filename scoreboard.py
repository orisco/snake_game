from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.pu()
        self.setposition((0, 320))
        self.print_score()

    def read_score(self):
        with open("data.txt", mode="r") as file:
            highscore = file.read()
            return int(highscore)

    def write_new_score(self):
        with open("data.txt", mode="w") as file:
            new_highscore = str(self.high_score)
            file.write(new_highscore)

    def increase_score(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_score()
        self.score = 0
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}" f", High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.setposition((0, 0))
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

