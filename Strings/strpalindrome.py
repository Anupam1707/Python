#To check if a string is palindrome or not
#strpalindrome.py
#1-11-22
#By Anupam Kanoongo

print("Welcome to the String Palindrome Checker")
print()

st = str(input("Enter the String : "))
rev = ""

for i in st:
    rev = i + rev

if rev == st:
    print("The String : ",st,"is a Palindrome String")
else :
    print("The String : ",st,"is not a Palindrome String")


##Output
##Welcome to the String Palindrome Checker
##
##Enter the String : racecar
##The String :  racecar is a Palindrome String
