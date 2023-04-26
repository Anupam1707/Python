#Create a dictionary with N records having ROLLNO, NAME, MARKS OF FIVE SUBJECTS and their respective values.
#4/2/23
#Stdntrec.py
#By Anupam Kanoongo

#Create a dictionary
print("Create a dictionary ")
print()
rec = {}
no = None
n = int(input("Number of Students : "))
for i in range(n):
    print("Student ",i+1)
    no = str(i+1)
    name = str(input("Name : "))
    roll = int(input("Roll No : "))
    m1 = int(input("Subject 1 : "))
    m2 = int(input("Subject 2 : "))
    m3 = int(input("Subject 3 : "))
    m4 = int(input("Subject 4 : "))
    m5 = int(input("Subject 5 : "))
    val = [name,roll,m1,m2,m3,m4,m5]
    key = "Student" + " " + no
    rec[key] = dict(zip(["Name","Roll No","Subject 1","Subject 2","Subject 3","Subject 4","Subject 5"],val))
    print()

#Display Dictionary
print("Display Dictionary")
print()
print(rec)
print()

#Access the value of a particular RECORD and store it in a LIST
print("Access the value of a particular RECORD and store it in a LIST")
print()
data = []
for i in rec.keys():
    print(rec[i]["Name"])
    data.append(rec[i]["Name"])

#Update the MARKS of a particular RECORD in the dictionary
print("Update the MARKS of a particular RECORD in the dictionary")
print()
n = int(input("Enter the number of student whose marks are to be changed : "))
su = int(input("Enter the number of subject whose marks are to be changed : "))
mk = int(input("Enter the new marks : "))
s = "Subject"+" "+ str(su)
no = "Student" + " " + str(n)
rec[no][s] = mk
print()

#Display Dictionary
print("Display Dictionary")
print()
print(rec)
print()

#Check if a particular RECORD exists in the dictionary and print the result
print("Check if a particular RECORD exists in the dictionary and print the result")
print()
rc = str(input("Enter a number of student whose existence is to be checked  : "))
state = ("Student" + " " + rc) in rec

if state == True:
    print("Record of student",rc,"exists")
else :
    print("Record of student",rc,"doesn't")

#Find the length of the dictionary and print the result
print("Find the length of the dictionary and print the result")
print()
l = len(rec)
print("Length of Dictionary : ",l)
print()

for i in rec:
    print(i)
    print()
    print("Name\t\tRoll No\t\tSub1\t\tSub 2\t\tSub 3\t\t\tSub 4\t\tSub 5")
    print(rec[i]["Name"],"\t\t",rec[i]["Roll No"],"\t\t",rec[i]["Subject 1"],"\t\t",rec[i]["Subject 2"],"\t\t",rec[i]["Subject 3"],"\t\t",rec[i]["Subject 4"],"\t\t",rec[i]["Subject 5"])

Output
Create a dictionary 

Number of Students : 2
Student  1
Name : John
Roll No : 1
Subject 1 : 87
Subject 2 : 98
Subject 3 : 68
Subject 4 : 89
Subject 5 : 78

Student  2
Name : Zach
Roll No : 2
Subject 1 : 87
Subject 2 : 98
Subject 3 : 67
Subject 4 : 89
Subject 5 : 78

Display Dictionary

{'Student 1': {'Name': 'John', 'Roll No': 1, 'Subject 1': 87, 'Subject 2': 98, 'Subject 3': 68, 'Subject 4': 89, 'Subject 5': 78}, 'Student 2': {'Name': 'Zach', 'Roll No': 2, 'Subject 1': 87, 'Subject 2': 98, 'Subject 3': 67, 'Subject 4': 89, 'Subject 5': 78}}

Access the value of a particular RECORD and store it in a LIST

John
Zach
Update the MARKS of a particular RECORD in the dictionary

Enter the number of student whose marks are to be changed : 2
Enter the number of subject whose marks are to be changed : 3
Enter the new marks : 71

Display Dictionary

{'Student 1': {'Name': 'John', 'Roll No': 1, 'Subject 1': 87, 'Subject 2': 98, 'Subject 3': 68, 'Subject 4': 89, 'Subject 5': 78}, 'Student 2': {'Name': 'Zach', 'Roll No': 2, 'Subject 1': 87, 'Subject 2': 98, 'Subject 3': 71, 'Subject 4': 89, 'Subject 5': 78}}

Check if a particular RECORD exists in the dictionary and print the result

Enter a number of student whose existence is to be checked  : 3
Record of student 3 doesn't
Find the length of the dictionary and print the result

Length of Dictionary :  2

Student 1

Name		    Roll No		    Sub1		    Sub 2		    Sub 3		    Sub 4		    Sub 5
John 		    1 		    87 		    98 		    68 		    89 		    78
Student 2

Name		    Roll No		    Sub1		    Sub 2		    Sub 3		    Sub 4		    Sub 5
Zach 		    2 		    87 		    98 		    71 		    89 		    78

