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

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for num_sides in range(3, 11):
    draw_shape(num_sides)

screen = Screen()
screen.exitonclick()
