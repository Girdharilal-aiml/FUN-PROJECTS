import turtle
import random

screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("#0a0a0a") 
screen.title("Live Growing Dense Fractal Tree")

screen.tracer(1) 

t = turtle.Turtle()
t.hideturtle()
t.speed(0) 
