from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Level(Turtle):
    '''class to keep track of the game level'''
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.pencolor("black")
        self.goto(-250, 270)

    def refresh(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over.\nAn lgbt touched you,\nYou are now gay, trans and vegan.\nYou feel happier this way.", align="center", font=FONT)