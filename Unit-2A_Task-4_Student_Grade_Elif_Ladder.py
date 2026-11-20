#program to grade a students marks
#taking marks from the user
Marks = int(input("Enter the marks out of 100: "))
if Marks >= 90:
    print(f"Grade: A (marks = {Marks})")
elif 80 <= Marks < 90:
    print(f"Grade: B (marks = {Marks})")
elif 70 <= Marks < 80:
    print(f"Grade: C (marks = {Marks})")
else:
    print(f"Grade: D (marks = {Marks})")