import turtle
import colorsys

def draw_amazing_fractal():

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Amazing Neon Fractal Design")
    
    t = turtle.Turtle()
    t.speed(12)
    t.width(1)
    t.hideturtle()
    
    turtle.tracer(23332, 33333)
    
    hue = 0.0
    
