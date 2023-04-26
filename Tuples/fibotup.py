#To insert first 9 numbers of a fibonacci series into a tuple
#fibotup.py
#26-11-22
#By Anupam Kanoongo

print("Welcome to the Fibonacci Tuple Maker")
print()
a = int(input("Enter the first number of the fibonacci series : "))
print()
b = int(input("Enter the second number of the fibinacci series : "))
print()

f1, f2, f3 = a,b,0
fibo = ()

fibo += (f1,)
fibo += (f2,)
for i in range(7):
    f3 = f1 +f2
    fibo += (f3,)
    f1, f2 = f2, f3

print(fibo)

##Output
##Welcome to the Fibonacci Tuple Maker
##
##Enter the first number of the fibonacci series : 10
##
##Enter the second number of the fibinacci series : 50
##
##(10, 50, 60, 110, 170, 280, 450, 730, 1180)
