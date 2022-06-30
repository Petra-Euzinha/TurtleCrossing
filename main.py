from turtle import Screen
from gays import LeftGay, RightGay
from player import Player, Finish
from level import Level
import time

SPEED = 0.1
GAME = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightgrey")
screen.title("lgbtcrossing")
screen.listen()
screen.tracer(0)
line = Finish()
player = Player()
level = Level()
level.refresh()
r_gay = RightGay()
l_gay = LeftGay()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

while GAME:
    screen.update()
    time.sleep(SPEED)
    r_gay.create_gay()
    r_gay.move()
    l_gay.create_gay()
    l_gay.move()

    if player.ycor() == 250:
        level.refresh()
        player.refresh()
        l_gay.refresh()
        r_gay.refresh()

    for gay in l_gay.left_gays:
        if gay.distance(player) < 20:
            level.game_over()
            player.refresh()
            GAME = False

    for gay in r_gay.right_gays:
        if gay.distance(player) < 20:
            level.game_over()
            player.refresh()
            GAME = False

screen.exitonclick()

