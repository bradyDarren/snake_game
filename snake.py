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
        snake_head = self.segments[0]
        if snake_head.heading() == 0 or snake_head.heading() == 180:
            if x_cor >= 0:
                x_cor = x_cor + 20
                additional_segment.goto(x=x_cor, y=y_cor)
                self.segments.append(additional_segment)
            else: 
                x_cor = x_cor - 20
                additional_segment.goto(x=x_cor, y=y_cor)
                self.segments.append(additional_segment)
        if snake_head.heading() == 90 or snake_head.heading() == 270:
            if y_cor >= 0:
                y_cor = y_cor + 20
                additional_segment.goto(x=x_cor, y=y_cor)
                self.segments.append(additional_segment)
            else: 
                y_cor = y_cor - 20
                additional_segment.goto(x=x_cor, y=y_cor)
                self.segments.append(additional_segment)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_xcor = self.segments[i- 1].xcor() 
            new_ycor = self.segments[i - 1].ycor() 
            self.segments[i].goto(x = new_xcor, y = new_ycor)
        self.segments[0].forward(20)


snake = Snake()
snake.create_snake()

for i in range(10):
    snake.move()



