from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    #constructor
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    #Creation of the snake Method
    def create_snake(self):
        #Create the body of the snake
        #Snake segments
        for i in STARTING_POSITION:
            self.add_segment(i)

    #Add a square to the body of the snake
    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_body.append(snake_segment)

    #Extend the boy of the snake
    def extend (self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for i in range (len(self.snake_body)-1,0,-1):
                x = self.snake_body[i - 1].xcor()
                y = self.snake_body[i - 1].ycor()
                self.snake_body[i].goto(x,y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
