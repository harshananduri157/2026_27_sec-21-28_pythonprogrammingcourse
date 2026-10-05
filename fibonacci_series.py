# program to print fibonacci series upto N terms using for loop
N = int(input("enter the number:"))
a, b = 0, 1
for i in range(N):
    print(a)
    nxt = a + b
    a = b
    b = nxt