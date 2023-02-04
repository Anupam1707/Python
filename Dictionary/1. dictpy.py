#To Create a dictionary with keys &quot;Name&quot;, &quot;Age&quot;, &quot;Country&quot; and &quot;Language&quot;. Assign
##appropriate values to these keys.
#4/2/23
#dictpy.py
#By Anupam Kanoongo

#Creating a dictionary
dt = {"Name":None, "Age":None, "Country":None, "Language":None}

print("Enter Name, Age, Country, Language")
for i in dt.keys():
    val = input("Enter :")
    dt[i]=val
    print()
    
print("Dictionary:","\n",dt)
print()

#Add a key Gender with an appropriate value to the dictionary.
dt["Gender"]= None
val = input("Enter your Gender : ")
dt["Gender"]= val
print()

print("Dictionary:","\n",dt)
print()

#Remove a key Language from the dictionary.
dt.pop("Language")

print("Dictionary:","\n",dt)
print()

#Sort the dictionary by keys and display the result.
keys = sorted(dt.keys())
print(keys)
print()

#Sort the dictionary by values and display the result.
values = sorted(dt.values())
print(values)
print()
