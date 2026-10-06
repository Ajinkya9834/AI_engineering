from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write_high_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score_from_file(self.high_score)
        self.score = 0
        self.write_high_score()

    def increase_score(self):
        self.score += 1
        self.write_high_score()
    
    def write_high_score(self):
        self.clear() # Clear everything that this Turtle has drawn or written.
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            high_score = int(file.read())
            return high_score
    
    def write_score_from_file(self, high_score):
        with open("data.txt", mode = "w") as file:
            file.write(str(high_score))

