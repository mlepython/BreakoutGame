from turtle import Turtle
import datetime
current_time = datetime.datetime.now()
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self, points):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.l_score = 0
        self.r_score = 0
        self.start_time = (current_time.minute, current_time.second)
        self.update_scoreboard(points)

    def update_scoreboard(self, points):
        self.clear()
        self.goto(-150, 390)
        self.write(self.lives, align=ALIGNMENT, font=FONT)
        self.goto(150, 390)
        self.write(points, align=ALIGNMENT, font=FONT)



    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    # def l_point(self):
    #     self.l_score += 1
    #     self.update_scoreboard()
    #
    # def r_point(self):
    #     self.r_score += 1
    #     self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1


class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.start_time = (current_time.minute, current_time.second)
        self.update_timer()

    def update_timer(self):
        self.clear()
        current_time = datetime.datetime.now()
        minute = current_time.minute - self.start_time[0]
        second = current_time.second - self.start_time[1]
        self.goto(0, 410)
        self.write(f"{minute}:{second}", align=ALIGNMENT, font=("Courier", 20, "normal"))