#To print the sum of n natural numbers
#3-9-22
#sumofn.py
#By Anupam Kanoongo

print("Welcome to the Custom Natural Number Adder")
print()
print("Enter the Number till which you want the sum of")
print()
num = int(input())

if num <= 0 :
    print("Error","\nPlease Enter a Positive Number")
    print()
    print("Enter the Number till which you want the sum of")
    print()


    num = int(input())
    sum = 0
    for i in range(num+1):
      sum+=i
    print(sum)
else :
    sum = 0
    for i in range(num+1) :
        sum+=i
    print("The Sum of Numbers from 0 to",num,"is",sum)

##Output
##Welcome to the Custom Natural Number Adder
##
##Enter the Number till which you want the sum of
##
##25
##The Sum of Numbers from 0 to 25 is 325

