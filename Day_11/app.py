
from flask import Flask
from flask_cors import CORS
from utils.utils import createResult, enableJWT
from routes.users import usersRouter
from routes.courses import coursesRouter
from routes.students import studentRouter
from routes.videos import videosRouter

app = Flask(__name__)
enableJWT(app)

@app.errorhandler(500)
def server_error(e):
    return createResult(repr(getattr(e, "original_exception", e)), None), 200

app.register_blueprint(usersRouter)
app.register_blueprint(coursesRouter)
app.register_blueprint(studentRouter)
app.register_blueprint(videosRouter)


CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


