from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)


def getConnection():
    return mysql.connector.connect(
        
        host="127.0.0.1",
        port=3306,
        user="root",
        password="system",
        database="sunbeam_portal",
        use_pure=True
    )



def executeQuery(sql, params):
    with getConnection() as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute(sql, params)
            if cur.description:
                return cur.fetchall()
            else:
                con.commit()
                return {"affectedRows": cur.rowcount}



@app.route("/video/all-videos", methods=["GET"])
def get_all_videos():
    course_id = request.args.get("course_id")

    if course_id:
        sql = "SELECT * FROM videos WHERE course_id = %s"
        result = executeQuery(sql, (course_id,))
    else:
        sql = "SELECT * FROM videos"
        result = executeQuery(sql, ())

    return jsonify(result)





@app.route("/video/add/", methods=["POST"])
def add_video():
    data = request.json

    conn = getConnection()
    cursor = conn.cursor()

    query = """
    INSERT INTO videos (course_id, title, youtube_url, description)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (
        data["course_id"],
        data["title"],
        data["youtube_url"],
        data["description"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Video added successfully"})





@app.route("/video/update/<int:video_id>", methods=["PUT"])
def update_video(video_id):
    data = request.json

    conn = getConnection()
    cursor = conn.cursor()

    query = """
    UPDATE videos
    SET course_id=%s, title=%s, youtube_url=%s, description=%s
    WHERE video_id=%s
    """

    cursor.execute(query, (
        data["course_id"],
        data["title"],
        data["youtube_url"],
        data["description"],
        video_id
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Video updated successfully"})




@app.route("/video/delete/<int:video_id>", methods=["DELETE"])
def delete_video(video_id):
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM videos WHERE video_id = %s",
        (video_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Video deleted successfully"})




if __name__ == "__main__":
    app.run(debug=True)

