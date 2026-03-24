# WAF to calculate diameter and area of circle using user defined values.

def circleCalc():
    rad = int(input("Enter the radius of the circle: "))
    
    diameter = rad * 2
    print("The diameter of the circle with radius", rad, "=", diameter)
    
    area = 3.14 * rad * rad
    print("The area of the circle with radius", rad, "=", area)
    
circleCalc()