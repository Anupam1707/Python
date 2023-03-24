#To check if a given number os perfect or not
#perfnum.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the Perfect Number Checker")
print()

def perf(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is a perfect number")
               print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is not a perfect number")
           
    else:
       print(num,"is a perfect number")

n = int(input("Enter a Number : "))
perf(n)

##Output
##Welcome to the Perfect Number Checker
##
##Enter a Number : 456
##456 is a perfect number
##2 times 228 is 456
