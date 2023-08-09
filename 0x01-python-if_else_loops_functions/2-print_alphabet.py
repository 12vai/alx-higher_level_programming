#!/usr/bin/python3
# 2-print_alphabet .py

"""print the alphabet in lowercase, not followed by a new line,"""
for char in range(ord('a'), ord('z')+1):
    print(chr(char), end='')

