from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

WALLCOLLISION = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# a string thet is shown on title bar of the window.
screen.title("My Snake Game") 
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.segments[0].xcor() > WALLCOLLISION or snake.segments[0].xcor() < -WALLCOLLISION or snake.segments[0].ycor() > WALLCOLLISION or snake.segments[0].ycor() < -WALLCOLLISION:
        scoreboard.reset()
        

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()