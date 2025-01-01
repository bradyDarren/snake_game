from turtle import Turtle, Screen
from scoreboard import Scoreboard
from snake import Snake
import random 


screen = Screen()
screen.listen()
"""#1 create a black background for the screen as well as the score count indicator."""
screen.bgcolor("black")
screen.setup(height=1000, width=1250)
screen.title("Classic Snake")
screen.tracer(0)

score_ycord = int(((screen.window_height()) / 2) - 50)
score = Scoreboard(ycord=score_ycord)
score.update_score()

"""#2 create a snake with a square body"""
snake = Snake()
snake.create_snake()

screen.update() # used to update the all of the code above. 

"""#3 implement the movement of the snake within the window. """
def up():
    if entire_snake[0].heading() != 270:
        entire_snake[0].setheading(90)
        entire_snake[0].forward(20)

def down():
    if entire_snake[0].heading() != 90:
        entire_snake[0].setheading(270)
        entire_snake[0].forward(20)

def left():
    if entire_snake[0].heading() != 0:
        entire_snake[0].setheading(180)
        entire_snake[0].forward(20)

def right():
    if entire_snake[0].heading() != 180:
        entire_snake[0].setheading(0)
        entire_snake[0].forward(20)

screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)

"""#4 randomize a circle that shows up to resemble food."""

def generate_food():
    food_xcord = random.randint(-600,600)
    food_ycord = random.randint(-475,475)
    food = Turtle(shape="circle")
    food.penup()
    food.color("blue")
    food.teleport(food_xcord,food_ycord) 

"""#5 If the snake comes into contact with the food make the snake grow."""

screen.exitonclick()
