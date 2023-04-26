#To find all perfect numbers between two numbers
#pperfnum.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the Perfect Number Finder")
print()

def perf(n1,n2):
    for i in range(n1,n2+1):
        if i > 1:
           for j in range(2,i):
               if (i % j) == 0:
                   print("Perfect Number : ",i)
                   break
               else:
                       pass
               
        else:
           print("Perfect Number : ",i)
       
n1 = int(input("Enter Starting Number : "))
print()
n2 = int(input("Enter Ending Number : "))
print()

perf(n1,n2)


##Output
##Welcome to the Perfect Number Finder
##
##Enter Starting Number : 3
##
##Enter Ending Number : 19
##
##Perfect Number :  4
##Perfect Number :  6
##Perfect Number :  8
##Perfect Number :  9
##Perfect Number :  10
##Perfect Number :  12
##Perfect Number :  14
##Perfect Number :  15
##Perfect Number :  16
##Perfect Number :  18
