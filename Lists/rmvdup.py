#To genrate a frequency table of elements of a list
#18-11-22
#rmvldup.py
#By Anupam Kanoongo

print("Welcome to the Duplicate remover (list)")
print()
print("Enter the list")
print()
ls = eval(input())
freq = 0
lst = [ ]

for i in ls:
    while i not in lst:
        freq = ls.count(i)
        lst.append(i)
print()
print(lst)

##Output
##Welcome to the Duplicate remover (list)
##
##Enter the list
##
##[4, 4, 2, 3, 4, 3, 4, 4, 2, 3, 3, 4, 2, 2, 3, 4, 1, 1, 3, 2]
##
##[4, 2, 3, 1]
