from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over", align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear() # Clear everything that this Turtle has drawn or written.
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
