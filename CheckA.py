ang1=float(input("Enter the First angle:"))
ang2=float(input("Enter the Second angle:"))
ang3=float(input("Enter the Third angle:"))
if ang1+ang2+ang3==180:
    if ang1==ang2==ang3:
        print("It is Valid.")
        print("The angle is Equilateral Angle")
    elif ang1!=ang2!=ang3:
        print("The angle is Scalene Angle")
    else:
        print("The angle is Isosceles Angle")
else:
    print("Invalid Angle")