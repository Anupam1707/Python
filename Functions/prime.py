#To check if a number if prime or not using function
#prime.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the Prime Number Checker")
print()

def prime(num):
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

n = int(input("Enter a number : "))
prime(n)


##Output
##Welcome to the Prime Number Checker
##
##Enter a number : 5
##5 is a prime number
