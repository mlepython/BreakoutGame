from turtle import Turtle


class Boundary(Turtle):

    def __init__(self, screen_size):
        super().__init__()
        self.left_boundary()
        self.right_boundary()
        self.top_boundary()

    def left_boundary(self):
        bounds = Turtle("square")
        bounds.color("white")
        bounds.shapesize(100, 0.1)
        bounds.penup()
        bounds.goto(-350, 0)

    def right_boundary(self):
        bounds = Turtle("square")
        bounds.color("white")
        bounds.shapesize(100, 0.1)
        bounds.penup()
        bounds.goto(350, 0)

    def top_boundary(self):
        bounds = Turtle("square")
        bounds.color("white")
        bounds.shapesize(0.1, 100)
        bounds.penup()
        bounds.goto(0, 400)