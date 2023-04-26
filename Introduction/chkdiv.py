# To check if one number is divisible by another number
#24-08-22
#chkdiv.py
#By Anupam Kanoongo 

print("Welcome to the divisibility checker")
print()
a = int(input("Enter the Divisor Number "))      #Input Values
b = int(input("Enter the Divident Number "))     #Input Values

if b%a==0 :
    print(b,"is divisible by",a)
else :
    print(b,"is not divisible by",a)


##Output
##Welcome to the divisibility checker
##
##Enter the Divisor Number 20
##Enter the Divident Number 7580
##7580 is divisible by 20
