from turtle import Turtle

class Scoreboard(Turtle): 
    def __init__(self, ycord):
        super().__init__()
        self.score = 0
        # hide the turtle cursor
        self.hideturtle()
        # lift the pen to avoid drawing lines
        self.penup()
        # set the intital position
        self.goto(x=0,y=ycord)
        # set the color of the text
        self.color("white","white")

    def update_score(self):
        # Clear the previous score
        self.clear()
        # Update the current score at the center of the screen
        self.write(f"Score: {self.score}",move=False,align="center",font=("Ariel",40,"normal"))

    def increase_score(self):
        # Increment the score by 1
        self.score += 1
        # Update the displayed score
        self.update_score()
