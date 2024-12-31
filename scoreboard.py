from turtle import Turtle

class Scoreboard: 
    score = 0
    score_display = Turtle()
    score_display.hideturtle()
    score_display.penup()
    score_display.goto(x=-10,y=450)
    score_display.color("white","white")
    score_display.write(f"Score: {score}",move=False,align="center",font=("Ariel",40,"normal"))
