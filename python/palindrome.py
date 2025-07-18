num =int(input("enter a number:"))
original = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num//10

if original == reversed_num:
   print("its a palindrome number ")
else:
   print("its not a palindrome number ")