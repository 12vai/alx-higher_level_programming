#!/usr/bin/python3

import sys

def add_arguments():
    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    return total

def add_user_inputs():
    total = 0
    while True:
        user_input = input("Enter a number (or 'end' to finish): ")
        if user_input == "end":
            break
        total += int(user_input)
    return total

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Add command-line arguments")
    print("2. Add user inputs")
    
    option = input("Enter the option number: ")
    
    if option == "1":
        total = add_arguments()
    elif option == "2":
        total = add_user_inputs()
    else:
        print("Invalid option")
        sys.exit(1)
    
    print("Total:", total)
