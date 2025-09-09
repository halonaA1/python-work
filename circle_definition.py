import sys
class Circle:
    units = 'cm'

    def __init__(self, radius, position=(0, 0 ),):
        self.radius = radius
        self.position = position
        self.diameter = 2 * radius
        self.area = 3.142 * radius**2

    def __str__(self):
        return f"I am a circle of radius {self.radius}{self.units}located at{self.position}"

def main():
    circle = Circle(radius = 8)
    print(circle)
    circle.position = (10, 12)
    print(circle)
    circle.radius = 12
    print(circle)
    print(str(circle))
    print(f"My diameter is {circle.diameter}")
    print(f"My area is {circle.area}")

    return 0

if __name__ == '__main__':
    sys.exit(main())