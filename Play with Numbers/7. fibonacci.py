#To print first N Fibonacci Numbers
#3-9-22
#fibonacci.py
#By Anupam Kanoongo

print("Welcome to the Custom Fibonacci printer")
print()
print("How many Fibonacci Numbers do you want")
print()
n = int (input())

if (n<0):
    print ("Enter a positive number")
    print()
    n = int (input())
else:
    f1, f2 = 0, 1
    if n == 1:
        print (f1)
    elif n == 2:
        print (f1,f2)
    else:
        print (f1,f2, end = ' ')
        for i in range (3, n+1):
            f3 = f1 + f2
            print (f3, end = ' ')
            f1 = f2
            f2 = f3


##Output
##Welcome to the Custom Fibonacci printer
##
##How many Fibonacci Numbers do you want
##
##15
##0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
