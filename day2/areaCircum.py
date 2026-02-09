import math

a = int(input("Enter radius of circle: "))
b = int(input("Enter length of rectangle: "))
c = int(input("Enter breadth of rectangle: "))

print("Area of circle:", math.pi * a * a )
print("Circumference of circle:", math.pi * a * 2)
print("Area of rectangle:", b * c)
print("Perimeter of rectangle:", 2 * b * c)