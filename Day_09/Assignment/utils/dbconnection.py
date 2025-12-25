import mysql.connector

def getDBConnection():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "system",
        database= "python",
        use_pure=True
    )

    return connection 