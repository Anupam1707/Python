#To count the number of uppercase, lowercase, alphabets, digits, and other symbols 
#typecnt.py
#1-11-22
#By Anupam Kanoongo

print("Welcome to the Character Type Counter")
print()

a = 0    
u = 0                        #Initial Assign
l = 0                        #Initial Assign
d = 0                        #Initial Assign
al = 0                       #Initial Assign
o = 0                        #Initial Assign

st = str(input("Enter your Word or Sentence : "))             # Input
print()

for i in st:
    if i.isupper():                      # Check for Upper
        u += 1
        al+= 1
    elif i.islower():                    # Check for Lower
        l += 1
        al+= 1
    elif i.isdigit():                    # Check for Digits
        d += 1
    else :                               # Other Symbols
        o += 1

a = len(st)

print("The Result Total Number of Characters : ",a)
print()
print("Number of Upper Case Characters : ",u)
print()
print("Number of Lower Case Characters : ",l)
print()
print("Number of Digits : ",d)
print()
print("Number of Alphabets : ",al)
print()
print("Number of Other Symbols (Spaces Are Included) : ",o)

##Output
##
##Welcome to the Character Type Counter
##
##Enter your Word or Sentence : # Anupam @ 123 #
##
##The Result Total Number of Characters :  16 
##
##Number of Upper Case Characters :  1 
##
##Number of Lower Case Characters :  5 
##
##Number of Digits :  3 
##
##Number of Alphabets : 6
##
##Number of Other Symbols (Spaces Are Included) :  7