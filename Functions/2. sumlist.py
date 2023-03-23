#To sum up the elements of a list
#sumlist.py
#23-3-23
#By Anupam Kanoongo

print("The List Sum Finder")
print()

def sumlst(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

ls = eval(input("Enter a List : "))

r = sumlst(ls)

print()
print("The Sum of all elements of the above list is",r)

##Output
##The List Sum Finder
##
##Enter a List : [1,2,3,4,5,6]
##
##The Sum of all elements of the above list is 21
