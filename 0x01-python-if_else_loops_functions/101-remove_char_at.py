#!/usr/bin/python3
def remove_char_at(s, n):
    new_str = ""
    for i in range(len(s)):
        if i != n:
            new_str += s[i]
    return new_str

# Example usage
original_str = "example"
position_to_remove = 2
result_str = remove_char_at(original_str, position_to_remove)
print(result_str)
