from turtle import Turtle
import random


class Food(Turtle): 
    def __init__(self):
        super().__init__(shape="circle") 
        self.penup() 
        self.color("blue", "blue")
        self.food_xlocation = []
        self.food_ylocation = []
        self.generate_food()

    def generate_food(self):
        for xaxis in range(-560,580,20):
            self.food_xlocation.append(xaxis)
        for yaxis in range(-460,480,20):
            self.food_ylocation.append(yaxis)
        
        xcor = random.choice(self.food_xlocation)
        ycor = random.choice(self.food_ylocation)
        self.teleport(x=xcor,y=ycor)

food = Food()
        