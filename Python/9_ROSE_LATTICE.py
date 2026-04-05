import turtle
import colorsys

def create_unique_art():

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#050505") 
    screen.tracer(2)  
    screen.title("Unique Mirrored Fractal Mandala")

    turtles = []
    colors = []
    
    num_colors = 100
    for i in range(num_colors):
        rgb = colorsys.hsv_to_rgb(i / num_colors, 0.8, 1)
        colors.append(rgb)

    for i in range(4):
        new_t = turtle.Turtle()
