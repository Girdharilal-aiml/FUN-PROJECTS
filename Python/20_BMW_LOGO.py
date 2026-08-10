import turtle
import math

def draw_digital_bmw():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#050505")
    screen.title("BMW")
    screen.tracer(1)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    COLORS = {
        "blue": "#0066AD",
        "white": "#FFFFFF",
        "chrome": "#E0E0E0",
        "grid": "#222222"
    }
        
    def draw_tech_ring(radius, width, color, segments=120):
        t.penup()
        t.pencolor(color)
        t.width(width)
        for i in range(segments + 1):
            angle = (i / segments) * 360
     