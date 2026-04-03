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

def write_text(x, y, text, color, size=18, bold=False):
    t.penup(); t.goto(x, y)
    font = ("Comic Sans MS", size, "bold" if bold else "normal")
    t.pencolor(color); t.write(text, align="center", font=font)

def draw_character(blink=False, mouth_open=False, bounce=0):
    by = bounce  # vertical offset for bounce

    # --- body ---
    circle_fill(0, -120 + by, 55, "#ffcce0")

    # --- head ---
    circle_fill(0, -10 + by, 70, "#ffcce0")

    # --- ears ---
    circle_fill(-58, 30 + by, 20, "#ffb3cc")
    circle_fill( 58, 30 + by, 20, "#ffb3cc")
    circle_fill(-58, 30 + by, 12, "#ff85aa")
    circle_fill( 58, 30 + by, 12, "#ff85aa")

    # --- eyes ---
    if blink:
        t.pencolor("#333"); t.width(3)
        t.penup(); t.goto(-25, 15 + by); t.pendown()
        t.goto(-10, 15 + by); t.penup()
        t.goto( 10, 15 + by); t.pendown()
        t.goto( 25, 15 + by); t.penup()
    else:
        circle_fill(-18, 18 + by, 10, "white")
        circle_fill( 18, 18 + by, 10, "white")
        circle_fill(-18, 16 + by,  6, "#222")
        circle_fill( 18, 16 + by,  6, "#222")
        circle_fill(-16, 18 + by,  2, "white")
        circle_fill( 16, 18 + by,  2, "white")

    # --- blush ---
    t.penup(); t.goto(-36, 5 + by)
    t.pencolor("#ffaacc"); t.fillcolor("#ffaacc")
    t.begin_fill(); t.circle(9); t.end_fill()
    t.penup(); t.goto( 27, 5 + by)
    t.begin_fill(); t.circle(9); t.end_fill()

    # --- nose ---
    circle_fill(0, 8 + by, 3, "#ff85aa")

    # --- mouth ---
    t.pencolor("#cc5577"); t.width(3)
    t.penup()
    if mouth_open:
        t.goto(-14, -6 + by); t.pendown()
        t.setheading(-60)
        t.circle(16, 120); t.penup()
        # little teeth
        t.fillcolor("white")
        t.goto(-8, -10 + by); t.begin_fill()
        for _ in range(4): t.forward(8); t.right(90)
        t.end_fill()
