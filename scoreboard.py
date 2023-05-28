from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_record.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_record.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def score_increase(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", align=ALIGNMENT, font=FONT)
