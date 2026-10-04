from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()
    
    def increase_score(self):
        self.score += 1
        self.clear() # Clear everything that this Turtle has drawn or written.
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))
