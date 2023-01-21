#To find the smallest fraction from the given numerator and denomenator
#smlfrac.py
#16-11-22
#By Anupam Kanoongo

a = 0
s = 10000000000
sm = 0

print("Welcome to the Smallest Fraction Finder")
print()
print("Enter the Numerators : ")
print()
num = eval(input())
print()
print("Enter the Denominators :-")
print()
denum = eval(input())
In = len(num)
Idn = len(denum)
if In == Idn :
    pass
else:
    print("The count of numberators is not equal to the count of denominators")
    print("Please Restart the Program")
for i in range(In):
    a = num[i]/denum[i]
    if a < s:
        s = a
        sm = i
print("The smallest fraction from the given numbers is",num[i],"/",denum[i],"with index number",i)

##Welcome to the Smallest Fraction Finder
##
##Enter the Numerators : 
##
##[1,2,3,4,5,6,7,8,9]
##
##Enter the Denominators :-
##
##[2,4,6,8,1,2,3,4,5]
##The smallest fraction from the given numbers is 9 / 5 with index number 8
