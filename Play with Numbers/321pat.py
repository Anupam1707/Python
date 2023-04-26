#To print pattern 1-12-123-1234
#14-9-22
#321pat.py
#By Anupam Kanoongo

print("Welcome to the Pattern Maker (321)")
print()
print("Enter the number of rows to print")
print()

n = int(input())

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("\n")
 

##Output
##Welcome to the Pattern Maker (123)
##
##Enter the number of rows to print
##
##15
##Welcome to the Pattern Maker (321)
##
##Enter the number of rows to print
##
##15
##15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
##
##14 13 12 11 10 9 8 7 6 5 4 3 2 1 
##
##13 12 11 10 9 8 7 6 5 4 3 2 1 
##
##12 11 10 9 8 7 6 5 4 3 2 1 
##
##11 10 9 8 7 6 5 4 3 2 1 
##
##10 9 8 7 6 5 4 3 2 1 
##
##9 8 7 6 5 4 3 2 1 
##
##8 7 6 5 4 3 2 1 
##
##7 6 5 4 3 2 1 
##
##6 5 4 3 2 1 
##
##5 4 3 2 1 
##
##4 3 2 1 
##
##3 2 1 
##
##2 1 
##
##1 

