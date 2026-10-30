n = int(input("Enter a number: "))
original = n
reverse = 0

for digit in str(n):
    reverse = reverse * 10 + int(digit)

if original >= 0 and original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")