#To manipulate the data of a contacts.txt file 
#contacts.py
#28-4-23
#By Anupam Kanoongo

def inp():
    with open("contacts.txt", "a") as c:
        name = None
        phone = None
        eml = None
        while name != "":
            name = str(input("Enter the Name : "))
            while name != "":
                phone = int(input("Enter the phone Number : "))
                eml = str(input("Enter the Email : "))
                c.write(f"{name} {phone} {eml}\n\n")
print()

def out():
    with open("contacts.txt", "r") as c:
        d = c.readlines()
    print("S.No\t\tName\t\tPhone\t\tEmail")
    for i in range(len(d)):
        print(f"{i+1}\t\t{d[i].split()[0]}\t\t{d[i].split()[1]}\t\t{d[i].split()[2]}")

def inpt():
    name = str("Enter the Name : ")
    phone = int(input("Enter the Phone Number : "))
    eml = str(input("Enter the Email : "))
    with open("contacts.txt","a") as i:
        i.write(f"Name : {name} Phone : {phone} Email : {eml}\n\n")