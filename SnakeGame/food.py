from turtle import Turtle
import random
class Food(Turtle):
    #Constructor
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed('fastest')
        self.refresh()
    #Function to move randomly the food
    def refresh(self):
        random_X = random.randint(-200,200)
        random_Y = random.randint(-200,200)
        self.goto(random_X,random_Y)