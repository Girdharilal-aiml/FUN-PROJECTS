import turtle
import colorsys

def draw_fractal_crystal():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=800)
    screen.title("Ultra-Lajawab Python Fractal Effect")
    screen.tracer(50)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.up()
