#To find the percentage of 5 Subjects
#percent.py
#23-07-2022
#By Anupam Kanoongo 

print("Welcome to the Percentage Finder")
print()
print("Enter your values")
print()
s1 = int(input("Enter the Marks in First Subject "))
s2 = int(input("Enter the Marks in Second Subject "))
s3 = int(input("Enter the Marks in Third Subject "))
s4 = int(input("Enter the Marks in Fourth Subject "))
s5 = int(input("Enter the Marks in Fifth Subject "))

t=500

percent = ((s1+s2+s3+s4+s5)/500)*100

print("The percentage acquired by the student with marks", s1,",",s2,",",s3,",",s4,",",s5,"is ", percent) 


##Output
##Welcome to the Percentage Finder
##
##Enter your values
##
##Enter the Marks in First Subject 81
##Enter the Marks in Second Subject 84
##Enter the Marks in Third Subject 87
##Enter the Marks in Fourth Subject 86
##Enter the Marks in Fifth Subject 83
##The percentage acquired by the student with marks 81 , 84 , 87 , 86 , 83 is  84.2
