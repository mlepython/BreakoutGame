from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0
        self.y_move = 5
        self.move_speed = 0.01
        self.bounce_count = 0
        self.top_boundary_count = 0
        self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(-280, 0)
        self.move_speed = 0.1
        self.bounce_x()