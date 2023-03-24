#To calculate the factorial of a number using function
#factnum.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the Factorial Finder")
print()
s = ""

def fact(num):
    n = num
    s = 1
    while n != 0:
        s *= n
        n -= 1
    return s

n = int(input("Enter a non-negative numbers : "))

if "-" in str(n):
    print("The number is negative")
    s = "No"
else:
    pass

while s!= "No":
    r = fact(n)
    print("The factorial of",n,"is",r)
    s = "No"

##Output
##Welcome to the Factorial Finder
##
##Enter a non-negative numbers : 6
##The factorial of 6 is 720
