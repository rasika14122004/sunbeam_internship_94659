# import Flask class from flask module
from flask import Flask

# create server instance usinf Flask class
server = Flask(__name__)

@server.get('/')
def homepage():
    return "This is a home page"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Student Management System</h1></body></html>"

# run server continuously to listen client
server.run()