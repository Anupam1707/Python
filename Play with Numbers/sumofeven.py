#To find the sum all even numbers between two given numbers
#3-9-22
#sumofeven.py
#By Anupam Kanoongo

print("Welcome to the Custom Even Number adder")
print()
print("Enter the Number from which you want to start the sum")
start = int(input())
print()
print("Enter the number till which you want to end the sum")
stop = int(input())
print()
sum = 0
for i in range(start,stop+1) :
    if i % 2 == 0 :
        sum += i
print("The Sum of Even Numbers between",start,"and",stop,"is",sum)


##Output
##Welcome to the Custom Even Number adder
##
##Enter the Number from which you want to start the sum
##1
##
##Enter the number till which you want to end the sum
##40
##
##The Sum of Even Numbers between 1 and 40 is 420
