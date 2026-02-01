from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_l_score = 0
        self.player_r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.player_r_score, align="center", font=("Courier", 50, "normal"))

    def increase_player_l_score(self):
        self.player_l_score += 1
        self.update_scoreboard()

    def increase_player_r_score(self):
        self.player_r_score += 1
        self.update_scoreboard()