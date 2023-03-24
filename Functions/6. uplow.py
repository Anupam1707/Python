#To count the uppercase and lowercase letters using function
#uplow.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the String Analyzer")
print()

def analyze(st):
    up = 0
    lo = 0
    for i in st:
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
    return up, lo

s = str(input("Enter a String : "))
u, l = analyze(s)

print("Uppercase Letters : ",u)
print("Lowercase Letters : ",l)

##Output
##Welcome to the String Analyzer
##
##Enter a String : DaLy CoLlEgE
##Uppercase Letters :  6
##Lowercase Letters :  5
