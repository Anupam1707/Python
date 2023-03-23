#To multiply the elements of a list using a function
#mullist.py
#23-3-23
#By Anupam Kanoongo

print("The List Product Finder")
print()

def mullst(lst):
    mul = 1
    for i in lst:
        mul *= i
    return mul

ls = eval(input("Enter a List : "))
r = mullst(ls)

print()
print("The Sum of all elements of the above list is",r)

##Output
##The List Sum Finder
##
##Enter a List : [1,2,3,4,5,6]
##
##The Sum of all elements of the above list is 720
