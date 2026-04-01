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
        t.color(random.choice(["#27ae60", "#2ecc71", "#a2d149", "#155e37"]))
        t.pensize(2)
        t.forward(branch_len)
        t.dot(random.randint(3, 6)) 
        t.backward(branch_len)
        return

    if branch_len > 45:
        t.color("#5d4037")
    else:
        t.color("#8d6e63") 

    t.pensize(thickness)
    t.forward(branch_len)

    pos = t.pos()
    heading = t.heading()

    angle = random.uniform(20, 30)
    reduction = random.uniform(8, 14)

    t.right(angle)
    grow_tree_step_by_step(branch_len - reduction, thickness * 0.75)
    
