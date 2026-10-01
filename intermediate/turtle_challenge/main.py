from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("coral")
# tim.speed("fastest")

for _ in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    # tim.right(10)

screen = Screen()
screen.exitonclick()
