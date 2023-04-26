
#To find the highest ans second highest number from n given numbers
#12-9-22
#h&sh.py
#By Anupam Kanoongo

print("Welcome to the Number Sorter 2.0")
print()
print("Enter your numbers now")
print()

i = 1
num = int(input("Number %d = " %i))
h = 0
sh = 0


while num != "end":
    i+=1
    num = int(input("Number %d = " %i))
    if num == 0:
        num = "end"
    elif h == 0:
        h = num
    elif h<num:
        sh = h
        h = num
        

print("The highest number of",i-1,"numbers is ",h,"and second highest is",sh)
    

##Output
##Welcome to the Number Sorter 1.0
##
##Enter your numbers now
##
##Number 1 = 5
##Number 2 = 10
##Number 3 = 15
##Number 4 = 2
##Number 5 = 20
##Number 6 = 25
##Number 7 = 30
##Number 8 = 35
##Number 9 = 49
##Number 10 = 57
##Number 11 = 0
##The highest number of 10 numbers is  57 and second highest is 49
