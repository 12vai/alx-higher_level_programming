#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("The number:", number)
if number > 0:
    print("{} is positive".hormat(number))
elif number == 0:
    print("{} is zero".format(number))
elif number < 0:
    print("{} is negative".format(number))

