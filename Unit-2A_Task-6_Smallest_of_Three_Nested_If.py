#python program that uses Nested if-else statement
#finding Smallest numbers among the given three numbers
#taking values from user
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
#Comparing A and B 
if A <= B:
    if A <= C:
        Smallest = A
        print(f"Smallest = {Smallest}")
    else:
        Smallest = C
        print(f"Smallest = {Smallest}")
else:
    if B <= C:
        Smallest = B
        print(f"Smallest = {Smallest}")
    else:
        Smallest = C
        print(f"Smallest = {Smallest}")