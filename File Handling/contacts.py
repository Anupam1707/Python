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
                c.write(f"Name : {name}\nPhone : {phone}\nEmail : {eml}\n\n")

def out():
    with open("contacts.txt", "r") as c:
        d = c.readlines()
    