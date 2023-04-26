#To print pattern 1-12-123-1234
#14-9-22
#123pat.py
#By Anupam Kanoongo

print("Welcome to the Pattern Maker (123)")
print()
print("Enter the number of rows to print")
print()

n = int(input())

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("\n")
 

##Output
##Welcome to the Pattern Maker (123)
##
##Enter the number of rows to print
##
##15
##1 
##
##1 2 
##
##1 2 3 
##
##1 2 3 4 
##
##1 2 3 4 5 
##
##1 2 3 4 5 6 
##
##1 2 3 4 5 6 7 
##
##1 2 3 4 5 6 7 8 
##
##1 2 3 4 5 6 7 8 9 
##
##1 2 3 4 5 6 7 8 9 10 
##
##1 2 3 4 5 6 7 8 9 10 11 
##
##1 2 3 4 5 6 7 8 9 10 11 12 
##
##1 2 3 4 5 6 7 8 9 10 11 12 13 
##
##1 2 3 4 5 6 7 8 9 10 11 12 13 14 
##
##1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
##
##
