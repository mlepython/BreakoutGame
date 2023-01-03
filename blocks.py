from turtle import Turtle
from random import *
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
N_BLOCKS = 10
N_ROWS = 8
BLOCK_SIZE = 3
BLOCK_HEIGHT = 0.5

class Blocks(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.shape("square")
        # self.color(choice(COLORS))
        # self.penup()
        # self.shapesize(1, 5)
        # self.goto(position)
        self.all_blocks = []
        # self.x_move=10
        # self.y_move=10
        # self.move_speed = 0.1

    def create_block_row(self, start_position, spacing):
        def block_color():
            if row == 0 or row == 1:
                color = "yellow"
                points = 1
            elif row == 2 or row == 3:
                color = "green"
                points = 3
            elif row == 4 or row == 5:
                color = "orange"
                points = 5
            elif row == 6 or row == 7:
                color = "red"
                points = 7
            else:
                color, points = 0, 0
            return color, points

        y = start_position[1]
        height = 20 * BLOCK_HEIGHT
        width = 20 * BLOCK_SIZE
        for row in range(N_ROWS):
            x = start_position[0] + BLOCK_SIZE * 10
            for index in range(N_BLOCKS):
                new_block = Turtle("square")
                color, new_block.points = block_color()
                new_block.color(color)
                new_block.penup()
                new_block.shapesize(BLOCK_HEIGHT, BLOCK_SIZE)
                new_block.goto(x, y)
                new_block.boundary = [x - width/2, y+height/2, x+width/2, y-height/2]
                self.all_blocks.append(new_block)
                x += spacing/N_BLOCKS
            y += height * 2

    def remove_block(self, block_to_remove):
        block_to_remove.hideturtle()
        self.all_blocks.remove(block_to_remove)
