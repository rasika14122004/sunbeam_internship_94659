from flask import Blueprint, request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity
import mysql.connector
import os
from utils.utils import crypto, createResult
import utils.db_connection as db

usersRouter = Blueprint("users", __name__, url_prefix="/users")

ADMIN_EMAIL = os.getenv("FIXED_ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("FIXED_ADMIN_PASSWORD")
STUDENT_PASSWORD = os.getenv("FIXED_STUDENT_PASSWORD")

if not all([ ADMIN_EMAIL, ADMIN_PASSWORD, STUDENT_PASSWORD]):
    raise RuntimeError("Missing environment variables")


# ---------------- SETUP ADMIN (ONE TIME ONLY) ----------------
@usersRouter.route("/setup-admin", methods=["POST"])
def setup_admin():
    check_sql = "SELECT email FROM users WHERE role='admin'"
    existing = db.executeQuery(check_sql, None)

    if existing:
        return createResult("Admin already exists")

    hashed_pwd = crypto.hash(ADMIN_PASSWORD)

    sql = "INSERT INTO users (email, password, role) VALUES (%s, %s, 'admin')"
    db.executeQuery(sql, (ADMIN_EMAIL, hashed_pwd))

    return createResult(None, "Admin created successfully")

# ---------------- REGISTER STUDENT ----------------
@usersRouter.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not data or "email" not in data:
        return createResult("Email required")

    hashed_pwd = crypto.hash(STUDENT_PASSWORD)

    sql = "INSERT INTO users (email, password, role) VALUES (%s, %s, 'student')"
    try:
        db.executeQuery(sql, (data["email"], hashed_pwd))
    except mysql.connector.IntegrityError:
        return createResult("Email already exists")

    return createResult(None, "Student registered with default password")

# ---------------- LOGIN (ADMIN + STUDENT) ----------------
@usersRouter.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # 1️⃣ Validate request
    if not data:
        return createResult("Email and password required", None)

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return createResult("Email and password required", None)

    # 2️⃣ Fetch user from DB
    sql = "SELECT email, password, role FROM users WHERE email=%s"
    result = db.executeQuery(sql, (email,))

    if not result:
        return createResult("Invalid email or password", None)

    user = result[0]

    # 3️⃣ Verify password (salt-safe, works every time)
    if not crypto.verify(password, user["password"]):
        return createResult("Invalid email or password", None)

    # 4️⃣ Create NEW token every login (THIS enables multiple logins)
    token = create_access_token(
        identity=user["email"],
        additional_claims={"role": user["role"]}
    )

    # 5️⃣ Success
    return createResult(None, {
        "email": user["email"],
        "role": user["role"],
        "token": token
    })


def admin_only():
    return get_jwt().get("role") == "admin"

def student_only():
    return get_jwt().get("role") == "student"

def current_user_email():
    return get_jwt_identity()
