import turtle
import random

def setup_canvas():
    screen = turtle.Screen()
    screen.bgcolor("#F5F5F0") 
    screen.setup(width=900, height=900)
    screen.title("Fluid Recursive Growth (Biological Ink)")
    screen.tracer(10)
    return screen

def grow(t, length, thickness, angle, wind):
    if length < 5:
        return
    t.pensize(thickness)
    
    color_val = int(255 - (thickness * 15))
    color_val = max(min(color_val, 200), 20)
    color_hex = f'#{color_val:02x}{color_val:02x}{color_val:02x}'
    t.pencolor(color_hex)
