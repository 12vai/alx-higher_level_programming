#!/usr/bin/python3

str = "python is an interpreted, interactive, object_oriented programming\
        language that combines remarkable power with very clear syntax"

str = str[39:66] + str[106:112] + str[:6]

word_first_3 = str[:3]
word_last_2 = str[-2:]
middle_word = str[1:-1]

print(f"word_first_3: {word_first_3}")
print(f"word_last_2: {word_last_2}")
print(f"middle_word: {middle_word}")

word = word_last_2 + word_first_3
print(f"word: {word}")
print(f"first_letter: {word[0]}")
print(f"last_letter: {word[-1]}")

reversed_word = word[::-1]
print(f"reversed_word: {reversed_word}")
print(f"word length: {len(word)}")
