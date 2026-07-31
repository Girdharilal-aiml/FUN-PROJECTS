import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("ULTRA FRACTAL EXPLOSION")
screen.tracer(120)
t = turtle.Turtle()
t.speed(0)
t.width(1)

hue = 0
def draw_fractal(x, y, angle, depth, length):
    global hue
    
    if depth == 0:
        return
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    color = colorsys.hsv_to_rgb(hue % 1, 1, 1)
    t.pencolor(color)
    hue += 0.002