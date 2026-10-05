# program to count the number of digits in a number using while loop
N = int(input("enter the number:"))
count = 0
while N > 0:
    N //= 10
    count += 1
print("number of digits:", count)