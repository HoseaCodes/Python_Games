from turtle import Turtle

x_position = [0, -20, -40]
move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for index in range(0, 3):
            self.grow(index)

    def grow(self, index):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(x=x_position[index], y=0)
        self.snake_body.append(snake)

    def extend(self):
        self.grow(self.snake_body[-1].position())

    def move(self):
        for index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(new_x, new_y)
        self.snake_body[0].forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

