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
initial_xcord = 0
entire_snake = []

for snake in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(x=initial_xcord,y=initial_ycord)
    entire_snake.append(snake)
    if len(entire_snake) != 3:
        initial_xcord -= 20
    # print(snake.position())


"""#3 implement the movement of the snake within the window. """
def move():
    for i in range(len(entire_snake)-1,0,-1):
        new_xcord = entire_snake[i-1].xcor()
        new_ycord = entire_snake[i-1].ycor()
        entire_snake[i].goto(new_xcord,new_ycord)
    entire_snake[0].forward(20)

def up():
    if entire_snake[0].heading() != 270:
        entire_snake[0].setheading(90)
        entire_snake[0].forward(10)

def down():
    if entire_snake[0].heading() != 90:
        entire_snake[0].setheading(270)
        entire_snake[0].forward(10)

def left():
    if entire_snake[0].heading() != 0:
        entire_snake[0].setheading(180)
        entire_snake[0].forward(10)

def right():
    if entire_snake[0].heading() != 180:
        entire_snake[0].setheading(0)
        entire_snake[0].forward(10)

screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)

game_on = True

while game_on: 
    move()

"""#4 randomize a circle that shows up to resemble food."""

"""#5 If the snake comes into contact with the food make the snake grow."""

screen.exitonclick()
