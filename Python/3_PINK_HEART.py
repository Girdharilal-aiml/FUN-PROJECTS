import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Amazing Neon Heart Animation")

t = turtle.Turtle()
t.speed(1)  
t.pensize(2)
t.hideturtle()

def heart_x(k):
    return 15 * math.sin(k)**3

def heart_y(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

def draw_amazing_heart():

    screen.tracer(2)
    
    for j in range(3): 
        t.penup()
       
        scale = 20 + (j * 2) 
        t.pensize(5 - j)
        
