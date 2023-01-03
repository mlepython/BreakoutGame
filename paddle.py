from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle_size = 8
        self.shape("square")
        self.color("white")
        self.paddle_width()
        self.shapesize(1, self.paddle_size)
        self.penup()
        self.goto(position)
        self.lives = 3
        self.boundary = self.paddle_boundary()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def paddle_boundary(self):
        x = self.xcor()
        y = self.ycor()
        height = 20
        width = height*self.paddle_size
        return [x - width/2, y+height/2, x+width/2, y-height/2]

    def paddle_width(self):
        self.paddle_size = 8

