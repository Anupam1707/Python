#To check if a number is a palindrome number
#12-9-22
#palindrome.py
#By Anupam Kanoongo

print("Welcome to the Palindrome Checker")
print()
print("Enter the number to be checked")
print()

num = int(input("Enter a value : "))  
temp = num  
rev = 0  
while num > 0:  
    dig = num % 10  
    rev = rev * 10 + dig  
    num = num // 10  
if temp == rev:  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  



##Output
##Welcome to the Palindrome Checker
##
##Enter the number to be checked
##
##Enter a value : 12345678987654321
##This value is a palindrome number!
