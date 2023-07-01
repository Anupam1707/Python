import pickle

def menu():
    print("1. Give an Entry\n2. Update an Entry\n3. Search an Entry\n4. Generate Report")
    choice = int(input("Enter an Option : "))
    if choice == 1:
            entry()
    elif choice == 2:
            update()
    elif choice == 3:
            search()
    elif choice == 4:
            report()
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
    main()
    
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
        main()
        
def report():
    sum = 0
    try:
        with open("EmpRec.dat", "rb") as file:
            while True:
                data = pickle.load(file)
                sum += data["Salary"]
    except:
        print("Total Salary is",sum)
        print()

def update():
    eno = int(input("Enter the Employee Number : "))
    print()
    try:
        with open("EmpRec.dat", "rb") as file:
            for i in range(eno):
                data  = pickle.load(file)
            file.seek(0)
            updt = up_menu()
            val = str(input("Enter the new value : "))
            if updt == "Salary":
                val = int(val)
            data[updt] = val
            for i in range(eno-1):
                temp = pickle.load(file)
            pickle.dump(data, file)
    except:
        print("None")
            
def main():
    start()
    while True:
        menu()
main()
