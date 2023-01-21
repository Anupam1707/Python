#To take some values and add until 0 is entered
#3-9-22
#adduntil0.py
#By Anupam Kanoongo

print("Welcome to the Addidng Machine")
print()
print("Now repeatedly you will be asked to enter numbers")
print()
print("These numbers will be added until you enter a '0'")
print()
print("Enter the maximum count of number you want to be added")
stop = int(input())
print()

sum = 0
print("Please Enter Numbers\n")
for i in range(1,stop+1):
    num = int(input("Number %d = " %i))

    if num == 0:
        break
    sum = sum + num

print("The Sum of the given",stop,"Numbers = ", sum)



##Output
##Welcome to the Addidng Machine
##
##Now repeatedly you will be asked to enter numbers
##
##These numbers will be added until you enter a '0'
##
##Enter the maximum count of number you want to be added
##10
##
##Please Enter Numbers
##
##Number 1 = 1
##Number 2 = 2
##Number 3 = 3
##Number 4 = 4
##Number 5 = 5
##Number 6 = 6
##Number 7 = 7
##Number 8 = 8
##Number 9 = 9
##Number 10 = 0
##The Sum of the given 10 Numbers =  45
