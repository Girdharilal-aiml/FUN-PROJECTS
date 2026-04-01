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
t.left(90)
t.penup()
t.goto(0, -350) 
t.pendown()

def grow_tree_step_by_step(branch_len, thickness):
    if branch_len < 6:
