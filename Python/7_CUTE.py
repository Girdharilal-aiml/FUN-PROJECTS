import turtle
import math
import time

s = turtle.Screen()
s.bgcolor("#0a0a1a")
s.setup(600, 600)
s.title("Hi! ♡")
s.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def clear(): t.clear()

def circle_fill(x, y, r, color):
    t.penup(); t.goto(x, y - r)
    t.pendown(); t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()

def draw_heart(x, y, size, color):
    t.penup(); t.goto(x, y)
    t.pendown()
    t.fillcolor(color); t.pencolor(color)
    t.begin_fill()
    t.setheading(140)
