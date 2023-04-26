##To write a program to create a nested tup too store roll number, name and marks of a student
##nestup.py
#27-11-22
#By Anupam Kanoongo

print("Welcome to the Student Record Maker using Tuple")
print()
n = int(input("Enter how many student's details are to be assigned : "))
r, name, mks = 0,"",0
record = ()

for i in range(1,n+1):
    print("Student ",i)
    name = str(input("Enter the Name of student :"))
    r = int(input("Enter the Roll Number of student :"))
    mks = int(input("Enter the Marks of student :"))
    print()
    record += ((name,r,mks),)

print("Name, Roll Number, Marks")
for i in record:
    print(i)

# Output
# Welcome to the Student Record Maker using Tuple

# Enter how many student's details are to be assigned : 5
# Student  1
# Enter the Name of student :John
# Enter the Roll Number of student :1       
# Enter the Marks of student :76

# Student  2
# Enter the Name of student :Olivia
# Enter the Roll Number of student :2       
# Enter the Marks of student :79

# Student  3
# Enter the Name of student :Brian
# Enter the Roll Number of student :3       
# Enter the Marks of student :67

# Student  4
# Enter the Name of student :Mia
# Enter the Roll Number of student :4       
# Enter the Marks of student :87

# Student  5
# Enter the Name of student :Ethan 
# Enter the Roll Number of student :5       
# Enter the Marks of student :68

# Name, Roll Number, Marks
# ('John', 1, 76)
# ('Olivia', 2, 79)
# ('Brian', 3, 67)
# ('Mia', 4, 87)
# ('Ethan', 5, 68)