#To print pattern A-BA-CBA-DCBA
#14-9-22
#cbapat.py
#By Anupam Kanoongo

print("Welcome to the Pattern Maker (A-BA-CBA)")
print()
print("Enter the number of rows to print")
print()
n = int(input())
ch = 65

for i in range(65,ch+n):

    for j in range(i,64,-1):
        print(chr(j),end=" ")
    print("\n")

##Output
##Welcome to the Pattern Maker (A-BA-CBA)
##
##Enter the number of rows to print
##
##10
##A 
##
##B A 
##
##C B A 
##
##D C B A 
##
##E D C B A 
##
##F E D C B A 
##
##G F E D C B A 
##
##H G F E D C B A 
##
##I H G F E D C B A 
##
##J I H G F E D C B A 
