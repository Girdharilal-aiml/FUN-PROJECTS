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
    t.penup()
    t.goto(0, -350)
    t.pendown()

    def grow_tree(branch_len, stroke_width):
        if branch_len < 10:
            t.pencolor(random.choice(["#32CD32", "#00FF00", "#7FFF00", "#228B22"]))
            t.pensize(stroke_width)
            t.forward(branch_len)
