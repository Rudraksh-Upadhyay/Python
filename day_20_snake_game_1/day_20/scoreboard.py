from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.up()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.goto(0, 280)
        # self.write(f"SCORE : {self.score}", False, "center", ("Arial", 12, "normal"))

        self.create_scoreboard()


    def create_scoreboard(self):
        self.write(f"SCORE : {self.score}", False, "center", ("Arial", 12, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.create_scoreboard()
        # self.write(f"SCORE : {self.score}", False, "center", ("Arial", 12, "normal"))

