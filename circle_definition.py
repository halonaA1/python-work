import sys
class Circle:
    units = 'cm'

    def __init__(self, radius, position=(0, 0 )):
        self.radius = radius
        self.position = position

    def __str__(self):
        return f"I am a circle of radius {self.radius}{self.units}located at{self.position}"

def main():
    circle = Circle(radius = 8)
    print(circle)
    circle.position = (10, 12)
    print(circle)
    circle.radius = 12
    print(circle)


    return 0

if __name__ == '__main__':
    sys.exit(main())