#To find the min and max number from n numbers in tuple
#tupmaxmin.py
#26-11-22
#By Anupam Kanoongo

print("Welcome to the Tuple Max and Min Finder")
print()
n = int(input("Enter how many numbers you want to insert in the tuple : "))
mx, mn, num = 0, 111111111111110,0
tup = ()

for i in range(1,n+1):
    num = int(input("Number %d : " %i))
    tup += (num,)
    if num > mx:
        mx = num
    elif num < mn:
        mn = num

print()
print("The Maximum Number Entered is : ",mx)
print("The Minimum Number Entered is : ",mn)
print("The Resultant Tuple is : ",tup)

##Output
##Welcome to the Tuple Max and Min Finder
##
##Enter how many numbers you want to insert in the tuple : 10
##Number 1 : 6
##Number 2 : 23
##Number 3 : 6
##Number 4 : 7
##Number 5 : 5
##Number 6 : 67
##Number 7 : 8
##Number 8 : 6
##Number 9 : 6
##Number 10 : 74
##
##The Maximum Number Entered is :  74
##The Minimum Number Entered is :  5
##The Resultant Tuple is :  (6, 23, 6, 7, 5, 67, 8, 6, 6, 74)
