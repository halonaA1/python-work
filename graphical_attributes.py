import sys
import math
import turtle


class Circle:
    units = 'cm'

    def __init__(self, radius, fill="yellow", stroke="black", position=(0, 0)):
        self.radius = radius
        self.position = position
        self.fill = fill
        self.stroke = stroke

        self.diameter = radius * 2

    def __str__(self):
        return f"circle of radius {self.radius} {self.units} located at {self.position}."

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 *math.pi * self.radius

    def arc_length(self, theta, radians=True):
        if radians:
            return theta * self.radius
        else:
            theta_radians = math.radians(theta)
            return theta_radians * self.radius

    def bounding_box(self):
        x_min = self.position[0] - self.radius
        x_max = self.position[0] + self.radius
        y_min = self.position[1] - self.radius
        y_max = self.position[1] + self.radius
        return x_min, y_min, x_max, y_max

    def draw_circle(self, pen):
        pen.up()
        pen.goto(self.position[0], self.position[1] - self.radius)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.circle(self.radius)
        pen.up()


class Rectangle:
    units = 'cm'

    def __init__(self, width, length, fill="green", stroke="black", position=(0, 0)):
        self.width = width
        self.length = length
        self.position = position
        self.fill = fill
        self.stroke = stroke
    def __str__(self):
        return f"rectangle of width {self.width} {self.units} located at {self.position}."

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (2 * self.width) + (2 * self.length)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.length ** 2)

    def bounding_box(self):
        x_min = self.position[0] - self.width / 2
        x_max = self.position[0] + self.width / 2
        y_min = self.position[1] - self.length / 2
        y_max = self.position[1] + self.length / 2
        return x_min, y_min, x_max, y_max

    def draw_rectangle(self, pen):
        pen.up()
        pen.goto(self.position[0], self.position[1] - self.length)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        for _ in range(2):
            pen.forward(self.width)
            pen.right(90)
            pen.forward(self.length)
            pen.right(90)
        pen.end_fill()
        pen.up()

class Square:
    units = 'cm'

    def __init__(self, side, fill="brown", stroke="black", position=(0, 0)):
        self.side = side
        self.position = position
        self.fill = fill
        self.stroke = stroke
    def __str__(self):
     return f"square of side {self.side} {self.units} located at {self.position}."
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return self.side * 4
    def diagonal(self):
        return math.sqrt(self.side ** 2 + self.side ** 2 )
    def bounding_box(self):
        x_min = self.position[0] - self.side / 2
        x_max = self.position[0] + self.side / 2
        y_min = self.position[1] - self.side / 2
        y_max = self.position[1] + self.side / 2
        return x_min,y_min, x_max, y_max

class Canvas(turtle.TurtleScreen):
    def __init__(self, width = 1200, height = 750, background="white"):
        self.canvas = turtle.getcanvas()
        super().__init__(self.canvas)
        self.width = width
        self.height = height
        turtle.screensize(width, height, background)
        self.pen = turtle.RawPen(self.canvas)

    def mystery_method(self):
        self.pen.up()
        self.pen.goto(0, self.height/ 2)
        self.pen.down()
        self.pen.goto(0, -self.height/ 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.up()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()



class Text:
    def __init__(self, text, colour = 'red' ,position=(0, 0)):
        self.text = text
        self.position = position
        self.colour = colour

class Square(Rectangle):
    def __init__(self, side,fill= "brown", stroke ="black", position=(0, 0)):
        super().__init__(side, side, fill , stroke  , position )
    def __str__(self):
        return f"square of side {self.width} {self.units} located at {self.position}."

def main():
    screen = turtle.Screen()
    pen = turtle.Turtle()

    circle = Circle(radius=60)
    print(circle)
    circle.position = (150, 100)
    print(circle)
    print(f"Circle diameter: {circle.diameter} {circle.units} ")
    print(f"Circle area = {circle.area()} {circle.units}^2")
    print(f"Circle perimeter = {circle.perimeter()} {circle.units}")
    print(f"Circle arc length = {circle.arc_length(0.5)} ")
    print(f" {circle.bounding_box() = }")
    circle.draw_circle(pen)

    rectangle = Rectangle(300, 500)
    print(rectangle)
    rectangle.position = (0,0)
    print(rectangle)
    print(f"Rectangle area = {rectangle.area()} {rectangle.units}^2")
    print(f"Rectangle perimeter = {rectangle.perimeter()} {rectangle.units}")
    print(f"Rectangle diagonal = {rectangle.diagonal()} {rectangle.units}")
    print(f"{rectangle.bounding_box()} ")
    rectangle.draw_rectangle(pen)


    square = Square(90)
    print(square)
    square.position = (150, 0)
    print(square)
    print(f"Square area = {square.area()} {square.units}^2")
    print(f"Square perimeter = {square.perimeter()} {square.units}")
    print(f"square diagonal = {square.diagonal()} {square.units}")
    print(f"{square.bounding_box()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())