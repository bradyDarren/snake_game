from turtle import Turtle, Screen
import random 


screen = Screen()
"""#1 create a black background for the screen as well as the score count indicator."""
screen.bgcolor("black")
screen.setup(height=1250, width=1250)
screen.title("Classic Snake")

score = 0
score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(x=-10,y=550)
score_display.color("white","white")
score_display.write(f"Score: {score}", move=True,align="center",font=("Ariel",40,"normal"))

"""#3 create a snake with a square body"""
initial_ycord = 0
intitial_xcord = 0

for _ in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(x=intitial_xcord,y=initial_ycord)
    intitial_xcord -= 20

"""#4 implement the movement of the snake within the window. """
def up() 
    snake.setheading(90)
    snake.forward(10)

def down()
    snake.setheading(270)
    snake.forward(10)

def left()
    snake.setheading(180)
    snake.forward(10)

def right():
    snake.setheading(0)
    snake.forward(10)

"""#4 randomize a circle that shows up to resemble food."""

"""#5 If the snake comes into contact with the food make the snake grow."""

screen.exitonclick()
