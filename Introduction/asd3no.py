# To compare three numbers and print in ascending order
#26-08-22
#asd4no.py
#By Anupam Kanoongo 

print("Welcome to the Ascending Order Writer")
print()

n1 = int(input("Enter First Number "))
n2 = int(input("Enter Second Number "))
n3 = int(input("Enter Third Number "))

if n1>n2 :
    if n1>n3 :
        f3 = n1
        f2 = n3
        f1 = n2

    else :
        f3 = n3
        f2 = n1
        f1 = n2

else :
    if n2>n3 :
        f3 = n2
        f2 = n3
        f1 = n1

    else :
        f3 = n3
        f2 = n2
        f1 = n1

print("The Correct Order of :-","\nNumber 1 : ",n1,"\nNumber 2 : ",n2,"\nNumber 3 : ",n3,"\n",f1,"<",f2,"<",f3)


##Output
##Welcome to the Ascending Order Writer
##
##Enter First Number 10
##Enter Second Number 70
##Enter Third Number 23
##The Correct Order of :- 
##Number 1 :  10 
##Number 2 :  70 
##Number 3 :  23 
## 10 < 23 < 70
