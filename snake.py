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

    def add_segment(self): 
        additional_segment = Turtle(shape="square")
        additional_segment.penup()
        additional_segment.color("white")
        x_cor = self.segments[len(self.segments) - 1].xcor()
        y_cor = (self.segments[len(self.segments)-1].ycor())
        if self.segments[0].heading() == 90 or self.segments[0] == 270:
            y_cor = y_cor + 20
            additional_segment.goto(x=x_cor, y=y_cor)
            self.segments.append(additional_segment)
        else: 
            x_cor = x_cor + 20
            additional_segment.goto(x=x_cor, y=y_cor)
            self.segments.append(additional_segment)


snake = Snake() 
snake.create_snake()
snake.add_segment()


    
            



