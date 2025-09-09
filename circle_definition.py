import sys
import math
class Circle:
    units = 'cm'

    def __init__(self, radius, position=(0, 0 )):
        self.radius = radius
        self.position = position
        self.diameter = 2 * radius
        self.area = 3.142 * radius**2

    def __str__(self):
        return f"I am a circle of radius {self.radius} {self.units} located at{self.position}"
def area(circle):
    return math.pi * circle.radius ** 2

def perimeter(circle):
    return math.pi * circle.radius * 2

def arc_length(circle, theta, radians = True):
    if radians:
        return theta * circle.radius
    else:
        theta_radians = math.radians(theta)
    return theta_radians * circle.radius

def bounding_box(circle):
    xmin = circle.position[0] - circle.radius
    xmax = circle.position[0] + circle.radius
    ymin = circle.position[1] - circle.radius
    ymax = circle.position[1] + circle.radius
    return xmin, ymin, xmax, ymax


def main():
    circle = Circle(radius = 8)
    print(circle)
    circle.position = (10, 12)
    print(circle)
    circle.radius = 12
    print(circle)
    print(str(circle))
    print(f"My diameter is {circle.radius * 2} {circle.units}")
    print(f"My area is {circle.area} {circle.units}^2")
    print(f"The area is {circle.area}")

    print(f"My perimeter is {perimeter(circle)}")
    print(f'My arc length is {arc_length(circle,0.6)}')
    print(f"{arc_length(circle, theta = 0.6) =  }")

    print(f"{bounding_box(circle) = }")


    return 0

if __name__ == '__main__':
    sys.exit(main())