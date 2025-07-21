# Count words, digits, and special characters

import string

text = input("Enter a sentence: ")
word_count = len(text.split())
digit_count = 0
special_count = 0

for char in text:
    if char.isdigit():
        digit_count += 1
    elif char in string.punctuation:
        special_count += 1

print("Words:", word_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)
