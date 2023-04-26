#To double the letters of a string
#dblstr.py
#21-10-22
#By Anupam Kanoongo

print("Welcome to the String Doubler")
print()

st = str(input("Enter your String : "))
print()

nst = ""
s = ""

for i in st:
    ord(i)
    s = chr(ord(i)) + chr(ord(i))
    nst += s

print("Original String : ",st)
print("Doubled String : ",nst)


##Output
##Welcome to the String Doubler
##
##Enter your String : The Daly College
##
##Original String :  The Daly College
##Doubled String :  TThhee  DDaallyy  CCoolllleeggee
