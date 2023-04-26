#To find all prime numbers between two numbers
#primes.py
#15-9-22
#By Anupam Kanoongo

print("Welcome to the prime number finder")
print()
print("Enter from where you want the numbers from : ")
start = int(input())
print()
print("Enter till which you want the numbers : ")
stop = int(input())

print("Prime numbers between", start, "and", stop, "are:")

for num in range(start, stop + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


##Output
##Welcome to the prime number finder
##
##Enter from where you want the numbers from : 
##1
##
##Enter till which you want the numbers : 
##20
##Prime numbers between 1 and 20 are:
##2
##3
##5
##7
##11
##13
##17
##19
