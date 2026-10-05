N = int(input("enter the number:"))
sum_of_digits = 0
while N > 0:
    digit = N % 10
    sum_of_digits += digit
    N //= 10
print("sum of digits:", sum_of_digits)