import random
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
tim.color("coral")
# tim.speed("fastest")

# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
    # tim.right(10)

pen_colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "pink",
]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
        

# for num_sides in range(3, 11):
#     tim.pencolor(random.choice(pen_colors))
#     draw_shape(num_sides)


direction = [tim.right, tim.left]
move = [tim.forward, tim.backward]




tim.speed("fastest")
tim.pensize(5)

for _ in range(200):   
    next_move = random.choice(move)
    next_direction = random.choice(direction)
    random_color = random.choice(pen_colors) 
    tim.pencolor(random_color)
    next_direction(90)
    next_move(20)
    





screen = Screen()
screen.exitonclick()
