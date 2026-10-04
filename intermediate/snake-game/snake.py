from turtle import Turtle

class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for pos in self.starting_positions:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(pos)
            self.segments.append(new_square)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # look for the last 2nd square and takes the x and y coordinates and
            # give it to the last square. same repeat for the first square, takes the cor and give to 2nd last.
            # square copies the position of the next square
            # 3rd copies the position of 2nd and 2nd last copies the position of 1st and so on
            seg_x_cor = self.segments[seg_num - 1].xcor()
            seg_y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(seg_x_cor, seg_y_cor)
        # this tell the first square to move forward by 20 spaces
        self.segments[0].forward(20)