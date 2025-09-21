import sys

def main():
    word = input("Word: ")
    print(f"{word= }")
    print("The word is %s." % word)
    print(f"The word is{word} of length{len(word)}.")
    character_count = dict()
    for letter in word:
        print(f"{letter = }")
        if letter not in character_count:
            character_count[letter] = word.count(letter)
        else:
            character_count[letter] = character_count[letter] + 1
    return 0

if __name__ == "__main__":
    sys.exit(main())

