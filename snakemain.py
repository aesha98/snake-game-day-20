from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

IS_GAME_ON = True
screen = Screen()

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while IS_GAME_ON:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # if snake head distance is lesser than the 10 x 10 dimension of the food then put the food in new location
    if snake.Snakebody[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.keepTrackScore()

    if snake.Snakebody[0].xcor() > 280 or snake.Snakebody[0].xcor() < -280 or snake.Snakebody[0].ycor() > 280 or \
            snake.Snakebody[0].ycor() < -280:
        IS_GAME_ON = False
        score.game_over()

    # detect colision with the tail
    for piece in snake.Snakebody:
        if piece == snake.Snakebody[0]:
            pass
        elif snake.Snakebody[0].distance(piece) < 10:
            IS_GAME_ON = False
            score.game_over()

screen.exitonclick()
