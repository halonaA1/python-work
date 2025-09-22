import sys
import turtle
import time

def draw_rectangle():
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(110)

def draw_circle(radius=80):
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
        pen.goto(50, 20)
        pen.down()
        pen.begin_fill()
        pen.pencolor("black")
        pen.fillcolor("yellow")
        pen.circle(radius)
        pen.end_fill()
        pen.up()

def draw_triangle():
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(60)
    turtle.goto(0, 0)
    turtle.done()

def main():
    draw_circle()
    draw_rectangle()
    draw_triangle()
    return 0

if __name__ == "__main__":
    sys.exit(main())

