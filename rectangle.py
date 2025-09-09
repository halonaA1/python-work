import sys
import math

class Rectangle:
    units = 'cm'
    def __init__(self, width, height, position=(0, 0)):
        self.width = width
        self.height = height
        self.position = position

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def diagonal(self):
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def bounding_box(self):
        xmin = self.position[0] - self.height
        xmax = self.position[0] + self.width
        ymin = self.position[1] - self.width
        ymax = self.position[1] + self.height

def main():
    rectangular = Rectangle(80, 100)
    print(f"{rectangular.perimeter() = } {rectangular.units}")
    print(f"{rectangular.area() = }{rectangular.units}^2")
    print(f"{rectangular.diagonal() =}{rectangular.units}")
    print(f"{rectangular.bounding_box()} =")

    return 0

if __name__ == '__main__':
    sys.exit(main())