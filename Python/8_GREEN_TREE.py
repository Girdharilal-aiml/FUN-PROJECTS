import turtle
import random

def draw_real_tree():
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.bgcolor("#111111")
    screen.title("The Ultimate Sick Green Tree")
    screen.tracer(10)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)
