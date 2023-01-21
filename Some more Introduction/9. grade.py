#To find the percentage of 5 Subjects
#grade.py
#26-08-2022
#By Anupam Kanoongo 

print("Welcome to the Grade Giver according to percentage")
print()
print("Enter your values")
print()
s1 = int(input("Enter the Marks in First Subject : "))
s2 = int(input("Enter the Marks in Second Subject : "))
s3 = int(input("Enter the Marks in Third Subject : "))
s4 = int(input("Enter the Marks in Fourth Subject : "))
s5 = int(input("Enter the Marks in Fifth Subject : "))
a = int(input("Enter the Total Marks per Subject : "))
t = a*5
p = ((s1+s2+s3+s4+s5)/t)*100

if p >= 90 :
    g = "A"
elif 80 <= p <= 90 :
    g = "B"
elif 70 <= p <= 80 :
    g = "C"
elif 60 <= p <= 70 :
    g = "D"
elif p <= 60 :
    g = "E"
else :
    pass

print("Result","\nSubject 1 : ",s1,"\nSubject 2 : ",s2,"\nSubject 3 : ",s3,"\nSubject 4 : ",s4,"\nSubject 5 : ",s5,"\nPercentage : ",p,"\nGrade : ",g)


##Output
##Welcome to the Grade Giver according to percentage
##
##Enter your values
##
##Enter the Marks in First Subject : 83
##Enter the Marks in Second Subject : 82
##Enter the Marks in Third Subject : 81
##Enter the Marks in Fourth Subject : 86
##Enter the Marks in Fifth Subject : 89
##Enter the Total Marks per Subject : 100
##Result 
##Subject 1 :  83 
##Subject 2 :  82 
##Subject 3 :  81 
##Subject 4 :  86 
##Subject 5 :  89 
##Percentage :  84.2 
##Grade :  B
