# To read two number and use the operator given
#26-08-22
#rd2op.py
#By Anupam Kanoongo 

print("Welcome to Custom Calculator")
print()
print("Enter the First Number to be operated")
n1 = int(input())
print("Enter the Second Number to be operated")
n2 = int(input())
print("Enter the opertator you want to use by typing --> (+,-,*,/)")

op = input()

if op == "+" :
    s = n1+n2
    a = "Addition"

elif op == "-" :
    s = n1-n2
    a = "Subtraction"

elif op == "*" :
    s = n1*n2
    a = "Multiplition"

elif op == "/" :
    s = n1/n2
    a = "Division"

print("Result as follows :-","\nNumber 1 :",n1,"\nNumber 2 :",n2,"\nOperator :",a,"\nAnswer   :",s)

##Output
##Welcome to Custom Calculator
##
##Enter the First Number to be operated
##20
##Enter the Second Number to be operated
##40
##Enter the opertator you want to use by typing --> (+,-,*,/)
##/
##Result as follows :- 
##Number 1 : 20 
##Number 2 : 40 
##Operator : Division 
##Answer   : 0.5
