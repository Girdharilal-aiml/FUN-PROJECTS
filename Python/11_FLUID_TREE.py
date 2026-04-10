import turtle
import random

def setup_canvas():
    screen = turtle.Screen()
    screen.bgcolor("#F5F5F0") 
    screen.setup(width=900, height=900)
    screen.title("Fluid Recursive Growth (Biological Ink)")
    screen.tracer(10)
