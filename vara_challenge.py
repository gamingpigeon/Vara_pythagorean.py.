ask=(input("give me 3 numbers and i will tell you what kind of triangle it is respond by  OK "))

a=float(input("enter the length of the first side: "))

b=float(input("enter the length of the second side: "))

c=float(input("enter the length of the second side: "))

if (a+b<c):
    print("this is not a triangle")
elif ((a**2)+(b**2) ==(c**2)):
    print("this is a right triangle")
elif ((a**2)+(b**2)<(c**2)):
    print("this is a obtuse triangle")
elif ((a**2)+(b**2)>(c**2)):
    print("this is an acute triangle")