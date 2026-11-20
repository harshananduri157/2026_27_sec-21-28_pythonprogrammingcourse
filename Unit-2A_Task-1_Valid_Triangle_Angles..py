angle_1=int(input("Enter an angle: "))
angle_2=int(input("Enter an angle: "))
angle_3=int(input("Enter an angle: "))
if angle_1 > 0 and angle_2 > 0 and angle_3 > 0 and angle_1 + angle_2 + angle_3 ==180:
    print(f"The triangle with angles {angle_1}, {angle_2} and {angle_3} is valid")
else:
    print(f"The triangle with angles {angle_1}, {angle_2} and {angle_3} is Not Valid")
