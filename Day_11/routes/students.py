from flask import Flask, jsonify, request,Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity
import mysql.connector
from passlib.hash import sha256_crypt
from routes.users import admin_only, student_only
from utils.db_connection import executeQuery
from utils.utils import createResult
crypto = sha256_crypt

studentRouter = Blueprint("students",__name__,url_prefix="/students")

@studentRouter.route('/register-to-course', methods=['POST'])
def register_to_course():
    sql = """
    INSERT INTO students(name, email,course_id , mob_no)
    VALUES (%s, %s, %s, %s)
    """
    params = (
        request.json["name"],
        request.json["email"],
        request.json["course_id"],
        request.json["mob_no"]
    )
    return createResult(None, executeQuery(sql, params))

@studentRouter.route('/change-password', methods=['PUT'])
@jwt_required()
def change_password():

    # 🔐 Allow only students
    if not student_only():
        return createResult("Student access required", None)

    email = get_jwt_identity()

    new_pass = request.json["newPassword"]
    confirm_pass = request.json["confirmPassword"]

    if new_pass != confirm_pass:
        return createResult("Passwords do not match", None)

    enc_pass = crypto.hash(new_pass)
    sql = "UPDATE users SET password=%s WHERE email=%s"
    return createResult(None, executeQuery(sql, (enc_pass, email)))


@studentRouter.route('/my-courses', methods=['GET'])
@jwt_required()
def my_courses():
    email = get_jwt_identity()

    sql = """
    SELECT c.course_id, c.course_name, c.decription,
           c.fees, c.start_date, c.end_date
    FROM students s
    JOIN courses c ON s.course_id = c.course_id
    WHERE s.email = %s
    """
    return createResult(None, executeQuery(sql, (email,)))

@studentRouter.route('/my-course-with-videos', methods=['GET'])
@jwt_required()
def my_course_with_videos():
    email = get_jwt_identity()

    sql = """
    SELECT c.course_name,
           v.title,
           v.youtube_url,
           v.decription
    FROM students s
    JOIN courses c ON s.course_id = c.course_id
    JOIN videos v ON v.course_id = c.course_id
    WHERE s.email = %s
      AND DATE_ADD(v.added_at, INTERVAL c.video_expire_days DAY) >= NOW()
    """
    return createResult(None, executeQuery(sql, (email,)))

# --------------------------- /admin/enrolled students ----------------------------------
@studentRouter.route('/enrolled/<int:course_id>', methods=['GET'])
@jwt_required()
def get_enrolled_students(course_id):
    if not admin_only():
        return createResult("Admin access required")

    q = "SELECT reg_no, name, email, mob_no FROM students WHERE course_id=%s"
    students = executeQuery(q, (course_id,))

    return createResult(None, students)


