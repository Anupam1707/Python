import pickle
import os
import time

inp = {}

def menu():
    print("1. Give an Entry\n2. Update an Entry\n3. Search an Entry\n4. Generate Report\n5. Delete Record")
    choice = int(input("Enter an Option : "))
    if choice == 1:
            entry()
    elif choice == 2:
            update()
    elif choice == 3:
            search()
    elif choice == 4:
            report()
    elif choice == 5:
            delrec()
    else:
            exit()
            
def up_menu():
    print("1. Update Name of Employee\n2. Update Designation of Employee\n3. Update Salary of Employee")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        choice = "Name"
    elif choice == 2:
        choice = "Designation"
    elif choice == 3:
        choice = "Salary"
    else:
        print("Please try again")
        up_menu()
    return choice

def start():
    try:
        with open("EmpRec.dat", "rb") as file:
            pass
        print("File Found")
        print()
    except FileNotFoundError:
        with open("EmpRec.dat", "wb") as file:
            pass
        print("New file created")
        print()
        
def entry():
    empno = int(input("Enter Employee Number : "))
    name = str(input("Enter the name of Employee : "))
    designation = str(input("Enter the Designation of the Employee : "))
    salary = int(input("Enter the Salary of Employee : "))
    inp = {"No":empno, "Name":name, "Designation":designation, "Salary":salary}
    with open("EmpRec.dat","ab") as file:
        pickle.dump(inp, file)
    print("Successfully Entered")
    print()
    
def search():
    eno = int(input("Enter the Employee Number : "))
    print()
    try:
        with open("EmpRec.dat","rb") as file:
          for i in range(eno):
              data = pickle.load(file)
          file.seek(0)
          for key in data.keys():
              print(key, "-",data[key])
          print()
        main()
    except:
        print("No record found with the id", eno)
        print()
        
def report():
    print("Emp No\tName\tDesignation\tSalary")
    sum = 0
    try:
        with open("EmpRec.dat", "rb") as file:
            while True:
                data = pickle.load(file)
                print(str(data["No"]) +"\t" + data["Name"] + "\t" + data["Designation"] + "\t\t" + str(data['Salary']))
                sum += data["Salary"]
    except:
        print("Total Salary is",sum)
        print()

def update():
    eno = int(input("Enter Employee Number : "))
    new = open("TempEmpRec.dat","wb")
    old = open("EmpRec.dat","rb")
    
def delrec():
    eno = int(input("Enter the Employee Number : "))
    print()
    try:
        with open("EmpRec.dat", "rb+") as file:
            while True:
                data = pickle.load(file)
                no = data["No"]
                if no <= eno and no != eno:
                    with open("TempEmpRec.dat","ab") as new:
                        pickle.dump(data, new)
        
    except:
        print("None")
        os.rename("TempEmpRec.dat", "NewEmpRec.dat")
        time.sleep(1)
        os.remove("EmpRec.dat")
        time.sleep(1)
        os.rename("NewEmpRec.dat","EmpRec.dat")
        print()
            
def main():
    start()
    while True:
        menu()

main()
