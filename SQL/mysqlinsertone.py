#Write a program in python to ask for a roll number and display related record from table schrec which is saved in MYSQL.
#Use MYSQL connector to connect with the database.

import mysql.connector as sqltor

rn = input("Please enter Roll Number : ")
nm = input("Please enter Name : ")
mobileno = input("Please enter Mobile Number : ")

# Connect to the MySQL server
connection = sqltor.connect(host='localhost',  user='root',  passwd='1234',  database='school',
    auth_plugin="mysql_native_password" )

if connection.is_connected() == False :
    print("Error connecting to MYSQL database")
    
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

cursor.execute("select * from schrec;")
data=cursor.fetchall()
tot1 = cursor.rowcount

# Execute the query with the data
cursor.execute("insert into schrec values ( '{}', '{}', '{}');".format(rn,nm,mobileno))

connection.commit()

cursor.execute("select * from schrec;")


data=cursor.fetchall()
tot2 = cursor.rowcount

if tot2-tot1 == 1:
    print("One Record is inserted successfully!")

connection.close()
