#To shift the index places of elemenys of a list
#sftlst.py
#16-8-22
#By Anupam Kanoongo

print("Welcome to the list shifter")
print()
print("Enter your list")
print()

ls = eval(input())
lst = ls[-1]

for i in range(-1,-len(ls),-1):
    ls[i]=ls[i-1]

ls[0]=lst
print(ls)

##Output
##Welcome to the list shifter
##
##Enter your list
##
##[1,2,3,4,5,6,7]
##[7, 1, 2, 3, 4, 5, 6]
