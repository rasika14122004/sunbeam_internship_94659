import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "system",
    database = "institute_management_db",
    use_pure = True
)


reg_no = int(input("Student Reg No: "))
new_mobile = input("New mobile number: ")

query = "UPDATE students SET mobile_no=%s WHERE reg_no=%s"

cursor = connection.cursor()

cursor.execute(query, (new_mobile, reg_no))


connection.commit()
print("Mobile number updated")

cursor.close()
connection.close()