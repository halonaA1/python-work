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
        canvas.create_text(self.position[0], self.position[1], text=self.text, font = ("Ariel", 14), fill= "brown")

    def main():
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])

        add_result = A + B
        mult_result = A * B
        matmul_result = A @ B

        norm_A = math.sqrt(np.sum( A ** 2))
        norm_B = math.sqrt(np.sum( B ** 2))

        root = tk.Tk()
        root.title("Numpy + Math + Canvas + Text")
        canvas = tk.Canvas(root, width=800, height=600, bg="white")
        canvas.pack()

        t1 = TextShape("Addition", f"A + B =\n {add_result}", position=(200, 100))
        t2 = TextShape("Elementwise Multiplication", f"A *B =\n {mult_result}", position=(200, 150))
        t3 = TextShape("Matrix Product", f"A @ B = \n {matmul_result}", position=(200, 200))
        t4 = TextShape("Norm", f"||A|| = {norm_A}", position=(200, 300))
        t5 = TextShape("Norm", f"||B|| = {norm_B}", position=(200, 400))

        for t in [t1, t2, t3, t4, t5]:
            t.draw(canvas)

        screen = turtle.Screen()
        screen.title("Turtle Window")
        pen = turtle.Turtle()
        pen.color("Black")
        pen.pensize(3)

        for _ in range(3):
            pen.forward(100)
            pen.left(90)

        root.mainloop()

        return 0

    if __name__ == "__main__":
        sys.exit(main())