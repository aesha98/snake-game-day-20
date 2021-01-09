from turtle import Turtle

SCORE = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.SCORE}", False, align="Center", font=("Roboto", 20, "normal"))

    def keepTrackScore(self):
        self.clear()
        self.SCORE += 1
        self.write(f"Score : {self.SCORE}", False, align="Center", font=("Roboto", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="Center", font=("Roboto", 20, "normal"))
