#!/usr/bin/python3
def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Example usage
power_result = pow(2, 3)
print(power_result)
