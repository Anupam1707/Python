#To find the factorial of given number
#3-9-22
#fact.py
#By Anupam Kanoongo

print("Welcome to the Factorial Finder")
print()
print("Enter the you want the factorial of")
print()
num = int(input())
fact = 1
for i in range(1,num+1) :
    fact = fact*i
print("The Factorial of",num,"is",fact)


##Output
##Welcome to the Factorial Finder
##
##Enter the you want the factorial of
##
##5
##The Factorial of 5 is 120
