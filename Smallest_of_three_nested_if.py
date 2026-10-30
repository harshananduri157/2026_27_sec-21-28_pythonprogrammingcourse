# print the smallest of three numbers using nested if-else
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a < b:
    if a < c:
        print("The smallest number is:", a)
    else:
        print("The smallest number is:", c)
else:
    if b < c:
        print("The smallest number is:", b)
    else:
        print("The smallest number is:", c)