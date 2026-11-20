#Unit-2B_Task-2_Multiplication_Table.py
N = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{N} x {i} = {N*i}")

# program to print multiplication table of a number using while loop
N = int(input("enter a number: "))
i = 1
while i <= 10:
    print(f"{N} x {i} = {N*i}")
    i += 1