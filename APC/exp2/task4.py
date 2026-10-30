n = int(input("How many numbers? "))

smallest = int(input("Enter number 1: "))

for i in range(2, n + 1):
    num = int(input("Enter next number: "))

    if num < smallest:
        smallest = num

print("Smallest number =", smallest)