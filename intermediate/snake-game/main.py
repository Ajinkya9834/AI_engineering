from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# a string thet is shown on title bar of the window.
screen.title("My Snake Game") 

square_1 = Turtle()
square_1.shape("square")
square_1.color("white")


square_2 = Turtle()
square_2.shape("square")
square_2.color("white")
square_2.goto(-20, 0)

square_3 = Turtle()
square_3.shape("square")
square_3.color("white")
square_3.goto(-40, 0)




screen.exitonclick()