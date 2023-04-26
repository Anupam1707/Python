#To find the max of three numbers using a function
#max3.py
#23-3-23
#By Anupam Kanoongo

print("Welcome to the Max Finder")
print()

def mx(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            mx = n1
        else :
            mx = n3
    else :
        if n2 > n3:
            mx = n2
        else:
            mx = n3

    return mx

tp = ()
for i in range(1,4):
    n = int(input("Number %d : "  %i))
    tp += (n,)

a, b, c = tp

r = mx(a, b, c)

print()
print("The Maximum Value from the given numbers is",r)

##Output
##Welcome to the Max Finder
##
##Number 1 : 5
##Number 2 : 10
##Number 3 : 3
##
##The Maximum Value from the given numbers is 10
