import sys
import turtle

def draw_rectangle():
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(110)
    turtle.done()

def main():
    draw_rectangle()
    return 0
if __name__ == '__main__':
    sys.exit(main())