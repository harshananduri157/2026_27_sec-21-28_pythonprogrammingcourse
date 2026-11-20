#python program that uses Nested if-else statement
#finding Largest numbers among the given three numbers
#taking values from user
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
#Comparing A and B 
if A >= B:
    if A >= C:
        largest = A
        print(f"largest = {largest}")
    else:
        largest = C
        print(f"largest = {largest}")
else:
    if B >= C:
        largest = B
        print(f"largest = {largest}")
    else:
        largest = C
        print(f"largest = {largest}")