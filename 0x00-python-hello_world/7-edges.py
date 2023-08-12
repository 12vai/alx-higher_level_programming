#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print("word_first_3:", word_first_3)
print("word_last_2:", word_last_2)
print("middle_word:", middle_word)

word = word_last_2 + word_first_3
print("word:", word)
print("first_letter:", word[0])
print("last_letter:", word[-1])
