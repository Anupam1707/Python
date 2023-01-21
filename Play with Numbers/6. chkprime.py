#To check if a number is prime or not
#3-9-22
#chkprime.py
#By Anupam Kanoongo

print("Welcome to the Prime Number Checker")
print()
print("Enter a number to be checked")
print()

num = int(input())

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")


##Output
##Welcome to the Prime Number Checker
##
##Enter a number to be checked
##
##10
##10 is not a prime number
##2 times 5 is 10
