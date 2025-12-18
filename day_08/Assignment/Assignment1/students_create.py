import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "system",
    database = "institute_management_db",
    use_pure = True
)


name = input("Student name: ")
email = input("Student email (must exist in users): ")
course_id = int(input("Course ID: "))
mobile = input("Mobile number: ")

query = """
INSERT INTO students
(name, email, course_id, mobile_no)
VALUES (%s, %s, %s, %s)
"""

cursor = connection.cursor()

cursor.execute(query, (name, email, course_id, mobile))


connection.commit()

cursor.close()
connection.close()
