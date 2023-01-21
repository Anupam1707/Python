#To find the sum of the digits of a number
#12-9-22
#sumofdigit.py
#By Anupam Kanoongo

print("Welcome to the Digit Adder")
print()
print("Enter the number to be added")
print()

num = int(input())
sum = 0
temp = num

while num != 0:
    digit = num % 10
    sum = sum + digit
    num //= 10

print("The Sum of the digits of",temp,"is",sum)


##Output
##Welcome to the Digit Adder
##
##Enter the number to be added
##
##1379
##The Sum of the digits of 1379 is 20
