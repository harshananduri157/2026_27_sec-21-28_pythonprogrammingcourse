# elif ladder example
grade = input("Enter your grade (A, B, C, D, F): ")

if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good!")
elif grade == "C":
    print("Average.")
elif grade == "D":
    print("Below Average.")
elif grade == "F":
    print("Fail.")
else:
    print("Invalid grade.")