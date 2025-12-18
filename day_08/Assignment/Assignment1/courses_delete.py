import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "institute_management_db",
    use_pure = True
)

course_id = int(input("Course ID to delete: "))

cursor = connection.cursor()

cursor.execute("DELETE FROM courses WHERE course_id=%s", (course_id,))

connection.commit()


print("Course deleted")


cursor.close()
connection.close()