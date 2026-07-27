import turtle
import colorsys

def draw_fractal(t, length, depth, hue):
    if depth == 0:
        return
    
    color = colorsys.hsv_to_rgb(hue % 1.0, 0.8, 1.0)
    t.pencolor(color)
    t.width(depth)
    

    

    
 