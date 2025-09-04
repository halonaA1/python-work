#d_squared = ...

import sys
def main():

 # a = (x1, y1, z1)
   x1 = float(input("x1: "))
   y1 = float(input("y1: "))
   z1 = float(input("z1:"))
  # b = ( x2, y2, z2)
   x2 = float(input("x2: "))
   y2 = float(input("y2:"))
   z2 = float(input("z2: "))
   print(type(x1))
   d_squared = (x1 - x2) **2 + (y1 - y2) **2 + (z1 - z2) ** 2
   print(f"{d_squared = }")
   return 0


if __name__ == "__main__":
    sys.exit(main())