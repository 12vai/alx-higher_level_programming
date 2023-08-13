#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return (my_list)

my_list = [1, 2, 3, 4, 5]
print(replace_in_list(my_list, 1, 8))
print(replace_in_list(my_list, 3, 9))
print(replace_in_list(my_list, 5, 10))
