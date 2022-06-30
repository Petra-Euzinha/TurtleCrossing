from turtle import Turtle
import random
from level import Level

FONT = ("Courier", 16, "normal")
COLORS = ["purple", "teal", "red", "blue", "yellow", "orange", "green"]
LEFT_LOCATIONS = [(-300, -180), (-300, -120), (-300, -60), (-300, 0), (-300, 60), (-300, 120), (-300, 180)]
RIGHT_LOCATIONS = [(300, -210), (300, -150), (300, -90), (300, -30), (300, 30), (300, 90), (300, 150), (300, 210)]
MOVE_DISTANCE = 10
level = Level()


class LeftGay(Turtle):
    '''class to generate random turtles from the left'''

    def __init__(self):
        super().__init__()
        self.left_gays = []

    def create_gay(self):
        if random.randint(0, 6) == 1:
            new_gay = Turtle("turtle")
            new_gay.shapesize(stretch_wid=1, stretch_len=1)
            new_gay.color(random.choice(COLORS))
            new_gay.speed("fastest")
            new_gay.penup()
            new_gay.goto(random.choice(LEFT_LOCATIONS))
            self.left_gays.append(new_gay)

    def move(self):
        for new_gay in self.left_gays:
            new_gay.goto(new_gay.xcor() + random.randint((2 * level.level
                                                          + MOVE_DISTANCE) / 5, 2 * level.level + MOVE_DISTANCE),
                         new_gay.ycor())

    def refresh(self):
        for gay in self.left_gays:
            gay.reset()


class RightGay(Turtle):
    '''class to generate random turtles from the right'''

    def __init__(self):
        super().__init__()
        self.right_gays = []

    def create_gay(self):
        if random.randint(0, 6) == 1:
            new_gay = Turtle("turtle")
            new_gay.setheading(180)
            new_gay.shapesize(stretch_wid=1, stretch_len=1)
            new_gay.color(random.choice(COLORS))
            new_gay.speed("fastest")
            new_gay.penup()
            new_gay.goto(random.choice(RIGHT_LOCATIONS))
            self.right_gays.append(new_gay)

    def move(self):
        for new_gay in self.right_gays:
            new_gay.goto(new_gay.xcor() - random.randint(MOVE_DISTANCE / 5, MOVE_DISTANCE), new_gay.ycor())

    def refresh(self):
        for gay in self.right_gays:
            gay.reset()
