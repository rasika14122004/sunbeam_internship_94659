from utils.dbConnection import getDBConnection

#to execute create, delete and update query

def executeQuery(query):
    #create connecion with mysql server
    connection = getDBConnection()

    #create cursor to execute a query and execute it
    cursor = connection.cursor()
    cursor.execute(query)

    #commit your changes to mysql server
    connection.commit()

    #close the cursor
    cursor.close()

    connection.close()