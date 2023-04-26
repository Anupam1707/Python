#To print pattern A-BC-DEF-GHIJ
#14-9-22
#a-bcpat.py
#By Anupam Kanoongo

print("Welcome to the Pattern Maker (A-BC)")
print()
print("Enter the number of rows to print")
print()
n = int(input())
ch = 65
for i in range(0,n):
    
    for j in range(0,i+1):
        char = chr(ch)
        print(char,end=" ")
        ch += 1
    print("\n")

##Output
##Welcome to the Pattern Maker (A-BC)
##
##Enter the number of rows to print
##
##7
##A 
##
##B C 
##
##D E F 
##
##G H I J 
##
##K L M N O 
##
##P Q R S T U 
##
##V W X Y Z [ \ 
