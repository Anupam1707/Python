#To find the sum of first x^n numbers
#9-9-22
#seriesx^n.py
#By Anupam Kanoongo

print("Welcome to the X^n NUmber Adder")
print()
print("Enter how many terms you want to add")
print()
n = int(input())
print("ENter the value of x")
print()
x = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + ((-(-1)**i)*(x**(i-1)))
    print((-(-1)**i*x**(i-1)), end= " ")
print("\n")
print("The Sum of first n numbers is",sum)


##Output
##Welcome to the X^n NUmber Adder
##
##Enter how many terms you want to add
##
##5
##ENter the value of x
##
##2
##1 -2 4 -8 16 
##
##The Sum of first n numbers is 11
