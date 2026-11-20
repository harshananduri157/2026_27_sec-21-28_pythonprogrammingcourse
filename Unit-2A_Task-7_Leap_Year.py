#finding whether the given year is a leap year or not
#Taking the input from th user
year = int(input("Enter the year: "))
if year % 400 == 0:
    print(f"{year} is a leap year")
else:
    if year % 100 == 0:
        print(f"{year} is not a leap year")
    else:
        if year % 4 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")