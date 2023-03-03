# Import libraries
from flask import Flask, request
from like_db import LikeDB
# Create an instance of Flask
app = Flask(__name__)
likeDB = LikeDB('like_db.json')
@app.route("/")
def home():
    return "Hello World!"

# End point for getting image
@app.route("/api/addImage", methods=["POST"])
def addImage():
    # Get the image from the request
    if request.method == "POST":
        # Get json data from request
        data = request.get_json(force=True)
        # Get the image id from data
        image_id = data["image_id"]
        # Get the message id from data
        message_id = data["message_id"]
        likeDB.add_image(image_id, message_id)
        print(f'Image id: {image_id} Message id: {message_id}')
    return {"status":200}


# @app.route('/api/all-like-dislike/<image_id>', methods=['GET'])
# def all_like_dislike():
#     image_id = likeDB['message_id']["image_id"]
#     print(image_id)
#     like, dislike = LikeDB.get_likes_dislike(image_id)
#     return like, dislike
# Run the app

@app.route('/add-like', methods = ['POST'])
def addLike():
    data  = request.get_json(force=True)
    print(data)
    user_id = data["user_id"]
    img_id = data["img_id"]
    print(data)
    likeDB.add_like(user_id, img_id)
    return {"status":200}

@app.route("/add-dislike", methods = ['POST'])
def disLike():
    data = request.get_json(force=True)
    print(data)
    user_id = data["user_id"]
    img_id = data["img_id"]
    likeDB.add_dislike(user_id, img_id)
    return {"status":200}




if __name__ == "__main__":
    app.run(debug=True)
