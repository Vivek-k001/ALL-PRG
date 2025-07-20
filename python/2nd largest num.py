# Find second largest number without sorting

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("No second largest number found.")
else:
    print("Second largest number is:", second)
