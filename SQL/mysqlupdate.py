#This program is used to update  record(s) from the table : schrec and database : school

import mysql.connector as sqltor

# Connect to the MySQL server
connection = sqltor.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='school',
    auth_plugin="mysql_native_password"
)
data_to_update = {
    'new_Rollno': '110',
    'new_Name': 'Sumit',
    'new_MobleNo': '1234566789',
    'condition_value': '101'
}
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# SQL query to update a record in the table
update_query = "UPDATE schrec SET Rollno = %s, Name = %s, MobileNo = %s WHERE Rollno = %s"

# Tuple containing the updated values and condition value
update_data = (data_to_update['new_Rollno'], data_to_update['new_Name'], data_to_update['new_MobleNo'], data_to_update['condition_value'])

# Execute the update query with the data
cursor.execute(update_query, update_data)

# Commit the changes to the database
connection.commit()

print("Record updated successfully!")


connection.close()
