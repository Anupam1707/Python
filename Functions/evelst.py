#To print all even number from a list
#evelst.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the Even Number Finder")
print()

def eve(ls):
    lst = []
    for i in ls:
        if i%2 == 0:
            lst.append(i)

    return lst

l = eval(input("Enter a list : "))
r = eve(l)

print("Original List : ",l)
print("Even Number from the List : ",r)

##Output
##Welcome to the Even Number Finder
##
##Enter a list : [1,2,3,4,5,6,7,8]
##Original List :  [1, 2, 3, 4, 5, 6, 7, 8]
##Even Number from the List :  [2, 4, 6, 8]
