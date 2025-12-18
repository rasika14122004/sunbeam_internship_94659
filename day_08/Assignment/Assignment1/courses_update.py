import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "system",
    database = "institute_management_db",
    use_pure = True
)

course_id = int(input("Course ID: "))
new_fees = int(input("New fees: "))

query = "UPDATE courses SET fees=%s WHERE course_id=%s"


cursor = connection.cursor()
cursor.execute(query, (new_fees, course_id))


connection.commit()
print("Course fees updated")

cursor.close()
connection.close()