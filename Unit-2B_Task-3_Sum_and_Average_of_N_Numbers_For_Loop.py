#taking input form the user
Enter_total_numbers= int(input("Enter how many numbers: "))

total_value = 0

for count in range(Enter_total_numbers):
    number = float(input("Enter a number: "))
    total_value = total_value + number

average = total_value/ Enter_total_numbers

print(f"Sum of {Enter_total_numbers} numbers is {total_value}")
print(f"Average of {Enter_total_numbers} numbers (sum {total_value}) is {average}")