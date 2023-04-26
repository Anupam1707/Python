#To find the number of occurences of a substring in a given string
#cntstr.py
#19-10-22
#By Anupam Kanoongo

print("Welcome to the string occurence counter")
print()

l = 0
ct = 0

s = str(input("Enter you Main Message : "))                                                     #Input

w = str(input("Enter the word to be checked from the main message : "))         #Input

for i in range(len(s)):
    if s[i] == w[0]:
        if s[i:i+len(w)] == w:
            ct+=1
print("The given Word '",w,"' occurs",ct,"times in '",s,"'")                      # Result

##Output
##Welcome to the string occurence counter
##
##Enter you Main Message : Over and Over Again
##Enter the word to be checked from the main message : Over
##The given Word ' Over ' occurs 2 times in ' Over and Over Again '
