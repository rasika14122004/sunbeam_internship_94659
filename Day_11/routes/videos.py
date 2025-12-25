from flask import Blueprint, Flask, request

from flask_jwt_extended import get_jwt_identity, jwt_required

from routes.users import admin_only

from utils.db_connection import executeQuery
from utils.utils import createResult





videosRouter = Blueprint("videos", __name__, url_prefix="/videos")



# -------- VIDEOS--------

#----------------------fetch all videos (filter on courseId)----------------------------------


@videosRouter.route('/all-videos/<int:course_id>', methods=['GET'])
@jwt_required()
def getAllVideos(course_id):
    email = get_jwt_identity()

    sql = """
    SELECT v.video_id,
           v.course_id,
           v.title,
           v.youtube_url,
           v.decription,
           v.added_at
    FROM students s
    JOIN videos v ON s.course_id = v.course_id
    WHERE s.email = %s
      AND s.course_id = %s
      AND DATE_ADD(v.added_at, INTERVAL
          (SELECT video_expire_days FROM courses WHERE course_id = %s)
          DAY
      ) >= NOW()
    """

    params = (email, course_id, course_id)
    result = executeQuery(sql, params)

    return createResult(None, result)


#---------------adds a new video to a course--------



@videosRouter.route("/add", methods=["POST"])

@jwt_required()

def add_video():

    if not admin_only():

        return createResult("Admin access required", None)



    data = request.json



    q = """

    INSERT INTO videos(course_id, title, youtube_url, decription)

    VALUES (%s, %s, %s, %s)

    """



    params = (

        data["course_id"],

        data["title"],

        data["youtubeURL"],

        data["decription"]

    )



    return createResult(None,executeQuery(q,params))

                                          

 #---------updates video details by videoId--------------



@videosRouter.route('/update/<int:video_id>', methods=['PUT'])

@jwt_required()

def update_video(video_id):

    if not admin_only():

        return createResult("Admin access required", None)



    data = request.json



    q = """

    UPDATE videos

    SET course_id=%s,

        title=%s,

        youtube_url=%s,

        decription=%s

    WHERE video_id=%s

    """



    params = (

        data["course_id"],

        data["title"],

        data["youtubeURL"],

        data["decription"],

        video_id

    )



    return createResult(None,executeQuery(q,params))

                                          

#-------------deletes a video by videoId---------

@videosRouter.route('/delete/<int:videoId>', methods=['DELETE'])

@jwt_required()

def delete_video(video_id):

    if not admin_only():

        return createResult("Admin access required", None)





    q = "DELETE FROM videos WHERE video_id = %s"

    params = (video_id,)



    return createResult(None,executeQuery(q,params))