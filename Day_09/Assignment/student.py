# import Flask class from flask module
from flask import Flask, request


from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/student', methods=['POST'])
def create_student():
    # extract data form form
    data = request.get_json()
    reg_no  = data.get('reg_no')
    name = data.get('name')
    email = data.get('email')
    course_id = data.get('course_id')
    mob_no = data.get('mob_no')
    profile_pic = data.get('profile_pic')
    
    query = f"""INSERT INTO students VALUES({reg_no}, '{name}', '{email}','{ course_id}','{ mob_no }','{profile_pic}');"""

    executeQuery(query)

    return "student is added successfully"

@server.route('/student', methods=['GET'])
def retrieve_students():
    # create a select query
    query = "select * from students;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"students : {data}"

@server.route('/student', methods=['PUT'])
def update_student():
    # extract data form form
    mob_no = request.get_json().get('mob_no')
    reg_no = request.get_json().get('reg_no')

    # create a query
    query = f"update students SET mob_no = '{mob_no}' where  reg_no = { reg_no};"

    # execute the query
    executeQuery(query=query)

    return "Mobile number is updated successfully"

@server.route('/student', methods=['DELETE'])
def delete_student():
    # extract data form form
    reg_no = request.get_json().get('reg_no')

    # create a query
    query = f"delete from students where reg_no = {reg_no};"

    # execute the query
    executeQuery(query=query)

    return "student is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)