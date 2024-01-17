#Write a program in python to show 2 records from table schrec which is saved in MYSQL.
#Use MYSQL connector to connect with the database.

import mysql.connector as sqltor

# Connect to the MySQL server
connection = sqltor.connect(host='localhost',  user='root',  passwd='1234',  database='school',
    auth_plugin="mysql_native_password" )

if connection.is_connected() == False :
    print("Error connecting to MYSQL database")
    
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute the query with the data
cursor.execute("select * from schrec;")

#data=cursor.fetchall()
data=cursor.fetchmany(2)

for row in data:
    print(row)
    

print("Record displayed successfully!")

connection.close()
