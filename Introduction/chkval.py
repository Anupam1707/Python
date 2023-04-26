# To figure out if the input value is a lowercase, uppercase or a digit
#26-08-22
#chval.py
#By Anupam Kanoongo 

print("Welcome to the Value Type Detector")
print()
print("This detector can detect LowerCase, UpperCase, Digit and Mixed Alphabet")
print()
print("Enter any type of value you want to know its category")
print()
a = input("Enter your Value : ")
b =""
if a >= "a" and a<= "z" :
    b = "LowerCase Character"
elif a >= "A"and a<= "Z" :
    b = "UpperCase Character"
elif a >= "0" and a<= "9" :
    b = "Digit"
elif (a >= "a" and a<= "z")and(a >= "A"and a<= "Z") :
    b = "Mixed Character"
else :
    b = ""
print()
print("The given value '",a,"' is a",b)



##Output
##Welcome to the Value Type Detector
##
##This detector can detect LowerCase, UpperCase, Digit and Mixed Alphabet
##
##Enter any type of value you want to know its category
##
##Enter your Value : IT
##
##The given value ' IT ' is a UpperCase Character
