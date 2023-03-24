#To fetch all the unique elements of a list
#unique.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the Unique Element Finder")
print()

def unique(ls):
    lst = []
    for i in ls:
        while i not in lst:
            lst.append(i)
    return lst

l = eval(input("Enter a list : "))
r = unique(l)

print("Original : ",l)
print("Unique : ",r)


##Output
##Welcome to the Unique Element Finder
##
##Enter a list : [1,1,2,2,3,3,3,5,5,5,5]
##Original :  [1, 1, 2, 2, 3, 3, 3, 5, 5, 5, 5]
##Unique :  [1, 2, 3, 5]
