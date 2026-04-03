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
    for _ in range(200):
        angle = _ / 200 * math.tau
        hx = size * 16 * math.sin(angle)**3
        hy = size * (13*math.cos(angle) - 5*math.cos(2*angle)
                    - 2*math.cos(3*angle) - math.cos(4*angle))
        t.goto(x + hx, y + hy)
    t.end_fill()
    t.penup()

def draw_star(x, y, size, color):
    t.penup(); t.goto(x, y)
    t.pencolor(color); t.pendown()
    t.width(2)
    for _ in range(5):
        t.forward(size); t.right(144)
    t.penup()
