# pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "system",
    database = "institute_management_db",
    use_pure = True
)

query = "select * from students;"

cursor = connection.cursor()

cursor.execute(query)

students = cursor.fetchall()

for values in students:
    print(values)


cursor.close()
connection.close()