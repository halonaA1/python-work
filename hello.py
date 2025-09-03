import sys

def main():
    name = input("What is your name?")
    age = int(input("what is your age?"))
    print(f"Hello{name}! In {2022 + (120 - age)}you will be 120 years old . Tough luck!")
    return 0

if __name__ == "__main__":
 sys.exit(main())
