


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from utils.utils import createResult
from routes.users import admin_only  # works now
import utils.db_connection as db
from utils.utils import createResult


coursesRouter = Blueprint("courses", __name__, url_prefix="/courses")


# -------- COURSES -----------

# ------------------all active course-------------------------------------------------
@coursesRouter.route('/all-active-courses', methods=['GET'])
@jwt_required()
def get_active_courses():
    q = "SELECT * FROM courses WHERE end_date >= CURDATE()"
    return createResult(data=db.executeQuery(q, None))

@coursesRouter.route('/add', methods=['POST'])

# ------------------add course--------------------------------------------------------
@coursesRouter.route('/addcourses', methods=['POST'])

@jwt_required()
def add_course():
    if not admin_only():
        return createResult("Admin access required")

    data = request.json
    q = """
    INSERT INTO courses(course_name,decription,fees,start_date,end_date,video_expire_days)
    VALUES(%s,%s,%s,%s,%s,%s)
    """
    params = (
        data["courseName"],
        data["decription"],
        data["fees"],
        data["startDate"],
        data["endDate"],
        data["videoExpireDays"]
    )
    return createResult(data=db.executeQuery(q, params))
# --------------------------update course-----------------------------------------------------------------------------------
@coursesRouter.route('/update-fees/<int:courseId>', methods=['PUT'])
@jwt_required()
def update_course_fees(courseId):
    if not admin_only():
        return createResult("Admin access required")

    data = request.get_json(silent=True)
    if not data or "fees" not in data:
        return createResult("Fees is required")

    q = "UPDATE courses SET fees=%s WHERE course_id=%s"
    params = (data["fees"], courseId)

    db.executeQuery(q, params)
    return createResult(None, "Course fees updated successfully")

# -------------------delete course-------------------------------
@coursesRouter.route('/delete/<int:courseId>', methods=['DELETE'])
@jwt_required()
def delete_course(courseId):
    if not admin_only():
        return createResult("Admin access required")

    # Step 1: Delete students enrolled in this course
    db.executeQuery("DELETE FROM student WHERE course_id=%s", (courseId,))

    # Step 2: Delete the course
    db.executeQuery("DELETE FROM courses WHERE course_id=%s", (courseId,))

    return createResult(None, "Course and enrolled students deleted successfully")
