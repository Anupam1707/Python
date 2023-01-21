#To find the lowest ans second lowest number from n given numbers
#12-9-22
#l&sl.py
#By Anupam Kanoongo

print("Welcome to the Number Sorter 1.0")
print()
print("Enter your numbers now")
print()

i = 1
num = int(input("Number %d = " %i))
l = 0
sl = 0


while num != "end":
    i+=1
    num = int(input("Number %d = " %i))
    if num == 0:
        num = "end"
    elif l == 0:
        l = num
    elif l>num:
        sl = l
        l = num
        

print("The lowest number of",i-1,"numbers is ",l,"and second lowest is",sl)
    

##Output
##Welcome to the Number Sorter 1.0
##
##Enter your numbers now
##
##Number 1 = 8
##Number 2 = 6
##Number 3 = 4
##Number 4 = 2
##Number 5 = 1
##Number 6 = 0
##The lowest number of 5 numbers is  1 and second lowest is 2
