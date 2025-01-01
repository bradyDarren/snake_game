class Food: 
    def generate_food():
    food_xcord = random.randint(-600,600)
    food_ycord = random.randint(-475,475)
    food = Turtle(shape="circle")
    food.penup()
    food.color("blue")
    food.teleport(food_xcord,food_ycord) 
