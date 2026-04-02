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
    t.clear()

    for wave in range(12):
        freq   = 1 + wave * 0.5
        amp    = 60 - wave * 3
        offset = wave * 30 - 180
        hue    = (wave / 12 + frame * 0.003) % 1.0
        sat    = 0.8
        val    = 0.7 + 0.3 * math.sin(frame * 0.05 + wave)
        r, g, b = colorsys.hsv_to_rgb(hue, sat, val)

        t.pencolor(r, g, b)
        t.width(1 + wave % 3)

        t.penup()
