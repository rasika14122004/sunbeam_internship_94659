import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "system",
    database = "institute_management_db",
    use_pure = True
)


name = input("Course name: ")
desc = input("Description: ")
fees = int(input("Fees: "))
start = input("Start date (YYYY-MM-DD): ")
end = input("End date (YYYY-MM-DD): ")
expire = int(input("Video expire days: "))

query = """
INSERT INTO courses
(course_name, description, fees, start_datde, end_date, video_expire_days)
VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor = connection.cursor()

cursor.execute(query, (name, desc, fees, start, end, expire))

connection.commit()

cursor.close()
connection.close()