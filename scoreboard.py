from turtle import Turtle

class Scoreboard(Turtle): 
    def __init__(self, xcord, ycord):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=xcord,y=ycord)
        self.color("white","white")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}",move=False,align="center",font=("Ariel",40,"normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
