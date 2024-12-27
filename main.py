from turtle import Turtle, Screen
import random 


screen = Screen()
"""#1 create a black background for the screen as well as the score count indicator."""
screen.bgcolor("black")

score = 0
score_display = Turtle()
score_display.penup()
score_display.color("white","white")
score_display.write(f"Score: {score}", move=True,align="center",font=("Ariel",20,"normal"))

"""#2 create a Score counter at the top of the screen"""
"""#3 create a snake with a square body"""

"""#4 randomize a circle that shows up to resemble food."""
"""#5 If the snake comes into contact with the food make the snake grow."""




screen.exitonclick()
