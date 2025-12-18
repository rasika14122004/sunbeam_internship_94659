# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "system",
    database = "python",
    use_pure = True
)

# form a query to be executed
rollno = int(input("Enter rollno of a student to be deleted : "))

query = f"delete from students where rollno = {rollno};"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()

