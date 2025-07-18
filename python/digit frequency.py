# Count how many times each digit appears in a number

num = input("Enter a number: ")
frequency = {}

for digit in num:
    if digit.isdigit():
        frequency[digit] = frequency.get(digit, 0) + 1

print("Digit Frequencies:")
for digit, count in frequency.items():
    print(f"{digit} → {count} times")
