#To Create a dictionary with keys Name, Age, Country and Language.
#Assign appropriate values to these keys.
#4/2/23
#dictpy.py
#By Anupam Kanoongo
from time import *
#Creating a dictionary
print("#Creating a dictionary")
dt = {"Name":None, "Age":None, "Country":None, "Language":None}

print("Enter Name, Age, Country, Language")
print()
for i in dt.keys():
    val = input("Enter :")
    dt[i]=val
    print()
    
print("Dictionary:","\n",dt)
print()
sleep(2)
#Add a key Gender with an appropriate value to the dictionary.
print("#Add a key Gender with an appropriate value to the dictionary.")
dt["Gender"]= None
val = input("Enter your Gender : ")
dt["Gender"]= val
print()

print("Dictionary:","\n",dt)
print()
sleep(2)
#Remove a key Language from the dictionary.
print("#Remove a key Language from the dictionary.")
dt.pop("Language")

print("Dictionary:","\n",dt)
print()
sleep(2)
#Sort the dictionary by keys and display the result.
print("#Sort the dictionary by keys and display the result.")
keys = sorted(dt.keys())
print("Sorted:","\n",keys)
print()
sleep(2)
#Sort the dictionary by values and display the result.
print("#Sort the dictionary by values and display the result.")
values = sorted(dt.values())
print("Sorted:","\n",values)
print()

##Output
###Creating a dictionary
##Enter Name, Age, Country, Language
##
##Enter :Anupam
##
##Enter :16
##
##Enter :India
##
##Enter :English
##
##Dictionary: 
## {'Name': 'Anupam', 'Age': '16', 'Country': 'India', 'Language': 'English'}
##
###Add a key Gender with an appropriate value to the dictionary.
##Enter your Gender : Male
##
##Dictionary: 
## {'Name': 'Anupam', 'Age': '16', 'Country': 'India', 'Language': 'English', 'Gender': 'Male'}
##
###Remove a key Language from the dictionary.
##Dictionary: 
## {'Name': 'Anupam', 'Age': '16', 'Country': 'India', 'Gender': 'Male'}
##
###Sort the dictionary by keys and display the result.
##Sorted: 
## ['Age', 'Country', 'Gender', 'Name']
##
###Sort the dictionary by values and display the result.
##Sorted: 
## ['16', 'Anupam', 'India', 'Male']
