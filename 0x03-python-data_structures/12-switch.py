#!/usr/bin/python3
def switch(a, b):
    # Your code here
    a, b = b, a
    return a, b

a = 5
b = 10
a, b = switch(a, b)
print("a =", a)
print("b =", b)
