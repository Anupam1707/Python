#To genrate a frequency table of elements of a list
#18-11-22
#freqlst.py
#By Anupam Kanoongo

print("Welcome to the Frequency Generator (list)")
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
        if freq > 1:
            print("The Number '",i,"'comes",freq,"times")
        elif freq == 1:
            print("The Number '",i,"'comes",freq,"time")

##Output
##Welcome to the Frequency Generator (list)
##
##Enter the list
##
##[4, 4, 2, 3, 4, 3, 4, 4, 2, 3, 3, 4, 2, 2, 3, 4, 1, 1, 3, 2]
##The Number ' 4 'comes 7 times
##The Number ' 2 'comes 5 times
##The Number ' 3 'comes 6 times
##The Number ' 1 'comes 2 times
