#To check if the given year is a leap year or not
#25-08-22
#chkleap.py
#By Anupam Kanoongo 

print("Welcome to the Leap Year checker")
print()
print("Enter the Year you want to check ")
print()
y = int(input( ))
if y%4 == 0 :
    print("The Year",y,"is a leap year")

else :
    print("The Year",y,"is not a leap year")


##Output
##Welcome to the Leap Year checker
##
##Enter the Year you want to check
##
##1968
##The Year 1968 is a leap year
