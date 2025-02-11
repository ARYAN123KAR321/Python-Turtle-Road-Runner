import turtle

FONT = ("Courier", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.scoreboard = turtle.Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("GAME OVER", align="center", font=FONT)