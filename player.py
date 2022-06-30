from turtle import Turtle
import random

FONT = ("Courier", 16, "normal")
COLORS = ["purple", "teal", "red", "blue", "yellow", "orange", "green"]
STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):
    '''class to create the character controled by the player'''

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)
        self.write("\n\nYou are a poor cishet man\ntrying to get across the pride\nparade in avenida paulista", align="center", font=FONT)

    def refresh(self):
        self.goto(0, -250)

    # Movement:
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        self.clear()
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def right(self):
        self.goto(self.xcor() + MOVE_DISTANCE,self.ycor() )

    def left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())


class Finish(Turtle):
    '''class to create the finishing line'''

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=27)
        self.color("teal")
        self.speed("fastest")
        self.pencolor("coral")
        self.penup()
        self.goto(0, FINISH_LINE_Y)
