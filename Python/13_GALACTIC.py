import turtle
import colorsys
import math

def draw_singularity():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1.0, height=1.0) 
    
    t = turtle.Turtle()
    t.speed(11000)
    turtle.delay(0)
    t.hideturtle()
    
    n = 1000 
    h = 10
    
    for i in range(n):
        color = colorsys.hsv_to_rgb(h, 0.9, 1)
        t.pencolor(color)
        h += 1/n
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(i * 135.5)
        t.forward(i)
        t.left(60)
