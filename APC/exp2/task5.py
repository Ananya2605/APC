n = int(input("Enter a number: "))
reverse = 0

for digit in str(abs(n)):
    reverse = reverse * 10 + int(digit)

if n < 0:
    reverse = -reverse

print("Reversed number =", reverse)