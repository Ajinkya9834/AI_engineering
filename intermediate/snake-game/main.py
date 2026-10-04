from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# a string thet is shown on title bar of the window.
screen.title("My Snake Game") 
screen.tracer(0)
# square_1 = Turtle()
# square_1.shape("square")
# square_1.color("white")
# square_2 = Turtle()
# square_2.shape("square")
# square_2.color("white")
# square_2.goto(-20, 0)
# square_3 = Turtle()
# square_3.shape("square")
# square_3.color("white")
# square_3.goto(-40, 0)

# to optimize the above code
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []

# for pos in starting_positions:
#     new_square = Turtle("square")
#     new_square.color("white")
#     new_square.penup()
#     new_square.goto(pos)
#     segments.append(new_square)
snake = Snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for loop runs in the reverse order of the squares
    # for seg_num in range(len(segments) - 1, 0, -1):
    #     # look for the last 2nd square and takes the x and y coordinates and
    #     # give it to the last square. same repeat for the first square, takes the cor and give to 2nd last.
    #     # square copies the position of the next square
    #     # 3rd copies the position of 2nd and 2nd last copies the position of 1st and so on
    #     seg_x_cor = segments[seg_num - 1].xcor()
    #     seg_y_cor = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(seg_x_cor, seg_y_cor)
    # # this tell the first square to move forward by 20 spaces
    # segments[0].forward(20)
    snake.move()


    
screen.exitonclick()