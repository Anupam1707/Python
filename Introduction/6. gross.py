#To find the gross salary of Amit by his Basic salary
#gross.py
#23-07-2022
#By Anupam Kanoongo 

print("Welcome to the Gross Salary Calculator")
print()
print("Enter your values")
print()
bs = int(input("Enter the Basic Salary of Amit "))

ea = 25/100*bs

hra = 15/100*bs

gross = bs+ea+hra

print("The gross Salary of Amit with Basic Salary",bs,"Earness Allowence",ea,"and House Rent Allowence",hra,"is", gross)

##Output
##Welcome to the Gross Salary Calculator
##
##Enter your values
##
##Enter the Basic Salary of Amit 15000
##The gross Salary of Amit with Basic Salary 15000 Earness Allowence 3750.0 and House Rent Allowence 2250.0 is 21000.0
