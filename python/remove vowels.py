# Remove all vowels from a string

text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
no_vowels = ""

for char in text:
    if char not in vowels:
        no_vowels += char

print("Without vowels:", no_vowels)
