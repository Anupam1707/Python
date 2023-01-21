#To count number of letters and print each reversed
#cntrev.py
#1-11-22
#By Anupam Kanoongo

print("Welcome to the Messege Reverser")
print()
print("Enter your Messege :- ")
print()
s = ""

st = str(input())

print()

a = st.split()

l = len(a)

print("Reversed Messege :- ")
print()
for i in range(l):
    p = a[i]
    for j in p:
        s = j+s

    print(s, end=" ")
    s = ""
print()
print("Total Number of Words : ",l)


##Output
##Welcome to the Messege Reverser
##
##Enter your Messege :- 
##
##The Daly College
##
##Reversed Messege :- 
##
##ehT ylaD egelloC 
##
##Total Number of Words :  3
