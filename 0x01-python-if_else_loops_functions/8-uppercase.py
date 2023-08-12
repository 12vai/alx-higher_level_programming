#!/usr/bin/python3
def uppercase(str):
    for char in str:
        lowercase_ascii = ord(char)
        uppercase_ascii = lowercase_ascii - 32 if 97 <= lowercase_ascii <= 122 else lowercase_ascii
        print("{:c}".format(uppercase_ascii), end='')
    print()
uppercase("hello")
