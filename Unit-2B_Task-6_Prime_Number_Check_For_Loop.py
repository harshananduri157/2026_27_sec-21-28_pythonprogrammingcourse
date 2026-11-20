#python program to check whether a given number is prime or not using for looppython program to check whether a given number is prime or not using for loop(assume the input number is between 1 and 100)
N = int(input("Enter a number between 1 and 100: "))
is_prime = True
for i in range(2, N):
    if N % i == 0:
        is_prime = False
        break
if is_prime and N > 1:
    print(f"{N} is a prime number.")
else:
    print(f"{N} is not a prime number.")
