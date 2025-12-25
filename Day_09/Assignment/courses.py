# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)


@server.route('/course', methods=['GET'])
def retrieve_courses():
    # create a select query
    query = "select * from courses;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"course : {data}"


@server.route('/course', methods=['POST'])
def create_course():
    # extract data form form
    # data = request.get_json()

    course_name = request.get_json().get('course_name')
    decription = request.get_json().get('decription')
    fees = request.get_json().get('fees')
    start_date = request.get_json().get('start_date')
    end_date = request.get_json().get('end_date')
    video_expire_days = request.get_json().get('video_expire_days')

      
    # create a query to add student into table
    query = """insert into courses(course_name, decription, fees, start_date, end_date, video_expire_days) values(%s,%s,%s,%s,%s,%s)"""
    
    values = (course_name, decription, fees, start_date, end_date, video_expire_days)

    #print(query)
    #execute the query 
    executeQuery(query=query,values = values)

    return "course is added successfully"

@server.route('/course', methods=['PUT'])
def update_course():
    # extract data form form
    course_id = request.get_json().get('course_id')
    new_fees = request.get_json().get('fees')

    # create a query
    query = f"update courses SET fees = '{new_fees}' where course_id = '{course_id}';"

    # execute the query
    executeQuery(query=query)

    return "fees is updated successfully"

@server.route('/course', methods=['DELETE'])
def delete_course():
    # extract data form form
    course_id = request.get_json().get('course_id')

    # create a query
    query = f"delete from courses where course_id = '{course_id}';"

    # execute the query
    executeQuery(query=query)

    return "course is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)