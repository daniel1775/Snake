#Creation of board of the game
from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time
#Creation of the board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Programate snake game")
screen.tracer(0)
#Creation of the Snake and the Food
snake = Snake()
food = Food()
scoreBoard = ScoreBoard()
#Listen keys method
def movement(method,direction):
    screen.listen()
    screen.onkey(method, direction)

def finish_game():
    global game_is_on
    game_is_on = False
    scoreBoard.game_over()

movement(snake.up, "Up")
movement(snake.left, "Left")
movement(snake.down, "Down")
movement(snake.right, "Right")

#Snake animation
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collition with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.increase_points();
        snake.extend()

    #Detect collition with the board
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        finish_game()

    #Detect collition with the body of the snake
    for i in snake.snake_body[slice(1, len(snake.snake_body))]:
        if snake.head.distance(i)<10:
            finish_game()
            
screen.exitonclick()