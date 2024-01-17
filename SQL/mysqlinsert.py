import mysql.connector as sqltor


#This program is used to insert one new record in the table : schrec and database : school

# Connect to the MySQL server
connection = sqltor.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='school',
    auth_plugin="mysql_native_password"
)
data_to_insert = {
    'Rollno': '102',
    'Name': 'Sumit',
    'MobileNo': '1134567899'
}
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# SQL query to insert a record into the table
insert_query = "INSERT INTO schrec (Rollno, Name, MobileNo) VALUES (%s, %s, %s)"

# Tuple containing the values to be inserted
record_data = (data_to_insert['Rollno'], data_to_insert['Name'], data_to_insert['MobileNo'])

# Execute the query with the data
cursor.execute(insert_query, record_data)

# Commit the changes to the database
connection.commit()

print("Record inserted successfully!")

connection.close()
