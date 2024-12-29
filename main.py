from turtle import Turtle, Screen
import random 


screen = Screen()
screen.listen()
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

"""#2 create a snake with a square body"""
initial_ycord = 0
intitial_xcord = 0
entire_snake = []

for snake in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(x=intitial_xcord,y=initial_ycord)
    entire_snake.append(snake)
    intitial_xcord -= 20
    # print(snake.position())


"""#3 implement the movement of the snake within the window. """
def move():
    for i in range(len(entire_snake)-1,0,-1):
        new_xcord = entire_snake[i-1].xcor()
        new_ycord = entire_snake[i-1].ycor()
        entire_snake[i].goto(new_xcord,new_ycord)

move()

def up():
    if entire_snake[0].heading() != 270:
        entire_snake

def down():
    snake.setheading(270)
    snake.forward(10)

def left():
    snake.setheading(180)
    snake.forward(10)

def right():
    snake.setheading(0)
    snake.forward(10)

screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)

"""#4 randomize a circle that shows up to resemble food."""

"""#5 If the snake comes into contact with the food make the snake grow."""

screen.exitonclick()
