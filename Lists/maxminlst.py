# To find the maximum and minimum values from specified range of a given list
#maxminlst.py
#17-11-22
#By Anupam Kanoongo

mn = 0
mx = 0
lst = [ ]

print("Welcome to the List Analyzer")
print()
print("Enter your list")
print()
ls = eval(input())
print()
a = int(input("Enter the starting index of the range : "))
print()
b = int(input("Enter the ending index of the range : "))
print()

lst = ls[a:b+1]

for i in lst:
    if i > mx:
        mx = i
for j in lst:
    if mn == 0:
        mn = j
    elif j < mn:
        mn = j

print("The Maximum value from the selection is : ",mx,"\nThe Minimum Value from the selection is : ",mn)

##Welcome to the List Analyzer
##
##Enter your list
##
##[1,2,3,4,5,6,7,8,9]
##
##Enter the starting index of the range : 3
##
##Enter the ending index of the range : 7
##
##The Maximum value from the selection is :  8 
##The Minimum Value from the selection is :  4
