#To find the sum of first n odd numbers
#9-9-22
#sumofnodd.py
#By Anupam Kanoongo

print("Welcome to the Odd Number Adder")
print()
print("Enter how many odd terms you want add")
print()
n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum +((2*i)-1)
    print(2*i-1, end=" ")
print("\n")
print("The Sum of first n odd numbers is",sum)


##Output
##Welcome to the Odd Number Adder
##
##Enter how many odd terms you want add
##
##10
##1 3 5 7 9 11 13 15 17 19 
##
##The Sum of first n odd numbers is 100
