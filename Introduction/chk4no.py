# To compare four numbers and print the biggest
#25-08-22
#chk4no.py
#By Anupam Kanoongo 

print("Welcome to the Number Comparing Program")
print()
n1 = int(input("Enter First Number "))
print()
n2 = int(input("Enter Second Number "))
print()
n3 = int(input("Enter Third Number "))
print()
n4 = int(input("Enter Fourth Number "))
print()

if n1>n2 :
    if n1>n3 :
        if n1>n4 :
            print("The Biggest of",n1,n2,n3,n4,"is",n1)

        else :
            print("The Biggest of",n1,n2,n3,n4,"is",n4)

    else :
        if n3>n4 :
            print("The Biggest of",n1,n2,n3,n4,"is",n3)

        else :
            print("The Biggest of",n1,n2,n3,n4,"is",n4)
else :
    if n2>n3 :
        if n2>n4 :
            print("The Biggest of",n1,n2,n3,n4,"is",n2)

        else :
            print("The Biggest of",n1,n2,n3,n4,"is",n4)

    else :
        if n3>n4 :
            print("The Biggest of",n1,n2,n3,n4,"is",n3)

        else :
            print("The Biggest of",n1,n2,n3,n4,"is",n4)


##Output
##Welcome to the Number Comparing Program
##
##Enter First Number 10
##
##Enter Second Number 40
##
##Enter Third Number 43
##
##Enter Fourth Number 80
##
##The Biggest of 10 40 43 80 is 80
