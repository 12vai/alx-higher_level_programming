#!/usr/bin/python3

a = 10
b = 5

import calculator_1 as calc

result_add = calc.add(a, b)
result_subtract = calc.subtract(a, b)
result_multiply = calc.multiply(a, b)
result_divide = calc.divide(a, b)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
