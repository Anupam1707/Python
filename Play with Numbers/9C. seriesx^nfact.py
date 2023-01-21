#To find the sum of first x^n numbers
#9-9-22
#seriesx^nfact.py
#By Anupam Kanoongo

print("Welcome to the X^n/n! Number Adder")
print()
print("Enter how many terms you want to add")
print()
n=int(input())
print("Enter the value of x")
print()
x=int(input())
print()
sum=0
fact=1
xv=0
for i in range(1,n+1):
    fact= fact*i
    f = (x**i)/(fact)
    sum = sum + f
    print(f)

print("\n")
print("The Sum of first n numbers is",sum)


##Output
##Welcome to the X^n/n! Number Adder
##
##Enter how many terms you want to add
##
##10
##Enter the value of x
##
##2
##
##2.0
##2.0
##1.3333333333333333
##0.6666666666666666
##0.26666666666666666
##0.08888888888888889
##0.025396825396825397
##0.006349206349206349
##0.0014109347442680777
##0.0002821869488536155
##
##
##The Sum of first n numbers is 6.388994708994708
