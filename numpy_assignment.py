import sys
import math
import turtle
import numpy as np
import tkinter as tk

class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"Shape name: {self.name}"

class TextShape(Shape):
    def __init__(self, name, text, position=(150, 150)):
        super().__init__(name)
        self.text = text
        self.position = position

    def draw(self, canvas):
        canvas.create_text(self.position[0], self.position[1], text=self.text, font = ("Times New Roman", 14), fill= "brown")
def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    add_result = A + B
    mult_result = A * B
    matmul_result = A @ B

    norm_A = math.sqrt(np.sum( A ** 2))
    norm_B = math.sqrt(np.sum( B ** 2))

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("\nA + B =\n", add_result)
    print("\nA * B (elementwise) =\n", mult_result)
    print("\nA @ B (matrix product) =\n", matmul_result)
    print(f"\n||A|| = {norm_A: .2f}")
    print(f"||B|| = {norm_B: .2f}")

    screen = turtle.Screen()
    screen.title("Turtle Window")
    pen = turtle.Turtle()
    pen.color("purple")
    pen.pensize(2)

    for _ in range(4):
        pen.forward(100)
        pen.left(90)
        pen.forward(100)

    turtle.done()
    return 0

if __name__ == "__main__":
    sys.exit(main())