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

def get_the_matrix(name):
    rows = int(input(f"Number of rows for matrix{name}: "))
    cols = int(input(f"Number of columns for matrix{name}:"))
    print(f"Enter elements for matrix{name} row by row: ")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row{i + 1}: ").split()))
        while len(row) != cols:
            print(f"Enter exact values.")
            row = list(map(float, input(f"Row{1 + 1}: ").split()))
        elements.append(row)
    return np.array(elements)

def main():
    A = get_the_matrix("A")
    B = get_the_matrix("B")

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