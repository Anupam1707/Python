# To merge two sorted lists
# 8-11-22
#mg2lst.py
#By Anupam Kanoongo

print("Welcome to the Sorted list merger")
print()
print("Enter your first list")
print()
l1 = eval(input())
print()
print("Enter your second list")
print()
l2 = eval(input())
print()

ln1 = len(l1)

ln2 = len(l2)

a = 0
b = 0
l = 0
r = ""
nl = [ ]
lst = [ ]
n = 1

if ln1 == ln2:
    pass
elif ln1 > ln2:
    l = ln1-ln2
    ln1 = ln1-l
elif ln1 < ln2:
    l = ln2-ln1
    ln2 = ln2-l

for i in range(ln1):
    if l1[i] == l2[i]:
        a = l1[i]
        b = l2[i]
        nl += [a,b]
        
    elif l1[i] > l2[i]:
        a = l1[i]
        b = l2[i]
        nl += [b,a]
        lst += [a]
        
    elif l1[i] < l2[i]:
        a = l1[i]
        b = l2[i]
        nl += [a,b]

if l == 0:
    pass
else :
    if ln1 > ln2:
        l1 -= lst
        print(l1)
        nl += l1

print(nl)

##Welcome to the Sorted list merger
##
##Enter your first list
##
##[1,3,5,7]
##Enter your second list
##
##[2,4,6,8]
##[1, 2, 3, 4, 5, 6, 7, 8]