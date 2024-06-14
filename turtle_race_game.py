from turtle import Turtle, Screen
from tkinter import messagebox
import random

turtles = {}
SPEEDS = [10, 20, 30]


def set_turtles():
    for i in range(1, 6):
        turtles[f"t{i}"] = Turtle()

    x = -230
    y = -100
    colors = ["red", "blue", "yellow", "purple", "green"]
    for _key in turtles:
        _turtle = turtles[_key]
        _turtle.shape("turtle")
        color = random.choice(colors)
        colors.remove(color)
        _turtle.color(color)
        _turtle.penup()
        _turtle.goto(x=x, y=y)
        y += 50


def turtle_race():
    set_turtles()
    race_on = True
    while race_on:
        for key in turtles:
            turtle = turtles[key]
            speed = random.choice(SPEEDS)
            turtle.forward(speed)
            if turtle.xcor() >= 230:
                pen_color, fill_color = turtle.color()
                return fill_color


def show_result(bet):
    winner = turtle_race()
    if bet.lower() == winner:
        message = "You win."
    else:
        message = f"You lose. The winner is: {winner}."
    messagebox.showinfo(title="Race Finished", message=message)
    exit()


s = Screen()
s.setup(width=500, height=400)

user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

show_result(user_bet)

s.exitonclick()
