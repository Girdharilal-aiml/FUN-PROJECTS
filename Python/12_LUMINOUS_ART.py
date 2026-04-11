import turtle
import colorsys

def draw_luminous_art():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Luminous Fractal Art")
    screen.setup(width=900, height=900)
    
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(5)
    t.hideturtle()
    
