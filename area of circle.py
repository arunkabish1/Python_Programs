from cmath import pi


def areaofcircle():
    radius=int(input("Enter the radius of circle:"))
    area= pi * pow(radius,2)
    print("Area of circle using cmath is %.4f" %area)
    print("Area of circle is",3.14*radius*radius)
areaofcircle()