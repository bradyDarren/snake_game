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
snake_head = Turtle(shape="square")
snake_head.penup()
snake_head.color("white")
print(snake_head.position())

snake_body = Turtle(shape="square")
snake_body.penup()
snake_body.color("white")
snake_body.goto(x=-20,y=0)
print(snake_body.position())

snake_tail = Turtle(shape="square")
snake_tail.penup()
snake_tail.color("white")
snake_tail.goto(x=-40,y=0)
print(snake_tail.position())

"""#4 randomize a circle that shows up to resemble food."""
"""#5 If the snake comes into contact with the food make the snake grow."""




screen.exitonclick()
