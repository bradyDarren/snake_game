from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
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
"""#3 implement the movement of the snake within the window. """
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

"""#4 randomize a circle that shows up to resemble food."""
game_one = True
food = Food()

while game_one: 
    screen.update()
    time.sleep(.05)
    snake.move()
    if snake.wall_collision():
        game_one = False
    if snake.tail_collision():
        game_one = False
    if snake.segments[0].distance(food) < 15:
        food.generate_food()
        snake.grow()
        score.increase_score()
    

screen.exitonclick()
