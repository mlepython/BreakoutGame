from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from blocks import Blocks
from random import *
from boundary import Boundary
from scoreboard import Scoreboard, Timer
import time

SCREEN_SIZE = (800, 1000)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -300))

ball = Ball((0, -280))
left_boundary, right_boundary, top_boundary, bottom_boundary = -350, 350, 400, -350

spacing = right_boundary - left_boundary

block_manager = Blocks((0, 0))
block_manager.create_block_row(start_position=(-350, 200), spacing=spacing)

Boundary(SCREEN_SIZE)
screen.onkey(paddle.go_up, "w")
screen.onkey(paddle.go_down, "s")
screen.onkeypress(paddle.go_right, "d")
screen.onkeypress(paddle.go_left, "a")

screen.listen()


def play_game():
    game_is_on = True
    game_points = 0
    score = Scoreboard(game_points)
    timer = Timer()
    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()
        screen.update()
        timer.update_timer()
        for block in block_manager.all_blocks:
            if block.boundary[3] - 10 < ball.ycor() < block.boundary[1] + 10 and \
                    block.boundary[0] - 10 < ball.xcor() < block.boundary[2] + 10:
                block_manager.remove_block(block)
                ball.bounce_y()
                game_points += block.points
                score.update_scoreboard(game_points)
                ball.bounce_count += 1
                if ball.bounce_count >= 10:
                    ball.move_speed *= 0.9
                    ball.bounce_count = 0

        if paddle.paddle_boundary()[3] - 5 < ball.ycor() < paddle.paddle_boundary()[1] + 5 and \
                paddle.paddle_boundary()[0] - 5 < ball.xcor() < paddle.paddle_boundary()[2] + 5:
            ball.bounce_y()
            if ball.xcor() < paddle.xcor() - 10:
                ball.x_move = -5
            elif ball.xcor() > paddle.xcor() + 10:
                ball.x_move = 5

        if ball.xcor() > right_boundary - 20:
            ball.bounce_x()
        if ball.xcor() < left_boundary + 20:
            ball.bounce_x()
        if ball.ycor() > top_boundary - 20:
            ball.bounce_y()

        if paddle.xcor() < left_boundary + paddle.paddle_size*10:
            paddle.goto(left_boundary + paddle.paddle_size*10, paddle.ycor())
        if paddle.xcor() > right_boundary - paddle.paddle_size*10:
            paddle.goto(right_boundary - paddle.paddle_size*10, paddle.ycor())

        if ball.ycor() < bottom_boundary:
            score.lose_life()
            score.update_scoreboard(game_points)
            paddle.goto((0, -300))
            ball.goto((0, -280))
            time.sleep(1)
            if score.lives == 0:
                score.game_over()
                game_is_on = False


play_game()
screen.exitonclick()
