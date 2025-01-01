from turtle import Turtle

class Snake: 
    def __init__(self):
        self.segments = []
        self.initial_xcord = 0
        self.initital_ycord = 0
    
    def create_snake(self):
        for segment in range(3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(x=self.initial_xcord, y=self.initital_ycord)
            print(segment.position())            
            self.segments.append(segment)
            if len(self.segments) != 3:
                self.initial_xcord -= 20

    
            



