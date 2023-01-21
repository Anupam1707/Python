# to solve a quadratic equation and print the result
#26-08-22
#quad_eqn.py
#By Anupam Kanoongo 

print("Welcome to the Quadratic Equation Solver")
print()
print("Enter the values of a, b, c for ax²+bx+c")
print()
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == 0:
    print("Error : Invalid Value for 'a'")
    print("The value of 'a' can never be 0")
    p = ""
    r1 = ""
    r2 = ""
else :
    d = (b**2)-4*a*c

    r1 = (-b+(d**1/2))/2*a
    r2 = (-b-(d**1/2))/2*a

    if d == 0 :
        p = "Real and Equal"
    elif d>0 :
        p = "Real"
    elif d<0 :
        p = "Imaginary"
    else :
        pass
print()
print("The Roots of the Equation",a,"x² +",b,"x +",c,"are :-","\nStat of Roots : ",p,"\nFirst Root    : ",r1,"\nSecond Root   : ",r2)
        

##Output
##Welcome to the Quadratic Equation Solver
##
##Enter the values of a, b, c for ax²+bx+c
##
##a = 1
##b = -8
##c = 16
##
##The Roots of the Equation 1 x² + -8 x + 16 are :- 
##Stat of Roots :  Real and Equal 
##First Root    :  4.0 
##Second Root   :  4.0
