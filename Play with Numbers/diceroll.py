#To roll a dice n times and count how much times each number is appearing
#diceroll.py
#15-9-22
#By Anupam Kanoongo

import random
from random import *

print("Welcome to the Dice Roller")
print()
print("Enter how many times do you want to roll the dice")
print()
n = int(input())
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

for i in range(0,n):

    num = randrange(1,7)

    if num == 1:
        n1+=1
    elif num == 2:
        n2+=1
    elif num == 3:
        n3+=1
    elif num == 4:
        n4+=1
    elif num == 5:
        n5+=1
    elif num == 6:
        n6+=1

print("On Rolling a dice",n,"times, the result is as follows : ")
print("Number 1 appeared",n1,"times")
print("Number 2 appeared",n2,"times")
print("Number 3 appeared",n3,"times")
print("Number 4 appeared",n4,"times")
print("Number 5 appeared",n5,"times")
print("Number 6 appeared",n6,"times")


##Output
##Welcome to the Dice Roller
##
##Enter how many times do you want to roll the dice
##
##25
##On Rolling a dice 25 times, the result is as follows : 
##Number 1 appeared 3 times
##Number 2 appeared 2 times
##Number 3 appeared 2 times
##Number 4 appeared 6 times
##Number 5 appeared 8 times
##Number 6 appeared 4 times

