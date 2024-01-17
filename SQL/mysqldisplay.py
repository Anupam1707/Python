#This program is used to display all records from the table : schrec and database : school

import mysql.connector as sqltor

# Connect to the MySQL server
connection = sqltor.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='school',
    auth_plugin="mysql_native_password"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# SQL query to insert a record into the table
insert_query = "select * from schrec;"

# Execute the query with the data
cursor.execute(insert_query)
row=cursor.fetchone()
while row is not None:

    print(row)
    row=cursor.fetchone()
# Commit the changes to the database
connection.commit()

print("Record inserted successfully!")

connection.close()
