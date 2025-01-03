from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.up()
        self.color("white")
        self.hideturtle()
        self.score = 0
        # self.high_score = 0
        with open("data.txt", "r") as h:
            self.high_score = int(h.read())

        self.goto(0, 260)

        self.create_scoreboard()


    def create_scoreboard(self):
        self.write(f"SCORE : {self.score}  HIGH SCORE : {self.high_score}", False, "center", ("Arial", 18, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as h:
                h.write(f"{self.high_score}")
        self.create_scoreboard()

    def reset_score(self):
        self.clear()
        self.score = 0
        self.create_scoreboard()

