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

#to input N numbers from the user. Store these numbers in a tuple.
#Print Maximum and minimum number from this tuple
print("Min Max from Tuple")
n = int(input("Enter the number of elements "))
numbers = ()
for i in range(n):
    v = int(input(f"Enter number {i+1} :"))
    numbers += (v,)
print()
print("Maximum Number from the above is",max(numbers))
print("Minimum Number from the above is",min(numbers))

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
##
##Min Max from Tuple
##Enter the number of elements 5
##Enter number 1 :5
##Enter number 2 :6
##Enter number 3 :4
##Enter number 4 :34
##Enter number 5 :54
##
##Maximum Number from the above is 54
##Minimum Number from the above is 4
