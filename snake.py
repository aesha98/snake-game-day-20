from turtle import Turtle, Screen

snakeStart = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ Model of the snake"""

    def __init__(self):
        self.Snakebody = []
        for snakebody in snakeStart:
            self.addbody(snakebody)

    def addbody(self, snakebody):
        snake = Turtle(shape="square")
        snake.speed(0)
        snake.penup()
        snake.fillcolor("white")
        snake.goto(snakebody)
        self.Snakebody.append(snake)

    def extend(self):
        self.addbody(self.Snakebody[-1].position())

    def move(self):
        for snake_num in range(len(self.Snakebody) - 1, 0, -1):
            x_pos = self.Snakebody[snake_num - 1].xcor()
            y_pos = self.Snakebody[snake_num - 1].ycor()
            self.Snakebody[snake_num].goto(x_pos, y_pos)

        self.Snakebody[0].fd(MOVE_DISTANCE)

    # self.Snakebody[0].left(90)

    def up(self):
        if self.Snakebody[0].heading() != DOWN:
            self.Snakebody[0].setheading(UP)

    def down(self):
        if self.Snakebody[0].heading() != UP:
            self.Snakebody[0].setheading(DOWN)

    def left(self):
        if self.Snakebody[0].heading() != RIGHT:
            self.Snakebody[0].setheading(LEFT)

    def right(self):
        if self.Snakebody[0].heading() != LEFT:
            self.Snakebody[0].setheading(RIGHT)
