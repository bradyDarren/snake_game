from turtle import Turtle

class Snake: 
    def __init__(self):
        self.segments = []
        self.initial_xcord = 0
        self.initital_ycord = 0
    
    def create_snake(self):
        for segment in range(3):
            segment = Turtle(shape="square")
            # lifts the pen to aviod drawing
            segment.penup()
            # set the intital color of the snake body
            segment.color("white")
            # sets the intital position of each section of the snake
            segment.goto(x=self.initial_xcord, y=self.initital_ycord)
            # print(segment.position())
            # adds each instance/section of the snake to a list
            self.segments.append(segment)
            # Adjust the x-cord of each segment
            if len(self.segments) != 3:
                self.initial_xcord -= 20

    def grow(self): 
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

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    
    def wall_collision(self):
        if self.segments[0].xcor() >= 600 or self.segments[0].xcor() <= -600 or self.segments[0].ycor() >= 500 or self.segments[0].ycor() <= -500:
            for segment in self.segments:
                segment.reset()
            game_over = Turtle() 
            game_over.hideturtle()
            game_over.penup()
            game_over.color("white","white")
            game_over.write("GAME OVER",move=False, align="center",font=("Ariel",40,"normal"))
            return True 
        return False
    
    def tail_collision(self):
        for section in range(1, len(self.segments)):
            segment = self.segments[section]
            if self.segments[0].distance(segment) < 15:
                for segment in self.segments:
                    segment.reset()
                game_over = Turtle() 
                game_over.hideturtle()
                game_over.penup()
                game_over.color("white","white")
                game_over.write("GAME OVER",move=False, align="center",font=("Ariel",40,"normal"))
                return True
        return False
           

            
        

