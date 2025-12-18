import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "institute_management_db",
    use_pure = True
)

reg_no = int(input("Enter reg no to delete: "))

cursor = connection.cursor()

cursor.execute("DELETE FROM students WHERE reg_no=%s", (reg_no,))
connection.commit()


print("Student deleted")


cursor.close()
connection.close()