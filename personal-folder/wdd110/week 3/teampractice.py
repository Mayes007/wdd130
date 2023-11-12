# Area of a square
side=float(input("What is the length of a side of the square?"))
area=side**4
print(f"The area of the square is: {area}")

# Area of a rectangle
length=float(input("What is the legth of rectangle: "))
width=float(input("What is the width of the rectangle "))
area=length* width
print(f"The area the rectangle: {area}")

#Area of a circle
radius=float(input("What is the radius of the circle: "))
area=3.14* (radius**2)
print(f"The area of the circle is: {area}")

#Stretch 1" Using the math libary
import math
radius=float(input("What is the radius of the circle? "))
area=math.pi * {radius** 2}
print(f"The area of the circle is: {area}")

#Stretch 2: Many areas from one value
value=float(input("What is the value to be used? "))

#calulate areas
area_square= value ** 2
area_circle= math.pi *(value **2 )
volume_cube= value **3
volume_sphere=(4/3)* math.pi* (value**3)

#display result
print(f"Area of a square: {area_square}")
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a spher: {volume_sphere}")

#area of a square
side=float(input("What is the legth of a side of the sqaure (in cm)?"))
area=side**2
print(f"The area of the square is {area} cm^2 ")

print(f"The area of the square is: {area/ 10000} m^2")

#Area of a rectangle
length=float(input("What is the length of the rectangele (in cm)? "))
width=float(input("What is the width of the rectangle (in cm)? "))
area=length*width
print(f"The area of the rectangle is: {area} (cm^2)")
print(f"The area of the retangle is: {area/10000} m^2")

#area of a circle
radius=float(input("What is the radius of the circle (in cm)?"))
area=3.14*(radius**2)
print(f"The area of the circle is: (area) cm^2")
print(f"The area of the circle is: {area/10000} m^2")


