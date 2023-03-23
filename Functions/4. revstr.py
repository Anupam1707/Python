#To reverse the elements of a list using function
#revstr.py
#23-3-23
#By Anupam Kanoongo

print("Welcome to the String Reverser")
print()

def rev(st):
    s = ""
    for i in st:
        s = i + s
    return s

st = str(input("Enter a String : "))
print()
r = rev(st)

print("Original String : ",st)
print("Reversed String : ",r)

##Output
##Welcome to the String Reverser
##
##Enter a String : daly1234
##
##Original String :  daly1234
##Reversed String :  4321ylad
