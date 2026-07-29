import turtle
import colorsys
import math

def draw_muralidhar_mandala():
    screen = turtle.Screen()
    screen.bgcolor("#000814")
    screen.title("Muralidhar")
    screen.setup(width=800, height=800)
    screen.tracer(2)
    t = turtle.Turtle()
    t.speed(0)
    t.width(1)
    t.hideturtle()
    iterations = 360
    for i in range(iterations):

        hue = (i / iterations) * 0.7 
        if i > 250:
            color = colorsys.hsv_to_rgb(0.12, 0.8, 1)
        else:
            color = colorsys.hsv_to_rgb(0.5 + (hue * 0.5), 0.9, 1)
        t.pencolor(color)
        
        angle = i * 137.508
        dist = i * 0.8
        
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(dist)
        t.pendown()
        

 