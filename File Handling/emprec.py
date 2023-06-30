import pickle
def menu():
    print("1. Give an Entry\n2. Update an Entry\n3. Search an Entry\n4. Generate Report")
    choice = int(input("Enter an Option : "))
    return choice

def start():
    try:
        with open("EmpRec.dat", "rb") as file:
            pass
    except :
        with open("EmpRec.dat", "wb") as file:
            pass
    
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
    
def main():
    start()
    choice = menu()
    while True:
        if choice == 1:
            entry()
        elif choice == 2:
            update()
        elif choice == 3:
            search()
        elif choice == 4:
            report()
        else:
            break
main()
