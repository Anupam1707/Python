# To find the area of triangle and the circumference of the circle
# areaandperimeter.py
# 23-07-2022
# By Anupam Kanoongo

print("Welcome to the Area and Perimeter Calculator")
print()
print("Enter your values")
print()
Base = int(input("Enter the Base of Triangle "))
Height = int(input("Enter the Height of Triangle "))
Radius = int(input("Enter the Radius of Circle "))

Area = 1/2*Base*Height

Circumference = 2*3.14*Radius

print("The area of the triangle with base", Base,"and height", Height,"is",Area ,
      "and the circumference of the circle of radius",Radius,"is",Circumference)

##Output
##Welcome to the Area and Perimeter Calculator
##
##Enter your values
##
##Enter the Base of Triangle 10
##Enter the Height of Triangle 5
##Enter the Radius of Circle 15
##The area of the triangle with base 10 and height 5 is 25.0 and the circumference of the circle of radius 15 is 94.2
