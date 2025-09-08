import sys

def main():
    number_list = [8, 3, 2, 6, 12, 7, 14, 332, 72, 9, ]
    for number in number_list:
        if number == 12:
            break
        square = number ** 2
        print(square)

if __name__ == "__main__":
    sys.exit(main())