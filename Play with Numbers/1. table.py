#To print the table of a number given by user
#3-9-22
#table.py
#By Anupam Kanoongo

print("Welcome to the Table Printer")
print()
print("Enter the Number you want to table of : ")

num = int(input())

for i in range(1,11) :
    print(num,"X",i,"=",num*i)

##Output
##Welcome to the Table Printer
##
##Enter the Number you want to table of : 
##5
##5 X 1 = 5
##5 X 2 = 10
##5 X 3 = 15
##5 X 4 = 20
##5 X 5 = 25
##5 X 6 = 30
##5 X 7 = 35
##5 X 8 = 40
##5 X 9 = 45
##5 X 10 = 50
