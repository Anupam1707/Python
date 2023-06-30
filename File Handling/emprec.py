import pickle
def start():
    try:
        with open("EmpRec.bin", "rb") as file:
            pass
    except :
        with open("EmpRec.bin", "wb") as file:
            pass
    
def entry():
    empno = int(input("Enter Employee Number : "))
    name = str(input("Enter the name of Employee : "))
    designation = str(input("Enter the Designation of the Employee : "))
    salary = int(input("Enter the Salary of Employee : "))
    inp = {"No":empno, "Name":name, "Designation":designation, "Salary":salary}
    with open("EmpRec.bin","ab") as file:
        pickle.dump(inp, file)
    print("Successfully Entered")
    print()

def search():
    eno = int(input("Enter the Employee Number : "))
    try:
        with open("EmpRec.bin","rb") as file:
          file.seek(eno)
          data = pickle.load(file)
          for key in data.keys():
              print(key, data[key])
    except:
        print("No record found with the id", eno)
        print()
def report():
    sum = 0
    try:
        with open("EmpRec.bin", "rb") as file:
            while True:
                data = pickle.load(file)
                sum += data["Salary"]
    except:
        print("Total Salary is",sum)
        print()
    
def main():
    start()
    print("1. Give an Entry\n2. Update an Entry\n3. Search an Entry\nGenerate Report")
    choice = int(input("Enter an Option : "))
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
