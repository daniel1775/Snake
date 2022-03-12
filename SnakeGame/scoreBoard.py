
from turtle import Turtle
class ScoreBoard(Turtle):
    FONT = ('Arial', 22, 'bold')
    ALIGN = 'center'
    points = 0
    def __init__ (self):
        
        super().__init__()
        self.penup()
        self.goto((0,260))
        self.showPoints()
        
            
    #Method to draw the points using turtle.write
    def showPoints (self):
        self.color("blue")
        self.write(f"Score: {self.points}", False, align=self.ALIGN, font = self.FONT)
        self.hideturtle()

    def increase_points(self):
        self.clear()
        self.points += 1
        self.showPoints()
    
    def game_over(self):
        self.clear()
        self.write("Game Over", False, align=self.ALIGN, font = self.FONT)