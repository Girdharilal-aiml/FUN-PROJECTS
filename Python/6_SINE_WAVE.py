import turtle
import math
import colorsys

s = turtle.Screen()
s.bgcolor("black")
s.setup(900, 700)
s.title("Sine Wave Painting")
s.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)
t.penup()

frame = 0

def draw():
    global frame
