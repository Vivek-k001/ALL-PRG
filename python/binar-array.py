# Creating a binary array (list of 0s and 1s)
binary_array = [0, 1, 1, 0, 1, 0, 1, 1]

# Function to count the number of 1s and 0s
def count_binary_elements(arr):
    count_zeros = arr.count(0)
    count_ones = arr.count(1)
    return count_zeros, count_ones

# Function to invert the binary array (flip 0s to 1s and vice versa)
def invert_binary_array(arr):
    return [1 - bit for bit in arr]

# Testing the functions
zeros, ones = count_binary_elements(binary_array)
print(f"Number of 0s: {zeros}, Number of 1s: {ones}")

inverted_array = invert_binary_array(binary_array)
print(f"Inverted Binary Array: {inverted_array}")
