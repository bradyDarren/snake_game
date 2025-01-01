from turtle import Turtle, Screen
from scoreboard import Scoreboard
from snake import Snake
import random 
import time


screen = Screen()
screen.listen()
"""#1 create a black background for the screen as well as the score count indicator."""
screen.bgcolor("black")
screen.setup(height=1000, width=1200)
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
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

"""#4 randomize a circle that shows up to resemble food."""
game_one = True

while game_one: 
    screen.update()
    time.sleep(.1)
    snake.move()
    snake.wall_collision()    

"""#5 If the snake comes into contact with the food make the snake grow."""
screen.exitonclick()
