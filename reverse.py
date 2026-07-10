# Program to count the number of digits using a while loop

num = int(input("Enter a number: "))

# Handle negative numbers
if num < 0:
    num = -num

# Special case for 0
if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1

print("Total number of digits:", count)