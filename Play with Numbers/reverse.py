#To reverse the number given by the user
#12-9-22
#reverse.py
#By Anupam Kanoongo

print("Welcome to the number reverser")
print()
print("Enter the number to be reversed")
print()

num = int(input())
rn = 0

while num != 0:
    digit = num % 10
    rn = rn * 10 + digit
    num //= 10

print("Reversed Number: ",rn)


##Output
##Welcome to the number reverser
##
##Enter the number to be reversed
##
##1234
##Reversed Number:  4321
