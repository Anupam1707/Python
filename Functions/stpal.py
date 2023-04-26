#To check if a given string is palindrome or not
#stpal.py
#24-3-24
#By Anupam Kanoongo

print("Welcome to the String Palindrome Checker")
print()
    
def pal(st):
    rev  = ""
    for i in st:
        rev = i + rev

    if rev == st:
        print("The String : ",st,"is a Palindrome String")
    else :
        print("The String : ",st,"is not a Palindrome String")

st = str(input("Enter the String : "))
pal(st)

##Output
##Welcome to the String Palindrome Checker
##
##Enter the String : madam
##The String :  madam is a Palindrome String
