#taking input from the user
total_number = int(input("Enter the total numbers: "))

number = float(input("Enter the number: "))

#using for loop
for count in range(total_number):
    num = float(input("Enter number: "))
    if num > number:
        number = num

print(f"largest among {total_number} numbers is {number}")