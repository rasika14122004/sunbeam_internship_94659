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
rollno = int(input("Enter rollno : "))
name = input("Enter name : ")
email = input("Enter email : ")
course = input("Enter course : ")

query = f"insert into students values({rollno}, '{name}', '{email}', '{course}');"

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

