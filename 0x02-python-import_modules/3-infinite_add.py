#!/usr/bin/python3

if __name__ == "__main__":
    """print the addition of all arguments."""
    total = 0
    while True:
        user_input = input("Enter a number (or 'end' to finish): ")
        if user_input == "end":
            break
        total += int(user_input)

    print(total)
