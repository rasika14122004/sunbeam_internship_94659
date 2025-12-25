from flask import jsonify


def createCustomResponse(msg, error=False):
    d = dict()

    if error == True:
        d  = {
            'status code':'?',
            'string':'?',
            'msg':msg
        }
    else:
        d  = {
            'status code':'200',
            'string':'OK',
            'msg':msg
        }

    return jsonify(d)